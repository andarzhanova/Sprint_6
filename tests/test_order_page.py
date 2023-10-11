import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from pages.customer_page import CustomerPage
from data.order_page_constants import OrderConstants
from locators.customer_page_locators import CustomerPageLocators
from pages.rental_page import RentalPage
from locators.rental_page_locators import RentalPageLocators
from pages.order_status_page import OrderStatusPage


@pytest.mark.usefixtures('driver')
class TestOrderPage:
    parameters = 'order_button, customer_data, metro_button, rental_data, days_button, colour_button'
    first_order_data = [MainPageLocators.ORDER_TOP_BUTTON, OrderConstants.FIRST_CUSTOMER,
                        CustomerPageLocators.CHERKIZ_METRO, OrderConstants.FIRST_RENTAL,
                        RentalPageLocators.ONE_DAY_BUTTON, RentalPageLocators.BLACK_BUTTON]
    second_order_data = [MainPageLocators.ORDER_LOWER_BUTTON, OrderConstants.SECOND_CUSTOMER,
                         CustomerPageLocators.KURSK_METRO, OrderConstants.SECOND_RENTAL,
                         RentalPageLocators.FOUR_DAYS_BUTTON, RentalPageLocators.GREY_BUTTON]

    @allure.title('Проверка оформления заказа')
    @allure.description(
        'Нажимаем кнопку заказать, заполняем форму заказа и проверяем, '
        'что появилось окно создания заказа с кнопкой "Посмотреть статус" '
    )
    @pytest.mark.parametrize(parameters, [first_order_data, second_order_data])
    def test_make_an_order_data_set_show_success_window(self, driver, order_button, customer_data, metro_button,
                                                        rental_data, days_button, colour_button):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.scroll_order_button(order_button)
        main_page.click_order_button(order_button)
        customer_page = CustomerPage(driver)
        customer_page.fill_out_customer_form(*customer_data, metro_button)
        rental_page = RentalPage(driver)
        rental_page.fill_out_rental_form(*rental_data, days_button, colour_button)
        rental_page.check_success_window()

    @allure.title('Проверка перехода на главную страницу "Самоката"')
    @allure.description('Нажимаем на логотип "Самокат" и проверяем, что произошёл переход главную страницу "Самоката"')
    def test_switch_on_main_page_click_scooter_logo_main_page_url(self, driver):
        rental_page = RentalPage(driver)
        rental_page.click_button_on_success_window()
        order_status_page = OrderStatusPage(driver)
        order_status_page.click_scooter_logo()
        main_page = MainPage(driver)
        main_page.check_switch_on_main_page()

    @allure.title('Проверка перехода на главную страницу Яндекса')
    @allure.description('Нажимаем на логотип "Яндекс" и проверяем, что произошёл переход главную страницу Яндекса')
    def test_switch_on_yandex_page_click_yandex_logo_yandex_page_url(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.check_switch_on_yandex()

    # @pytest.mark.parametrize(
    #     'order_button, customer_data, metro_button, rental_data, days_button, colour_button',
    #     [
    #         [MainPageLocators.ORDER_TOP_BUTTON, OrderConstants.FIRST_CUSTOMER, CustomerPageLocators.CHERKIZ_METRO,
    #          OrderConstants.FIRST_RENTAL, RentalPageLocators.ONE_DAY_BUTTON, RentalPageLocators.BLACK_BUTTON],
    #         [MainPageLocators.ORDER_LOWER_BUTTON, OrderConstants.SECOND_CUSTOMER, CustomerPageLocators.KURSK_METRO,
    #          OrderConstants.SECOND_RENTAL, RentalPageLocators.FOUR_DAYS_BUTTON, RentalPageLocators.GREY_BUTTON]
    #     ]
    # )
