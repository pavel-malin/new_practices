# Exception handling in context manager
import contextlib


@contextlib.contextmanager
def MyContext():
    print("do something first")
    try:
        yield 42
    finally:
        print("do something else")


with MyContext() as value:
    print("about to raise")
    raise ValueError("let's try it")
    print(value)
