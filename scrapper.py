# %%

from bs4 import BeautifulSoup
import requests
import pandas as pd

urlNagoya = "https://jmty.jp/aichi/sale-all/g-all/a-459-nagoya?keyword=%E3%82%AB%E3%83%A1%E3%83%A9"
urlSuginami = "https://jmty.jp/tokyo/sale-all/g-all/a-270-suginami?keyword=%E3%82%AB%E3%83%A1%E3%83%A9"


pageNagoya = requests.get(urlNagoya).text

soup = BeautifulSoup(pageNagoya, features="html.parser")
print(soup)

# %%

item_list = soup.find_all("div", class_ = "p-item-content-info")

item_list

# %%

table_titles = ["Name", "Price", "Description", "Link" ] 


df = pd.DataFrame(columns=table_titles)


for item in item_list:
    name = item.find("div", class_ = "p-item-title").text.strip()
    
    price = item.find("div", class_ = "p-item-most-important").text.replace(",", "").replace("円", "").strip()
    
    description = item.find("div", class_ = "p-item-detail").text.strip()
    
    title = item.find("a")
    link = title.get("href")
    
    item_row = [name, price, description, link]
    
    l = len(df)
    df.loc[l] = item_row
    
    # print(name, price, description, link)
df    
    