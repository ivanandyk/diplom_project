from pages.base_page import BasePage
from locators.admin_page_locators import AdminPageLocators


class AdminPage(BasePage):

    def check_admin_page(self):
        site_administration = self.find_element(
            AdminPageLocators.LOCATOR_ADMIN_PAGE_CONTENT).text
        assert site_administration == "Site administration"

    def open_group_page(self):
        self.find_element(
            AdminPageLocators.LOCATOR_ADMIN_PAGE_FIELD).click()
