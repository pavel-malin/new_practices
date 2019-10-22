# Using singledispatch to dispatch a method call
import functools


class SnareDrum(object):
    pass


class Cymbal(object):
    pass


class Stick(object):
    pass


class Brushes(object):
    pass


@functools.singledispatch
def play(instrument, accessory):
    raise NotImplementedError("Cannot play these")


@play.register(SnareDrum)
def _(instrument, accessory):
    if isinstance(accessory, Stick):
        return "POC!"
    if isinstance(accessory, Brushes):
        return "SHHHHH!"
    raise NotImplementedError("Cannot play these")


@play.register(Cymbal)
def _(instrument, accessory):
    if isinstance(accessory, Brushes):
        return "FRCCCHHT!"
    raise NotImplementedError("Cannot play these")
