import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from email_report import sendemail
import requests
import logging

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

with open("config.yaml", "r") as f:
    data = yaml.safe_load(f)
    
@pytest.fixture()
def token():
    return get_login()


@pytest.fixture()
def login():
    res1 = requests.post(data["path_1"], data={"username": data["username"], "password": data["password"]})
    return res1.json()["token"]


@pytest.fixture()
def find_id():
    return 91749


@pytest.fixture()
def title():
    return "Зимушка зима"


@pytest.fixture()
def description():
    return "Я люблю зимушку - зиму за эту чистоту на улицах, за веселые игры, за то волшебство, в которое так ве"

@pytest.fixture()
def select_input_login():
    return '''//*[@id="login"]/div[1]/label/input'''


@pytest.fixture()
def select_input_password():
    return '''//*[@id="login"]/div[2]/label/input'''


@pytest.fixture()
def select_input_button():
    return '''button'''


@pytest.fixture()
def select_error():
    return '''//*[@id="app"]/main/div/div/div[2]/h2'''


@pytest.fixture()
def select_hello_user():
    return '''//*[@id="app"]/main/nav/ul/li[3]/a'''


@pytest.fixture()
def site():
    site_class = Site(testdata['address'])
    yield site_class
    site_class.close()

@pytest.fixture(scope='session')
def send_email():
    yield
    sendemail()

@pytest.fixture()
def login():
    response = requests.post(test_data["url_login"],
                             data={'username': test_data["login_1"], 'password': test_data["password_1"]})
    if response.status_code == 200:
        return response.json()['token']
