import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Select_product_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы
    price_button = "//div[@class='filter-group filter-range']"
    price_slider = "//span[@class='ui-slider-handle ui-corner-all ui-state-default' and @style='left: 100%;']"
    companies_button = "//div[@class='filter-group filter-checkbox-list' and @name='BRAND']"
    silikomart_brand_button = "//span[@class='filter-checkbox__text' and text()='Silikomart']"
    pavoni_brand_button = "//span[@class='filter-checkbox__text' and text()='Pavoni']"
    bonne_brand_button = "//span[@class='filter-checkbox__text' and text()='Bonne']"
    availability_button = "//div[@class='filter-group filter-checkbox-list' and @name='AVAILABLE_ON_STORES']"
    shop_online_button = "//span[@class='filter-checkbox__text' and text()='Интернет-магазин']"
    sorter_button = "//div[@class='sort-dropdown__selected']"
    sort_by_price_button = "//a[@data-value='По цене (сначала дешевые)']"
    add_to_cart_button = "//div[@id='bx_3966226736_9180']//div[@class='add-to-cart__button-wrapper']"
    cart_button = "//div[@class='top-menu']//div[@class='top-menu__right']//a[@class='top-menu__basket']"

    # Геттеры
    def get_price_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_button)))

    def get_price_slider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider)))

    def get_companies_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.companies_button)))

    def get_silikomart_brand_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.silikomart_brand_button)))

    def get_pavoni_brand_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pavoni_brand_button)))

    def get_bonne_brand_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bonne_brand_button)))

    def get_availability_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.availability_button)))

    def get_shop_online_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shop_online_button)))

    def get_sorter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorter_button)))

    def get_sort_by_price_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_price_button)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    # Действия
    def click_price_button(self):
        self.get_price_button().click()
        print("Click price button")

    def move_slider_to_target(self, target_left=34.9882):
        price_slider = self.get_price_slider()

        # Начальное значение left в атрибуте style
        current_left = 100  # Начинаем с 100% (как указано в локаторе)

        # Считываем ширину ползунка
        slider_width = price_slider.size['width']

        # Вычисляем шаг для перемещения (например, сдвиг на 5% за раз)
        step_size = 1  # Можно настроить шаг перемещения в процентах

        actions = ActionChains(self.driver)

        # Перемещаем ползунок, пока не достигнем целевого значения
        while current_left > target_left:
            # Вычисляем смещение
            offset = (current_left - target_left) / 100 * slider_width

            # Выполняем перемещение ползунка на вычисленное смещение
            actions.click_and_hold(price_slider).move_by_offset(-offset, 0).release().perform()

            # Ожидаем немного, чтобы изменения успели отобразиться
            time.sleep(0.2)

            # Обновляем текущую позицию ползунка
            style = price_slider.get_attribute('style')
            current_left = float(style.split('left: ')[1].split('%')[0])  # Извлекаем значение left

            # Логирование для отладки
            print(f"Current left: {current_left}%")

        print(f"Slider moved to {current_left}%")
        time.sleep(2)

    def click_companies_button(self):
        self.get_companies_button().click()
        print("Click brand button")
        time.sleep(2)

    def click_silikomart_brand_button(self):
        self.get_silikomart_brand_button().click()
        print("Click silikomart button")
        time.sleep(3)

    def click_pavoni_brand_button(self):
        self.get_pavoni_brand_button().click()
        print("Click pavoni button")
        time.sleep(3)

    def scroll_and_click(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'nearest'});", element)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(element)).click()

    def click_bonne_brand_button(self):
        bonne_brand_button_element = self.get_bonne_brand_button()
        self.scroll_and_click(bonne_brand_button_element)
        print("Click bonne button")
        time.sleep(3)

    def click_availability_button(self):
        self.get_availability_button().click()
        print("Click availability button")
        time.sleep(3)

    def click_shop_online_button(self):
        self.get_shop_online_button().click()
        print("Click brand button")
        time.sleep(3)

    def click_sorter_button(self):
        self.get_sorter_button().click()
        print("Click sorter button")
        time.sleep(3)

    def click_sort_by_price_button(self):
        self.get_sort_by_price_button().click()
        print("Click sort by price button")
        time.sleep(3)

    def click_add_to_cart_button(self):
        add_to_cart_button_element = self.get_add_to_cart_button()
        self.scroll_and_click(add_to_cart_button_element)
        print("Click add to cart button")
        time.sleep(3)

    def scroll_to_top(self):
        # Прокручиваем страницу наверх
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)  # Пауза для ожидания
        print("Страница прокручена вверх.")

    def click_cart_button(self):
        self.scroll_to_top()
        cart_button_element = self.get_cart_button()
        self.driver.execute_script("arguments[0].click();", cart_button_element)
        time.sleep(1)
        print("Clicked on the cart button.")
       # Методы

    def select_product(self):
        # Закрытие рекламы и изменение цены
        self.get_current_url()
        self.click_price_button()
        self.move_slider_to_target()
        self.click_companies_button()
        self.click_silikomart_brand_button()
        self.click_pavoni_brand_button()
        self.click_bonne_brand_button()
        self.click_availability_button()
        self.click_shop_online_button()
        self.click_sorter_button()
        self.click_sort_by_price_button()
        self.click_add_to_cart_button()
        self.click_cart_button()











