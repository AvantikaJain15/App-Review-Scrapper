from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

class Amazon:
    def __init__(self, url):
        self.url =url
        self.driver = None
        self.review_page_url = None
        self.main_dict ={
            "Star": [],
            "Summary": [],
            "Description": []
        }
        self.page_count = 0
    def open_link(self):
        options =Options()
        options.page_load_strategy = 'normal'
        self.driver =webdriver.Chrome(options= options)
        self.driver.get(self.url)
        self.driver.maximize_window()
        