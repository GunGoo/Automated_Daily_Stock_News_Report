# GSA

GSA (GunGoo's Stock Analysis)

- Anaconda Environment: GSA
- Git branch: duke

## Brainstorming Section

- Web - Dashboard - HOT stocks
  - giving alert when there is a positive news of a stock on my watchlist
- for each hot stocks, have list of related news from news sites.
- show if the overall news are posotive or negative
- how positive, how negative are they
- alpaca -> show my own algorithm's performance
- seperated section for SPAC and news

- Positivitiy and negativity rate impact on stock price learn from the historical data
- For Tesla, Gary Black, Elon Musk, etc Twitter tweets.

  - Show how ARK is trading on Tesla from LucidBetaTracker.

- Daily/last 3 month volume rank -> quant analysis

### 12/27/2020 - News Scrapping

- Use this dataset, and test it on the scrapped news
  - https://www.kaggle.com/geminikeggler/stock-sentiment-analysis-classification-nlp/comments#932468
- Get list of news sites
- Get analysis reports
- Google how to scrap websites using python

1. Using Selenium framework in Anaconda Environment

   - Install Selenium

     ```
     $ conda install -c conda-forge selenium
     ```

   - if the following error occurs,

     ```
     selenium.common.exceptions.WebDriverException: Message: 'chromedriver.exec' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
     ```

     - Put your chromedriver into the python interpreter path: ex) ./bin/python

     - If you are using Mac, and have access error, use the following code in where chromedriver is saved.

       ```
       xattr -d com.apple.quarantine chromedriver
       ```

## 12/28/2020 Update

- After trying Selenium, I figured out that it is not what I wanted. 1
- add, remove button for watchlist
- scrap 5 latest news for each stocks and show positive or negative
- do Quant Analysis that I learn from the book
- figure out how to scrap parameters for Quanting

## 12/30/2020 Update

- Tried using Beautiful soup but the news site (SeekingAlpha) blocks me: blocking bot usage
- probably trying Selenium again to get the quant table.

## 12/31/2020 Update

- Find a way to scrap table from "https://www.sec.gov/edgar/searchedgar/companysearch.html"
