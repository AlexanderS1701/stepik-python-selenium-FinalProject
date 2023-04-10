from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        add_to_cart_btn.click()

    def should_be_message_about_product_added_to_basket(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        product_added_to_basket_message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE).text
        assert product_title == product_added_to_basket_message, f"Product {product_title} do not added to basket"
