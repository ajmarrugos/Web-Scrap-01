#!/usr/bin/python3
""" Contains the CLI that guides the user
    on the use of the WebScrapping Tool
"""
import json
import math
from time import sleep
from var_pack import msg
from datetime import datetime

# Wait time controller
sleep_time = 1

# Classes to process
classes = ['Offer']

# Constants
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
pages = ['computrabajo.com/']
countries = ['Mexico', 'Colombia', 'Argentina', 'Chile']
currencies = ['mxp', 'cop', 'ars', 'clp']

# Selected options
cur_pag = int()
cur_currency = str()
cur_country = str()

# Request Query
job_search = str()
num_offers = int()
num_pages = 1
my_url = str()
url_list = []
html_r = str()

def time_bar():
    now = datetime.now()
    ct = now.strftime("%H:%M:%S")
    print("\n" + msg.bar + ct + "\n")

def step0():
    """ Prints a Welcome Message to the screen """
    print("\n" + msg.welcome + "\n" + msg.bar + "\n")
    print(msg.intro1)
    print(msg.intro2)

def step1():
    """ Method used to select the URL WebScrapper to use """
    global cur_pag;
    time_bar()
    print(msg.quest1)

    for i, page in enumerate(pages):
        print(i + 1, page)

    answer1 = input("\n" + "R// ")

    if answer1 == '':
        print(msg.not_typed)
        step1()

    if answer1 != '1':
        print(msg.bad_selection)
        step1()

    if answer1 == '1':
        cur_pag = pages[0]
        print(msg.selection + cur_pag)

def step2():
    """ Method used to select the country to set a currency """
    global cur_country, cur_currency;
    time_bar()
    print(msg.quest2)
    print(msg.opt_count + str(len(countries)) + " options:")

    for i, country in enumerate(countries):
        print(i + 1, country)

    answer = input("\n" + "R// ")

    if answer == '':
        print(msg.not_typed)
        step2()

    while type(answer) != int:
        try:
            answer = int(answer)
        except:
            print(msg.not_int)
            step2()

    if answer > len(countries) or answer == 0:
        print(msg.bad_selection)
        step2()

    else:
        cur_country = countries[answer - 1]
        cur_currency = currencies[answer - 1]
        print(msg.selection + cur_country)
        print(msg.currency_format + (cur_currency).upper())

    return None

def step3():
    """ Method used to get the Position or Role to search """
    global job_search, my_url;
    time_bar()
    print(msg.quest3)

    answer = input("\n" + "R// ")

    if answer == '':
        print(msg.not_typed)
        step3()

    answer = ''.join(filter(lambda x: not x.isdigit(), answer))
    job_search = answer
    print(msg.typed + job_search)

def step4():
    """ Method used to get the number of offers to request """
    global num_offers, num_pages;
    time_bar()
    print(msg.quest4)

    answer = input("\n" + "R// ")

    if answer == '':
        print(msg.not_typed)
        step4()

    while type(answer) != int:
        try:
            answer = int(answer)
        except:
            print(msg.not_int)
            step4()

    else:
        num_offers = answer
        num_pages = math.ceil(num_offers / 20)

def url_builder():
    """ Function used to build a URL """
    global cur_pag, job_search, num_offers, my_url, url_list, num_pages, headers, html_r;
    time_bar()
    print(msg.quest5 + "\n")

    for i in range(num_pages):
        my_url = 'https://' + cur_currency[0:2] + '.' + cur_pag + 'trabajo-de-' + job_search + '/?p=' + str(i + 1)
        url_list.append(my_url)
        print(my_url)

    print("\n" + msg.total_pages + str(num_pages))
    answer = input("\n" + "R// ")

    if answer == 'y' or 'yes':
        time_bar();
        print(msg.working)
        for i in range(3):
            sleep(sleep_time)
            print(".")

        request_caller();

    else:
        print("Ok, going back...")
        step1()

def request_caller():
    """ """
    global num_pages;

    data_list = list()
    for page in range(info_scrapper):
        offers = offer_getter(page)
        for x in offers:
            data_list.append(info_scrapper(x))
        print(data_list)

    with open("retrieve_data.json", "w+") as jsonfile:
        json.dump(data_list, jsonfile, ensure_ascii=False)
        print(f'PAGE {page} --- Data retrieval completed!')

def offer_getter():
    """  """
    global headers, url_list;

    response = requests.get(str(url), headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    offer_boxes = soup.find_all('a', 'js-o-link')
    offer_urls = ['https://www' + '.' + cur_pag[:-1] + '.' + cur_currency[0:2] + '/' + urls.get('href') for urls in offer_boxes]

    print(url_list[0])
    print(offer_urls)


def info_scrapper(url):
    """ """
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')

    buffer = {}
    # Get Offer tittle
    try:
        offer_tittle = soup.find('h1', {'class': 'fwB fs24 mb5 box_detail w100_m'}).text
        buffer['Offer_tittle'] = offer_tittle
        print(buffer)
    except:
        buffer['Offer_tittle'] = 'N/A'
        print(buffer)
        print(msg.didnot_get)

    # Get Company Name
    try:
        comp_name = soup.find('a', {'class': 'dIB fs16 js-o-link'}).text
        buffer['Company'] = comp_name
        print(buffer)
    except:
        buffer['Company'] = 'N/A'
        print(buffer)
        print(msg.didnot_get)

    # Get Offer Location
    try:
        location = soup.find('p', {'class': 'fs16'}).text
        buffer['Location'] = location
        print(buffer)
    except:
        buffer['Location'] = 'N/A'
        print(buffer)
        print(msg.didnot_get)

    # Get Offer description
    try:
        description = soup.find('p', {'class': 'mbB'}).text
        buffer['Description'] = description
        print(buffer)
    except:
        buffer['Description'] = 'N/A'
        print(buffer)
        print(msg.didnot_get)

    # Get Offer Salary
    try:
        salary = soup.find('p', {'class': 'fwB fs21'}).text
        buffer['Salary'] = salary
    except:
        buffer['Salary'] = 'N/A'
        print(msg.didnot_get)

step0();
step1();
step2();
step3();
step4();
url_builder();
