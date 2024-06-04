import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import login, load_cookies
from feed import scrape_n_posts
from post import scrape_post
from data import scrape_from_links, posts_to_excel
from prettyprinter import cpprint
from dotenv import load_dotenv

load_dotenv()

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument('--disable-gpu')
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--disable-images")
options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 2}
)

browser = webdriver.Chrome(options=options)

login_email = os.getenv("FB_LOGIN_EMAIL")
login_pass = os.getenv("FB_LOGIN_PASS")
fb_feed = os.getenv("FB_FEED_URL")
amount = int(os.getenv("AMOUNT"))
batch_size = int(os.getenv("BATCH_SIZE"))
output_file = os.getenv("OUTPUT_FILE")
login_wait = int(os.getenv("LOGIN_WAIT"))

print(login_email, login_pass, fb_feed, amount, batch_size, output_file)

if not os.path.exists("cookies.pkl"):
    login(browser=browser, email=login_email, password=login_pass, wait=login_wait)

load_cookies(browser=browser)

scrape_n_posts(browser=browser, feed=fb_feed, amount=amount, batch_size=batch_size)
scrape_from_links(browser, batch_size=batch_size)
posts_to_excel(output="output.xlsx")

browser.quit()