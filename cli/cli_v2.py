#!/usr/bin/python3
""" Contains the Command Line Interface that allows
    User to manipulate the program
"""

import click
import json
import math
import requests
from cli.var_pack import msg

PAGES = {
    "1": "computrabajo.com/"
}

DOMAINS = {
    "1": "mx",
    "2": "co",
    "3": "ar",
    "4": "cl"
}

page = ""
search = ""

@click.command()
@click.argument("pag", type=click.Choice(PAGES.keys()), default="1")
@click.argument("dom", type=click.Choice(DOMAINS.keys()), default="1")
@click.option("-p", "--pos", prompt="Type the position you want to search ", help="Position to search")
def url_builder(pag, dom, pos):
    """c"""
    global page, search;

    page = 'https://' + dom + '.' + pag

    search = 'trabajo-de-' + pos + '?p='

    return(page + search)

@click.command()
@click.option("--num", prompt="Enter number of offers to get ", help="Number of Offers")
def request_trigger(num):
    """ """
    # Sets a list where to acomulate data
    data_list = list()
    num_offers = int(num);

    # Divides offer quantity to get pages to search
    num_pages = math.ceil(num_offers / 20)

    # Will iterate and look on every page to get inside offer boxes
    for i in range(1, num_pages+1):
        print("\n" + "Looking inside page # " + str(i))
        offers = get_url_list(page, search, i)

        # Will iterate, enumerate and extract every Job Offer found
        for x, offers in enumerate(offers):
            print("\n" + "Extracting data from Offer # " + str(x))
            print(offers)

            got_dictionary = job_scrapper(offers)
            data_list.append(got_dictionary)

            """
            current_offer = JobOffer(**got_dictionary)
            storage.new(current_offer)
            storage.save()
            print('Data saved')
            """

    with open("output_data.json", "w+") as jsonfile:
        json.dump(data_list, jsonfile, ensure_ascii=False)
        print(f'PAGE {page} --- Data saved!')


if __name__ == "__main__":
    url_builder()
