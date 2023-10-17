from .base_page import BasePage
from .data import RegistrationPageData
from .locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def input_login(self):
        registration_email = self.browser.find_element(*RegistrationPageLocators.REGISTRATION_EMAIL)
        registration_email.send_keys(*RegistrationPageData.REGISTRATION_EMAIL)

    def input_password(self):
        registration_password = self.browser.find_element(*RegistrationPageLocators.REGISTRATION_PASSWORD)
        registration_password.send_keys(*RegistrationPageData.REGISTRATION_PASSWORD)

    def input_password_confirm(self):
        registration_password_confirm = self.browser.find_element(*RegistrationPageLocators.REGISTRYPASSWORD_CONF)
        registration_password_confirm.send_keys(*RegistrationPageData.REGISTRATION_PASSWORD)

    def submit_button(self):
        registration_button = self.browser.find_element(*RegistrationPageLocators.REGISTRATION_BTN)
        registration_button.submit()

    def go_to_main_page(self):
        main_link = self.browser.find_element(*RegistrationPageLocators.MAIN_LINK)
        main_link.click()

    def go_to_login_page(self):
        register_link = self.browser.find_element(*RegistrationPageLocators.LOGIN_LINK)
        register_link.click()
