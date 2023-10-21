import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BaselPage


class MainPage(BaselPage):

    @allure.step('Нажимаем кнопку «Заказать»')
    def click_order_button(self, button):
        self.scroll(button)
        self.wait_for_element_to_be_clickable(button)
        self.click_on_element(button)

    @allure.step('Проверяем, что открылась главная страница "Самоката"')
    def check_switch_on_main_page(self):
        current_url = self.get_current_url()
        assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.step('Нажимаем на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.YANDEX_LOGO)
        self.click_on_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Переходим на главную страницу "Дзен"')
    def switch_on_yandex(self):
        self.go_to_site('https://dzen.ru/?yredirect=true')

    @allure.step('Нажимаем на вопрос')
    def click_question_button(self, button):
        self.scroll(button)
        self.wait_for_element_to_be_clickable(button)
        self.click_on_element(button)

    @allure.step('Проверяем, что открылся соответствующий текст ответа')
    def check_answer_text(self, answer, expected_text):
        self.wait_for_visibility_of_element(answer)
        actually_text = self.get_actually_text(answer)
        assert actually_text == expected_text
