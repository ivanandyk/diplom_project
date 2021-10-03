from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = "http://localhost:8000/"

    def open_base_page(self):
        self.driver.implicitly_wait(5)
        self.driver.get(self.base_page)

    def find_element(self, locator: tuple, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f'Can not find element {locator}')
