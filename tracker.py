from selenium import webdriver
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from tkinter import ttk
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading


options = webdriver.ChromeOptions()
options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument('--log-level=3')
options.add_argument('--enable-javascript')



driver = webdriver.Chrome( options=options)

giochiGratisEpic = []
giochiGratisGoG = []
giochiGratisPrime = []

def Epic(Lista):
    driver = webdriver.Chrome( options=options)
    driver.get("https://store.epicgames.com/it/")
    contentEpic = driver.page_source
    soupEpic = BeautifulSoup(contentEpic, "html.parser")
    for a in soupEpic.find_all("div", class_="css-1vu10h2"):
        name= a.find('span', attrs={'class':'css-119zqif'})
        Lista.append(name.text)

def GoG(Lista):
    driver = webdriver.Chrome( options=options)
    driver.get("https://www.gog.com/partner/free_games")
    contentGog = driver.page_source
    soupGoG = BeautifulSoup(contentGog, "html.parser")
    for b in soupGoG.find_all("span", class_="product-title__text"):
        Lista.append(b.text)

def Prime(Lista):
    driver = webdriver.Chrome( options=options)
    driver.get("https://gaming.amazon.com/intro")
    try:
        e = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'tw-amazon-ember tw-amazon-ember-bold tw-bold tw-c-text-overlay tw-font-size-6'))
        )
        
    except Exception as e:
        print("")
    contentPrime = driver.page_source
    soupGoG = BeautifulSoup(contentPrime, "html.parser")


    for c in soupGoG.find_all("p", class_="tw-amazon-ember tw-amazon-ember-bold tw-bold tw-c-text-overlay tw-font-size-6"):
        Lista.append(c.text)

def crea_colonna(master, lista, titolo):
    frame = ttk.Frame(master)
    frame.pack(side=tk.TOP, padx=10, pady=10, anchor='w')
    
    label = ttk.Label(frame, text=titolo, font=('Arial', 14, 'bold'))
    label.pack(anchor='w')
    
    for elemento in lista:
        elemento_label = ttk.Label(frame, text=elemento, font=('Arial', 12))
        elemento_label.pack(anchor='w')

def main():
    
    root = tk.Tk()
    root.title("Tracker Giochi Gratis")
    
    
    root.geometry("400x700")
    
    
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)
    
    canvas = tk.Canvas(main_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    
    scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    scrollable_frame = ttk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    
    crea_colonna(scrollable_frame, giochiGratisEpic, "EPIC")
    crea_colonna(scrollable_frame, giochiGratisPrime, "PRIME")
    crea_colonna(scrollable_frame, giochiGratisGoG, "GOG")
    

    
    def _on_mouse_wheel(event):
        if event.delta:
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        elif event.num == 5:
            canvas.yview_scroll(1, "units")
        elif event.num == 4:
            canvas.yview_scroll(-1, "units")

    canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
    canvas.bind_all("<Button-4>", _on_mouse_wheel)
    canvas.bind_all("<Button-5>", _on_mouse_wheel)

    
    def _on_arrow_keys(event):
        if event.keysym in ('Up', 'Down'):
            canvas.yview_scroll(1 if event.keysym == 'Down' else -1, "units")

    root.bind_all("<Up>", _on_arrow_keys)
    root.bind_all("<Down>", _on_arrow_keys)

    
    root.mainloop()

if __name__ =="__main__":
    t1 = threading.Thread(target=Epic, args=(giochiGratisEpic,))
    t2 = threading.Thread(target=GoG, args=(giochiGratisGoG,))
    t3 = threading.Thread(target=Prime, args=(giochiGratisPrime,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    main()
    
    
    
    


