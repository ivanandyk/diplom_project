from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(
        executable_path="/Users/ivanandyk/Documents/Python/ftm/chromedriver",
        options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
