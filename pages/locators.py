from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//header/div/div/div[2]/span/a")

class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4 h3 a")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_CART_BTN = (By.CLASS_NAME, 'btn-add-to-basket')
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
