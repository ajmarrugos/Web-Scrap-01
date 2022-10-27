#!/usr/bin/python3
""" Contains the Web Scrapping Engine that helps
    the program to process data and make URL Requests
"""

import json
import math
import requests
# from cli_app import request_trigger
from cli.var_pack import msg
from datetime import datetime
from bs4 import BeautifulSoup
from db.models import storage
from db.models.job_offer import JobOffer

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

pag = "computrabajo.com/"
dom = "co"
pos =  "abogado"
num_offers = "19"

page = ""
search = ""

def welcome():
    print(msg.welcome)
    print(msg.intro1)
    print(msg.intro2)

def time_bar():
    """ """
    now = datetime.now()
    ct = now.strftime("%H:%M:%S")
    print("\n" + msg.bar + ct + "\n")

def url_builder(dom, pag, pos):
    """ """
    global page, search;
    #
    page = 'https://' + dom + '.' + pag
    #
    search = 'trabajo-de-' + pos + '?p='
    #
    return(page + search)


def get_url_list(page, search, num):
    """ """
    global headers;

    url = page + search + str(num)

    # Makes a URL request and saves the response into a variable
    req = requests.get(url, headers=headers)

    # Uses BeautifulSoup to parse the text response from last request
    soup = BeautifulSoup(req.text, 'html.parser')

    # Scraps the soup to fetch some tags
    offers_data = soup.find_all('a', 'js-o-link')

    # Makes a list of new URLs from the results found
    url_list = [page + urls.get('href') for urls in offers_data]

    # Prints the content of the list
    print(url)
    return(url_list)


def job_scrapper(url):
    """ """
    buffer = {}

    # Makes a URL request and saves the response into a variable
    res = requests.get(url, headers=headers)

    # Uses BeautifulSoup to parse the text response from last request
    soup = BeautifulSoup(res.text, 'html.parser')

    # Get Offer tittle
    try:
        offer_tittle = soup.find('h1', {'class': 'fwB fs24 mb5 box_detail w100_m'}).text
        buffer['Offer_tittle'] = offer_tittle
        print(buffer)
    except:
        buffer['Offer_tittle'] = 'N/A'
        print(buffer)
        print("\n" + msg.didnot_get)

    # Get Company Name
    try:
        company = soup.find('a', {'class': 'dIB fs16 js-o-link'}).text
        buffer['Company'] = company
        print(buffer)
    except:
        buffer['Company'] = 'N/A'
        print(buffer)
        print("\n" + msg.didnot_get)

    # Get Offer Location
    try:
        location = soup.find('p', {'class': 'fs16'}).text
        buffer['Location'] = location
        print(buffer)
    except:
        buffer['Location'] = 'N/A'
        print(buffer)
        print("\n" + msg.didnot_get)

    # Get Offer description
    try:
        description = soup.find('p', {'class': 'mbB'}).text
        buffer['Description'] = description
        print(buffer)
    except:
        buffer['Description'] = 'N/A'
        print(buffer)
        print("\n" + msg.didnot_get)

    # Get Offer requirements
    try:
        requirements = ''
        reqmnt = soup.find('ul', {'class': 'disc mbB'}).find_all('li')
        for i in reqmnt:
            requirements = requirements + i.text + ';'
        buffer['Requirements'] = requirements
    except:
        buffer['Requirements'] = 'N/A'
        print("\n" + msg.didnot_get)

    # Get Offer Salary
    try:
        salary = soup.find('p', {'class': 'fwB fs21'}).text
        buffer['Salary'] = salary
    except:
        buffer['Salary'] = 'N/A'
        print("\n" + msg.didnot_get)
    
    return buffer


def request_trigger(num_offers):
    """ """
    # Sets a list where to acomulate data
    data_list = list()
    num_offers = int(num_offers);

    # Divides offer quantity to get pages to search
    num_pages = math.ceil(num_offers / 20)

    # Will iterate and look on every page to get inside offer boxes
    for i in range(1, num_pages+1):
        time_bar()
        print("Looking inside page # " + str(i))
        offers = get_url_list(page, search, i)

        # Will iterate, enumerate and extract every Job Offer found
        for x, offers in enumerate(offers):
            time_bar()
            print("Extracting data from Offer # " + str(x))
            print(offers)
            got_dictionary = job_scrapper(offers)
            data_list.append(got_dictionary)
            current_offer = JobOffer(**got_dictionary)
            storage.new(current_offer)
            storage.save()
            print('Data saved')

    #
    with open("output_data.json", "w+") as jsonfile:
        json.dump(data_list, jsonfile, ensure_ascii=False)
        print(f'PAGE {page} --- Data saved!')

welcome();

url_builder(dom, pag, pos);

request_trigger(num_offers);
