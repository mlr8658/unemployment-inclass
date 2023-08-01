#unemployment

# instead of this method, we are going to set up an environment with the password instead
#from getpass import getpass

#API_KEY = getpass("Please input your AlphaVantage API Key: ")

# now were using the .env file instead
#from getpass import getpass
#
#API_KEY = getpass("Please input your AlphaVantage API Key: ")

import os
from dotenv import load_dotenv
import requests
import json
from pprint import pprint
from statistics import mean
from plotly.express import line


load_dotenv() #> invoking this function loads contents of the ".env" file into the script's environment...

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")


#if we want to change our formatting, we only need to change it in one place rather than everywhere we spit a number out
def format_pct(my_number):
    """
    Formats a percentage number like 3.6555554 as percent, rounded to two decimal places.

    Param my_number (float) like 3.6555554

    Returns (str) like '3.66%'
    """
    return f"{my_number:.2f}%"
#would update to .4f if we want 4 decimal places




request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
print(type(parsed_response))
pprint(parsed_response)


data = parsed_response["data"]


# Challenge A
#
# What is the most recent unemployment rate? And the corresponding date?
# Display the unemployment rate using a percent sign.

print("-------------------------")
print("LATEST UNEMPLOYMENT RATE:")
#print(data[0])
#print(f"{data[0]['value']}%", "as of", data[0]["date"])
print(format_pct(float(data[0]['value'])), "as of", data[0]["date"])




# Challenge B
#
# What is the average unemployment rate for all months during this calendar year?
# ... How many months does this cover?


this_year = [d for d in data if "2023-" in d["date"]]

rates_this_year = [float(d["value"]) for d in this_year]
#print(rates_this_year)

print("-------------------------")
#print("AVG UNEMPLOYMENT THIS YEAR:", f"{mean(rates_this_year)}%")
print("AVG UNEMPLOYMENT THIS YEAR:", f"{format_pct(mean(rates_this_year))}")
print("NO MONTHS:", len(this_year))


# Challenge C
#
# Plot a line chart of unemployment rates over time.


dates = [d["date"] for d in data]
rates = [float(d["value"]) for d in data]

fig = line(x=dates, y=rates, title="United States Unemployment Rate over time", labels= {"x": "Month", "y": "Unemployment Rate"})
fig.show()