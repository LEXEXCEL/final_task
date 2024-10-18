from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM_SELECTOR = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM_SELECTOR = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON_SELECTOR = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_NAME_IN_CART = (By.CSS_SELECTOR, ".alert-noicon:nth-child(1) strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main [class='price_color']")
    ITEM_PRICE_IN_CART = (By.CSS_SELECTOR, ".alert-noicon:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")