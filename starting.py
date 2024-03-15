
import sqlite3
import requests
from bs4 import BeautifulSoup
from time import sleep

def get_db():
    """Getting a database in SQlite"""
    conn = sqlite3.connect(r'/Users/wazinak/Desktop/Pet Projects/powerfull_parse/my_data.db')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY,
    name TEXT,
    author TEXT, 
    link TEXT
    )
    ''')
    conn.commit()
    conn.close()

def check_status():
    elements_list = []
    for p in range(1, 11):
        url = f'https://book24.ru/novie-knigi/page-{p}/'
        r = requests.get(url)
        # print(r.status_code)
        print(p)
        # sleep(1)
        soup = BeautifulSoup(r.text, 'lxml')
        elements = soup.find_all('div', class_='product-list__item')
        elements_list.extend(elements)
        #print(url)
    return elements_list


def getting_info():
    elements = check_status()
    data = []
    host = 'https://book24.ru'
    for i in elements:
        name = i.find('a', class_='product-card__name').text
        try:
            author = i.find('div', class_='author-list product-card__authors-holder').text
        except AttributeError:
            continue
        link = i.find('div', class_='product-card__content').find('a').get('href')
        data.append([name, author, host+link])

    return data

def insert_db():
    data = getting_info()
    conn = sqlite3.connect(r'/Users/wazinak/Desktop/Pet Projects/powerfull_parse/my_data.db')
    cur = conn.cursor()

    for item in data:
        cur.execute("INSERT INTO data (name, author, link) VALUES (?,?,?)", (item[0],item[1],item[2]))

    conn.commit()
    conn.close()

def del_duplicate():
    conn = sqlite3.connect(r'/Users/wazinak/Desktop/Pet Projects/powerfull_parse/my_data.db')
    cur = conn.cursor()

    sql_query = """
    DELETE FROM data
    WHERE rowid NOT IN
    (
        SELECT MIN(rowid)
        FROM data
        GROUP BY name
    )
    """
    cur.execute(sql_query)
    conn.commit()
    conn.close()
    print('Дубликаты удаленны')


def main():
    get_db()
    getting_info()
    insert_db()
    del_duplicate()


if __name__ == '__main__':
    main()
