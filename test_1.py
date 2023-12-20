from testpage import OperationsHelper, get, post, get_post, login
import logging
import yaml
import time
import requests

with open('testdata.yaml') as f:
    test_data = yaml.safe_load(f)

def test_step_1(browser, send_email):
    logging.info("Test 1 Srarting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'

def test_step_2(browser, send_email):
    logging.info("Test 2 Srarting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(test_data['login'])
    testpage.enter_pass(test_data['password'])
    testpage.click_login_button()
    assert testpage.get_login_enter_text() == 'Blog'

def test_step_3(browser,send_email):
    logging.info("Test 3 Srarting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(test_data['login'])
    testpage.enter_pass(test_data['password'])
    testpage.click_login_button()
    testpage.click_create_button()
    time.sleep(test_data['sleep_time'])
    testpage.create_post_title(test_data['title_name'])
    testpage.create_post_description(test_data['description_name'])
    testpage.create_post_content(test_data['content_name'])
    time.sleep(test_data['sleep_time'])
    testpage.click_create_post_button()
    time.sleep(test_data['sleep_time'])
    testpage.go_to_site()
    assert testpage.get_res_create_text() == test_data['title_name']

def test_step_4(browser,send_email):
    logging.info("Test 4 Srarting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(test_data['login'])
    testpage.enter_pass(test_data['password'])
    testpage.click_login_button()
    testpage.click_contact()
    time.sleep(test_data['sleep_time'])
    testpage.contact_us_name(test_data['your_name'])
    testpage.contact_us_email(test_data['your_email'])
    testpage.contact_us_content(test_data['your_content'])
    testpage.click_contact_us()
    time.sleep(test_data['sleep_time'])
    assert testpage.alert() == 'Form successfully submitted'

def test_step5(login):
    logging.info("Test 5 Starting")
    res = get(login)
    lst = res['data']
    lst_id = [el["id"] for el in lst]

    assert 92773 in lst_id, 'Testing fail'

def test_step6(login):
    logging.info("Test 6 Starting")
    all_posts = get_post(login)
    lst = all_posts['data']
    lst_description = [el["description"] for el in lst]

    assert "Я люблю зимушку - зиму за эту чистоту на улицах, за веселые игры, за то волшебство, в которое так ве" in lst_description, 'Testing fail'
