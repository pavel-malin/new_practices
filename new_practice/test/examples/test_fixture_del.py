'''
Cleaning the scanned object.

import pytest

@pytest.fixture
def database():
    db = < some database connection >
    yield db
    db.close()

def test_insert(database):
    database.insert(123)
'''
