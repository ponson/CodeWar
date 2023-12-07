import unittest
import datetime
import re


class TestMetaclass(unittest.TestCase):

    def test_case1(self):
        print(f"case 1: attrs= {User.__dict__.keys()}")
        self.assertTrue(not hasattr(User, 'first_name'))

    def test_case2(self):
        self.user = User()
        print(f"case 2: attrs= {self.user.__dict__.keys()}")
        # self.assertEqual(self.user.first_name, 'Adam')
        self.assertEqual(self.user.last_name, None)
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

class ValidationError(Exception):
    pass


class Field:
    def __init__(self, blank=False, default=None):
        self.name = ''
        self._default = default
        self.blank = blank

    @property
    def default(self):
        if callable(self._default):
            return self._default()
        return self._default

    def validate(self, value):
        if not self.blank and value is None:
            raise ValidationError(self.name, 'missing value')

        if value is not None and not self.is_type_ok(value):
            raise ValidationError(self.name, 'wrong type')

    def is_type_ok(self, value):
        return True


class CharField(Field):
    def __init__(self, min_length=0, max_length=None, **kwargs):
        super(CharField, self).__init__(**kwargs)
        self.max_length = max_length
        self.min_length = min_length

    def validate(self, value):
        super(CharField, self).validate(value)

        if value is not None and self.min_length and len(value) < self.min_length:
            raise ValidationError(self.name, 'Too short')
            
        if value is not None and self.max_length and len(value) > self.max_length:
            raise ValidationError(self.name, 'Too long')

    def is_type_ok(self, value):
        return isinstance(value, str)


class EmailField(Field):
    def validate(self, value):
        super(EmailField, self).validate(value)

        if value is not None and not re.match('[.a-z]+@[a-z]+\.[a-z]{2,6}', value):
            raise ValidationError(self.name, 'not valid e-mail')


class BooleanField(Field):
    def is_type_ok(self, value):
        return isinstance(value, bool)


class DateTimeField(Field):
    def __init__(self, auto_now=False, **kwargs):
        if auto_now and kwargs.get('default') is None:
            kwargs['default'] = datetime.datetime.now
        super(DateTimeField, self).__init__(**kwargs)
        self.auto_now = auto_now
        
    def is_type_ok(self, value):
        return isinstance(value, datetime.datetime)


class IntegerField(Field):
    def __init__(self, min_value=None, max_value=None, **kwargs):
        super(IntegerField, self).__init__(**kwargs)
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        super(IntegerField, self).validate(value)
        
        if value is not None and self.min_value and value < self.min_value:
            raise ValidationError(self.name, 'too small')

        if value is not None and self.max_value and value > self.max_value:
            raise ValidationError(self.name, 'too big')
        
    def is_type_ok(self, value):
        return isinstance(value, int)

class MetaModel(type):
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

        return super(MetaModel, meta).__new__(meta, class_name, bases, new_class_dict)


class Model(metaclass=MetaModel):
    _attribute_ = {}

    def __init__(self, **kwargs):
        for attr in self._attributes_.values():
            print(f"attr: {attr}, default: {attr.default}")
            setattr(self, attr.name, kwargs.get(attr.name, attr.default))

    def validate(self):
        for attr in self._attributes_.values():
            attr.validate(getattr(self, attr.name))


class User(Model):
    first_name = CharField(max_length=30, default='Adam')
    last_name = CharField(max_length=50)
    email = EmailField()
    is_verified = BooleanField(default=False)
    date_joined = DateTimeField(auto_now=True)
    age = IntegerField(min_value=5, max_value=120, blank=True)


if __name__ == '__main__':
    # tests = ['test_case1']
    tests = ['test_case1', 'test_case2', 'test_case3', 'test_case4', 'test_case5', 'test_case6']
    suite = unittest.TestSuite(map(TestMetaclass, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)

    # test all
    # unittest.main(verbosity=2)