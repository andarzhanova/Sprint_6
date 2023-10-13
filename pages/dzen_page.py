import allure
from pages.base_page import BaselPage


class DzenPage(BaselPage):

    @allure.step('Проверяем, что открылась главная страница "Дзен"')
    def check_switch_on_yandex(self):
        current_url = self.get_current_url()
        assert current_url == "https://dzen.ru/?yredirect=true", 'Главная страница "Дзен" не открылась'
