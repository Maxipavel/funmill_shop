import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators

    place_order_button = "//a[@onclick='checkOut();']"
    clear_cart = "//a[@class='clear_cart']"
    return_to_main_page = "//span[@itemprop='title']"

    # Getters

    def select_place_order_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.place_order_button)))

    def select_clear_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.clear_cart)))

    def select_return_to_main_page(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.return_to_main_page)))


    # Actions

    def click_place_order_button(self):
        self.select_place_order_button().click()
        print("Click place order button")

    def click_select_clear_cart(self):
        self.select_clear_cart().click()
        print("Click select clear cart")

    def click_return_to_main_page(self):
        self.select_return_to_main_page().click()
        print("Click return to main page")


    # Methods

    def click_order_button(self):
        self.get_current_url()
        self.select_place_order_button()
        time.sleep(2)

    def click_clear_cart(self):
        self.click_select_clear_cart()
        time.sleep(2)

    def click_return_main_page(self):
        self.click_return_to_main_page()
        time.sleep(2)




