import pytest
from time import time
from math import pi as PI
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
from .pages.main_page import MainPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'

        # Generating email and password
        random_email = str(time()) + "@fakemail.org"
        random_password = str(time() * PI)

        # Registration user with generated email and password
        register = LoginPage(browser, link)
        register.open()
        register.go_to_login_page()
        register.register_new_user(random_email, random_password)

        # Assertion
        register.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = MainPage(browser, link)
        page.open()

        product_page = ProductPage(browser, browser.current_url)

        assert product_page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The message presented product in the basket."

    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = MainPage(browser, link)
        page.open()

        product_page = ProductPage(browser, browser.current_url)
        product_page.add_to_cart()
        product_page.solve_quiz_and_get_code()

        product_page.should_be_correct_item_name()
        product_page.should_be_correct_price()


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

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()

    product_page.should_be_correct_item_name()
    product_page.should_be_correct_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'

    page = MainPage(browser, link)
    page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()

    assert product_page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "The message presented after adding product to basket."


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'

    page = MainPage(browser, link)
    page.open()

    product_page = ProductPage(browser, browser.current_url)

    assert product_page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "The message presented product in the basket."


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'

    page = MainPage(browser, link)
    page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()

    result = product_page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
    assert result is True, "The message has not disappeared."


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    page = ProductPage(browser, link)
    page.open()

    login_page = LoginPage(browser, browser.current_url)
    login_page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.go_to_basket_page()

    basket_page.should_not_be_items_in_basket()
    basket_page.is_text_empty_basket_presented()
