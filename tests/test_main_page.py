import time
import pytest
from pages.data import MainPageData
from pages.main_page import MainPage


@pytest.mark.regression
def test_go_to_login_page(browser):
    link = MainPageData.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot(r'..\screenshot\result5.png')


@pytest.mark.regression
def test_go_to_register_page(browser):
    link = MainPageData.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_register_page()
    browser.save_screenshot(r'..\screenshot\result11.png')


@pytest.mark.filter
def test_filter_by_parrot(browser):
    link = MainPageData.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.click_drop_down()
    time.sleep(5)
    page.choose_parrot()
    time.sleep(5)
    browser.save_screenshot(r'..\screenshot\result9.png')


@pytest.mark.filter
def test_filter_by_cat(browser):
    link = MainPageData.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.click_drop_down()
    time.sleep(5)
    page.choose_cat()
    time.sleep(5)
    browser.save_screenshot(r'..\screenshot\result10.png')


@pytest.mark.filter
def test_filter_by_name(browser):
    link = MainPageData.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.filter_by_name_input_name()
    browser.save_screenshot(r'..\screenshot\result12.png')
    time.sleep(5)


def test_go_to_page_3(browser):
    link = MainPageData.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.click_page_3()
    time.sleep(3)
    browser.save_screenshot(r'..\screenshot\result13.png')


def test_thumbs_up(browser):
    link = MainPageData.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.thumbs_up()
    time.sleep(5)
    browser.save_screenshot(r'..\screenshot\result19.png')
