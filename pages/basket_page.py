from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), \
            'The basket has items, but it should not be.'

    def is_text_empty_basket_presented(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET), \
            'The text "empty basket" has not been presented, but it should.'
