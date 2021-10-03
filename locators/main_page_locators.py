from selenium.webdriver.common.by import By


class MainPageLocators:

    LOCATOR_MAIN_PAGE_APP = (
        By.XPATH, "//h1[@class='jumbotron-heading']")
    LOCATOR_MAIN_PAGE_SUBMIT = (
        By.XPATH, "//a[@class='btn btn-primary my-2']")
