import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from bs4 import Tag
from time import sleep

def login(browser: WebDriver, email: str, password: str, wait: int):
    """
    Logs in the using the given email and password and
    saves a cookie.pkl file for next logins.
    """

    browser.get("https://www.facebook.com/login")
    browser.find_element(By.CSS_SELECTOR, "input#email").send_keys(email)
    browser.find_element(By.CSS_SELECTOR, "input#pass").send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "button#loginbutton").click()
    sleep(wait)
    pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))

def load_cookies(browser: WebDriver):
    browser.get("https://www.facebook.com/")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)

def prefix_str(string: str, prefix: str):
    return prefix + string

def find_nested(element: Tag, depth: int):
    current_element = element
    for _ in range(depth):
        current_element = current_element.find(recursive=False)
    return current_element

def get_link(browser: WebDriver, post, time_xpath: str):
    a = post.find_element(By.XPATH, time_xpath)
    browser.execute_script("""
    var event = new FocusEvent('focusin', {
        'view': window,
        'bubbles': true,
        'cancelable': true
        });
    arguments[0].dispatchEvent(event)
    """, a)
    return a.get_attribute("href")

def remove_all_images(browser: WebDriver):
    browser.execute_script("""
    let images = document.getElementsByTagName('img');
    for (let i = 0; i < images.length; i++) {
        images[i].parentNode.removeChild(images[i]);
    }
    let iframes = document.getElementsByTagName('iframe');
    for (let i = 0; i < iframes.length; i++) {
        iframes[i].parentNode.removeChild(iframes[i]);
    }
    """)