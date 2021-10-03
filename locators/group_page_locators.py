from selenium.webdriver.common.by import By


class GroupPageLocators:

    LOCATOR_GROUP_PAGE_CONTENT = (
        By.XPATH, "//div[@id='content']/h1")
    LOCATOR_GROUP_PAGE_TEXT = (
        By.XPATH, "//input[@type='text']")
    LOCATOR_GROUP_PAGE_SUBMIT = (
        By.XPATH, "//input[@type='submit']")
    LOCATOR_GROUP_PAGE_RESULT = (
        By.XPATH, "//table[@id='result_list']/tbody/tr/th/a")
