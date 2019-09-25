'''
No waste of computing power

import pytest

@pytest.fixture(scope="module")
def database():
    db = < some database connection >
    yield db
    db.close()


def test_insert(database):
    database.insert(123)

'''
