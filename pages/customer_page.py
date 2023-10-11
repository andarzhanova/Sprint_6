import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.customer_page_locators import CustomerPageLocators


class CustomerPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_customer_page(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(CustomerPageLocators.CUSTOMER_HEADER))

    def set_name(self, name):
        self.driver.find_element(*CustomerPageLocators.NAME_FIELD).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*CustomerPageLocators.SURNAME_FIELD).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*CustomerPageLocators.ADDRESS_FIELD).send_keys(address)

    def click_metro_field(self):
        self.driver.find_element(*CustomerPageLocators.METRO_FIELD).click()

    def scroll_metro(self, metro):
        element = self.driver.find_element(*metro)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_metro(self, metro):
        self.driver.find_element(*metro).click()

    def set_phone(self, phone):
        self.driver.find_element(*CustomerPageLocators.PHONE_FIELD).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*CustomerPageLocators.NEXT_BUTTON).click()

    @allure.step('Заполняем форму "Для кого самокат"')
    def fill_out_customer_form(self, name, surname, address, phone, metro):
        self.wait_for_load_customer_page()
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_metro_field()
        self.scroll_metro(metro)
        self.click_metro(metro)
        self.set_phone(phone)
        self.click_next_button()
