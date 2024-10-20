from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON_SELECTOR)
        add_to_cart_button.click()

    def should_be_message_disappear_after_adding_product(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The message has not disappeared."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The message presented product in the basket, but should not be"

    def should_be_correct_item_name(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), \
            "The item name has not been specified."
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text

        assert self.is_element_present(*ProductPageLocators.ITEM_NAME_IN_CART), \
            "The item name has not been provided in the message."
        item_name_in_cart = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_CART).text

        assert item_name == item_name_in_cart, "An incorrect item has been added to the cart."

    def should_be_correct_price(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), \
            "The price of the item has not been provided."
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text

        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE_IN_CART), \
            "The price of the item has not been specified in the message."
        item_price_in_cart = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_IN_CART).text

        assert item_price == item_price_in_cart, "An incorrect price was presented in the cart."

