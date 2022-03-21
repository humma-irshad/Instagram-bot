import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


CHROME_DRIVER_PATH = "YOUR_CHROME_DRIVER_PATH"
SIMILAR_ACCOUNT = 'bookriot'
USERNAME = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'


class InstaFollower():

    def __init__(self, driver_path):
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.instagram.com")
        form_inputs = self.driver.find_elements(By.TAG_NAME, 'div input')
        time.sleep(5)
        form_inputs[0].send_keys(USERNAME)
        form_inputs[1].send_keys(PASSWORD)
        form_inputs[0].send_keys(Keys.ENTER)
        # save info modal (not saving our info)
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button").click()
        # notification modal (turn on)
        self.driver.find_element(By.CLASS_NAME, "mt3GC button").click()

    def find_followers(self):
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.instagram.com/bookriot/')
        time.sleep(2)
        # see followers
        account_stats = self.driver.find_elements(By.TAG_NAME, 'ul span')
        account_stats[1].click()
        # scroll down from the top of the modal element by the height of the modal
        scroll = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            time.sleep(2)

    def follow(self):
        self.driver.implicitly_wait(10)
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element(By.XPATH,
                    '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_btn.click()


my_bot = InstaFollower(CHROME_DRIVER_PATH)

my_bot.login()
my_bot.find_followers()
my_bot.follow()