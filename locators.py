from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    # Главная страница
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Авторизация
    LOGIN_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Регистрация
    REGISTER_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    REGISTER_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    REGISTER_ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")

    # Переход на вход из разных форм
    LOGIN_LINK_FROM_REGISTER = (By.XPATH, "//a[text()='Войти']")
    LOGIN_LINK_FROM_FORGOT_PASSWORD = (By.XPATH, "//a[text()='Войти']")

    # Личный кабинет
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button__') and text()='Выход']")

    # Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__') and @href='/']")
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]")

    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")
    TOPPINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")
