from requests import get
from bs4 import BeautifulSoup
import openpyxl

BASE_URL = "https://ek.ua"
URL = f"{BASE_URL}/ua/ek-list.php?presets_=12495%2C12496&katalog_=745&pf_=1&order_=pop&save_podbor_=1"
HEADERS = {
   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
FILE_NAME = "watch.csv"
table_data = []
with open(FILE_NAME, "w", encoding="utf-8") as file:
   page = get(URL, headers=HEADERS)
   soup = BeautifulSoup(page.content,  "html.parser")
   w_list = soup.find(name="form", id="list_form1").find_all(name="div", id="he8dz12w3ul")
   n = 1

   for w in w_list:
       w_model = w.find(name="span", class_="u").find(string=True, recursive=False).strip()
       w_url = BASE_URL + w.get("href")
       w_stores = w.find_all(name="div", class_="sn-div").find(string=True, recursive=False).strip()
       w_price = w.find(name="div", class_=" model-price-range").find(string=True, recursive=False).strip()

       print(f"{n}: {w_model}, URL: {w_url}, stores: {w_stores}, prise: {w_price}")

       file.write(f"{n}: {w_model}, URL: {w_url}, stores: {w_stores}, prise: {w_price}")

       n += 1