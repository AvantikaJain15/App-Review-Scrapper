from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

class Flipkart:
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
            review_footer = self.driver.find_element(By.CSS_SELECTOR, "div[class='col pPAw9M']")
            review_link_a = review_footer.find_element(By.TAG_NAME, "a")
            if review_footer:
                review_link = review_link_a.get_attribute("href")

                if review_link:
                    print(f"INFO | Review Link found.")
                    self.driver.get(review_link)
                    review_link_a = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div/a[1]")
                    review_link = review_link_a.get_attribute("href")
                    print(f"INFO | {review_link}")
                    print(f"INFO | Opening Review page.")
                    self.review_page_url = review_link
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
            review_list_xpath = "//*[@id='container']/div/div[3]/div/div/div[2]"
            review_list = self.driver.find_element(By.XPATH, review_list_xpath)
            reviews = review_list.find_elements(By.CSS_SELECTOR, "div[class='cPHDOP col-12-12']")

            if review_list:

                print(f"INFO | Total reviews to fetch from page {self.page_count} are {len(reviews)}")
                print(f"INFO | Fetching reviews from page {self.page_count}")
                total_reviews = len(reviews)
                for i in range(1, total_reviews - 1):
                    review = reviews[i]
                    review_id = review.get_attribute("id")
                    review_star_xpath = "//*[@id='customer_review-" + str(review_id) + "']/div[2]/a/i"
                    review_summary_xpath = "//*[@id='customer_review-" + str(review_id) + "']/div[2]/a/span[2]"
                    review_description_xpath = "//*[@id='customer_review-" + str(review_id) + "']/div[4]/span/span"

                    try: 
                        review_star = review.find_element(By.CSS_SELECTOR, "div[class='XQDdHH Ga3i8K']").text
                    except Exception as e:
                        review_star = None
                    
                    try:
                        review_summary = review.find_element(By.CSS_SELECTOR, "p[class='z9E0IG']").text
                    except Exception as e:
                        review_summary = None
                    
                    try: 
                        review_description = review.find_element(By.CSS_SELECTOR, "div[class='ZmyHeo']").text
                    except Exception as e:
                        review_description = None
                    
                    if review_star == None and review_summary == None and review_description == None:
                        continue

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

            total_pages_div1 = self.driver.find_elements(By.CSS_SELECTOR, "div[class='cPHDOP col-12-12']")[-1]
            total_pages_div = total_pages_div1.find_element(By.CSS_SELECTOR, "div[class='_1G0WLw mpIySA']")
            total_pages = total_pages_div.find_elements(By.TAG_NAME, "span")[0].text
            total_pages = total_pages.split()[-1]
            total_pages = int(total_pages.replace(",", ""))
            total_pages = int(total_pages)

            next_page_a_nav = self.driver.find_element(By.CSS_SELECTOR, "nav[class='WSL9JP']")
            next_page_a = next_page_a_nav.find_elements(By.TAG_NAME, "a")[-1]
            next_page_url = next_page_a.get_attribute("href")

            print(f"INFO | Total pages found: {total_pages} ")

            for i in range(1, min(total_pages, 10)):
                self.page_count = i

                print(f"INFO | Creating URL for {i} page...")
                page_index = next_page_url.find('page=')
                if page_index != -1:
                    new_url = next_page_url[:page_index + len('page=')] + str(i)
                    print(f"INFO | URL for {i} page: {new_url}")

                next_page_url = new_url
                if(next_page_url):
                    print(f"INFO | Next page found")
                    print(f"INFO | Next page loading...")
                    self.driver.get(str(next_page_url))
                    print(f"INFO | Next page loaded successfully.")
                else:
                    print(f"INFO | URL not found for page {self.page_count}")
                    break

                print(f"INFO | Etracting reviews from page {self.page_count}...")
                self.extract_reviews()
                
        except Exception as e:
            print(f"ERROR | Exception occured in get_all_reviews function ")
        
        return self.main_dict
        self.close()
    
    def close(self):
        if self.driver:
            self.driver.quit()

