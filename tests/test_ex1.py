import pytest


@pytest.mark.xfail
@pytest.mark.skip
@pytest.mark.slow
def test_example():
    print("tariq")
    assert 1 == 1


def test_example1():
    assert 1 == 1
