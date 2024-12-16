import datetime

from selenium.webdriver import ActionChains


class Base():
    def __init__(self, driver):
        self.driver = driver

    # method current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print('current url ' + get_url)

    # method assert word
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    # method screenshot
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('screen/' + name_screenshot)

    # method assert word
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')

    # Method for scrolling to the element
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        print("Scrolled to the element")


