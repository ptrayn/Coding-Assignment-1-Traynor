import requests
import csv
import time
import json
import datetime
#Polygon documentation
#https://polygon.io/docs/stocks/getting-started

#API key for polygon.io
api_key = 'qqiMpszYH688dHMSUgqfOQnBMDGi5phH'

currentDate = time.strftime("%Y-%m-%d")
# List of ticker symbols for the companies you're interested in
ticker_symbols = [
    "MMM", "ABT", "ABBV", "ACN", "ATVI", "ADBE", "AMD", "AES", "AFL",
    "A", "APD", "AKAM", "ALK", "ALB", "ARE", "ALGN", "ALLE", "LNT",
    "ALL", "GOOGL", "GOOG", "MO", "AMZN", "AMCR", "AEE", "AAL", "AEP", "AXP",
    "AIG", "AMT", "AWK", "AMP", "ABC", "AME", "AMGN", "APH", "ADI", "ANSS",
    "AON", "AOS", "APA", "AAPL", "AMAT", "APTV", "ADM", "ANET", "AJG",
    "AIZ", "T", "ATO", "ADSK", "ADP", "AZO", "AVB", "AVY", "BKR",
    "BAC", "BK", "BAX", "BDX", "BBY", "BIO", "BIIB", "BLK", "BA", "BKNG",
    "BWA", "BXP", "BSX", "BMY", "AVGO", "BR", "BF.B", "CHRW", "CDNS",
    "CPB", "COF", "CAH", "KMX", "CCL", "CARR", "CAT", "CBOE", "CBRE", "CDW",
    "CE", "CNC", "CNP", "CTLT", "CF", "SCHW", "CHTR", "CVX", "CMG",
    "CB", "CHD", "CI", "CINF", "CTAS", "CSCO", "C", "CFG", "CLX",
    "CME", "CMS", "KO", "CTSH", "CL", "CMCSA", "CMA", "CAG", "CXO", "COP",
    "ED", "STZ", "COO", "CPRT", "GLW", "CTVA", "COST", "CCI", "CSX", "CMI",
    "CVS", "DHI", "DHR", "DRI", "DVA", "DE", "DAL", "XRAY", "DVN", "DXCM",
    "FANG", "DLR", "DFS", "DISH", "DG", "DLTR", "D", "DPZ",
    "DOV", "DOW", "DTE", "DUK", "DD", "DXC", "EMN", "ETN", "EBAY",
    "ECL", "EIX", "EW", "EA", "EMR", "ETR", "EOG", "EFX", "EQIX", "EQR",
    "ESS", "EL", "ETSY", "EVRG", "ES", "RE", "EXC", "EXPE", "EXPD", "EXR",
    "NVDA", "FFIV", "META", "FAST", "FRT", "FDX", "FIS", "FITB", "FE", "FRC",
    "FISV", "FLT", "FLIR", "FLS", "FMC", "F", "FTNT", "FTV", "FBHS", "FOXA",
    "FOX", "BEN", "FCX", "GPS", "GRMN", "IT", "GD", "GE", "GIS", "GM",
    "GPC", "GILD", "GL", "GPN", "GS", "GWW", "HRB", "HAL", "HBI", "HIG",
    "HAS", "HCA", "PEAK", "HSIC", "HSY", "HES", "HPE", "HLT", "HOLX", "HD"
]
# ticker_symbols = ["NVDA"]

#Print the number of ticker symbols
print(len(ticker_symbols))

# Define the base API endpoint
base_url = 'https://api.polygon.io/v2/aggs/ticker/'

# Specify the date for which you want data (e.g., '2023-01-09')
# Get today's date
today = datetime.date.today()
date = '2023-01-09'

# Set a delay between requests in seconds (e.g., 1 second)
request_delay = 1

# Set the number of requests after which to wait for 1 minute
requests_per_batch = 5

# Field translations
field_translations = {
    "c": "Closing_Price",
    "h": "Highest_Price",
    "l": "Lowest_Price",
    "n": "Num_Transactions",
    "o": "Open_Price",
    "v": "Volume",
    "vw": "Average_Price"
}
count = 0
set_of_companies = set()

# Open a CSV file for writing processed data
with open('daily_aggregated_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Symbol', 'Date', 'Closing_Price', 'Highest_Price', 'Lowest_Price', 'Num_Transactions', 'Open_Price', 'Volume', 'Average_Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Open a CSV file for writing raw data
    with open('daily_aggregated_data_raw.csv', 'w', newline='') as raw_csvfile:
        raw_fieldnames = ['Symbol', 'Raw_Data']
        raw_writer = csv.DictWriter(raw_csvfile, fieldnames=raw_fieldnames)
        raw_writer.writeheader()

        # Loop through the ticker symbols
        for i, ticker_symbol in enumerate(ticker_symbols, start=1):
            # Define the complete API endpoint for the current symbol and date
            url = f'{base_url}{ticker_symbol}/range/1/day/{date}/{date}?apiKey={api_key}'

            # Make the GET request
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()
                if "results" in data and data["results"]:
                    # Translate field names and handle missing 't' field
                    if ticker_symbol not in set_of_companies:
                        translated_data = {field_translations[key]: value for key, value in data["results"][0].items() if key in field_translations}
                        translated_data['Symbol'] = ticker_symbol
                        translated_data['Date'] = date
                        writer.writerow(translated_data)

                        # Write raw data to the raw CSV file
                        raw_writer.writerow({'Symbol': ticker_symbol, 'Raw_Data': json.dumps(data)})

                        set_of_companies.add(ticker_symbol)
                        count += 1
                else:
                    print(f'Error for {ticker_symbol}: No results found in the response.')
            else:
                print(f'Error for {ticker_symbol}: Unable to retrieve data. Status code: {response.status_code}')

            # Delay before making the next request to avoid rate limiting
            time.sleep(request_delay)

            # If we've made requests_per_batch requests, wait for 1 minute
            if i % requests_per_batch == 0 and i != len(ticker_symbols):
                print(f'Waiting for 1 minute...')
                time.sleep(60)

print('Processed data saved to daily_aggregated_data.csv')
print('Raw data saved to daily_aggregated_data_raw.csv')
print(count, "companies added")