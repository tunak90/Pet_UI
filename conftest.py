import pytest
from selenium import webdriver
from pages.data import LoginPageData
from pages.login_page import LoginPage


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture()
def login(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.input_login()
    page.input_password()
    page.submit_button()
