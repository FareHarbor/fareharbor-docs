<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Setup](#setup)
    - [Dependencies](#dependencies)
    - [Request headers](#request-headers)
    - [Root URL](#root-url)
- [Listing companies](#listing-companies)
- [Listing items for a company](#listing-items-for-a-company)
- [Listing availabilities for an item](#listing-availabilities-for-an-item)
- [Listing customer type rates for an availability](#listing-customer-type-rates-for-an-availability)
- [Creating a booking for an availability](#creating-a-booking-for-an-availability)
- [Retrieving a booking](#retrieving-a-booking)
- [Entire script](#entire-script)

<!-- markdown-toc end -->

# Setup

## Dependencies

The Python json package.

    import json

The Python requests library. Installation instructions: 
http://docs.python-requests.org/en/latest/user/install/#install

    import requests

## Request headers

    APP_KEY = 'your app key'
    USER_KEY = 'your user key'

    HEADERS = {
        'X-FareHarbor-API-App': APP_KEY,
        'X-FareHarbor-API-User': USER_KEY
    }

## Root URL

    ROOT_URL = 'https://test.fareharbor.com/api/external/v1'

# Listing companies

    companies_url = '%s/companies/' % ROOT_URL
    
    print(companies_url)

    response = requests.get(companies_url, headers=HEADERS)

    response_data = json.loads(response.text)
    companies = response_data['companies']

    for company in companies:
        print(company)

# Listing items for a company

    company = companies[0]
    
    items_url = '%s/companies/%s/items/' % (ROOT_URL, company['shortname'],)
    
    print(items_url)

    response = requests.get(items_url, headers=HEADERS)

    response_data = json.loads(response.text)
    items = response_data['items']

    for item in items:
        print(item)
        
# Listing availabilities for an item

    item = items[0]
    
    availabilities_url = '%s/companies/%s/items/%i/availabilities/date/2015-12-01/' % (
        ROOT_URL, 
        company['shortname'],
        item['pk'],
    )
    
    print(availabilities_url)
    
    response = requests.get(availabilities_url, headers=HEADERS)
    
    response_data = json.loads(response.text)
    availabilities = response_data['availabilities']
    
    for availability in availabilities:
        print(availability)
        
# Listing customer type rates for an availability

    availability = availabilities[0]
    
    customer_type_rates = availability['customer_type_rates']
    
    for customer_type_rate in customer_type_rates:
        print(customer_type_rate)
        
# Creating a booking for an availability

    customer_type_rate = customer_type_rates[0]

    book_url = '%s/companies/%s/availabilities/%i/bookings/' % (
        ROOT_URL,
        company['shortname'],
        availability['pk'],
    )
    
    print(book_url)
    
    request_data = {
        'contact': {
            'name': 'John Doe',
            'phone': '415-098-1234',
            'email': 'johndoe@gmail.com'
        },
        'customers': [
            {
                'customer_type_rate': customer_type_rate['pk']
            }
        ],
        "note": "Optional booking note.",
        "voucher_number": "V-35791209"
    }
    request_data = json.dumps(request_data)

    response = requests.post(book_url, data=request_data, headers=HEADERS)
    
    response_data = json.loads(response.text)
    booking = response_data['booking']
    
    print(booking)
    
# Retrieving a booking

    booking_url = '%s/companies/%s/bookings/%s/' % (
        ROOT_URL, 
        company['shortname'],
        booking['uuid'],
    )

    print(booking_url)

    response = requests.get(booking_url, headers=HEADERS)
    
    response_data = json.loads(response.text)
    booking = response_data['booking']
        
    print(booking)
    
# Entire script

    import json
    import requests

    APP_KEY = 'your app key'
    USER_KEY = 'your user key'

    HEADERS = {
        'X-FareHarbor-API-App': APP_KEY,
        'X-FareHarbor-API-User': USER_KEY
    }

    ROOT_URL = 'https://test.fareharbor.com/api/external/v1'

    # COMPANIES

    companies_url = '%s/companies/' % ROOT_URL

    print(companies_url)

    response = requests.get(companies_url, headers=HEADERS)

    response_data = json.loads(response.text)
    companies = response_data['companies']

    for company in companies:
        print(company)

    # ITEMS

    company = companies[0]

    items_url = '%s/companies/%s/items/' % (ROOT_URL, company['shortname'],)

    print(items_url)

    response = requests.get(items_url, headers=HEADERS)

    response_data = json.loads(response.text)
    items = response_data['items']

    for item in items:
        print(item)

    # AVAILABILITIES

    item = items[0]

    availabilities_url = '%s/companies/%s/items/%i/availabilities/date/2015-12-01/' % (
        ROOT_URL,
        company['shortname'],
        item['pk'],
    )

    print(availabilities_url)

    response = requests.get(availabilities_url, headers=HEADERS)

    response_data = json.loads(response.text)
    availabilities = response_data['availabilities']

    for availability in availabilities:
        print(availability)

    # CUSTOMER TYPE RATES

    availability = availabilities[0]

    customer_type_rates = availability['customer_type_rates']

    for customer_type_rate in customer_type_rates:
        print(customer_type_rate)

    # CREATE BOOKING

    customer_type_rate = customer_type_rates[0]

    book_url = '%s/companies/%s/availabilities/%i/bookings/' % (
        ROOT_URL,
        company['shortname'],
        availability['pk'],
    )

    print(book_url)

    request_data = {
        'contact': {
            'name': 'John Doe',
            'phone': '415-098-1234',
            'email': 'johndoe@gmail.com'
        },
        'customers': [
            {
                'customer_type_rate': customer_type_rate['pk']
            }
        ],
        "voucher_number": "V-35791209"
    }
    request_data = json.dumps(request_data)

    response = requests.post(book_url, data=request_data, headers=HEADERS)

    response_data = json.loads(response.text)
    booking = response_data['booking']

    print(booking)

    # RETRIEVE BOOKING

    booking_url = '%s/companies/%s/bookings/%s/' % (
        ROOT_URL,
        company['shortname'],
        booking['uuid'],
    )

    print(booking_url)

    response = requests.get(booking_url, headers=HEADERS)

    response_data = json.loads(response.text)
    booking = response_data['booking']

    print(booking)
