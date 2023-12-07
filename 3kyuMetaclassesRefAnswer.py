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

    def validate(self, value):
        if not self.blank and value is None:
            raise ValidationError(self.name, 'missing value')

        if value is not None and not self.is_type_ok(value):
            raise ValidationError(self.name, 'wrong type')

    def is_type_ok(self, value):
        return True


class CharField(Field):
    def __init__(self, min_length=0, max_length=None, **kwds):
        super(CharField, self).__init__(**kwds)
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, value):
        super(CharField, self).validate(value)

        if value is not None and self.min_length and len(value) < self.min_length:
            raise ValidationError(self.name, 'too short')

        if value is not None and self.max_length and len(value) > self.max_length:
            raise ValidationError(self.name, 'too long')

    def is_type_ok(self, value):
        return isinstance(value, str)


class EmailField(CharField):
    def validate(self, value):
        super(EmailField, self).validate(value)

        if value is not None and not re.match(r'[.a-z]+@[a-z]+\.[a-z]{2,6}', value):
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
        new_class_dict = {}

        for attribute_name, attribute in class_dict.items():
            if not isinstance(attribute, Field):
                new_class_dict[attribute_name] = attribute
                continue
            attribute.name = attribute_name
            new_class_dict.setdefault('_attributes_', {}).setdefault(
                attribute_name, attribute)

        return super(ModelMeta, meta).__new__(meta, class_name, bases, new_class_dict)


class Model(metaclass=ModelMeta):
    _attributes_ = {}

    def __init__(self, **kwds):
        for attr in self._attributes_.values():
            setattr(self, attr.name, kwds.get(attr.name, attr.default))

    def validate(self):
        for attr in self._attributes_.values():
            attr.validate(getattr(self, attr.name))
