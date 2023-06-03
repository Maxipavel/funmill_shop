import time
import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.checkout_page import Checkout_page
from pages.end_page import End_page
from pages.login_page import Login_page
from pages.main_page import Main_page


@allure.description("Test_buy product")
def test_buy_product(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\Pavel\\PycharmProjects\\Resource\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Start test")
    # логинимся
    login = Login_page(driver_g)
    login.authorization()
    # входим в корзину чтобы удалить то, что было в ней
    enter_clear_cart_page = Main_page(driver_g)
    enter_clear_cart_page.select_cart_for_clear()
    clear_cart_page = Cart_page(driver_g)
    clear_cart_page.click_clear_cart()
    # возвращаемся в главное меню
    return_main = Cart_page(driver_g)
    return_main.click_return_main_page()
    # набираем игры в семейной категории
    choose_boardgames = Main_page(driver_g)
    choose_boardgames.select_product()
    # входим в корзину и нажимаем оплатить
    enter_cart_page = Cart_page(driver_g)
    enter_cart_page.click_place_order_button()
    # заполняем данные пользователя и делаем checkout
    checkout = Checkout_page(driver_g)
    checkout.input_checkout_information()
    # скроллим страницу вниз
    page_down_scroll = End_page(driver_g)
    page_down_scroll.scroll_down()
    #  Делаем скриншот заказа
    screenshot = End_page(driver_g)
    screenshot.screen()

    time.sleep(3)



