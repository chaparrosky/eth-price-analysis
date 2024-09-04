
# Ethereum (ETH) Time Series Analysis

This project analyzes the historical price data of Ethereum (ETH) using time series analysis techniques. The goal is to explore the data, identify key trends, and find the days with the highest returns over various periods (3 months, 6 months, 9 months, and 1 year).

## Table of Contents
- [Installation](#installation)
- [Data Overview](#data-overview)
- [Analysis Steps](#analysis-steps)
- [Best Return Days](#best-return-days)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run the analysis, you'll need to install the necessary Python libraries. You can do this by using `pip` and the `requirements.txt` file provided or by manually installing the libraries.

### Using `requirements.txt`

```bash
pip install -r requirements.txt
```

### Manually Installing Required Libraries

If you prefer to install the libraries manually, here is the list:

```bash
pip install yfinance
pip install pandas
pip install matplotlib
pip install statsmodels
```

### Required Libraries

- **yfinance**: Used to fetch historical data for Ethereum (ETH).
- **pandas**: For data manipulation and analysis.
- **matplotlib**: For creating visualizations of the data.
- **statsmodels**: For performing statistical tests and time series analysis.

## Data Overview

The dataset includes the following columns:

- **Date**: The trading day.
- **Open**: The price of ETH at the start of the day.
- **High**: The highest price of ETH during the day.
- **Low**: The lowest price of ETH during the day.
- **Close**: The price of ETH at the end of the day.
- **Adj Close**: Adjusted closing price, accounting for dividends and splits (if applicable).
- **Volume**: The number of ETH traded during the day.

The data ranges from January 1, 2017, to September 3, 2024.

## Analysis Steps

1. **Data Loading and Preprocessing:**
   - Fetch historical data for Ethereum using the yfinance library.
   - Clean and preprocess the data, including handling missing values and adding features like daily returns and moving averages.

2. **Data Visualization:**
   - Visualize the closing prices of ETH, along with 7-day and 30-day moving averages.
   - Plot the daily returns to understand the volatility.

3. **Finding Best Return Days:**
   - Identify the day with the highest return within different time periods (3 months, 6 months, 9 months, and 1 year).
   - Calculate the buying price (previous day's close) and selling price (closing price on the best return day).

## Best Return Days

For each period (3 months, 6 months, 9 months, 1 year), the analysis finds:

- The day with the highest return.
- The price at which ETH could have been bought (previous day's close).
- The price at which ETH could have been sold (closing price on the day of the highest return).
- The percentage return.

## Results

After running the analysis, the script will output the best return days for each period along with the buying and selling prices. This information is useful for understanding the volatility of Ethereum and identifying the most profitable periods.

Example Output:

```plaintext
In the last 3 months:
   - Best return day: YYYY-MM-DD
   - Buying price (previous day close): $X.XX
   - Selling price: $Y.YY
   - Return: Z.ZZ%

In the last 6 months:
   - Best return day: YYYY-MM-DD
   - Buying price (previous day close): $A.AA
   - Selling price: $B.BB
   - Return: C.CC%
```

## Contributing

If you want to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Any contributions are welcome!
