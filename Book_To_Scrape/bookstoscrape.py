from bs4 import BeautifulSoup
import requests
import csv
import json

url='https://books.toscrape.com/'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
books=soup.find_all('article',class_='product_pod')

Books_data=[]

for book in books:


    product_link=book.div.a['href']
    product_link=url + product_link
    img_src=book.div.a.img['src']
    img_src=url + img_src
    rating=book.p['class'][1]
    title=book.h3.a['title']
    price=book.find('div',class_='product_price').p.text

    book_info={
        "title":title,
        "product_link":product_link,
        "img_src":img_src,
        "rating":rating,
        "price":price.replace('\u00c2\u00a3','')

    }
    Books_data.append(book_info)
    
with open('Book_To_Scrape.json','w') as file:
    json.dump(Books_data,file,indent=4)
print("saved")    

  





    
    