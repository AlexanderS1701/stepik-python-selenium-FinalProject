from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_CART_BTN = (By.CLASS_NAME, 'btn-add-to-basket')
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
