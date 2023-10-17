import uuid


class LoginPageData:
    LOGIN_PAGE_URL = "http://34.141.58.52:8080/#/login"
    LOGIN_EMAIL = "df@mail.ru"
    LOGIN_PASS = "hjk89"


class RegistrationPageData:
    REGISTRATION_PAGE_URL = "http://34.141.58.52:8080/#/register"
    e = uuid.uuid4().hex
    REGISTRATION_EMAIL = f"{e}@gmail.com"
    REGISTRATION_PASSWORD = "fgh7890"


class MainPageData:
    MAIN_PAGE_URL = "http://34.141.58.52:8080/#/"
    FILTER_BY_NAME = "Tosha"


class ProfilePageData:
    PROFILE_PAGE_URL = "http://34.141.58.52:8080/#/profile"
    NAME_PET = "Donald"
    AGE_PET = "3"
