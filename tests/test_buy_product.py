import time

from selenium import webdriver


from pages.cart_page import Cart_page
from pages.checkout_page import Checkout_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.select_product_page import Select_product_page

def test_buy_product():
    driver = webdriver.Chrome()

    print('Start Test 1')

    login = Login_page(driver)
    login.authorization()
    time.sleep(5)

    mp = Main_page(driver)
    mp.select_categories()

    time.sleep(3)

    spp = Select_product_page(driver)
    spp.select_product()
    time.sleep(3)

    cp = Cart_page(driver)
    cp.product_confirmation()
    time.sleep(3)

    cip = Checkout_page(driver)
    cip.input_info()

    time.sleep(5)

    print('Finish test')

