from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    REGISTER_LINK = (By.XPATH, "//*[@id='app']/header[1]/div[1]/ul[1]/li[2]/a[1]/span[1]")
    DROP_DOWN_FILTER = (By.CLASS_NAME, "p-dropdown-trigger")
    DROP_DOWN_PARROT = (By.XPATH, "//li[@id='pv_id_2_4']")
    DROP_DOWN_CAT = (By.XPATH, "//li[@id='pv_id_2_1']")
    FILTER_NAME = (By.XPATH, "//*[@id='petName']")
    PAGE_3 = (By.XPATH, "//*[@id='app']/main[1]/div[1]/div[2]/div[3]/span[1]/button[3]")
    THUMBS_UP = (
    By.XPATH, "//*[@id='app']/main[1]/div[1]/div[2]/div[2]/div[1]/div[5]/div[1]/div[3]/div[2]/span[1]/i[1]")


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")
    MAIN_LINK = (By.XPATH, "//*[@id='app']/header[1]/div[1]/div[1]/img[1]")
    REGISTER_LINK = (By.XPATH, "//*[@id='app']/header[1]/div[1]/ul[1]/li[2]/a[1]/span[1]")


class RegistrationPageLocators:
    REGISTRATION_EMAIL = (By.XPATH, "//*[@id='login']")
    REGISTRATION_PASSWORD = (By.XPATH, "//input[@type='password']")
    REGISTRYPASSWORD_CONF = (By.XPATH, "//div[@id='confirm_password']/input")
    REGISTRATION_BTN = (By.XPATH, "//div[@id='pv_id_2_content']/div/form/div[4]/button/span[2]")
    MAIN_LINK = (By.XPATH, "//*[@id='app']/header[1]/div[1]/div[1]/img[1]")
    LOGIN_LINK = (By.XPATH, "//*[@id='app']/header[1]/div[1]/ul[1]/li[1]/a[1]/span[1]")


class ProfilePageLocators:
    PROFILE_PET_IMG = (By.XPATH, "//*[@id='app']/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/img[1]")
    ADD_PET_BUTTON = (By.XPATH, "//*[@id='app']/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]")
    ADD_PET_NAME = (By.ID, "name")
    CHOOSE_PET_TYPE = (By.XPATH, "//*[@id='typeSelector']")
    CHOOSE_PET_TYPE_CAT = (By.XPATH, "//li[contains(.,'cat')]")
    CHOOSE_PET_GENDER = (By.XPATH, "//*[@id='genderSelector']")
    CHOOSE_PET_GENDER_MALE = (By.XPATH, "//li[contains(.,'Male')]")
    ADD_PET_AGE = (By.XPATH, "//*[@id='age']/input[1]")
    SUBMIT_ADD_PET_BTN = (By.XPATH, "//*[@id='app']/main[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[3]/button[1]")
    CHOOSE_PHOTO_BTN = (By.XPATH, "//*[@id='app']/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span[1]")
    SUBMIT_PHOTO_BTN = (By.XPATH, "//*[@id='app']/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span[1]/span[2]")

    DELETE_PET_BTN = (By.XPATH, "//div[@id='app']/main/div/div/div[2]/div/div/div/div[2]/button[2]/span[2]")
    SUBMIT_DELETE_PET_BTN = (By.XPATH, "//span[contains(.,'Yes')]")
