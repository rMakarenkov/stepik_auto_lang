import time
import credentials

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_different_languages(browser):
    browser.get(credentials.URL)
    time.sleep(3)
    WebDriverWait(browser, 5).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#default > header > div.navbar.primary.navbar-static-top.navbar-inverse > div")))
    assert browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button") is not None, "Element not found in base URL"
