import pytest
from .pages.locators import ProductPageLocators
from .pages.product_page import CartButtonPage
from .pages.main_page import MainPage


@pytest.mark.parametrize('link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail
        ),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ])
def test_guest_can_add_product_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()

    product_page = CartButtonPage(browser, browser.current_url)
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()

    product_page.should_be_correct_item_name()
    product_page.should_be_correct_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0')
    page.open()

    product_page = CartButtonPage(browser, browser.current_url)
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()

    result = product_page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
    assert result is True, "The message presented after adding product to basket."


def test_guest_cant_see_success_message(browser):
    page = MainPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0')
    page.open()

    product_page = CartButtonPage(browser, browser.current_url)

    result = product_page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
    assert result is True, "The message presented product in the basket."


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = MainPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0')
    page.open()

    product_page = CartButtonPage(browser, browser.current_url)
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()

    result = product_page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
    assert result is True, "The message has not disappeared."
