import pytest
import myapp


@pytest.fixture(params=["mysql", "postgresql"])
def database(request):
    d = myapp.driver(request.param)
    d.start()
    yield d
    d.stop()


def test_insert(database):
    database.insert("somedata")
