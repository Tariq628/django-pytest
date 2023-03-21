import pytest
# function   Run once per test
# class   Run once per class of test
# module   Run once per module OR fixture_1 run only once
# session   Run once per session OR fixture_1 run everytime when funnction run in session


# fixture_1 run everytime when funnction run in session
@pytest.fixture(scope="session")
def fixture_1():
    print("Run fixture 1")
    return 1


def test_example1(fixture_1):
    print("Run-example-1")
    num = fixture_1
    assert num == 1


def test_example2(fixture_1):
    print("Run-example-2")
    num = fixture_1
    assert num == 1
