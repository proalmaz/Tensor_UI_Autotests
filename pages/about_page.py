from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AboutPage(BasePage):
    WORK_IMAGES = (By.CSS_SELECTOR, ".tensor_ru-About__block3-image-wrapper")

    def get_work_images(self):
        return self.find_elements(self.WORK_IMAGES)

    def check_images_size(self):
        images = self.get_work_images()
        if not images:
            return False

        first_width = images[0].size.get("width")
        first_height = images[0].size.get('height')

        for img in images:
            if img.size.get("width") != first_width or img.size.get('height') != first_height:
                return False

        return True
