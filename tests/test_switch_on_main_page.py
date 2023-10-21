import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage


@allure.feature('Переход на главную страницу "Самоката"')
class TestOrderPage:
    @allure.title('Проверка перехода на главную страницу "Самоката"')
    @allure.description('Нажимаем на логотип "Самокат" и проверяем, что произошёл переход главную страницу "Самоката"')
    def test_switch_on_main_page_click_scooter_logo_main_page_url(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button(MainPageLocators.ORDER_TOP_BUTTON)
        order_page = OrderPage(driver)
        order_page.click_scooter_logo()
        main_page.check_switch_on_main_page()
        