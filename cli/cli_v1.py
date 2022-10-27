#!/usr/bin/python3
""" Contains the CLI that guides the user
    on the use of the WebScrapping Tool
"""
import json
import math
import scrap_engine
from time import sleep
from var_pack import msg
from datetime import datetime

# Wait time controller
sleep_time = 1

# Classes to process
classes = ['Offer']

# Constants
pages = ['computrabajo.com/']
countries = ['Mexico', 'Colombia', 'Argentina', 'Chile']
currencies = ['mxp', 'cop', 'ars', 'clp']

# Selected options
pag = int()
dom = str()
cur_currency = str()

# Request Query
pag = "computrabajo.com/"
dom = "ar"
pos =  "desarrollador"
num_offers = "25"


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
    global pag;
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
        pag = pages[0]
        print(msg.selection + pag)

def step2():
    """ Method used to select the country to set a currency """
    global dom, cur_currency;
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
        dom = countries[answer - 1]
        cur_currency = currencies[answer - 1]
        print(msg.selection + dom)
        print(msg.currency_format + (cur_currency).upper())

    return None

def step3():
    """ Method used to get the Position or Role to search """
    global pos, my_url;
    time_bar()
    print(msg.quest3)

    answer = input("\n" + "R// ")

    if answer == '':
        print(msg.not_typed)
        step3()

    answer = ''.join(filter(lambda x: not x.isdigit(), answer))
    pos = answer
    print(msg.typed + pos)

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

step0();
step1();
step2();
step3();
url_builder(dom, pag, pos);
step4();

request_trigger(num_offers);

if __name__ == '__main__':
    welcome()
