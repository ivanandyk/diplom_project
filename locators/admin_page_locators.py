from selenium.webdriver.common.by import By


class AdminPageLocators:

    LOCATOR_ADMIN_PAGE_CONTENT = (
        By.XPATH, "//div[@id='content']/h1")
    LOCATOR_ADMIN_PAGE_FIELD = (
        By.XPATH, "//tr[@class='model-group']/th/a")
