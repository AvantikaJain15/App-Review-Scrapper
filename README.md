# Product-Review-Scrapper

# Overview

The project aims to scrape product reviews from two major e-commerce websites, Amazon and Flipkart, to gather and analyze customer feedback on various products. This can be useful for comparative analysis, market research, or sentiment analysis.

# Features
1. Multi-site Scraping
Amazon and Flipkart: The project is designed to scrape product reviews from two major e-commerce platforms: Amazon and Flipkart.
2. Dynamic Review Extraction
Review Details: Extracts key details from product reviews, including star ratings, review summaries, and review descriptions.
Pagination Handling: Handles pagination to scrape multiple pages of reviews.
3. Error Handling
Exception Handling: Includes basic exception handling to manage potential issues during scraping, such as missing elements or failed page loads.
4. Data Storage
CSV Export: Saves the scraped review data into CSV files (amazon.csv and flipkart.csv) for further analysis or use.


# Technologies Used

- Programming Languages: Python
- Libraries and Frameworks:
  - **Data Analysis:** Pandas, NumPy
  - **Web Scraping:** Selenium

# Prerequisites

Ensure you have the following libraries installed:

- pandas
- selenium==4.22.0
- requests
- matplotlib

# Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/Product-Review-Scrapper.git
   ```

2. Navigate to the project directory:

   ```sh
   cd Product-Review-Scrapper
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

# Usage

1. Running the application:
   
   Add the Amazon and Flipkart product links in the `main.py` file. The program will automatically scrape the reviews for these products and provide sentiment analysis along with summaries of positive and negative reviews.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

By following these instructions, you can replicate the project setup and effectively run the sentiment analysis and summarization tasks.