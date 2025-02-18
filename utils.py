import random
import string
from config import Config
from locators import StellarBurgersLocators as Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def generate_unique_email():
    return f"testuser_{''.join(random.choices(string.digits, k=5))}@yandex.ru"


def generate_valid_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


def generate_invalid_password():
    return ''.join(random.choices(string.ascii_letters, k=5))


def register_user(driver, email, password):
    driver.get(Config.URLS["register"])
    driver.find_element(*Locators.REGISTER_NAME_INPUT).send_keys("Тест")
    driver.find_element(*Locators.REGISTER_EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.REGISTER_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Config.URLS["login"]))


def login_user(driver, email, password):
    driver.get(Config.URLS["login"])
    driver.find_element(*Locators.LOGIN_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Config.URLS["main"]))


def wait_for_element(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
