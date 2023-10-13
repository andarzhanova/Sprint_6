from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_TOP_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')  # Верхняя кнопка "Заказать"
    ORDER_LOWER_BUTTON = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button')  # Нижняя кнопка "Заказать"
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')  # Логотип "Яндекс"
    PAYMENT_QUESTION_BUTTON = (By.ID, 'accordion__heading-0')  # Кнопка с вопросом об оплате
    PAYMENT_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-0"]/p')  # Текст ответа об оплате
    SEVERAL_SCOOTERS_QUESTION_BUTTON = (By.ID, 'accordion__heading-1')  # Кнопка с вопросом про несколько самокатов
    SEVERAL_SCOOTERS_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-1"]/p')  # Текст ответа про несколько самокатов
    RENTAL_TIME_QUESTION_BUTTON = (By.ID, 'accordion__heading-2')  # Кнопка с вопросом про время аренды
    RENTAL_TIME_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-2"]/p')  # Текст ответа про время аренды
    ORDER_TODAY_QUESTION_BUTTON = (By.ID, 'accordion__heading-3')  # Кнопка с вопросом про заказ сегодня
    ORDER_TODAY_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-3"]/p')  # Текст ответа про заказ сегодня
    LATER_EARLIER_QUESTION_BUTTON = (By.ID, 'accordion__heading-4')  # Кнопка с вопросом: вернуть позже/раньше
    LATER_EARLIER_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-4"]/p')  # Текст ответа про возврат позже/раньше
    CHARGING_QUESTION_BUTTON = (By.ID, 'accordion__heading-5')  # Кнопка с вопросом про зарядку
    CHARGING_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-5"]/p')  # Текст ответа про зарядку
    CANCEL_QUESTION_BUTTON = (By.ID, 'accordion__heading-6')  # Кнопка с вопросом об отмене
    CANCEL_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-6"]/p')  # Текст ответа про отмену
    LOCATION_QUESTION_BUTTON = (By.ID, 'accordion__heading-7')  # Кнопка с вопросом про МКАД
    LOCATION_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-7"]/p')  # Текст ответа про МКАД
