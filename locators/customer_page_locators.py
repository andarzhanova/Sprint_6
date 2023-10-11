from selenium.webdriver.common.by import By


class CustomerPageLocators:
    CUSTOMER_HEADER = (By.CLASS_NAME, 'Order_Header__BZXOb')  # Заголовок "Для кого самокат"
    NAME_FIELD = (By.CSS_SELECTOR, '[placeholder="* Имя"]')  # Поле "Имя"
    SURNAME_FIELD = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')  # Поле "Фамилия"
    ADDRESS_FIELD = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')  # Поле "Адрес"
    METRO_FIELD = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')  # Поле "Станция метро"
    PHONE_FIELD = (By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]')  # Поле "Телефон"
    CHERKIZ_METRO = (By.XPATH, '//div[text()="Черкизовская"]')  # Станция метро "Черкизовская"
    KURSK_METRO = (By.XPATH, '//div[text()="Курская"]')  # Станция метро "Курская"
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')  # Кнопка "Далее"
