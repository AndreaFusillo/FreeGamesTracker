from selenium import webdriver
from bs4 import BeautifulSoup
import tkinter as tk
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument('--log-level=3')
options.add_argument('--enable-javascript')

window = tk.Tk()
window.geometry("600x600")
window.title("FreeGamesTracker")
window.resizable(False, False)
window.configure(background="white")

if __name__ == "__main__":
    window.mainloop()

driver = webdriver.Chrome( options=options)
driver.get("https://store.epicgames.com/it/")
contentEpic = driver.page_source

soupEpic = BeautifulSoup(contentEpic, "html.parser")

giochiGratisEpic = []
giochiGratisGoG = []
giochiGratisPrime = []

for a in soupEpic.find_all("div", class_="css-1vu10h2"):
    name= a.find('span', attrs={'class':'css-119zqif'})
    giochiGratisEpic.append(name.text)



driver.get("https://www.gog.com/partner/free_games")
contentGog = driver.page_source
soupGoG = BeautifulSoup(contentGog, "html.parser")

for b in soupGoG.find_all("span", class_="product-title__text"):
    giochiGratisGoG.append(b.text)

driver.get("https://gaming.amazon.com/intro")

try:
    elemento = WebDriverWait(driver, 13).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'tw-amazon-ember tw-amazon-ember-bold tw-bold tw-c-text-overlay tw-font-size-6'))
    )
    
except Exception as e:
    print(f"")
contentPrime = driver.page_source
soupGoG = BeautifulSoup(contentPrime, "html.parser")


for c in soupGoG.find_all("p", class_="tw-amazon-ember tw-amazon-ember-bold tw-bold tw-c-text-overlay tw-font-size-6"):
    giochiGratisPrime.append(c.text)
   


print("GIOCHI GRATIS DEI VARI CLIENT")
print("EPIC STORE:")
print(giochiGratisEpic)
print("PRIME GAMING")
print(giochiGratisPrime)
print("GOG.COM")
print(giochiGratisGoG)
#for b in giochiGratis:
    #print(giochiGratis.find_all("span", class_="css-119zqif"))

