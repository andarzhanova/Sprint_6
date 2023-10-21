import allure
from selenium.webdriver import Keys
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BaselPage


class OrderPage(BaselPage):

    @allure.step('Ожидаем загрузку окна "Для кого самокат"')
    def wait_for_load_customer_window(self):
        self.wait_for_visibility_of_element(OrderPageLocators.CUSTOMER_HEADER)

    @allure.step('Заполняем поле "Имя"')
    def set_name(self, name):
        self.send_keys(OrderPageLocators.NAME_FIELD, name)

    @allure.step('Заполняем поле "Фамилия"')
    def set_surname(self, surname):
        self.send_keys(OrderPageLocators.SURNAME_FIELD, surname)

    @allure.step('Заполняем поле "Адрес"')
    def set_address(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('Нажимаем на поле "Станция метро"')
    def click_metro_field(self):
        self.click_on_element(OrderPageLocators.METRO_FIELD)

    @allure.step('Выбираем метро из списка')
    def choose_metro(self, metro):
        self.scroll(metro)
        self.wait_for_element_to_be_clickable(metro)
        self.click_on_element(metro)

    @allure.step('Заполняем поле "Телефон"')
    def set_phone(self, phone):
        self.send_keys(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step('Заполняем форму "Для кого самокат"')
    def fill_out_customer_form(self, name, surname, address, phone, metro):
        self.wait_for_load_customer_window()
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_metro_field()
        self.choose_metro(metro)
        self.set_phone(phone)

    @allure.step('Нажимаем на кнопку "Далее"')
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Ожидаем загрузку окна "Про аренду"')
    def wait_for_load_rental_window(self):
        self.wait_for_visibility_of_element(OrderPageLocators.RENTAL_HEADER)

    @allure.step('Заполняем поле даты аренды')
    def set_date(self, date):
        self.send_keys(OrderPageLocators.DATE_FIELD, date)
        self.send_keys(OrderPageLocators.DATE_FIELD, Keys.ENTER)

    @allure.step('Нажимаем на поле "Срок аренды"')
    def click_period_field(self):
        self.click_on_element(OrderPageLocators.PERIOD_FIELD)

    @allure.step('Выбираем количество суток')
    def click_days_button(self, days_button):
        self.click_on_element(days_button)

    @allure.step('Выбираем цвет')
    def click_colour_button(self, colour_button):
        self.click_on_element(colour_button)

    @allure.step('Заполняем поле для комментария')
    def set_comment(self, comment):
        self.send_keys(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step('Заполняем форму "Про аренду"')
    def fill_out_rental_form(self, date, comment, days_button, colour_button):
        self.wait_for_load_rental_window()
        self.set_date(date)
        self.click_period_field()
        self.click_days_button(days_button)
        self.click_colour_button(colour_button)
        self.set_comment(comment)

    @allure.step('Нажимаем кнопку "Заказать"')
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Ожидаем загрузку окна "Хотите оформить заказ?"')
    def wait_for_load_order_header(self):
        self.wait_for_visibility_of_element(OrderPageLocators.ORDER_HEADER)

    @allure.step('Нажимаем кнопку "Да"')
    def click_yes_button(self):
        self.click_on_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Проверяем, что появилось окно создания заказа с кнопкой "Посмотреть статус"')
    def check_success_window(self):
        self.wait_for_visibility_of_element(OrderPageLocators.BUTTON_ON_SUCCESS_WINDOW)
        actually_text = self.get_actually_text(OrderPageLocators.BUTTON_ON_SUCCESS_WINDOW)
        assert actually_text == 'Посмотреть статус', 'Окно создания заказа с кнопкой "Посмотреть статус" не появилось'

    @allure.step('Нажимаем на логотип "Самокат"')
    def click_scooter_logo(self):
        self.wait_for_element_to_be_clickable(OrderPageLocators.SCOOTER_LOGO)
        self.click_on_element(OrderPageLocators.SCOOTER_LOGO)
