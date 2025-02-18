from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from locators import StellarBurgersLocators as Locators
from utils import generate_unique_email, generate_valid_password, generate_invalid_password


def test_successful_registration(driver):
    email = generate_unique_email()
    password = generate_valid_password()
    driver.get(Config.URLS["register"])
    driver.find_element(*Locators.REGISTER_NAME_INPUT).send_keys("Тест")
    driver.find_element(*Locators.REGISTER_EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.REGISTER_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Config.URLS["login"]))
    assert driver.current_url == Config.URLS["login"]


def test_registration_with_short_password(driver):
    email = generate_unique_email()
    password = generate_invalid_password()
    driver.get(Config.URLS["register"])
    driver.find_element(*Locators.REGISTER_NAME_INPUT).send_keys("Тест")
    driver.find_element(*Locators.REGISTER_EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.REGISTER_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    error_message = driver.find_element(*Locators.REGISTER_ERROR_MESSAGE).text
    assert "Некорректный пароль" in error_message
