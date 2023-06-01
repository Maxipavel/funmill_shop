import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class End_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators

    pop_up_message = "//div[@class='toast toast_show']"

    # Getters

    def pop_up_warning_phone(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.pop_up_message)))

    # Actions
    def scroll_down_page(self):
        self.driver_g.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("Scroll page down")

    def screenshot(self):
        self.get_screenshot()
        print("Get screenshot")

    def pop_up(self):
        self.pop_up_warning_phone().click()
        print("Pop up warning phone message - DONE!")

    # Methods

    def scroll_down(self):
        self.scroll_down_page()

    def screen(self):
        self.get_current_url()
        time.sleep(3)
        self.pop_up()
        self.screenshot()




