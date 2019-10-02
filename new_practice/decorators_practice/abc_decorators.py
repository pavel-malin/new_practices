import abc


class BasePizza(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_radius(self):
        """Method that should do something."""
