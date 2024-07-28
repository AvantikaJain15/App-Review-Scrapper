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
    flipkart_url = 'https://www.flipkart.com/apple-2020-macbook-air-m1-8-gb-256-gb-ssd-mac-os-big-sur-mgn63hn-a/p/itm3c872f9e67bc6?pid=COMFXEKMGNHZYFH9&lid=LSTCOMFXEKMGNHZYFH9P56X45&marketplace=FLIPKART&q=macbook+air+m1&store=6bo%2Fb5g&spotlightTagId=FkPickId_6bo%2Fb5g&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=60e5b3b2-3e04-47a0-be72-038585b0a70c.COMFXEKMGNHZYFH9.SEARCH&ppt=sp&ppn=sp&ssid=v5yhxbm1wg0000001720890411475&qH=be9862f704979d6e'
    amazon_url = 'https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=sr_1_1?crid=3TPNN5S6RDWIA&dib=eyJ2IjoiMSJ9.HvIbKicK-wBXX5On3-PhncUUI90SvNmRPDR4mtGr2dztW3w_hFtzZ1NcBpQSSSPJ9o-hVBq29lAcMOwoSNevCI-L2UH4ogqdygVBpECsQTSn7LvoyBwlWTKWyDtQipIU9Zt2IaYvNeCi1H7TQgulKdvUlQmSJZMkEdQ7RRx8tJnc4mWMqEwdFTD3_aHyIZ6annjOJbvXWEYEv0dMHOrTmtKsCkVt7FRFoRbrTeKkIzo.DuYe9VF9bscMcsLX7-lzibbrMUTZ4dNYz1D0FBEjZfk&dib_tag=se&keywords=Apple+2020+Macbook+Air+Apple+M1+-+%288+GB%2F256+GB+SSD%2FMac+OS+Big+Sur%29+MGN63HN%2FA+%2813.3+inch%2C+Space+Grey%2C+1.29+kg%29&nsdOptOutParam=true&qid=1720890431&sprefix=%2Caps%2C234&sr=8-1'
    result_dict = {}
    scrape_amazon(amazon_url, result_dict) 
    scrape_flipkart(flipkart_url, result_dict)
    amazon_df = pd.DataFrame(result_dict['amazon'], columns=result_dict['amazon'].keys())
    print(amazon_df)

    flipkart_df = pd.DataFrame(result_dict['flipkart'], columns=result_dict['flipkart'].keys())
    print(flipkart_df)
    
