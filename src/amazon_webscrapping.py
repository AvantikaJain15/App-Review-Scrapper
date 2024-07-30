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

    def extract_reviews(self):
        try:
            review_list_xpath = "//*[@id='cm_cr-review_list']"
            review_list = self.driver.find_element(By.XPATH, review_list_xpath)
            reviews = review_list.find_elements(By.CSS_SELECTOR, "div[data-hook='review']")

            if review_list:
                print(f"INFO | Total reviews to fetch from page {self.page_count} are {len(reviews)}")
                print(f"INFO | Fetching reviews from page {self.page_count}")
                for review in reviews:
                    review_id = review.get_attribute("id")
                    review_star_xpath = "//*[@id='customer_review-" + str(review_id) + "']/div[2]/a/i"
                    review_summary_xpath = "//*[@id='customer_review-" + str(review_id) + "']/div[2]/a/span[2]"
                    review_description_xpath = "//*[@id='customer_review-" + str(review_id) + "']/div[4]/span/span"
                    try: 
                        review_star_ele = review.find_element(By.XPATH, review_star_xpath)
                        review_star_class = review_star_ele.get_attribute("class") 
                        review_star_ = review_star_class.split()[-2]
                        review_star = review_star_.split('-')[-1]
                    except Exception as e:
                        review_star = None

                    try:
                        review_summary = review.find_element(By.XPATH, review_summary_xpath).text
                    except Exception as e:
                        review_summary = None
                    
                    try: 
                        review_description = review.find_element(By.XPATH, review_description_xpath).text
                    except Exception as e:
                        review_description = None

                    if review_star:
                        self.main_dict['Star'].append(review_star)
                    else:
                        self.main_dict['Star'].append(None)

                    if review_summary:
                        self.main_dict['Summary'].append(review_summary)
                    else:
                        self.main_dict['Summary'].append(None)

                    if review_description:
                        self.main_dict['Description'].append(review_description)
                    else:
                        self.main_dict['Description'].append(None)

                print(f"INFO | {len(reviews)} reviews from page {self.page_count} appended in dictionary.")
            else:
                print(f"INFO | Review list not found on page {self.page_count}.")

        except Exception:
            print(f"ERROR | Exception occured in extract_reviews function for page {self.page_count}.") 
    def get_all_reviews(self):
        try:
            self.get_reviewpage()

            while(1):
                self.page_count += 1
                print(f"INFO | Etracting reviews from page {self.page_count}...")
                self.extract_reviews()
                
                print(f"INFO | Searching for next page")
                next_page_xpath = "//*[@id='cm_cr-pagination_bar']/ul/li[2]/a"
                if not next_page_xpath:
                    print(f"INFO | Page {self.page_count} not found")
                    break
                next_page_a = self.driver.find_element(By.XPATH, next_page_xpath)
                if(next_page_a):
                    next_page_url = next_page_a.get_attribute("href")
                    if(next_page_url):
                        print(f"INFO | Next page found")
                        print(f"INFO | Next page loading...")
                        print(f"{next_page_url}")
                        self.driver.get(str(next_page_url))
                        print(f"INFO | Next page loaded successfully.")
                    else:
                        print(f"INFO | URL not found for page {self.page_count}")
                        break
                else:
                    print("INFO | No page left")
                    break
        
        except Exception as e:
            print(f"ERROR | Exception occured in get_all_reviews function ")
        
        return self.main_dict
        self.close()
    
    def close(self):
        if self.driver:
            self.driver.quit()

