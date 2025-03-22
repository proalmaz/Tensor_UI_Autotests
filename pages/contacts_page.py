from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactsPage(BasePage):
    TENSOR_BANNER = (By.CSS_SELECTOR, "div.sbisru-Contacts__border-left--border-xm > a.sbisru-Contacts__logo-tensor")
    REGION_TEXT = (By.XPATH, "//div[contains(@class, 'sbisru-Contacts__relative')]//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    PARTNERS_TEXT = (By.CSS_SELECTOR, "div.sbisru-Contacts-List__item")
    REGIONS_WINDOW = (By.CSS_SELECTOR, "div.sbis_ru-Region-Panel")

    def click_tensor_banner(self):
        self.click(self.TENSOR_BANNER)
        self.switch_to_last_window()

    def get_region(self):
        return self.find_element(self.REGION_TEXT).text

    def get_partners_list(self):
        return self.find_elements(self.PARTNERS_TEXT)

    def change_region(self, region_name):
        self.click(self.REGION_TEXT)
        self.find_element(self.REGIONS_WINDOW)

        target_region = (By.XPATH, f"//li[contains(@class, 'sbis_ru-Region-Panel__item')]//span[contains(text(),'{region_name}')]")
        self.click(target_region)

        self.wait_for_text(self.REGION_TEXT, region_name)

    def wait_for_page_load(self, expected_url_part, expected_title, timeout=10):
        self.wait_for_url(expected_url_part, timeout)
        self.wait_for_title(expected_title, timeout)
