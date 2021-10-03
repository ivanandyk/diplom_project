from selenium.webdriver.common.by import By


class LoginPageLocators:

    LOCATOR_LOGIN_PAGE_FORM = (
        By.XPATH, "//a[@href='/admin/']")
    LOCATOR_LOGIN_PAGE_USERNAME = (
        By.XPATH, "//*[@id='id_username']")
    LOCATOR_LOGIN_PAGE_PASSWORD = (
        By.XPATH, "//*[@id='id_password']")
    LOCATOR_LOGIN_PAGE_SUBMIT = (
        By.XPATH, "//input[@type='submit']")
