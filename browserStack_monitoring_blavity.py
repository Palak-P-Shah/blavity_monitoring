from selenium import webdriver
# from monitoring import *
# from environment import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time, os

url_blavity = "https://blavity.com/"
url_blavity_dummy_failure = "https://google.com/"
url_shadowandact = "https://shadowandact.com/"
url_afrotech = "https://afrotech.com/"
url_travelnoire = "https://travelnoire.com/"
url_21ninety = "https://21ninety.com/"

# username = os.getenv("palakshah_rcAxD5")
# access_key = os.getenv("s2rqmyxFs8r999bzvGXJ")
# build_name = os.getenv("BStack-[Python] Monitoring Test for all 5 apps of blavity, blavity.com, shadowandact.com, travelnoire.com, 21ninety.com, afrotech.com")
# browserstack_local = os.getenv("BROWSERSTACK_LOCAL")
# browserstack_local_identifier = os.getenv("BROWSERSTACK_LOCAL_IDENTIFIER")

# caps = {
#  'os': 'Windows',
#  'os_version': '10',
#  'browserstack.debug': 'True',
#  'browser': 'chrome',
#  'browser_version': 'latest',
#  'name': 'BStack-[Jenkins] Sample Test', # test name
#  'build': build_name, # CI/CD job name using BROWSERSTACK_BUILD_NAME env variable
#  'browserstack.local': browserstack_local,
#  'browserstack.localIdentifier': browserstack_local_identifier,
#  'browserstack.user': username,
#  'browserstack.key': access_key
# }
#
# driver = webdriver.Remote(
#     command_executor='https://hub-cloud.browserstack.com/wd/hub',
#     desired_capabilities=caps)
BROWSERSTACK_USERNAME = 'palakshah_rcAxD5'
BROWSERSTACK_ACCESS_KEY = 's2rqmyxFs8r999bzvGXJ'
desired_cap = {
 'os_version': '10',
 'resolution': '1920x1080',
 'browser': 'Chrome',
 'browser_version': 'latest',
 'os': 'Windows',
 'build_name': 'BStack-[Python] Monitoring Test for all 5 apps of blavity, blavity.com, shadowandact.com, travelnoire.com, 21ninety.com, afrotech.com', # test name
 'name': 'BStack-[Python] Monitoring Test for all 5 apps of blavity, blavity.com, shadowandact.com, travelnoire.com, 21ninety.com, afrotech.com', # test name
 'build': 'BStack Build Number 1' # CI/CD job or build name
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
          'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title did not matched! for Afrotech"}}')
        driver.quit()

    if driver.current_url == url_blavity:
        print("inside url do match for blavity.com")
        driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "url matched! for blavity"}}')
    else:
        print("inside url does not match for blavity.com")
        driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "url did not matched! for blavity"}}')
        driver.quit()
    assert driver.current_url == url_blavity, "url does not match"


def post_page_load_pop_up(url):
    print("inside function post_page_load_pop_up with url as , ", url)
    if url == url_afrotech:
        print("within the if loop to wait if website is afrotech for event promo")
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
          By.XPATH, "//div[@class='ub-emb-iframe-wrapper ub-emb-visible']//button[@type='button'][normalize-space()='×']")))
    if url == url_blavity or url == url_shadowandact or url == url_afrotech or url == url_21ninety:
        try:
            print("inside try", url)
            event_promo_pop_up = driver.find_element_by_xpath(
              "//div[@class='ub-emb-iframe-wrapper ub-emb-visible']//button[@type='button'][normalize-space()='×']")
            driver.execute_script("arguments[0].click();", event_promo_pop_up)
        except NoSuchElementException:
            print("event promo pop-up does not exist")
    if url == url_afrotech:
        print("within the if loop to wait if website is afrotech for accept")
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
          By.XPATH, "//button[text()='Accept']")))
        footer_xpath = driver.find_element(By.XPATH, "//button[text()='Accept']")
        driver.execute_script("arguments[0].click();", footer_xpath)
    else:
        footer_xpath = driver.find_element(By.XPATH, "//button[text()='Accept']")
        driver.execute_script("arguments[0].click();", footer_xpath)
    if url == url_blavity:
        print("inside if", url)
        if driver.title == "The Community for Black Creativity and News - Blavity News":
            driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched! for Blavity"}}')
        else:
            driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title did not matched! for Blavity"}}')
            driver.quit()
        assert driver.title == "The Community for Black Creativity and News - Blavity News", "title does not match for blavity page"
    if url == url_afrotech:
        try:
            WebDriverWait(driver, 40).until(ec.title_is("AfroTech"))
        except TimeoutException:
            driver.execute_script(
              'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title did not matched! for Afrotech"}}')
            driver.quit()
        print("inside if", url)
        if driver.title == "AfroTech":
            driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched! for AfroTech"}}')
        else:
            driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title did not matched! for AfroTech"}}')
            driver.quit()
        assert driver.title == "AfroTech", "title does not match for AfroTech page"
    if url == url_shadowandact:
        print("inside if", url)
        if driver.title == "SHADOW & ACT":
            driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched! for shadowandact"}}')
        else:
          driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title did not matched! for shadowandact"}}')
          driver.quit()
        assert driver.title == "SHADOW & ACT", "title does not match for SHADOW & ACT page"
    if url == url_travelnoire:
        print("inside if", url)
        if driver.title == "Travel Noire":
            driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched! for travelnoire"}}')
        else:
            driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title did not matched! for travelnoire"}}')
            driver.quit()
        assert driver.title == "Travel Noire", "title does not match for Travel Noire page"
    if url == url_21ninety:
        print("inside if", url)
        if driver.title == "21Ninety":
            driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched! for 21ninety"}}')
        else:
            driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title did not matched! for 21ninety"}}')
            driver.quit()
        assert driver.title == "21Ninety", "title does not match for 21Ninety page"


def after_one_is_verifird(url):
    driver.get(url)
    time.sleep(5)
    print(driver.title)


def page_load_shadowandact():
    try:
        WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))
    except TimeoutException:
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title did not matched! for SHADOW & ACT"}}')
        driver.quit()
    if driver.current_url == url_shadowandact:
        driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "url matched! for shadowandact"}}')
    else:
        driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "url did not matched! for shadowandact"}}')
        driver.quit()
    assert driver.current_url == url_shadowandact, "url does not match"
    print("url do match for ShadowAndAct")


def page_load_21ninety():
    try:
        WebDriverWait(driver, 40).until(ec.title_is("21Ninety"))
    except TimeoutException:
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title did not matched! for 21Ninety"}}')
        driver.quit()
    if driver.current_url == url_21ninety:
       driver.execute_script(
      'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Url matched! for 21ninety"}}')
    else:
       driver.execute_script(
       'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Url did not matched! for 21ninety"}}')
       driver.quit()
    assert driver.current_url == url_21ninety, "url does not match for 21Ninety"
    print("url do match for 21ninety")


def page_load_afrotech():
    try:
        WebDriverWait(driver, 40).until(ec.title_is("AfroTech"))
    except TimeoutException:
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title did not matched! for Afrotech"}}')
        driver.quit()
    if driver.title == "AfroTech":
        driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched! for Afrotech"}}')
    else:
        driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title did not matched! for Afrotech"}}')
        driver.quit()
    assert driver.title == "AfroTech", "title does not match for AfroTech"
    print("title do match for afrotech")
    # WebDriverWait(driver, 40).until(ec.title_is("AfroTech"))
    if driver.current_url == url_afrotech:
        driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "url matched! for Afrotech"}}')
    else:
      driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "url did not matched! for Afrotech"}}')
      driver.quit()
    assert driver.current_url == url_afrotech, "url does not match for Afrotech.com"
    print("url do match for afrotech")


def page_load_travelnoire():
    try:
        WebDriverWait(driver, 40).until(ec.title_is("Travel Noire"))
    except TimeoutException:
        driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Url did not matched! for travelnoire"}}')
        driver.quit()
    if driver.current_url == url_travelnoire:
        driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Url matched! for travelnoire"}}')
    else:
        driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Url did not matched! for travelnoire"}}')
        driver.quit()
    assert driver.current_url == url_travelnoire, "url does not match"
    print("url do match for travelnoire")


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


environment(url_blavity)
page_load_blavity()
post_page_load_pop_up(url_blavity)
after_one_is_verifird(url_shadowandact)
page_load_shadowandact()
post_page_load_pop_up(url_shadowandact)
after_one_is_verifird(url_travelnoire)
page_load_travelnoire()
post_page_load_pop_up(url_travelnoire)
after_one_is_verifird(url_21ninety)
page_load_21ninety()
post_page_load_pop_up(url_21ninety)
# login_and_logout()
after_one_is_verifird(url_afrotech)
page_load_afrotech()
# post_page_load_pop_up(url_afrotech)
driver.quit()

# environment(url_travelnoire)
# page_load_travelnoire()
# # after_one_is_verifird(url_travelnoire)
# # page_load_travelnoire()
# # post_page_load_pop_up(url_travelnoire)
