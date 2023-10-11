import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def driver():
    browser = webdriver.Firefox()
    browser.get("https://qa-scooter.praktikum-services.ru/")

    yield browser
    browser.quit()
