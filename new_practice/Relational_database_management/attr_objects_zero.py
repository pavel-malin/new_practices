# Using attr.ib() with Transform Argument
import attr


@attr.s
class Car(object):
    color = attr.ib(converter=str)
    speed = attr.ib(default=0)

    @speed.validator
    def speed_validator(self, attribute, value):
        if value < 0:
            raise ValueError("Value cannot be negative")


'''
Using frozen=True:
>>>import attr
>>>@attr.s(frozen=True)
...class Car(object):
... color = attr.ib()
>>>{Car('blue'), Car('blue'), Car('red')}
{Car(color='red'), Car(color='blue')}
>>>Car('blue').color = 'red'
attr.exception.FrozenInstanceError
'''
