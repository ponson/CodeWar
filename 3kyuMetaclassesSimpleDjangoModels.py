import unittest
import datetime
import re

class ValidationError(Exception):
    pass

class Field:
    def __init__(self, default=None, blank=False):
        self.name = ''
        self._default = default
        self.blank = blank

    @property
    def default(self):
        if callable(self._default):
            return self._default()
        return self._default
        # return 'Ponson'

    def validate(self, value):
        if not self.blank and value is None:
            raise ValidationError(self.name, 'missing value')

        if value is not None and not self.is_type_ok(value):
            raise ValidationError(self.name, 'wrong type')
        
    def is_type_ok(self, value):
        return True


class TestMetaclass(unittest.TestCase):

    def test_case1(self):
        print(f"test case1: {not hasattr(User, 'first_name')}")
        self.assertTrue(not hasattr(User, 'first_name'))

    def test_case2(self):
        self.user = User()
        print(f"first name value: {self.user.first_name}")
        self.assertEqual(self.user.first_name, 'Adam')
        self.assertEqual(self.user.last_name, None)
        print(f"Verified value: {self.user.is_verified}")
        self.assertEqual(self.user.is_verified, False)

    def test_case3(self):
        self.user = User()
        self.user.email = 'adam@example.com'
        self.assertEqual(self.user.email,  'adam@example.com')

    def test_case4(self):
        self.user = User(first_name='Liam', last_name='Smith',
                         email='liam@example.com')
        self.assertEqual(self.user.first_name, 'Liam')
        self.assertEqual(self.user.last_name,  'Smith')
        self.assertEqual(self.user.email,  'liam@example.com')

    def test_case5(self):
        self.user = User(first_name='Liam', last_name='Smith',
                         email='liam@example.com')
        self.user.validate()
        self.user.age = 999
        self.assertRaises(ValidationError, self.user.validate)

    def test_case6(self):
        self.user1 = User()
        self.user1.first_name = 'John'
        self.user1.last_name = 'Doe'

        self.user2 = User()
        self.user2.first_name = 'Somebody'
        self.user2.last_name = 'Else'

        self.assertEqual(self.user1.first_name, 'John')
        self.assertEqual(self.user1.last_name,  'Doe')

        self.assertEqual(self.user2.first_name, 'Somebody')
        self.assertEqual(self.user2.last_name,  'Else')

    def test_case7(self):
        with self.assertRaises(ValueError):
            raise_if_negative(-1)

    def test_case8(self):
        self.assertRaises(ValueError, to_upper, '')


def to_upper(value):
    if not value:
        raise ValueError('Value cannot be empty')
    return value.upper()


def raise_if_negative(value):
    if value < 0:
        raise ValueError('Value cannot be negative')

# class A(metaclass=Meta):
#     X = 1


class CharField(Field):

    def __init__(self, min_length=0, max_length=None, **kwds):
        super(CharField, self).__init__(**kwds)
        self.max_length = max_length
        self.min_length = min_length

    def validate(self, value):
        super(CharField, self).validate(value)

        if value is not None and self.min_length and len(value) < self.min_length:
            raise ValidationError(self.name, 'too short')

        if value is not None and self.max_length and len(value) > self.max_length:
            raise ValidationError(self.name, 'too long')

    def is_type_ok(self, value):
        return isinstance(value, str)


class EmailField(Field):
    def validate(self, value):
        super(EmailField, self).validate(value)

        if value is not None and not re.match('[.a-z]+@[a-z]+\.[a-z]{2,6}', value):
            raise ValidationError(self.name, 'not valid e-mail')


class BooleanField(Field):
    def is_type_ok(self, value):
        return type(value) == bool


class DateTimeField(Field):
    def __init__(self, auto_now=False, **kwds):
        if auto_now and kwds.get('default') is None:
            kwds['default'] = datetime.datetime.now
        super(DateTimeField, self).__init__(**kwds)
        self.auto_now = auto_now
    
    def is_type_ok(self, value):
        return isinstance(value, datetime.datetime)


class IntegerField(Field):
    def __init__(self, min_value=None, max_value=None, **kwds):
        super(IntegerField, self).__init__(**kwds)
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        super(IntegerField, self).validate(value)

        if value is not None and self.min_value and value < self.min_value:
            raise ValidationError(self.name, 'too small')

        if value is not None and self.max_value and value > self.max_value:
            raise ValidationError(self.name, 'too big')
    
    def is_type_ok(self, value):
        return type(value) == int

class ModelMeta(type):
    def __new__(meta, class_name, bases, class_dict):
        print(f"meta is: {meta}")
        print(f"class_name is: {class_name}")
        print(f"bases is: {bases}")
        print(f"class_dict is: {class_dict}")

        new_class_dict = {}

        for attribute_name, attribute in class_dict.items():
            if not isinstance(attribute, Field):
                new_class_dict[attribute_name] = attribute
                continue
            attribute.name = attribute_name
            new_class_dict.setdefault('_attributes_', {}).setdefault(attribute_name, attribute)
            
        return super(ModelMeta, meta).__new__(meta, class_name, bases, new_class_dict)


class Model(metaclass=ModelMeta):
    print('checkpoint 1')
    # _attributes_ = {}

    def __init__(self, **kwds):
        for attr in self._attributes_.values():
            print(f"attr: {attr}")
            setattr(self, attr.name, kwds.get(attr.name, attr.default))

    def validate(self):
        for attr in self._attributes_.values():
            attr.validate(getattr(self, attr.name))
        


class User(Model):
    print('checkpoint 2')
    first_name = CharField(max_length=30, default='Adam')
    last_name = CharField(max_length=50)
    email = EmailField()
    is_verified = BooleanField(default=False)
    date_joined = DateTimeField(auto_now=True)
    age = IntegerField(min_value=5, max_value=120, blank=True)


if __name__ == '__main__':
    # tests = ['test_case1']
    # tests = ['test_case1', 'test_case2', 'test_case3', 'test_case4', 'test_case5', 'test_case6']
    # suite = unittest.TestSuite(map(TestMetaclass, tests))
    # unittest.TextTestRunner(verbosity=2).run(suite)

    unittest.main(verbosity=2)
