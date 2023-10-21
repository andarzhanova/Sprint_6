import allure
from pages.main_page import MainPage
from pages.dzen_page import DzenPage


@allure.feature('Переход на главную страницу "Дзен"')
class TestOrderPage:
    @allure.title('Проверка перехода на главную страницу "Дзен"')
    @allure.description('Нажимаем на логотип "Яндекс" и проверяем, что произошёл переход главную страницу "Дзен"')
    def test_switch_on_yandex_page_click_yandex_logo_yandex_page_url(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_on_yandex()
        dzen_page = DzenPage(driver)
        dzen_page.check_switch_on_yandex()
