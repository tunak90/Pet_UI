import time
import pytest
from pages.data import ProfilePageData
from pages.profile_page import ProfilePage


@pytest.mark.smoke
def test_add_pet(browser, login):
    link = ProfilePageData.PROFILE_PAGE_URL
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_add_pet_button()
    page.go_to_add_pet_age()
    page.go_to_add_pet_name()
    page.go_to_choose_pet_type()
    time.sleep(2)
    page.choose_pet_type_cat()
    page.go_to_choose_pet_gender()
    time.sleep(2)
    page.choose_pet_gender_male()
    page.submit_add_pet_btn()
    time.sleep(4)
    page.send_pet_photo()
    time.sleep(3)
    page.submit_add_pet_photo()
    time.sleep(3)
    browser.save_screenshot(r'..\screenshot\result17.png')


def test_delete_pet(browser, login):
    link = ProfilePageData.PROFILE_PAGE_URL
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(5)
    page.go_to_delete_pet_button()
    page.submit_delete_pet_button()
    browser.save_screenshot(r'..\screenshot\result18.png')
