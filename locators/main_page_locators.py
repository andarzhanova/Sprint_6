from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_TOP_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')  # Верхняя кнопка "Заказать"
    ORDER_LOWER_BUTTON = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button')  # Нижняя кнопка "Заказать"
    YANDEX_LOGO = (By.XPATH, '//a[1]')  # Логотип "Яндекс"
