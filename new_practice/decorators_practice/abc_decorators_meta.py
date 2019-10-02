''' Using a subclass to extend the signature of its parent's abstract method
import abc


class BasePizza(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_ingredients(self):
        """Returns the ingredient list."""

class Calzone(BasePizza):
    def get_ingredients(self, with_egg=False):
        egg = Egg() if with_egg else None
        return self.ingredients + [egg]
'''


import abc


class BasePizza(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_ingredients(self):
        """Returns the ingredient list."""


class DiesPizza(BasePizza):
    @staticmethod
    def get_ingredients():
        return None
