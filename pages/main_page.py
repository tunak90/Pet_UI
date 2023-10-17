import pyautogui
from .base_page import BasePage
from .data import MainPageData
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_register_page(self):
        register_link = self.browser.find_element(*MainPageLocators.REGISTER_LINK)
        register_link.click()

    def click_page_3(self):
        page_3 = self.browser.find_element(*MainPageLocators.PAGE_3)
        page_3.doubleclick()

    def click_drop_down(self):
        drop_down_filter = self.browser.find_element(*MainPageLocators.DROP_DOWN_FILTER)
        drop_down_filter.click()

    def choose_parrot(self):
        drop_down_parrot = self.browser.find_element(*MainPageLocators.DROP_DOWN_CAT)
        drop_down_parrot.click()

    def choose_cat(self):
        drop_down_cat = self.browser.find_element(*MainPageLocators.DROP_DOWN_CAT)
        drop_down_cat.click()

    def filter_by_name_input_name(self):
        fill_name = self.browser.find_element(*MainPageLocators.FILTER_NAME)
        fill_name.send_keys(MainPageData.FILTER_BY_NAME)
        pyautogui.press('enter')

    def thumbs_up(self):
        thumbs = self.browser.find_element(*MainPageLocators.THUMBS_UP)
        thumbs.click()
