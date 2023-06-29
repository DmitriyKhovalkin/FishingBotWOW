# -*- coding: cp1251 -*-
import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint

#Условия для обращения
main_url = 'https://market.csgo.com/?t=all&rs=50;2000&sd=desc'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.75',
    'accept': '*/*'
           }

#Список предметов(оружия)
guns = []
#Константа
FILE = 'market.csv'

#Обращение к сайту
def get_html(url):
    r = requests.get(url, headers=headers)
    return r

#Основная функция
def parse(main_url = main_url):
    html = get_html(main_url)

    if html.status_code == 200:
        scr = html.text.encode('utf-8', 'ignore')
        soup = BeautifulSoup(scr, "lxml")
        all_items = soup.find_all('a', class_='item')

        for item in all_items[:-9]:
            name = item.find('div', class_="name").text[1:-1]
            price = item.find('div', class_="price").text.replace(" ", "").replace("\xa0", "")

            if name == None:
                continue
            else:
                guns.append({
                    'name': name.strip(),
                    'price': float(price),

            }
            )


#Функция сохранения файла
def save(items, path):
    with open(path, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название предмета', 'Цена'])
        for item in items:
            writer.writerow([item['name'], item['price']])




if __name__ == '__main__':
    parse(main_url)
    print("Первая итерация завершена.\n====================")

    for i in range(2, 6):
        main_url = f'https://market.csgo.com/?t=all&p={i}&rs=50;2000&sd=desc'
        parse(main_url)
        time.sleep(randint(2, 4))
        print(f"{i}-я из 50 итерация успешна \n====================")

    save(guns,FILE)