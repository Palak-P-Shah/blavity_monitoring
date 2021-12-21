from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

url_21ninety = "https://21ninety.com/"
BROWSERSTACK_USERNAME = 'palakshah_rcAxD5'
BROWSERSTACK_ACCESS_KEY = 's2rqmyxFs8r999bzvGXJ'
desired_cap = {
 'os_version': '10',
 'resolution': '1920x1080',
 'browser': 'Chrome',
 'browser_version': 'latest',
 'os': 'Windows',
 'build_name': 'BStack-[Python] Monitoring Test for 21ninenty.com',  # test name
 'name': 'BStack-[Python] Monitoring Test for 21ninenty.com',  # test name
 'build_name': 'BStack-[Python] Monitoring Test for 21ninety.com',  # test name
 'name': 'BStack-[Python] Monitoring Test for 21ninety.com',  # test name
 'build': 'BStack Build Number'  # CI/CD job or build name
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


def page_load_21ninety():
    try:
        WebDriverWait(driver, 40).until(ec.title_is("21Ninety"))
    except TimeoutException:
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": '
          '{"status":"failed", "reason": "for 21Ninety, took too long but no response, checking title"}}')
        driver.quit()
    if driver.current_url == url_21ninety:
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": '
          '{"status":"passed", "reason": "Url matched! for 21ninety"}}')
    else:
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": '
          '{"status":"failed", "reason": "Url did not matched! for 21ninety"}}')
        driver.quit()
    print("url do match for 21ninety")


environment(url_21ninety)
page_load_21ninety()
driver.quit()
