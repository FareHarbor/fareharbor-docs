#!/usr/bin/env python

"""Retrieve bookings via FH External API

To use this sample script, set the FH_API_APP and FH_API_USER
environment variables in your shell.

"""

import os

import requests

api_base_url = os.environ.get('FH_API_BASE_URL', 'https://fareharbor.com/api/external/v1/')

HEADERS = {
    'X-FareHarbor-API-App': os.environ.get('FH_API_APP', ''),
    'X-FareHarbor-API-User': os.environ.get('FH_API_USER', ''),
}

date_ranges = [
    ('2023-01-01', '2023-01-08'),
    ('2023-01-08', '2023-01-15'),
    # etc.
]


def bookings_for_item(company_shortname, item_pk):
    item_bookings = []
    company_url = f'{api_base_url}companies/{company_shortname}/'
    for first, last in date_ranges:
        availabilities_url = f'{company_url}items/{item_pk}/minimal/availabilities/date-range/{first}/{last}/'
        print(availabilities_url)
        availabilities = requests.get(availabilities_url, headers=HEADERS).json()['availabilities']
        for availability in availabilities:
            url = f'{company_url}availabilities/{availability["pk"]}/bookings/'
            print(url)
            bookings = requests.get(url, headers=HEADERS).json()['bookings']
            print(bookings)
            item_bookings += bookings
    return item_bookings


all_bookings = []

companies_url = f'{api_base_url}companies/'
print(companies_url)
companies = requests.get(companies_url, headers=HEADERS).json()['companies']
print(companies)
for company in companies:
    items_url = f'{companies_url}{company["shortname"]}/items/'
    items = requests.get(items_url, headers=HEADERS).json()['items']
    for item in items:
        all_bookings += bookings_for_item(company['shortname'], item['pk'])

print(f'{len(all_bookings)} total bookings')
