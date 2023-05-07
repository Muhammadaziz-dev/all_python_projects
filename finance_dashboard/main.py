import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# Get stock prices from Yahoo Finance
df = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1577836800&period2=1609459199&interval=1d&events=history')

# Clean and prepare the data
df['Date'] = pd.to_datetime(df['Date'])
df = df[['Date', 'Adj Close']]
df.set_index('Date', inplace=True)

# Plot the stock prices
plt.plot(df['Adj Close'])
plt.title('Apple Inc. Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.show()

# Get news articles from Google News
url = 'https://newsapi.org/v2/everything?'
parameters = {
    'q': 'Apple Inc.',
    'sortBy': 'relevancy',
    'apiKey': 'YOUR_API_KEY'
}
response = requests.get(url, params=parameters)

# Print the top 5 articles
for i in range(5):
    print(response.json()['articles'][i]['title'])
