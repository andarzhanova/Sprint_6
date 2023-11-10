import allure
from selenium.webdriver.common.by import By
from pages.base_page import BaselPage


class DzenPage(BaselPage):
    DZEN_LOGO = (By.CLASS_NAME, 'desktop-base-header__logo-tA')  # Логотип "Дзен"

    @allure.step('Ожидаем загрузку главной страницы "Дзен"')
    def wait_for_load_dzen(self):
        self.wait_for_visibility_of_element(self.DZEN_LOGO)

    @allure.step('Проверяем, что открылась главная страница "Дзен"')
    def check_switch_on_yandex(self):
        current_url = self.get_current_url()
        assert current_url == "https://dzen.ru/?yredirect=true", 'Главная страница "Дзен" не открылась'
