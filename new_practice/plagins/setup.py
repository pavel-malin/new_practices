from setuptools import setup

setup(
    name="hello",
    version="1",
    packages=["hello"],
    entry_points={
        "pytimed": [
            "hello = hello: say_hello",
        ],
    },
)
