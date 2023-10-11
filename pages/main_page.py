import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def get_main_page(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def scroll_order_button(self, button):
        element = self.driver.find_element(*button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажимаем кнопку «Заказать»')
    def click_order_button(self, button):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(button)).click()

    def check_switch_on_main_page(self):
        current_url = self.driver.current_url
        assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.step('Нажимаем на логотип "Яндекс"')
    def click_yandex_logo(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.YANDEX_LOGO)).click()

    def check_switch_on_yandex(self):
        current_url = self.driver.current_url
        print(current_url)
        assert current_url == "https://dzen.ru/?yredirect=true", "Главная страница Яндекса не открылась"
