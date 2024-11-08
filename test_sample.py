import os

import allure
import pytest


@pytest.fixture
def my_fixture():
    print("测试函数前运行")  # set up
    yield
    print("测试函数后运行")  # tear down


# content of test_sample.py
def inc(x):
    return x + 1


@pytest.mark.xfail
def test_answer():
    assert inc(3) == 5


@pytest.mark.parametrize("x,y", [(1, 2), (3, 4)])
@pytest.mark.usefixtures("my_fixture")
def test_sleep(x, y):
    assert x + y


@allure.feature("User")
@allure.story("Login")
@allure.title("User logs in")
@allure.severity("minor")
@allure.issue("https://github.com/allure-framework/allure-python/issues/1")
@allure.testcase("https://github.com/allure-framework/allure-python/issues/1")
@allure.description("""User logs in""")
@allure.epic("Allure")
@allure.parent_suite("Suite")
@allure.suite("Smoke")
@allure.sub_suite("SubSuite")
@allure.tag("tag1", "tag2")
@allure.link("http://google.com", name="Login")
@allure.id("1234567890")
@pytest.mark.parametrize("x,y", [(1, 2), (3, 4)])
def test_login(x, y, my_fixture):
    with allure.step("User logs in"):
        assert 1 == 1

    with allure.step("User logs in 1111"):
        assert 2 == 2


if __name__ == "__main__":
    pytest.main()

