# Decorator update using wraps from functools


from setuptools import functools


def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper


class Store(object):
    @check_is_admin
    def get_food(self, username, food):
        """Get food from storage."""
        return self.storage.get(food)
