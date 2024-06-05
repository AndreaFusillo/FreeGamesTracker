from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument('--log-level=3')

chromedriver_path = "C:\\Users\\andre\\chromedriver-win64\\chromedriver.exe"
service = Service(chromedriver_path)
print(chromedriver_path)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://store.epicgames.com/it/")
contentEpic = driver.page_source

soupEpic = BeautifulSoup(contentEpic, "html.parser")

giochiGratisEpic = []
giochiGratisGoG = []
for a in soupEpic.find_all("div", class_="css-1vu10h2"):
    name= a.find('span', attrs={'class':'css-119zqif'})
    giochiGratisEpic.append(name.text)



driver.get("https://www.gog.com/partner/free_games")
contentGog = driver.page_source
soupGoG = BeautifulSoup(contentGog, "html.parser")

for b in soupGoG.find_all("span", class_="product-title__text"):
    giochiGratisGoG.append(b.text)

print("GIOCHI GRATIS TEMPORANEI DI RILIEVO DEI VARI CLIENT")
print("EPIC STORE:")
print(giochiGratisEpic)
print("GOG.COM")
print(giochiGratisGoG)
#for b in giochiGratis:
    #print(giochiGratis.find_all("span", class_="css-119zqif"))
