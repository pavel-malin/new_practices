from setuptools import functools
import inspect


def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(f, *args, **kwargs)
        if func_args.get('username') != 'admin':
            raise Exception("This user allowed to get food")
        return f(*args, **kwargs)
    return wrapper


@check_is_admin
def get_food(username, type='chocolate'):
    return type + " nom nom nom nom!"
