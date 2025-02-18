from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from locators import StellarBurgersLocators as Locators
from utils import login_user


def test_login_via_main_button(driver, registered_user):
    email, password = registered_user
    driver.get(Config.URLS["main"])
    driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
    login_user(driver, email, password)
    WebDriverWait(driver, 5).until(EC.url_to_be(Config.URLS["main"]))
    assert driver.current_url == Config.URLS["main"]


def test_login_via_account_button(driver, registered_user):
    email, password = registered_user
    driver.get(Config.URLS["main"])
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    login_user(driver, email, password)
    WebDriverWait(driver, 5).until(EC.url_to_be(Config.URLS["main"]))
    assert driver.current_url == Config.URLS["main"]


def test_login_via_register_form(driver, registered_user):
    email, password = registered_user
    driver.get(Config.URLS["register"])
    driver.find_element(*Locators.LOGIN_LINK_FROM_REGISTER).click()
    login_user(driver, email, password)
    WebDriverWait(driver, 5).until(EC.url_to_be(Config.URLS["main"]))
    assert driver.current_url == Config.URLS["main"]


def test_login_via_forgot_password_form(driver, registered_user):
    email, password = registered_user
    driver.get(Config.URLS["forgot_password"])
    driver.find_element(*Locators.LOGIN_LINK_FROM_FORGOT_PASSWORD).click()
    login_user(driver, email, password)
    WebDriverWait(driver, 5).until(EC.url_to_be(Config.URLS["main"]))
    assert driver.current_url == Config.URLS["main"]
