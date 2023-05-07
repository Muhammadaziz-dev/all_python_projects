import yfinance as yf
import csv
import matplotlib.pyplot as plt

# Define the stock symbols to analyze
symbols = ["AAPL", "GOOG", "MSFT", "AMZN", "FB"]

# Define the start and end dates for the historical data
start_date = "2023-01-01"
end_date = "2024-12-31"

# Define the output file format and fields
output_format = "csv"
output_fields = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]

# Define the rise and fall thresholds as percentages
rise_threshold = 5.0
fall_threshold = -5.0

# Define the counters for the rise and fall days
num_rise_days = {}
num_fall_days = {}

# Define dictionaries for storing the date and close price data
dates = {}
prices = {}

# Loop over the stock symbols
for symbol in symbols:
    # Download the historical data from Yahoo Finance
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    # Define the output file name
    output_file = f"{symbol}_historical_data.{output_format}"

    # Write the historical data to a CSV file
    with open(output_file, "w", newline="") as csv_file:
        # Create a CSV writer object
        writer = csv.writer(csv_file)

        # Write the header row
        writer.writerow(output_fields)

        # Write the data rows
        for index, row in stock_data.iterrows():
            writer.writerow([index.strftime("%Y-%m-%d")] + list(row))

    # Initialize the counters and lists for the current symbol
    num_rise_days[symbol] = 0
    num_fall_days[symbol] = 0
    dates[symbol] = []
    prices[symbol] = []

    # Open the input file for reading
    with open(output_file, "r") as csv_file:
        # Create a CSV reader object
        reader = csv.reader(csv_file)

        # Skip the header row
        next(reader)

        # Read the rows and store the data
        for row in reader:
            # Get the date and close price
            date = row[0]
            close = float(row[4])

            # Store the data
            dates[symbol].append(date)
            prices[symbol].append(close)

            # Calculate the daily percentage change
            if len(prices[symbol]) > 1:
                prev_close = prices[symbol][-2]
                pct_change = (close - prev_close) / prev_close * 100

                # Determine whether the stock has risen or fallen
                if pct_change > rise_threshold:
                    num_rise_days[symbol] += 1
                elif pct_change < fall_threshold:
                    num_fall_days[symbol] += 1

    # Print the results for the current symbol
    print(
        f"{symbol} has risen {num_rise_days[symbol]} days and fallen {num_fall_days[symbol]} days based on a rise threshold of {rise_threshold}% and a fall threshold of {fall_threshold}%.")

    # Create a line plot of the close prices for the current symbol
    plt.plot(dates[symbol], prices[symbol], label=symbol)

# Set the plot title and axis labels
plt.title("Stock Close Prices")
plt.xlabel("Date")
