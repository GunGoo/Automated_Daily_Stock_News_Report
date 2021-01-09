from bs4 import BeautifulSoup
import requests
import collections


def daily_report():
    url = "https://seekingalpha.com/market-news/all"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html.parser")
    news = soup.find(name="ul", attrs={"class": "mc-list", "id": "mc-list"})
    news_entries = collections.defaultdict(list)
    for tag in news.find_all(name="li", attrs={"class": "mc"}):
        try:
            # Find news ticker
            news_ticker = (
                tag.find(name="div", attrs={"class": "media-left"}).find("a").text
            )

            # Find news title
            news_title = (
                tag.find(name="div", attrs={"class": "media-body"})
                .find(name="div", attrs={"class": "title"})
                .find("a")
                .text
            )

            # Find news link
            # news_link = tag.find()

            # Find news date
            news_date = (
                tag.find(name="div", attrs={"class": "mc-share-info"})
                .find(name="span", attrs={"class": "item-date"})
                .text
            )

            if "Today" in news_date:
                news_entries[news_ticker].append((news_date, news_title))

            if "Yesterday" in news_date:
                splitted_date = news_date.split(" ")
                hour, period = splitted_date[1].split(":")[0], splitted_date[2]
                if period == "PM" and 4 <= int(hour) < 12:
                    news_entries[news_ticker].append((news_date, news_title))

        except:
            pass
    final_news_entries = []
    for ticker, news_list in news_entries.items():
        for news in news_list:
            date, news_heading = news[0], news[1]
            each_news = [ticker, news_heading]
            final_news_entries.append(each_news)

    # for news in final_news_entries:
    #     print(news)
    return final_news_entries


# daily_report()