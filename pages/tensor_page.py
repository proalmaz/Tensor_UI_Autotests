from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TensorPage(BasePage):
    POWER_BLOCK = (By.XPATH, "//p[contains(text(),'Сила в людях')]")
    ABOUT_LINK = (By.XPATH, "//a[contains(text(),'Подробнее') and @href='/about']")

    def check_power_in_people_block(self):
        return self.find_element(self.POWER_BLOCK) is not None

    def click_about(self):
        self.click(self.ABOUT_LINK)

