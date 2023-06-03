import time

import allure
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    # Locators

    category_family = "//li[@class='catitem-10']"
    games_atlantis = "//a[@data-product-id='3395']"
    games_pachwork = "//a[@data-product-id='457']"
    games_project_l = "//a[@data-product-id='8090']"
    cart = "//div[@class='bx-hdr-profile']"


    # Getters

    def select_category_family(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_family)))

    def select_games_atlantis(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.games_atlantis)))

    def select_games_pachwork(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.games_pachwork)))

    def select_games_project_l(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.games_project_l)))

    def get_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions

    def click_category_family(self):
        self.select_category_family().click()
        print("Click family category")

    def click_games_atlantis(self):
        self.select_games_atlantis().click()
        print("Click game atlantis")

    def click_games_pachwork(self):
        self.select_games_pachwork().click()
        print("Click games pachwork")

    def click_games_project_l(self):
        self.select_games_project_l().click()
        print("Click games project_l")

    def click_cart(self):
        self.get_cart().click()
        print("Click Enter Cart")


    # Methods

    def select_product(self):
        with allure.step("Select product"):
            Logger.add_start_step(method='select_product')
            self.get_current_url()
            self.click_category_family()
            time.sleep(1)
            self.click_games_atlantis()
            time.sleep(1)
            self.click_games_pachwork()
            time.sleep(1)
            self.click_games_project_l()
            time.sleep(1)
            self.click_cart()
            Logger.add_end_step(url=self.driver_g.current_url, method='select_product')

    def select_cart_for_clear(self):
        Logger.add_start_step(method='select_cart_for_clear')
        self.get_current_url()
        self.click_cart()
        Logger.add_end_step(url=self.driver_g.current_url, method='select_cart_for_clear')




