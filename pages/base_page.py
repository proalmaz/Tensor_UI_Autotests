from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_for_text(self, locator, expected_text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, expected_text))

    def wait_for_url(self, expected_url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(expected_url_part))

    def wait_for_title(self, expected_title, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.title_is(expected_title))

    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])