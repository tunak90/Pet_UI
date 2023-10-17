from .base_page import BasePage
from .data import LoginPageData
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def input_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(*LoginPageData.LOGIN_EMAIL)

    def input_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(*LoginPageData.LOGIN_PASS)

    def submit_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_button.submit()

    def go_to_main_page(self):
        main_link = self.browser.find_element(*LoginPageLocators.MAIN_LINK)
        main_link.click()

    def go_to_register_page(self):
        register_link = self.browser.find_element(*LoginPageLocators.REGISTER_LINK)
        register_link.click()

    # def find_profile(self):
    #     profile = self.browser.find_element(*LoginPageLocators.EXIT_BUTTON)
