import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from faker import Faker

class Checkout_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.fake = Faker()

    # locators

    adress_button = "//div[@class='bx-soa-pp-company-smalltitle bx-soa-delivery-title' and text()='Самовывоз из магазина (Пражская/Южная)']"
    payment_method_button = "//div[@class='bx-soa-pp-company-smalltitle' and text()='Наличными в магазине (Пражская)']"
    last_name = '//input[@data-code="LAST_NAME"]'
    first_name = '//input[@data-code="NAME"]'
    order_button = "//div[@id='bx-soa-properties']//div[@class='bx-soa-more']//div[@class='bx-soa-more-btn col-xs-12']//a[@class='btn btn-default btn-lg bx-soa-prop-order-save' and text()='Оформить заказ']"

    # Getters

    def get_adress_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.adress_button)))

    def get_payment_method_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_method_button)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))

    # Actions
    def generate_random_data(self):
        first_name = self.fake.first_name()  # Генерация случайного имени
        last_name = self.fake.last_name()  # Генерация случайной фамилии
        return first_name, last_name

    def input_first_name(self, first_name):
        first_name_element = self.get_first_name()
        self.scroll_to_element(first_name_element)
        self.get_first_name().send_keys(first_name)
        print('Input first name')

    def input_last_name(self, last_name):
        last_name_element = self.get_last_name()
        self.scroll_to_element(last_name_element)
        self.get_last_name().send_keys(last_name)
        print('Input last name')
        time.sleep(5)

    def click_adress_button(self):
        adress_button_element = self.get_adress_button()
        self.scroll_to_element(adress_button_element)
        self.get_adress_button().click()
        print('Click adress button')
        time.sleep(5)

    def click_payment_method_button(self):
        payment_method_button_element = self.get_payment_method_button()
        self.scroll_to_element(payment_method_button_element)
        self.get_payment_method_button().click()
        print('Click payment method button')
        time.sleep(3)

    def click_order_button(self):
        order_button_element = self.get_order_button()
        self.scroll_to_element(order_button_element)
        self.get_order_button().click()
        print('Click order button')
        time.sleep(3)


    # Methods
    def input_info(self):
        self.get_current_url()
        self.click_adress_button()
        self.click_payment_method_button()
        first_name, last_name = self.generate_random_data()
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.click_order_button()




