import requests
from bs4 import BeautifulSoup
import csv

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
all_books = []

# نعملو حلقة على الصفحات الأولى مثلاً (5 صفحات)
for page in range(1, 6):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        link = "http://books.toscrape.com/catalogue/" + book.h3.a["href"]

        all_books.append([title, price, link])

# نكتب البيانات في ملف CSV
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Link"])
    writer.writerows(all_books)

print("✅ تم حفظ البيانات في ملف books.csv")
