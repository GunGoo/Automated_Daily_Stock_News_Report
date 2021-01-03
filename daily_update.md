## 12/26/2020 - Brainstorming Section

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

- Tried using Beautiful soup but the site (SeekingAlpha) blocks me: blocking bot usage
- probably trying Selenium again to get the quant table.

## 12/31/2020 Update

- Find a way to scrap table from "https://www.sec.gov/edgar/searchedgar/companysearch.html"
- 20:40 -> working with Selenium to scrap data. this might work!!
- Repo name change to "Quant-Automation"

## 01/01/2021 Update

- Good to create a github cheatsheet for myself
  - In case I changed the name of the repository, I need to switch git remote location in terminal.
    ```
    git remote set-url origin (NEW_URL)
    ```
- Project Idea: scrapping articles issued after prev-day close and before today's market open.

  - Reporting list of companies that had positive news
    - with title of the related articles via email

- Sentiment Analysis

  - US market TECH articles today, count how many positive news and negative news
  - compare with QQQ

- **Seeking Alpha web Scrapping - Sector News**

  - QQQ needs to be presented to see market trend
  - scrap each sectors' stocks and report positive stocks via email
  - Adding features
    - showing stocks performance on the positive news. Next day
  - for the sentiment analysis, I can use dataset on kaggle to train and save model
  - Automatically starts computer by configuring BIOS and run scheduled task everyday
  - Can have 2 seperate emails; 1 for my portfolio, 1 for in general

- **IDEA: Estimated Target Stock Price Calculator**

  - Target Price = (estimated revenue \* ps ratio)/# of shares

- **IDEA: Can do Quants using Yahoo Finance!!**
  - Yahoo finance conversation (comments) sentiment analysis

## 01/02/2021

- **IDEA**: simulate myself working as a data scientist at a company, and find, clean, and organize data for companies using hadoop or spark. Think in a way to analyze large amounts of complex raw and processed information to find patterns that will benefit an organization and help drive stretegic business decisions.

  - creating a report and explain the reasong for the patterns

- **Seeking Alpha web Scrapping - Sector News** Update
  - Ideas:
    - possibly support different languages for the report using google translate
    - possibly support correction of prediction result to improve the sentiment analysis model
    - possibly support tech forum comments analysis for better prediction result
  - Features:
    - was able to clean and parse the scrapped data into the following format
      ```
      dict["ticker"] = list[ tuple(date, title) ]
      ```

## 01/03/2021

- ## **Automated Deaily Stock News Report** Update
  - Figure out how to send email through python daily.
    - window scheduler
    - Bios auto on/off
