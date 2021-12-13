from selenium.common.exceptions import NoSuchElementException
# from browserStack_monitoring_blavity import *
from environment import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def environment(url):
    driver.maximize_window()
    driver.get(url)
    time.sleep(5)
    print(driver.title)


def after_one_is_verifird(url):
    driver.get(url)
    time.sleep(5)
    print(driver.title)


def page_load_blavity():
    WebDriverWait(driver, 40).until(ec.title_is("The Community for Black Creativity and News - Blavity News"))
    assert driver.current_url == url_blavity, "url does not match"
    print("url do match for blavity")

def page_load_shadowandact():
    WebDriverWait(driver, 40).until(ec.title_is("SHADOW & ACT"))
    assert driver.current_url == url_shadowandact, "url does not match"
    print("url do match for ShadowAndAct")

def page_load_21ninety():
    WebDriverWait(driver, 40).until(ec.title_is("21Ninety"))
    assert driver.current_url == url_21ninety, "url does not match"
    print("url do match for 21ninety")

def page_load_afrotech():
    WebDriverWait(driver, 40).until(ec.title_is("AfroTech"))
    assert driver.current_url == url_afrotech, "url does not match"
    print("url do match for afrotech")


def page_load_travelnoire():
    WebDriverWait(driver, 40).until(ec.title_is("Travel Noire"))
    assert driver.current_url == url_travelnoire, "url does not match"
    print("url do match for travelnoire")


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
        assert driver.title == \
               "The Community for Black Creativity and News - Blavity News", \
               "title does not match for blavity page"
    if url == url_afrotech:
        print("inside if", url)
        assert driver.title == "AfroTech", "title does not match for AfroTech page"
    if url == url_shadowandact:
        print("inside if", url)
        assert driver.title == "SHADOW & ACT", "title does not match for SHADOW & ACT page"
    if url == url_travelnoire:
        print("inside if", url)
        assert driver.title == "Travel Noire", "title does not match for Travel Noire page"
    if url == url_21ninety:
        print("inside if", url)
        assert driver.title == "21Ninety", "title does not match for 21Ninety page"
    # try:
    #     driver.switch_to.frame("sp_message_iframe_565136")
    #     pop_up_text = driver.find_element(By.XPATH, "//p[normalize-space()='We value your privacy']")
    #     if pop_up_text.is_displayed():
    #         accept_button = driver.find_element(By.XPATH, "//button[@title='Accept']")
    #         accept_button.click()
    #     driver.switch_to.parent_frame()
    # except NoSuchElementException:
    #     print("blavity news privacy pop-up does not exist")


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


# environment(url_blavity)
# page_load_blavity()
# post_page_load_pop_up(url_blavity)
# after_one_is_verifird(url_shadowandact)
# page_load_shadowandact()
# post_page_load_pop_up(url_shadowandact)
# after_one_is_verifird(url_travelnoire)
# page_load_travelnoire()
# post_page_load_pop_up(url_travelnoire)
# after_one_is_verifird(url_21ninety)
# page_load_21ninety()
# post_page_load_pop_up(url_21ninety)
# login_and_logout()
# after_one_is_verifird(url_afrotech)
# page_load_afrotech()
# post_page_load_pop_up(url_afrotech)
# driver.quit()
