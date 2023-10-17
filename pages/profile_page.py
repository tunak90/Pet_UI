from .base_page import BasePage
from .data import ProfilePageData
from .locators import ProfilePageLocators


class ProfilePage(BasePage):
    def go_to_add_pet_button(self):
        add_pet_button = self.browser.find_element(*ProfilePageLocators.ADD_PET_BUTTON)
        add_pet_button.click()

    def go_to_add_pet_name(self):
        add_pet_name = self.browser.find_element(*ProfilePageLocators.ADD_PET_NAME)
        add_pet_name.send_keys(*ProfilePageData.NAME_PET)

    def go_to_choose_pet_type(self):
        choose_pet_type = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_TYPE)
        choose_pet_type.click()

    def choose_pet_type_cat(self):
        choose_pet_type_cat = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_TYPE_CAT)
        choose_pet_type_cat.click()

    def go_to_choose_pet_gender(self):
        choose_pet_gender = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_GENDER)
        choose_pet_gender.click()

    def choose_pet_gender_male(self):
        choose_pet_gender_male = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_GENDER_MALE)
        choose_pet_gender_male.click()

    def go_to_add_pet_age(self):
        add_pet_age = self.browser.find_element(*ProfilePageLocators.ADD_PET_AGE)
        add_pet_age.send_keys(*ProfilePageData.AGE_PET)

    def submit_add_pet_btn(self):
        submit_add_pet_btn = self.browser.find_element(*ProfilePageLocators.SUBMIT_ADD_PET_BTN)
        submit_add_pet_btn.submit()

    def send_pet_photo(self):
        send_pet_photo = self.browser.find_element(*ProfilePageLocators.CHOOSE_PHOTO_BTN)
        send_pet_photo.send_keys(r"..\dog-puppy.jpg")


    def submit_add_pet_photo(self):
        submit_add_pet_photo = self.browser.find_element(*ProfilePageLocators.SUBMIT_PHOTO_BTN)
        submit_add_pet_photo.click()

    def go_to_delete_pet_button(self):
        delete_pet_button = self.browser.find_element(*ProfilePageLocators.DELETE_PET_BTN)
        delete_pet_button.click()

    def submit_delete_pet_button(self):
        submit_delete_pet_button = self.browser.find_element(*ProfilePageLocators.SUBMIT_DELETE_PET_BTN)
        submit_delete_pet_button.click()
