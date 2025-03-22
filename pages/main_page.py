from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    CONTACTS_BUTTON = (By.CSS_SELECTOR, "div.sbisru-Header-ContactsMenu")
    MODAL_WINDOW = (By.CSS_SELECTOR, "div.sbisru-Header-ContactsMenu__items")
    MORE_OFFICES_LINK = (By.CSS_SELECTOR, "div.sbisru-Header-ContactsMenu__items > a.sbisru-link.sbis_ru-link")

    def go_to_contacts(self):
        self.click(self.CONTACTS_BUTTON)
        self.find_element(self.MODAL_WINDOW)
        self.click(self.MORE_OFFICES_LINK)
