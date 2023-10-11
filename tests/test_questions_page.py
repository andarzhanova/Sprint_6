import pytest
import allure
from locators.questions_page_locators import QuestionPageLocators
from pages.questions_page import QuestionsPage
from data.question_page_constants import AnswerConstants


@pytest.mark.usefixtures('driver')
class TestQuestionPage:

    @allure.title('Проверка открытия текста ответа')
    @allure.description('Нажимаем на вопрос и проверяем, что открылся соответствующий текст ответа')
    @pytest.mark.parametrize(
        'button, answer, expected_text',
        [
            [QuestionPageLocators.PAYMENT_QUESTION_BUTTON, QuestionPageLocators.PAYMENT_ANSWER,
             AnswerConstants.PAYMENT_ANSWER],
            [QuestionPageLocators.SEVERAL_SCOOTERS_QUESTION_BUTTON, QuestionPageLocators.SEVERAL_SCOOTERS_ANSWER,
             AnswerConstants.SEVERAL_SCOOTERS_ANSWER],
            [QuestionPageLocators.RENTAL_TIME_QUESTION_BUTTON, QuestionPageLocators.RENTAL_TIME_ANSWER,
             AnswerConstants.RENTAL_TIME_ANSWER],
            [QuestionPageLocators.ORDER_TODAY_QUESTION_BUTTON, QuestionPageLocators.ORDER_TODAY_ANSWER,
             AnswerConstants.ORDER_TODAY_ANSWER],
            [QuestionPageLocators.LATER_EARLIER_QUESTION_BUTTON, QuestionPageLocators.LATER_EARLIER_ANSWER,
             AnswerConstants.LATER_EARLIER_ANSWER],
            [QuestionPageLocators.CHARGING_QUESTION_BUTTON, QuestionPageLocators.CHARGING_ANSWER,
             AnswerConstants.CHARGING_ANSWER],
            [QuestionPageLocators.CANCEL_QUESTION_BUTTON, QuestionPageLocators.CANCEL_ANSWER,
             AnswerConstants.CANCEL_ANSWER],
            [QuestionPageLocators.LOCATION_QUESTION_BUTTON, QuestionPageLocators.LOCATION_ANSWER,
             AnswerConstants.LOCATION_ANSWER]
        ]
    )
    def test_dropdown_list_click_on_button_show_answer_text(self, driver, button, answer, expected_text):
        questions_page = QuestionsPage(driver)
        questions_page.scroll_last_question()
        questions_page.wait_for_load_questions_page()
        questions_page.click_question_button(button)
        questions_page.check_answer_text(answer, expected_text)
