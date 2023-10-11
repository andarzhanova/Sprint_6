import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class OrderStatusPage:

    scooter_logo = (By.XPATH, '//a[2]')  # Логотип "Самокат"

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на логотип "Самокат"')
    def click_scooter_logo(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(self.scooter_logo)).click()
