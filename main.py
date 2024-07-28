import pandas as pd
from src.amazon_webscrapping import Amazon
from src.flipkart_webscrapping import Flipkart 

def scrape_amazon(amazon_url, result_dict):
    amazon_scraper = Amazon(amazon_url)
    result_dict['amazon'] = amazon_scraper.get_all_reviews()

def scrape_flipkart(flipkart_url, result_dict):
    flipkart_scrapper = Flipkart(flipkart_url)
    result_dict['flipkart'] = flipkart_scrapper.get_all_reviews()
