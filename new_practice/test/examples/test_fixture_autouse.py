import os

import pytest


@pytest.fixture(autouse=True)
def change_user_env():
    curuser = os.environ.get("USER")
    os.environ["USER"] = "foobar"
    yield
    os.environ["USER"] = curuser


def test_user():
    assert os.getenv("USER") == "foobar"
