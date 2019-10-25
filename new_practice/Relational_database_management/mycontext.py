# Declaring a context manager applying yield to a value
import contextlib


@contextlib.contextmanager
def MyContext():
    print("do something first")
    yield 42
    print("do something else")


with MyContext() as value:
    print(value)
