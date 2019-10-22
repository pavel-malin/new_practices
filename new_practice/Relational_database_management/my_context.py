import contextlib


@contextlib.contextmanager
def MyContext():
    print("do something first")
    yield
    print("do something else")


with MyContext():
    print("hello world")
