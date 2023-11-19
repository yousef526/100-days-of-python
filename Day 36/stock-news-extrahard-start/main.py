import requests
from newsapi import NewsApiClient
import os
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and
#  the day before yesterday then print("Get News").

stock_api_key = "HT7SWJWINS"
params_stock = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    'apikey':stock_api_key,
}

js = requests.get("https://www.alphavantage.co/query",params=params_stock)
js.raise_for_status()
stock_data = js.json()['Time Series (Daily)']
data1 = stock_data['2023-08-25']
data2 = stock_data['2023-08-24']
diff = (float(data1['4. close']) - float(data2['4. close'])) / float(data1['4. close'])
send_bool = True if diff >= 0.03 else False

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_api_key = "acf5da01d937555fff21129c6"
apiEndpoint = "https://newsapi.org/v2/top-headlines"

news_api_params = {
    "country":'us',
    "category":"business",
    "apiKey":news_api_key,

}

news = requests.get(apiEndpoint,params=news_api_params)
articles = news.json()['articles'][:3]
#print(articles)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
for article in articles:
    account_sid = 'AC7c9e1deec732c2a8886e5f9'
    auth_token = '6f8fef7c393a719c2cc'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"""
            TSLA: 🔺{round(diff,2)}% \n
            Headline:{article['title']}\n
            Brief:{article['description']}
        """,
        from_='+18702767596',
        to='+201068430709'
    )

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

