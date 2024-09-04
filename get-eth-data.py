import yfinance as yf

# Define the ticker symbol for Ethereum (use ETH-USD for ETH prices in USD)
ticker = 'ETH-USD'

# Fetch historical data (daily frequency)
eth_data = yf.download(ticker, start='2017-01-01', end='2024-09-03')
# Display the first few rows
print(eth_data.head())

# Optionally, save the data to a CSV file
eth_data.to_csv('eth-historical-data.csv')
