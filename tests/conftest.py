import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver


@pytest.fixture()
def set_up():
    print('start test')
    yield
    print('Finish test')

@pytest.fixture(scope = 'module')
def set_group():
    print('enter system')
    yield
    print('Exit system')

