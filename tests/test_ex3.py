import pytest


@pytest.fixture
def yield_fixture():
    print("Start test phase")
    yield 6
    print("End test phase")


def test_example(yield_fixture):
    print("Run exmaple 1")
    assert yield_fixture == 6
