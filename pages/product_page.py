from .base_page import BasePage
from .locators import CartPage


class CartButtonPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*CartPage.ADD_TO_CART_BUTTON_SELECTOR)
        add_to_cart_button.click()

    def should_be_added_item_to_cart(self):
        self.should_be_correct_item_name()
        self.should_be_correct_price()

    def should_be_correct_item_name(self):
        assert self.is_element_present(*CartPage.ITEM_NAME), "The item name has not been specified."
        item_name = self.browser.find_element(*CartPage.ITEM_NAME).text

        assert self.is_element_present(*CartPage.ITEM_NAME_IN_CART), "The item name has not been provided in the message."
        item_name_in_cart = self.browser.find_element(*CartPage.ITEM_NAME_IN_CART).text

        assert item_name == item_name_in_cart, "An incorrect item has been added to the cart."

    def should_be_correct_price(self):
        assert self.is_element_present(*CartPage.ITEM_PRICE), "The price of the item has not been provided."
        item_price = self.browser.find_element(*CartPage.ITEM_PRICE).text

        assert self.is_element_present(*CartPage.ITEM_PRICE_IN_CART), "The price of the item has not been specified in the message."
        item_price_in_cart = self.browser.find_element(*CartPage.ITEM_PRICE_IN_CART).text

        assert item_price == item_price_in_cart, "An incorrect price was presented in the cart."

