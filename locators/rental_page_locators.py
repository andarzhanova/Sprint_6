from selenium.webdriver.common.by import By


class RentalPageLocators:
    RENTAL_HEADER = (By.CLASS_NAME, 'Order_Header__BZXOb')  # Заголовок "Про аренду"
    DATE_FIELD = (By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')  # Поле даты аренды
    PERIOD_FIELD = (By.CLASS_NAME, 'Dropdown-placeholder')  # Поле "Срок аренды"
    ONE_DAY_BUTTON = (By.XPATH, '//div[text() = "сутки"]')  # Кнопка "сутки"
    FOUR_DAYS_BUTTON = (By.XPATH, '//div[text() = "четверо суток"]')  # Кнопка "четверо суток"
    BLACK_BUTTON = (By.ID, 'black')  # Кнопка "черный"
    GREY_BUTTON = (By.ID, 'grey')  # Кнопка "серый"
    COMMENT_FIELD = (By.CSS_SELECTOR, '[placeholder="Комментарий для курьера"]')  # Поле для комментария
    ORDER_BUTTON = (By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text()="Заказать"]')  # Кнопка "заказать"
    ORDER_HEADER = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')  # Заголовок "Хотите оформить заказ?"
    YES_BUTTON = (By.XPATH, '//button[text()="Да"]')  # Кнопка "Да"
    BUTTON_ON_SUCCESS_WINDOW = (By.XPATH, '//button[text()="Посмотреть статус"]')  # Кнопка "Посмотреть статус"
