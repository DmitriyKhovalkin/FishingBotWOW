import json
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from random import randint
import requests

FILE_csv = "file_csv.csv"
FILE_json = "file_json.json"
list_items = []
def get_html(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Safari/537.36',
        'accept': '*/*'
    }
    r = requests.get(url, headers=headers)
    return r


def check_site(url):
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service("E:\Parsing\Selenium_tutorial\driver\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        service.start()
        driver.get(url)
        time.sleep(randint(4, 6))
        with open("index1.html", "w", encoding='utf-8-sig') as file:
            file.write(driver.page_source)

    except Exception as ex:
        print(ex, "Ошибка!")
    finally:
        print("Закончили сохранять страницы.\nПереходим к следующему этапу...")
        driver.close()
        driver.quit()




def parce_site():
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service("E:\Parsing\Selenium_tutorial\driver\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    print("Открываем страницу")
    with open("index1.html", encoding='utf-8-sig') as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    all_items = soup.find_all('div', class_='product-card__wrapper')
    count = 0

    print("Ищем первые элементы")

    try:
        service.start()
        for item in all_items:
            name = item.find_next('span', class_='goods-name').text
            href = item.find_next('a', class_='product-card__main j-card-link').get('href')
            discount_price = item.find_next('p', class_='product-card__price price j-cataloger-price').text.strip()[:7]
            full_price = item.find_next('p', class_='product-card__price price j-cataloger-price').text.strip()[8:].strip()


            driver.get(href)
            time.sleep(randint(4, 6))
            search_info = driver.find_element(By.XPATH,
                                              '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[2]/div[2]/button')
            search_info.click()
            time.sleep(randint(1, 2))

            color = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/div[4]/div[2]/div/div[1]/p/span').text
            compound = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/div[3]/div/p/span[2]').text
            description = driver.find_element(By.XPATH,
                                              '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[2]/section[1]/div[2]/div[1]/p').text
            packing_width = driver.find_element(By.XPATH,
                                                '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[1]/td/span').text
            packing_length = driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[2]/td/span').text
            packing_height = driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[3]/td/span').text
            cut = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[4]/td/span').text
            picture = driver.find_element(By.XPATH,
                                          '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[5]/td/span').text
            material_texture = driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[6]/td/span').text
            clasp_type = driver.find_element(By.XPATH,
                                             '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[7]/td/span').text
            caring_for_things = driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[8]/td/span').text
            age_group = driver.find_element(By.XPATH,
                                            '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[9]/td/span').text
            hood = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[10]/td/span').text
            growth = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[11]/td/span').text
            size = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[12]/td/span').text
            model = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[13]/td/span').text
            appointment = driver.find_element(By.XPATH,
                                              '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[14]/td/span').text
            elements = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[15]/td/span').text
            like_heroes = driver.find_element(By.XPATH,
                                              '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[16]/td/span').text
            lining = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[17]/td/span').text
            made = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[18]/td/span').text
            complict = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[19]/td/span').text
            gender = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[20]/td/span').text
            season = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/main/div[2]/div/div[3]/div/div[3]/section/div[3]/div[1]/div/div[1]/div/table/tbody/tr[21]/td/span').text


    except Exception as ex:
        print(ex, "Ошибка!")

    finally:
        print("Закончили сохранять страницы.\nПереходим к следующему этапу...")
        driver.close()
        driver.quit()
        print("Запись данных в список")
        list_items.append({
            'name': name,
            'href': href,
            'discount_price': discount_price,
            'full_price': full_price,
            'color': color,
            'compound': compound,
            'description': description,
            'packing_width': packing_width,
            'packing_length': packing_length,
            'packing_height': packing_height,
            'cut': cut,
            'picture': picture,
            'material_texture': material_texture,
            'clasp_type': clasp_type,
            'caring_for_things':  caring_for_things,
            'age_group': age_group,
            'hood': hood,
            'growth':growth,
            'size': size,
            'model':model,
            'appointment': appointment,
            'elements': elements,
            'like_heroes': like_heroes,
            'lining': lining,
            'made': made,
            'complict': complict,
            'gender': gender,
            'season': season,
        })
        count += 1
        print(f'{count} - товар просканирован')
    print('Происходит сохранение, не выключайте компьютер.')
    save(list_items, FILE_csv, FILE_json)


def save(items, path_csv, path_json):
    with open(path_csv, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название фирмы', 'Краткое описание', 'Страница на сайте', "Телефон", 'Сайт'])
        for list_items in items:
            writer.writerow([
                list_items['name'],
                list_items['href'],
                list_items['discount_price'],
                list_items['full_price'],
                list_items['color'],
                list_items['compound'],
                list_items['description'],
                list_items['packing_width'],
                list_items['packing_length'],
                list_items['packing_height'],
                list_items['cut'],
                list_items['picture'],
                list_items['material_texture'],
                list_items['clasp_type'],
                list_items['caring_for_things'],
                list_items['age_group'],
                list_items['hood'],
                list_items['growth'],
                list_items['size'],
                list_items['model'],
                list_items['appointment'],
                list_items['elements'],
                list_items['like_heroes'],
                list_items['lining'],
                list_items['made'],
                list_items['complict'],
                list_items['gender'],
                list_items['season']
            ])
    with open(path_json, 'w', encoding='utf-8-sig') as file:
        json.dump(items, file, indent=4, ensure_ascii=False
                  )
    print("Сохрание завершено.")


def main():
    # url = 'https://www.wildberries.ru/brands/sharp-and-?sort=popular&cardsize=c516x688&page=1'
    # check_site(url)
    parce_site()




if __name__=='__main__':
    main()





"""Алгоритм удаления дудликатов"""
    # a = [{"r": "2", 'c': "3"}, {"r": "4", 'c': "3"}]
    # if [{"r": "2"}] in a:
    #     print(a)
    # else:
    #     print('not')
    #
    # print(len(a))

    # for k in range(0,len(a)):
    #     if a[k]["r"] == "2":
    #         a.pop(k)
    #         break
    # print(a)