import time
import pytest
from pages.data import RegistrationPageData
from pages.registration_page import RegistrationPage


@pytest.mark.smoke
def test_registration(browser):
    link = RegistrationPageData.REGISTRATION_PAGE_URL
    page = RegistrationPage(browser, link)
    page.open()
    page.input_login()
    page.input_password()
    page.input_password_confirm()
    page.submit_button()
    time.sleep(3)
    browser.save_screenshot(r'..\screenshot\result14.png')


@pytest.mark.regression
def test_go_to_main(browser):
    link = RegistrationPageData.REGISTRATION_PAGE_URL
    page = RegistrationPage(browser, link)
    page.open()
    page.go_to_main_page()
    time.sleep(3)
    browser.save_screenshot(r'..\screenshot\result15.png')


@pytest.mark.regression
def test_go_to_login(browser):
    link = RegistrationPageData.REGISTRATION_PAGE_URL
    page = RegistrationPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot(r'..\screenshot\result16.png')
