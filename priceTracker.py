import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Example product (replace with real one for demo)
URL = "https://www.amazon.in/dp/B0C9JMCQ88"
headers = {"User-Agent": "Mozilla/5.0"}

def get_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    # Demo: Replace with correct tag for product
    price = soup.find("span", {"class": "a-price-whole"})
    if price:
        return int(price.get_text().replace(",", "").strip())
    return None

target_price = 50000
prices = []

for i in range(3):  # Just run 3 times for demo
    price = get_price()
    if price:
        print(f"Current Price: ₹{price}")
        prices.append(price)
        if price < target_price:
            print("Alert: Price dropped below target!")
    time.sleep(2)

df = pd.DataFrame(prices, columns=["Price"])
df.to_csv("price_history.csv", index=False)
print("Saved price history to price_history.csv")
