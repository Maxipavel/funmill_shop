from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger
import allure

class Login_page(Base):

    url = 'https://funmill.ru/personal/'

    # Locators

    user_name = "//input[@name='USER_LOGIN']"
    password = "//input[@name='USER_PASSWORD']"
    login_button = "//input[@name='Login']"
    main_word = "//h1[@class='fm-page-title']"

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods

    def authorization(self):
        with allure.step("Аuthorization"):
            Logger.add_start_step(method='authorization')
            self.driver_g.get(self.url)
            self.driver_g.maximize_window()
            self.get_current_url()
            self.input_user_name('maxipavel@gmail.com')
            self.input_password('1234ASDgf')
            self.click_login_button()
            self.assert_word(self.get_main_word(), 'Личный кабинет')
            Logger.add_end_step(url=self.driver_g.current_url, method='authorization')

