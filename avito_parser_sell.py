import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep


def get_db():
    """Getting a database in SQlite"""
    conn = sqlite3.connect(r'/Users/wazinak/Desktop/Pet Projects/powerfull_parse/apple_data.db')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS apple_products (
    id INTEGER PRIMARY KEY,
    num_id INT,
    name TEXT, 
    price INT,
    description TEXT,
    link TEXT
    )
    ''')
    conn.commit()
    conn.close()




def get_chromedriver():
    chrome_options = webdriver.ChromeOptions()
    service = Service(executable_path=ChromeDriverManager().install())
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=800,700")
    chrome_options.add_argument("--disable-blink-features=AutomationConrtolled")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(options=chrome_options, service=service)
    return driver


def macbookpro():
    driver = get_chromedriver()
    driver.get('https://www.avito.ru/moskva/noutbuki/novoe-ASgBAgICAUTwvA2G0jQ?cd=1&q=macbook+pro+2023&s=104')
    sleep(5)
    return driver


def get_page_num_mbp():
    driver = macbookpro()
    soup = BeautifulSoup(driver.page_source, 'lxml')
    pages = soup.find('a', class_='styles-module-item-kF45w styles-module-item_size_s-Tvz95 '
                                  'styles-module-item_last-vIJIa styles-module-item_link-_bV2N').find(
        'span', class_='styles-module-text-InivV').text
    return pages


def get_list_mbp():
    data = []
    url = 'https://www.avito.ru'
    driver = macbookpro()
    soup = BeautifulSoup(driver.page_source, 'lxml')
    pages = get_page_num_mbp()
    elements = soup.find_all('div', class_='iva-item-root-_lk9K photo-slider-slider-S15A_ '
                                           'iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_'
                                           'lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum')
    for p in range(int(pages)):
        driver.execute_script("window. scrollBy(0, 11550)")
        sleep(4)
        driver.find_element('xpath', '//*[@id="app"]/div/div[3]/div/'
                                     'div[2]/div[3]/div[3]/div[4]/nav/ul/li[9]/a').click()
        for i in elements:
            num_id = i.get('data-item-id')
            name = i.find('h3', class_='styles-module-root-TWVKW styles-module-root-_KFFt styles-module-size_l-_oGDF '
                                       'styles-module-size_l_compensated-OK6a6 styles-module-size_l-hruVE '
                                       'styles-module-ellipsis-LKWy3 styles-module-weight_bold-Kpd5F '
                                       'stylesMarningNormal-module-root-OSCNq '
                                       'stylesMarningNormal-module-header-l-qvNIS').text
            price = i.find('div', class_='price-price-JP7qe').find_all('meta')[1].get('content')
            description = i.find('p', class_='styles-module-root-_KFFt styles-module-size_s-awPvv '
                                             'styles-module-size_s_compensated-Wo8uc styles-module-size_s-_P6ZA '
                                             'styles-module-ellipsis-LKWy3 stylesMarningNormal-module-root-OSCNq '
                                             'stylesMarningNormal-module-paragraph-s-_c6vD '
                                             'styles-module-noAccent-nZxz7 styles-module-root_bottom-XgXHc '
                                             'styles-module-margin-bottom_6-nU1Wp').text.replace("\n", "")
            link = i.find('a', class_='styles-module-root-QmppR styles-module-root_noVisited-aFA10').get('href')
            data.append([num_id, name, price, description, url + link])
        return data


def imac2017():
    driver = get_chromedriver()
    driver.get(
        'https://www.avito.ru/moskva/nastolnye_kompyutery/monobloki-ASgBAgICAUS02xKOqY0D?cd=1&q=imac+27+2017&s=104')
    sleep(4)
    return driver


def get_page_num_imac2017():
    driver = imac2017()
    soup = BeautifulSoup(driver.page_source, 'lxml')
    pages = soup.find('a', class_='styles-module-item-kF45w styles-module-item_size_s-Tvz95 '
                                  'styles-module-item_last-vIJIa styles-module-item_link-_bV2N').find(
        'span', class_='styles-module-text-InivV').text
    return pages


def get_list_imac2017():
    data = []
    url = 'https://www.avito.ru/'
    driver = imac2017()
    soup = BeautifulSoup(driver.page_source, 'lxml')
    pages = get_page_num_imac2017()
    elements = soup.find_all('div', class_='iva-item-root-_lk9K photo-slider-slider-S15A_ '
                                           'iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_'
                                           'lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum')
    for p in range(int(pages)):
        driver.execute_script("window. scrollBy(0, 11550)")
        sleep(4)
        driver.find_element('xpath', '//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[3]/div[4]/nav/ul/li[4]/a').click()
        sleep(3)
        for i in elements:
            num_id = i.get('data-item-id')
            name = i.find('h3', class_='styles-module-root-TWVKW styles-module-root-_KFFt styles-module-size_l-_oGDF '
                                       'styles-module-size_l_compensated-OK6a6 styles-module-size_l-hruVE '
                                       'styles-module-ellipsis-LKWy3 styles-module-weight_bold-Kpd5F '
                                       'stylesMarningNormal-module-root-OSCNq '
                                       'stylesMarningNormal-module-header-l-qvNIS').text
            price = i.find('div', class_='price-price-JP7qe').find_all('meta')[1].get('content')
            description = i.find('p', class_='styles-module-root-_KFFt styles-module-size_s-awPvv '
                                             'styles-module-size_s_compensated-Wo8uc styles-module-size_s-_P6ZA '
                                             'styles-module-ellipsis-LKWy3 stylesMarningNormal-module-root-OSCNq '
                                             'stylesMarningNormal-module-paragraph-s-_c6vD '
                                             'styles-module-noAccent-nZxz7 styles-module-root_bottom-XgXHc '
                                             'styles-module-margin-bottom_6-nU1Wp').text.replace("\n", "")
            link = i.find('a', class_='styles-module-root-QmppR styles-module-root_noVisited-aFA10').get('href')
            data.append([num_id, name, price, description, url + link])
            # print(num_id, name)
        return data


def imac2019():
    driver = get_chromedriver()
    driver.get('https://www.avito.ru/moskva/nastolnye_kompyutery/monobloki-ASgBAgICAUS02xKOqY0D?q=imac+27+2019&s=104')
    sleep(5)
    return driver


def get_page_num_imac2019():
    driver = imac2019()
    soup = BeautifulSoup(driver.page_source, 'lxml')
    pages = soup.find('a', class_='styles-module-item-kF45w styles-module-item_size_s-Tvz95 '
                                  'styles-module-item_last-vIJIa styles-module-item_link-_bV2N').find(
        'span', class_='styles-module-text-InivV').text
    return pages


def get_list_imac2019():
    data = []
    url = 'https://www.avito.ru/'
    driver = imac2019()
    soup = BeautifulSoup(driver.page_source, 'lxml')
    pages = get_page_num_imac2019()
    elements = soup.find_all('div', class_='iva-item-root-_lk9K photo-slider-slider-S15A_ '
                                           'iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_'
                                           'lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum')
    for p in range(int(pages)):
        driver.execute_script("window. scrollBy(0, 11550)")
        sleep(4)
        driver.find_element('xpath', '//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[3]/div[4]/nav/ul/li[4]/a').click()
        sleep(3)
        for i in elements:
            num_id = i.get('data-item-id')
            name = i.find('h3', class_='styles-module-root-TWVKW styles-module-root-_KFFt styles-module-size_l-_oGDF '
                                       'styles-module-size_l_compensated-OK6a6 styles-module-size_l-hruVE '
                                       'styles-module-ellipsis-LKWy3 styles-module-weight_bold-Kpd5F '
                                       'stylesMarningNormal-module-root-OSCNq '
                                       'stylesMarningNormal-module-header-l-qvNIS').text
            price = i.find('div', class_='price-price-JP7qe').find_all('meta')[1].get('content')
            description = i.find('p', class_='styles-module-root-_KFFt styles-module-size_s-awPvv '
                                             'styles-module-size_s_compensated-Wo8uc styles-module-size_s-_P6ZA '
                                             'styles-module-ellipsis-LKWy3 stylesMarningNormal-module-root-OSCNq '
                                             'stylesMarningNormal-module-paragraph-s-_c6vD '
                                             'styles-module-noAccent-nZxz7 styles-module-root_bottom-XgXHc '
                                             'styles-module-margin-bottom_6-nU1Wp').text.replace("\n", "")
            link = i.find('a', class_='styles-module-root-QmppR styles-module-root_noVisited-aFA10').get('href')
            data.append([num_id, name, price, description, url + link])
            # print(num_id, name)
        return data
def insert_db():
    data = get_list_imac2019()
    data += get_list_mbp()
    data += get_list_imac2017()
    conn = sqlite3.connect(r'/Users/wazinak/Desktop/Pet Projects/powerfull_parse/apple_data.db')
    cur = conn.cursor()
    for item in data:
        cur.execute("INSERT INTO apple_products (num_id, name, price, description, link) VALUES (?,?,?,?,?)", (item[0],item[1],item[2],item[3],item[4]))

    conn.commit()
    conn.close()


def del_duplicate():
    conn = sqlite3.connect(r'/Users/wazinak/Desktop/Pet Projects/powerfull_parse/apple_data.db')
    cur = conn.cursor()
    sql_query = """
        DELETE FROM apple_products
        WHERE rowid NOT IN
        (
            SELECT MIN(rowid)
            FROM apple_products
            GROUP BY num_id
        )
        """
    cur.execute(sql_query)
    conn.commit()
    conn.close()
    print('Дубликаты удаленны')


def main():
    get_db()
    get_list_mbp()
    get_list_imac2017()
    get_list_imac2019()
    insert_db()
    del_duplicate()


if __name__ == '__main__':
    main()
