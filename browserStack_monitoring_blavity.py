from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

url_blavity = "https://blavity.com/"
BROWSERSTACK_USERNAME = 'palakshah_rcAxD5'
BROWSERSTACK_ACCESS_KEY = 's2rqmyxFs8r999bzvGXJ'
desired_cap = {
 'os_version': '10',
 'resolution': '1920x1080',
 'browser': 'Chrome',
 'browser_version': 'latest',
 'os': 'Windows',
 'build_name': 'BStack-[Python] Monitoring Test for blavity.com',  # test name
 'name': 'BStack-[Python] Monitoring Test for blavity.com',  # test name
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


def page_load_blavity():
    try:
        WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))
    except TimeoutException:
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": '
          '{"status":"failed", "reason": for blavity.com, took too long but no response, checking title"}}')
        driver.quit()
    if driver.current_url == url_blavity:
        print("inside url do match for blavity.com")
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": '
          '{"status":"passed", "reason": "url matched! for blavity"}}')
    else:
        print("inside url does not match for blavity.com")
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": '
          '{"status":"failed", "reason": "url did not matched! for blavity"}}')
        driver.quit()


environment(url_blavity)
page_load_blavity()
driver.quit()
