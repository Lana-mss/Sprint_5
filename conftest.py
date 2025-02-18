import pytest
from selenium import webdriver

from utils import generate_unique_email, generate_valid_password, register_user, login_user


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.delete_all_cookies()
    browser.quit()


@pytest.fixture(scope="function")
def registered_user(driver):
    email = generate_unique_email()
    password = generate_valid_password()
    register_user(driver, email, password)
    return email, password


@pytest.fixture(scope="function")
def authorized_driver(driver):
    email = generate_unique_email()
    password = generate_valid_password()
    register_user(driver, email, password)
    login_user(driver, email, password)
    yield driver
