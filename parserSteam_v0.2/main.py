# -*- coding: cp1251 -*-
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import csv


ua = UserAgent()
guns = []
FILE = "steammarket.csv"

def chrome():

    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={ua.random}")
    service = Service('E:\Parsing\Selenium_tutorial\driver\chromedriver.exe')
    browser = webdriver.Chrome(service=service, options=options)

    try:
        service.start()


        #browser = webdriver.Remote(service.service_url)

        browser.get('https://steamcommunity.com/market/search?appid=730')
        time.sleep(9)
        with open("index1.html", "w", encoding='utf-8-sig') as file:
            file.write(browser.page_source)
        for i in range(2, 11):
            browser.get(f'https://steamcommunity.com/market/search?appid=730#p{i}_popular_desc')
            time.sleep(4)
            with open(f"index{i}.html", "w", encoding='utf-8-sig') as file:
                file.write(browser.page_source)


    except Exception as ex:
        print(ex, "  Шо за хуйня?!")
    finally:
        print("Закончили сохранять страницы Steam.\nПереходим к следующему этапу...")
        browser.close()
        browser.quit()

#Парсим Стим
def parce_steam():
    for i in range(1, 11):
        with open(f"index{i}.html", encoding='utf-8-sig') as file:
            src = file.read()
        soup = BeautifulSoup(src, "lxml")

        items = soup.find_all('div', class_='market_listing_row market_recent_listing_row market_listing_searchresult')

        for item in items:
            names = item.find_next('div', class_='market_listing_item_name_block')
            name = names.find_next('span').text.strip()
            items_price = item.find_next('div', class_='market_listing_right_cell market_listing_their_price')
            item_price1 = items_price.find_next('span').find('span').text
            guns.append({
                'name': name,
                'normal_price': item_price1

            }
            )
        print(f"{i}-я страница готова")
#Функция сохранения файла
def save(items, path):
    with open(path, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название предмета', 'Цена Steam'])
        for item in items:
            writer.writerow([item['name'], item['normal_price']])


if __name__ == '__main__':
    chrome()
    parce_steam()
    save(guns, FILE)


