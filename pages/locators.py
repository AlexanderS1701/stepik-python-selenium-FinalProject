from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/1"
    LOGIN_FORM = (By.ID, "login_form1")
    REGISTER_FORM = (By.ID, "register_form1")