
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Login_page(Base):

    url = 'https://dvemorkovki.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    enter_button = "//a[@class='top-menu-profile-button header__button button button_theme_liner-green auth-modal-link']"
    user_name = "//input[@class='form__control feedback-form__control feedback-form__control_type_email feedback-form__control_required' and @type='text']"
    password = "//input[@class='form__control feedback-form__control feedback-form__control_required' and @type='password']"
    login_button = "//button[@type='submit' and contains(text(), 'Войти')]"

    # Getters

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    # Actions
    def click_enter_button(self):
        self.get_enter_button().click()
        print('Click enter button')

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('Input User Name')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input Password')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')



    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_enter_button()
        self.input_user_name('ivan_sorokin80@mail.ru')
        self.input_password('Sorokin80!')
        self.click_login_button()

