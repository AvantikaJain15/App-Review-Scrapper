import pandas as pd
from src.amazon_webscrapping import Amazon
from src.flipkart_webscrapping import Flipkart 

def scrape_amazon(amazon_url, result_dict):
    amazon_scraper = Amazon(amazon_url)
    result_dict['amazon'] = amazon_scraper.get_all_reviews()

def scrape_flipkart(flipkart_url, result_dict):
    flipkart_scrapper = Flipkart(flipkart_url)
    result_dict['flipkart'] = flipkart_scrapper.get_all_reviews()

def main():
    flipkart_url = input('Enter the Flipkart product URL: ')
    amazon_url = input('Enter the Amazon product URL: ')
    result_dict = {}
    scrape_amazon(amazon_url, result_dict) 
    scrape_flipkart(flipkart_url, result_dict)
    amazon_df = pd.DataFrame(result_dict['amazon'], columns=result_dict['amazon'].keys())
    print(amazon_df)
    amazon_df.to_csv("amazon.csv")

    flipkart_df = pd.DataFrame(result_dict['flipkart'], columns=result_dict['flipkart'].keys())
    print(flipkart_df)
    flipkart_df.to_csv("flipkart.csv")
if __name__ == "__main__":
    main()