#!/usr/bin/python3
""" Contains the default WebScrapper Processor for:
    Computrabajo domains to get Job Offers data
"""

import requests
from cli import cli_app
from var_pack import msg
from bs4 import BeautifulSoup

url_list = []

def offer_getter():
    """  """
    global num_pages;
    data_list = list()
    for i in range(num_pages):
        res = requests.get(url_list[i+1], headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

    url_offer = soup.find_all('a', 'js-o-link')

    offer_list = ['http://' + cur_currency[0:2] + '.' + cur_pag + urls.get('href') for urls in url_offer]

    print(offer_list)
    print(data_list)

def html_process():
    """ """
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
