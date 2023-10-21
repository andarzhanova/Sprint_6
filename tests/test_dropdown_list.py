import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data.main_page_constants import AnswerConstants


@allure.feature('Выпадающий список вопросов')
class TestQuestionPage:

    @allure.title('Проверка открытия текста ответа')
    @allure.description('Нажимаем на вопрос и проверяем, что открылся соответствующий текст ответа')
    @pytest.mark.parametrize(
        'button, answer, expected_text',
        [
            [MainPageLocators.PAYMENT_QUESTION_BUTTON, MainPageLocators.PAYMENT_ANSWER,
             AnswerConstants.PAYMENT_ANSWER],
            [MainPageLocators.SEVERAL_SCOOTERS_QUESTION_BUTTON, MainPageLocators.SEVERAL_SCOOTERS_ANSWER,
             AnswerConstants.SEVERAL_SCOOTERS_ANSWER],
            [MainPageLocators.RENTAL_TIME_QUESTION_BUTTON, MainPageLocators.RENTAL_TIME_ANSWER,
             AnswerConstants.RENTAL_TIME_ANSWER],
            [MainPageLocators.ORDER_TODAY_QUESTION_BUTTON, MainPageLocators.ORDER_TODAY_ANSWER,
             AnswerConstants.ORDER_TODAY_ANSWER],
            [MainPageLocators.LATER_EARLIER_QUESTION_BUTTON, MainPageLocators.LATER_EARLIER_ANSWER,
             AnswerConstants.LATER_EARLIER_ANSWER],
            [MainPageLocators.CHARGING_QUESTION_BUTTON, MainPageLocators.CHARGING_ANSWER,
             AnswerConstants.CHARGING_ANSWER],
            [MainPageLocators.CANCEL_QUESTION_BUTTON, MainPageLocators.CANCEL_ANSWER,
             AnswerConstants.CANCEL_ANSWER],
            [MainPageLocators.LOCATION_QUESTION_BUTTON, MainPageLocators.LOCATION_ANSWER,
             AnswerConstants.LOCATION_ANSWER]
        ]
    )
    def test_dropdown_list_click_on_button_show_answer_text(self, driver, button, answer, expected_text):
        main_page = MainPage(driver)
        main_page.click_question_button(button)
        main_page.check_answer_text(answer, expected_text)
