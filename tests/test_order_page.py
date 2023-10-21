import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from data.order_page_constants import OrderConstants


@allure.feature('Заказ самоката')
class TestOrderPage:

    @allure.title('Проверка оформления заказа')
    @allure.description(
        'Нажимаем кнопку заказать, заполняем форму заказа и проверяем, '
        'что появилось окно создания заказа с кнопкой "Посмотреть статус" '
    )
    @pytest.mark.parametrize(
        'order_button, customer_data, metro_button, rental_data, days_button, colour_button',
        [
            [MainPageLocators.ORDER_TOP_BUTTON, OrderConstants.FIRST_CUSTOMER, OrderPageLocators.CHERKIZ_METRO,
             OrderConstants.FIRST_RENTAL, OrderPageLocators.ONE_DAY_BUTTON, OrderPageLocators.BLACK_BUTTON],
            [MainPageLocators.ORDER_LOWER_BUTTON, OrderConstants.SECOND_CUSTOMER, OrderPageLocators.KURSK_METRO,
             OrderConstants.SECOND_RENTAL, OrderPageLocators.FOUR_DAYS_BUTTON, OrderPageLocators.GREY_BUTTON]
        ]
    )
    def test_make_an_order_data_set_show_success_window(self, driver, order_button, customer_data, metro_button,
                                                        rental_data, days_button, colour_button):
        main_page = MainPage(driver)
        main_page.click_order_button(order_button)
        order_page = OrderPage(driver)
        order_page.fill_out_customer_form(*customer_data, metro_button)
        order_page.click_next_button()
        order_page.fill_out_rental_form(*rental_data, days_button, colour_button)
        order_page.click_order_button()
        order_page.wait_for_load_order_header()
        order_page.click_yes_button()
        order_page.check_success_window()
