from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from locators import StellarBurgersLocators as Locators
from utils import wait_for_element


def test_logout_from_account(authorized_driver):
    authorized_driver.get(Config.URLS["main"])
    wait_for_element(authorized_driver, Locators.ACCOUNT_BUTTON).click()
    wait_for_element(authorized_driver, Locators.LOGOUT_BUTTON).click()
    WebDriverWait(authorized_driver, 5).until(EC.url_to_be(Config.URLS["login"]))
    assert authorized_driver.current_url == Config.URLS["login"]
