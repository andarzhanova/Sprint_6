import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import Keys
from locators.rental_page_locators import RentalPageLocators


class RentalPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_rental_page(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(RentalPageLocators.RENTAL_HEADER))

    def set_date(self, date):
        self.driver.find_element(*RentalPageLocators.DATE_FIELD).send_keys(date)

    def click_enter(self):
        self.driver.find_element(*RentalPageLocators.DATE_FIELD).send_keys(Keys.ENTER)

    def click_period_field(self):
        self.driver.find_element(*RentalPageLocators.PERIOD_FIELD).click()

    def click_days_button(self, days_button):
        self.driver.find_element(*days_button).click()

    def click_colour_button(self, colour_button):
        self.driver.find_element(*colour_button).click()

    def set_comment(self, comment):
        self.driver.find_element(*RentalPageLocators.COMMENT_FIELD).send_keys(comment)

    def click_order_button(self):
        self.driver.find_element(*RentalPageLocators.ORDER_BUTTON).click()

    def wait_for_load_order_header(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(RentalPageLocators.ORDER_HEADER))

    def click_yes_button(self):
        self.driver.find_element(*RentalPageLocators.YES_BUTTON).click()

    @allure.step('Заполняем форму "Про аренду"')
    def fill_out_rental_form(self, date, comment, days_button, colour_button):
        self.wait_for_load_rental_page()
        self.set_date(date)
        self.click_enter()
        self.click_period_field()
        self.click_days_button(days_button)
        self.click_colour_button(colour_button)
        self.set_comment(comment)
        self.click_order_button()
        self.wait_for_load_order_header()
        self.click_yes_button()

    def check_success_window(self):
        actually_text = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(RentalPageLocators.BUTTON_ON_SUCCESS_WINDOW)).text
        assert actually_text == 'Посмотреть статус', 'Окно создания заказа с кнопкой "Посмотреть статус" не появилось'

    @allure.step('Нажимаем кнопку "Посмотреть статус"')
    def click_button_on_success_window(self):
        self.driver.find_element(*RentalPageLocators.BUTTON_ON_SUCCESS_WINDOW).click()
