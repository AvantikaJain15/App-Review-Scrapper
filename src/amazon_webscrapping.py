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

    def get_reviewpage(self):
        try:
            self.open_link()
            review_footer_xpath = "//*[@id='reviews-medley-footer']"
            review_footer = self.driver.find_element(By.XPATH, review_footer_xpath)
            review_link = None
            if review_footer:
                review_url_xpath = "//*[@id='reviews-medley-footer']/div[2]/a"
                review_tag = review_footer.find_element(By.XPATH, review_url_xpath)
                review_link = review_tag.get_attribute("href")

                if review_link:
                    print(f"INFO | Review Link found.")
                    print(f"INFO | {review_link}")
                    self.review_page_url = review_link
                    print(f"INFO | Opening Review page.")
                    self.driver.get(self.review_page_url)
                    return
                else:
                    print("ERROR | Review Link not found")
            else:
                print("ERROR | Review footer not found")
        except Exception as e:
            print(f"ERROR | Review footer not found Error : {e}")