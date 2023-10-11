import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.questions_page_locators import QuestionPageLocators


class QuestionsPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переходим в раздел «Вопросы о важном»')
    def scroll_last_question(self):
        element = self.driver.find_element(*QuestionPageLocators.LOCATION_QUESTION_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_load_questions_page(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(QuestionPageLocators.QUESTIONS_HEADER))

    @allure.step('Нажимаем на вопрос')
    def click_question_button(self, button):
        self.driver.find_element(*button).click()

    def check_answer_text(self, answer, expected_text):
        actually_text = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(answer)).text
        assert actually_text == expected_text
