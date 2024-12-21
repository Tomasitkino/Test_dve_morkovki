
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    categories_button = "//a[@class='top-menu__item-link  top-menu__item-link_catalog']"
    select_category = "//li[@class='menu-left__item menu-left__item_custom menu-left__item_custom' and @data-node='0']//a[@class='menu-left__item-link']"

    def get_categories_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.categories_button)))

    def get_select_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_category)))
    # Actions

    def click_categories_button(self):
        self.get_categories_button().click()
        print('Click menu category')

    def click_select_category(self):
        self.get_select_category().click()
        print('Click select category')

    # Methods
    def select_categories(self):
        self.get_current_url()
        self.click_categories_button()
        self.click_select_category()
