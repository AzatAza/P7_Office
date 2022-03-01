from fixtures.locators.locators import LoginLocators
from fixtures.models.data import Data
from fixtures.pages.base_page import fill_element, click_element, open_auth_page, close_browser, get_list


def auth(is_submit: bool = True):
    """
    Fill in fields on the auth page and proceed to get OS
    """
    open_auth_page()
    fill_element(Data.random().first_name, locator=LoginLocators.LOGIN_FIRST_NAME)
    fill_element(Data.random().last_name, locator=LoginLocators.LOGIN_LAST_NAME)
    fill_element(Data.random().email, locator=LoginLocators.LOGIN_EMAIL)
    fill_element(Data.random().phone, locator=LoginLocators.LOGIN_PHONE)
    click_element(locator=LoginLocators.LOGIN_CHECKBOX_ACC)
    if is_submit:
        click_element(locator=LoginLocators.LOGIN_BTN)


def get_list_os():
    os = get_list(locator=LoginLocators.OS)
    return os


def quit_browser():
    close_browser()
