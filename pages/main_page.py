from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def check_main_page(self):
        simple_django_application = self.find_element(
            MainPageLocators.LOCATOR_MAIN_PAGE_APP).text
        assert simple_django_application == "Simple Django Application",\
            f"Simple Django Application not eq {simple_django_application}"

    def open_admin_page(self):
        self.find_element(
            MainPageLocators.LOCATOR_MAIN_PAGE_SUBMIT).click()
