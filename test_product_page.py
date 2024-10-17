from .pages.product_page import CartButtonPage
from .pages.main_page import MainPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

    page = MainPage(browser, link)
    page.open()

    product_page = CartButtonPage(browser, browser.current_url)
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_added_item_to_cart()
