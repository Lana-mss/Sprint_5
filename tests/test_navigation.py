from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from locators import StellarBurgersLocators as Locators


def test_personal_account_for_registered_user(authorized_driver):
    authorized_driver.get(Config.URLS["main"])
    authorized_driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    assert authorized_driver.current_url == Config.URLS["profile"]


def test_personal_account_for_unregistered_user(driver):
    driver.get(Config.URLS["main"])
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    assert driver.current_url == Config.URLS["login"]


def test_constructor_transition_from_account(authorized_driver):
    authorized_driver.get(Config.URLS["main"])
    authorized_driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    WebDriverWait(authorized_driver, 10).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)).click()
    WebDriverWait(authorized_driver, 5).until(EC.url_to_be(Config.URLS["main"]))
    assert authorized_driver.current_url == Config.URLS["main"]


def test_constructor_transition_from_logo(authorized_driver):
    authorized_driver.get(Config.URLS["main"])
    authorized_driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    WebDriverWait(authorized_driver, 10).until(EC.element_to_be_clickable(Locators.LOGO_BUTTON)).click()
    WebDriverWait(authorized_driver, 5).until(EC.url_to_be(Config.URLS["main"]))
    assert authorized_driver.current_url == Config.URLS["main"]


def test_sauces_section_transition(driver):
    driver.get(Config.URLS["main"])
    driver.find_element(*Locators.SAUCES_SECTION).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SAUCES_SECTION)).click()
    assert "Соусы" in driver.find_element(*Locators.SAUCES_SECTION).text


def test_toppings_section_transition(driver):
    driver.get(Config.URLS["main"])
    driver.find_element(*Locators.TOPPINGS_SECTION).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.TOPPINGS_SECTION)).click()
    assert "Начинки" in driver.find_element(*Locators.TOPPINGS_SECTION).text


def test_buns_section_transition(driver):
    driver.get(Config.URLS["main"])
    driver.find_element(*Locators.SAUCES_SECTION).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SAUCES_SECTION)).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUNS_SECTION)).click()
    assert "Булки" in driver.find_element(*Locators.BUNS_SECTION).text
