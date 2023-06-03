import time

import allure
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Checkout_page(Base):

    # Locators

    city_name = "//input[@id='select-city']"
    drop_down_city_name = "//a[@data-name='Москва']"
    post_office = "//label[@class='radio-delivery rus_post']"
    bank_card = "//label[@class='radio-payment card_online']"
    buyer_name = "//input[@id='userNameInput']"
    buyer_email = "//input[@id='userEmailInput']"
    buyer_phone = "//input[@id='userPhoneInput']"
    buyer_adress = "//input[@id='userRusPostAddressInput']"
    buyer_zip = "//input[@id='userZIPInput']"
    approve_check = "//input[@class='agreeCheckbox']"
    buyer_commentary = "//textarea[@class='form-control custom-textarea']"
    buyer_checkout_button = "//button[@class='btn btn-default btn-lg btn-order-save']"


    # Getters

    def input_city_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_name)))
    def input_drop_down_city_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.drop_down_city_name)))
    def input_post_office(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.post_office)))
    def input_bank_card(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.bank_card)))
    def input_buyer_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.buyer_name)))
    def input_buyer_email(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.buyer_email)))
    def input_buyer_phone(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.buyer_phone)))
    def input_buyer_adress(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.buyer_adress)))
    def input_buyer_zip(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.buyer_zip)))
    def input_approve_check(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.approve_check)))
    def input_buyer_commentary(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.buyer_commentary)))
    def input_buyer_checkout_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.buyer_checkout_button)))

    # Actions

    def user_city_name_clear(self):
        self.input_city_name().clear()
        print("Clear checkout city name")

    def user_drop_down_city_name(self):
        self.input_drop_down_city_name().click()
        print("Click drop down bar")

    def user_city_name_checkout(self, city_name):
        self.input_city_name().send_keys(city_name)
        print("Input checkout city name")

    def user_post_office_checkout(self):
        self.input_post_office().click()
        print("Click checkout post office")

    def user_bank_card_checkout(self):
        self.input_bank_card().click()
        print("Click checkout bank card")

    def user_buyer_name_clear(self):
        self.input_buyer_name().clear()
        print("Clear buyer name")

    def user_buyer_name_checkout(self, buyer_name):
        self.input_buyer_name().send_keys(buyer_name)
        print("Input checkout buyer name")

    def user_buyer_email_clear(self):
        self.input_buyer_email().clear()
        print("Clear buyer email")

    def user_buyer_email_checkout(self, buyer_email):
        self.input_buyer_email().send_keys(buyer_email)
        print("Input checkout buyer email")

    def user_buyer_phone_checkout_click(self):
        self.input_buyer_phone().click()
        print("Click buyer phone checkout")

    def user_buyer_phone_checkout(self, buyer_phone):
        self.input_buyer_phone().send_keys(buyer_phone)
        print("Input checkout buyer phone. Специально ввел ошибочный номер, чтобы выскочила ошибка, так как иначе будет сделан заказ, что не хорошо по отношению к магазину")

    def user_buyer_adress_checkout(self, buyer_adress):
        self.input_buyer_adress().send_keys(buyer_adress)
        print("Input checkout buyer adress")

    def user_buyer_zip_checkout(self, buyer_zip):
        self.input_buyer_zip().send_keys(buyer_zip)
        print("Input checkout buyer zip")

    def user_approve_check_checkout(self):
        self.input_approve_check().click()
        print("Click checkout approve_check")

    def user_buyer_commentary_checkout(self, buyer_commentary):
        self.input_buyer_commentary().send_keys(buyer_commentary)
        print("Input checkout buyer commentary")

    def user_checkout_button_checkout(self):
        self.input_buyer_checkout_button().click()
        print("Click checkout button")

    # Methods

    def input_checkout_information(self):
        with allure.step("Input checkout information"):
            Logger.add_start_step(method='input_checkout_information')
            self.get_current_url()
            time.sleep(1)
            self.user_city_name_clear()
            time.sleep(1)
            self.user_city_name_checkout('Москва')
            time.sleep(2)
            self.user_drop_down_city_name()
            time.sleep(3)
            self.user_post_office_checkout()
            time.sleep(1)
            self.user_bank_card_checkout()
            time.sleep(1)
            self.user_buyer_name_clear()
            self.user_buyer_name_checkout('Иванов Иван Иванович')
            time.sleep(1)
            self.user_buyer_email_clear()
            self.user_buyer_email_checkout('proverka@mail.ru')
            time.sleep(1)
            self.user_buyer_phone_checkout_click()
            self.user_buyer_phone_checkout('92137647')
            time.sleep(1)
            self.user_buyer_adress_checkout('Археологическая улица 3, дом 2, кв 666')
            time.sleep(1)
            self.user_buyer_zip_checkout('192666')
            time.sleep(1)
            self.user_approve_check_checkout()
            time.sleep(1)
            self.user_buyer_commentary_checkout('Позвонить заранее, так как внизу злые бабки могут отобрать мои настолочки')
            time.sleep(1)
            self.user_checkout_button_checkout()
            Logger.add_end_step(url=self.driver_g.current_url, method='input_checkout_information')




