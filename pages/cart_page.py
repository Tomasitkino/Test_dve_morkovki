import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    checkout_button = '//button[@data-entity="basket-checkout-button"]'

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Actions
    def click_checkout_button(self):
        checkout_button_element = self.get_checkout_button()
        self.scroll_to_element(checkout_button_element)
        checkout_button_element.click()
        print("Click checkout button")
        time.sleep(10)



    # Methods
    def product_confirmation(self):
        self.get_current_url()
        self.click_checkout_button()


