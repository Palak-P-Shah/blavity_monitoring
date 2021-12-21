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
<<<<<<< HEAD
 'build_name': 'BStack-[Python] Monitoring Test for 21ninenty.com',  # test name
 'name': 'BStack-[Python] Monitoring Test for 21ninenty.com',  # test name
=======
 'build_name': 'BStack-[Python] Monitoring Test for 21ninety.com',  # test name
 'name': 'BStack-[Python] Monitoring Test for 21ninety.com',  # test name
>>>>>>> 5f2f9f2 (21ninety)
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


def login_and_logout():
    print("inside function login and logout")
    write_story = driver.find_element(By.XPATH, "//a[normalize-space()='SUBMIT A STORY']")
    write_story.click()
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
      By.XPATH, "//h2[normalize-space()='Login']")))
    email = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
    email.send_keys("fortestpurposesonly5@gmail.com")
    psswd = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    psswd.send_keys("test22pass")
    submit = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    submit.click()
    WebDriverWait(driver, 40).until(ec.url_matches("https://legacy.21ninety.com/"))
    try:
        accept = driver.find_element(By.XPATH, "//a[normalize-space()='Accept']")
        accept.click()
    except NoSuchElementException:
        print("pop-up does not exist")
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
      By.XPATH, "//a[normalize-space()='Sign out']")))
    sign_out = driver.find_element(By.XPATH, "//a[normalize-space()='Sign out']")
    sign_out.click()
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
      By.XPATH, "//h1[normalize-space()='THE LATEST']")))


<<<<<<< HEAD
def post_page_load_pop_up(url):
    try:
        event_promo_pop_up = driver.find_element_by_xpath(
          "//div[@class='ub-emb-iframe-wrapper ub-emb-visible']//button[@type='button'][normalize-space()='×']")
        driver.execute_script("arguments[0].click();", event_promo_pop_up)
    except NoSuchElementException:
        print("event promo pop-up does not exist")
    print("inside function post_page_load_pop_up with url as , ", url)
    if driver.title == "21Ninety":
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": '
          '{"status":"passed", "reason": "Title matched! for 21ninety"}}')
    else:
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": '
          '{"status":"failed", "reason": "Title did not matched! for 21ninety"}}')
        driver.quit()
=======
# def post_page_load_pop_up(url):
#     try:
#         # event_promo_pop_up = driver.find_element_by_xpath(
#         #   "//div[@class='ub-emb-iframe-wrapper ub-emb-visible']//button[@type='button'][normalize-space()='×']")
#         driver.execute_script("arguments[0].click();", event_promo_pop_up)
#     except NoSuchElementException:
#         print("event promo pop-up does not exist")
#     print("inside function post_page_load_pop_up with url as , ", url)
#     if driver.title == "21Ninety":
#         driver.execute_script(
#           'browserstack_executor: {"action": "setSessionStatus", "arguments": '
#           '{"status":"passed", "reason": "Title matched! for 21ninety"}}')
#     else:
#         driver.execute_script(
#           'browserstack_executor: {"action": "setSessionStatus", "arguments": '
#           '{"status":"failed", "reason": "Title did not matched! for 21ninety"}}')
#         driver.quit()
>>>>>>> 5f2f9f2 (21ninety)


environment(url_21ninety)
page_load_21ninety()
driver.quit()
