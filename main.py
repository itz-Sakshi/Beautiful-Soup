import requests
import os
import bs4
import pandas as pd

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# url = "https://timesofindia.indiatimes.com/city/delhi"

# def fetchAndSaveToFile(url, path):
#     r = requests.get(url) #  getting all the html content on the url page 
#     with open(path, "w", encoding="utf-8") as f:
#         f.write(r.text)


# fetchAndSaveToFile(url, "data/timesOfIndia.html")

# you can get the api key from your free account in scraperApi
api_key = os.getenv('SCRAPERAPI_KEY')  # Load API key from environment variable

payload = {'api_key': api_key, 'url': 'https://www.amazon.ca/s?k=iphone+16+pro+case&crid=3UAR39Y1S1CCX&sprefix=ip%2Caps%2C104&ref=nb_sb_ss_ts-doa-p_1_2'}
r = requests.get('https://api.scraperapi.com', params=payload)

soup = bs4.BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())
# headings = soup.find_all('h1')

# for heading in headings:
#     print(heading.text.strip())

# finding all the product names on the page
products = soup.find_all(class_="a-section a-spacing-none a-spacing-top-small s-title-instructions-style")
i = 0
for product in products:
    i += 1
    # print(f"{i}: {product.get_text()}\n\n")


# Finding all the prices and storing in the array
j = 0
pricesArr = []
for price in soup.find_all(class_="a-price"):
    j += 1
    # Access the first child and get the text
    price_text = price.find(class_="a-offscreen").get_text()
    pricesArr.append(price_text)

print(j)

data = {}

# printing products along with prices
products = soup.find_all(class_="a-section a-spacing-none a-spacing-top-small s-title-instructions-style")
i = 0
for product in products:
    data[i] = {}  # Initialize the dictionary entry
    data[i]["name"] = product.get_text()  
    data[i]["price"] = pricesArr[i] if i < len(pricesArr) else None  # Avoid IndexError
    print(f"{i + 1}: {data[i]['name']}\n Price: {data[i]['price']}\n")
    i += 1

# Convert the dictionary to a DataFrame
df = pd.DataFrame.from_dict(data, orient='index')

# Save the DataFrame to a CSV file
df.to_csv('products.csv', index=False)

    
# Just for fun
# i = 0
# for div in soup.find_all(class_="celwidget"):
#     i += 1

#     # Convert div.children to a list to access elements by index
#     div_children = list(div.children)
    
#     # Check if the first child is a Tag (and not a NavigableString)
#     if len(div_children) > 0 and isinstance(div_children[0], bs4.element.Tag):
#         first_child = div_children[0]
#         first_child_children = list(first_child.children)
        
#         # Check if the first child has children and is also a Tag
#         if len(first_child_children) > 0 and isinstance(first_child_children[0], bs4.element.Tag):
#             print(first_child_children[0])

#     if i == 1:
#         break
