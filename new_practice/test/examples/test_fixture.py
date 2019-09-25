'''
Simple fixture example.

import pytest


@pytest.fixture
def database():
    return < some database connection >


def test_insert(database):
    database.insert(123)
'''
