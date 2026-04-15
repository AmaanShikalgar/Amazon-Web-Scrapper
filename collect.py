from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'title': [], 'price':[], 'link':[]}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}",encoding="utf-8") as f:
            html_doc = f.read()  
                
        soup = BeautifulSoup(html_doc,'html.parser')
       
        #title 
        t = soup.find("h2")
        title = t.get_text()
        
        #price
        p = soup.find("span", attrs={"class": 'a-price-whole'})
        price = p.get_text()
        
        #link
        a = soup.find("a", class_="a-link-normal")
        link = None 
        if a:
            href = a.get("href")
            if href:
                link = "https://amazon.in" + href

    
        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)
        
    except Exception as e:
        print(e)
        
#create dataframe        
df = pd.DataFrame(data=d)

df = df.dropna()
#save csv
df.to_csv("data.csv",index=False)

print("Data Saved to data.csv")