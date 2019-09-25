import pytest


@pytest.mark.dicttest
def test_something():
    a = ['a', 'b']
    assert a == a


def test_something_else():
    assert False
