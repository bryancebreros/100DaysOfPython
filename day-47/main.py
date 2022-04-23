import os

import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

my_email = os.environ["EMAIL"]
password = os.environ["email_pass"]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,es-MX;q=0.8,es;q=0.7,ko;q=0.6'
}

response = requests.get('https://www.amazon.com.mx/dp/B07DK13HKX/?coliid=I3DRX9EWYJP0EL&colid=39Q3YUA03ERTW&psc=1&ref_=lv_ov_lig_dp_it', headers=HEADERS)

soup = BeautifulSoup(response.content, "lxml")
price = soup.find("span", class_='a-price-whole').get_text()
clean_price = price.split(".")[0]
if "," in clean_price:
    final_price = clean_price.split(",")
    final_price = int(final_price[0] + final_price[1])
else:
    final_price = int(clean_price)
if final_price < 1001:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="cebrerosbryan@gmail.com",
                            msg=f"Subject:FIRE EMBLEM\n\nAPROVECHA: {final_price}.")

