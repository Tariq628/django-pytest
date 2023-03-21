import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user("test", "test@test.com", "test")
    count = User.objects.all().count()
    print(count)
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True


@pytest.fixture(scope="session")
# @pytest.fixture()
def user_1(db):
    user = User.objects.create_user("test-user")
    print("create-user")
    return user


def test_set_check_password1(user_1):
    print("check-user1")
    assert user_1.username == "test-user"


def test_set_check_password2(user_1):
    print("check-user2")
    assert user_1.username == "test-user"


@pytest.fixture
def new_user1(db, new_user_factory):
    #     # pytest -rP also print everything
    return new_user_factory("Test_user", "password", "MyName")


def test_new_user2(new_user2):
    assert new_user2.is_staff


@pytest.mark.django_db
def test_new_user(db, user_factory):
    user = user_factory.build()
    # user = user_factory.create()
    print(user)
    print(user_factory.username)
    print(User.objects.all().count())
    assert True


def test_product(product_factory):
    product = product_factory.build()
    print(product.description)
    assert True
