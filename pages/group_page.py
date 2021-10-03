from pages.base_page import BasePage
from locators.group_page_locators import GroupPageLocators


class GroupPage(BasePage):

    def check_group_page(self):
        select_group_to_change = self.find_element(
            GroupPageLocators.LOCATOR_GROUP_PAGE_CONTENT).text
        assert select_group_to_change == "Select group to change", \
            f"Select group to change not eq {select_group_to_change}"

    def check_result(self, created_group):
        group_result = self.find_element(
            GroupPageLocators.LOCATOR_GROUP_PAGE_RESULT).text
        assert group_result == created_group, \
            f"created_group not eq {group_result}"
