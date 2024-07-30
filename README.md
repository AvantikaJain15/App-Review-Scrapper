# Product-Review-Scrapper

# Overview

This project aims to develop an advanced sentiment analysis tool using a Bi-LSTM model.

# Features

- Bi-LSTM Model: Implements a Bidirectional Long Short-Term Memory (Bi-LSTM) model for sentiment analysis, providing highly accurate results by considering the context from both directions in the text.
- Automatic Categorization: Categorizes scraped reviews into predefined categories automatically.
- Summarization: Utilizes the Transformer-based BART model to summarize product reviews, delivering concise and relevant information.

# Technologies Used

- Programming Languages: Python
- Libraries and Frameworks:
  - **Data Analysis:** Pandas, NumPy
  - **Web Scraping:** Selenium
  - **Summarization:** Hugging Face's Transformers (BART model)

 Prerequisites

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