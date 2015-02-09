FareHarbor External Integration API
-----------------------------------
# Set up

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

    ROOT_URL = 'https://fareharbor.com/api/external/v1'

# Listing companies

	companies_url = '%s/companies/' % ROOT_URL
	
	print companies_url

	response = requests.get(companies_url, headers=HEADERS)

	companies = json.parse(response.text)

	for company in companies:
    	print company

# Listing items for a company

	company = companies[0]
	
	items_url = '%s/companies/%s/items/' % (ROOT_URL, company['shortname'],)
	
	print items_url

	response = requests.get(items_url, headers=HEADERS)

	items = json.parse(response.text)

	for item in items:
    	print item
    	
# Listing availabilities for an item

	item = items[0]
	
	availabilities_url = '%s/companies/%s/items/%i/availabilities/date/2015-12-01/' % (
	    ROOT_URL, 
	    company['shortname'],
	    item['pk'],
	)
	
	print availabilities_url
	
	response = requests.get(availabilities_url, headers=HEADERS)
	
	availabilities = json.parse(response.text)
	
	for availability in availabilities:
		print availability
		
# Listing customer type rates for an availability

	availability = availabilities[0]
	
	customer_type_rates = availability['customer_type_rates']
	
	for customer_type_rate in customer_type_rates:
		print customer_type_rate
		
# Creating a booking for an availability

	customer_type_rate = customer_type_rates[0]

	book_url = '%s/companies/%s/availabilities/%i/bookings/' % (
		ROOT_URL,
		company['shortname'],
		availability['pk'],
	)
	
	print book_url
	
	data = {
		'contact': {
			'name': 'John Doe',
			'phone': '415-098-1234',
			'email': 'johndoe@gmail.com'
		},
		'customers': {
			'customer_type_rate': customer_type_rate['pk']
		}
	}
	
	response = requests.post(book_url, data=data, headers=HEADERS)
	
	booking = json.parse(response.text)
	
	print booking
	
# Retrieving a booking

	booking_url = '%s/companies/%s/bookings/%s/' % (
		ROOT_URL, 
		company['shortname'],
		booking['uuid'],
	)

	print booking_url

	response = requests.get(booking_url, headers=HEADERS)
	
	booking = json.parse(response.text)
	
	print booking
	


