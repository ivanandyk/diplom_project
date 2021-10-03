from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def check_login(self):
        django_administration = self.find_element(
            LoginPageLocators.LOCATOR_LOGIN_PAGE_FORM).text
        assert django_administration == "Django administration", \
            f"Select group to change not eq {django_administration}"

    def login_steps(self):
        username = self.find_element(
            LoginPageLocators.LOCATOR_LOGIN_PAGE_USERNAME)
        username.send_keys("admin")
        password = self.find_element(
            LoginPageLocators.LOCATOR_LOGIN_PAGE_PASSWORD)
        password.send_keys("password")
        submit = self.find_element(
            LoginPageLocators.LOCATOR_LOGIN_PAGE_SUBMIT)
        submit.click()
