# Using attr.ib() to declare attributes
import attr


@attr.s
class Car(object):
    color = attr.ib()
    speed = attr.ib(default=0)


'''
>>> Car('blue')
Car(color='blue', speed=0)
'''
