from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from hakusai.scraping.StepClass import Step


class Driver:
    def __init__(self):
        browser = webdriver.Chrome()
        self.browser = browser
        self.url = ""
        self.translate = {
            "クリック": "click",
            "文字入力": "insert",
            "文字入力後Enter": "insert_and_enter",
            "待つ": "wait",
            "スクロール": "scroll",
        }

    def access_url(self, url):
        self.url = url
        self.browser.get(url)

    def end(self):
        self.browser.close()

    def translate_action_name(self, action_name):
        return self.translate[action_name]

    def select_xpath(self, xpath: str):
        return self.browser.find_element(By.XPATH, xpath)

    def click(self, xpath: str):
        elem = self.select_xpath(xpath)
        elem.click()

    def click_enter(self, xpath: str):
        elem = self.select_xpath(xpath)
        elem.send_keys(Keys.ENTER)

    def insert_data(self, xpath: str, content: str):
        elem = self.select_xpath(xpath)
        elem.send_keys(content)

    def insert_and_enter(self, xpath: str, content: str):
        elem = self.select_xpath(xpath)
        elem.send_keys(content)
        elem.send_keys(Keys.ENTER)

    def scroll_by_elem(self, xpath: str):
        elem = self.select_xpath(xpath)
        self.browser.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth' });", elem)

    def wait(self, wait_time: int):
        time.sleep(wait_time)

    def sort_steps(self, steps: List[Step]):
        return steps
