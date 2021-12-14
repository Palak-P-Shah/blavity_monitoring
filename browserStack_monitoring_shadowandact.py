from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

url_shadowandact = "https://shadowandact.com/"
BROWSERSTACK_USERNAME = 'palakshah_rcAxD5'
BROWSERSTACK_ACCESS_KEY = 's2rqmyxFs8r999bzvGXJ'
desired_cap = {
 'os_version': '10',
 'resolution': '1920x1080',
 'browser': 'Chrome',
 'browser_version': 'latest',
 'os': 'Windows',
 'build_name': 'BStack-[Python] Monitoring Test for shadowandact.com', # test name
 'name': 'BStack-[Python] Monitoring Test for shadowandact.com', # test name
 'build': 'BStack Build Number' # CI/CD job or build name
}
desired_cap['browserstack.debug'] = True
driver = webdriver.Remote(
    command_executor='https://'+BROWSERSTACK_USERNAME+':'+BROWSERSTACK_ACCESS_KEY+'@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)


def environment(url):
    driver.maximize_window()
    driver.get(url)
    time.sleep(5)
    print(driver.title)


def page_load_shadowandact():
    try:
        WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))
    except TimeoutException:
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": '
          '{"status":"failed", "reason": "for SHADOW & ACT shadowandact.com, '
          'took too long but no response, checking title"}}')
        driver.quit()
    if driver.current_url == url_shadowandact:
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": '
          '{"status":"passed", "reason": "url matched! for shadowandact"}}')
    else:
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": '
          '{"status":"failed", "reason": "url did not matched! for SHADOW & ACT"}}')
        driver.quit()


environment(url_shadowandact)
page_load_shadowandact()
driver.quit()
