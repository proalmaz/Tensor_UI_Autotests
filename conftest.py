import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

USE_LOCAL_DRIVER = os.getenv("USE_LOCAL_DRIVER", "false").lower() == "true"
CHROMEDRIVER_PATH = r"C:\chromedriver\chromedriver.exe"

def get_driver():
    if USE_LOCAL_DRIVER:
        service = Service(CHROMEDRIVER_PATH)
    else:
        service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service)


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    driver.maximize_window()
    yield driver
    driver.quit()
