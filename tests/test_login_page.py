import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.data import LoginPageData
from pages.locators import ProfilePageLocators
from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.regression
def test_login(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.input_login()
    page.input_password()
    page.submit_button()
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_PET_IMG))
    browser.save_screenshot(r'..\screenshot\result6.png')
    # profile = page.find_profile()
    # assert profile


@pytest.mark.regression
def test_go_to_main(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.go_to_main_page()
    time.sleep(3)
    browser.save_screenshot(r'..\screenshot\result7.png')


@pytest.mark.regression
def test_go_to_register(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.go_to_register_page()
    time.sleep(3)
    browser.save_screenshot(r'..\screenshot\result8.png')
