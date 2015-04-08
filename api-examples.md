FareHarbor External Integration API
-----------------------------------
# Examples

## Companies endpoint

### Retrieve a list of companies

Request:
    
    $ curl -H "X-FareHarbor-API-App: APP-KEY" -H "X-FareHarbor-API-User: USER-KEY" https://fareharbor.com/api/external/v1/companies/ 

Response:

    {
      "companies": [
        {
          'name': 'XYZ Scuba',
          'shortname': 'xyz'
        }
      ]
    }

## Items endpoint

### Retrieve a list of items for a company

Request:

    $ curl -H "X-FareHarbor-API-App: APP-KEY" -H "X-FareHarbor-API-User: USER-KEY" https://fareharbor.com/api/external/v1/companies/xyz/items/

Response:

    {
      "items": [
        {
          "cancellation_policy": "If you cancel your reservation outside 48 hours of dive trip, 100% refund will be given.",
          "cancellation_policy_safe_html": "\u003cp\u003eIf you cancel your reservation outside 48 hours of dive trip, 100% refund will be given.\u003c\/p\u003e",
          "description": "We’ll take you on two thrilling tank dives.",
          "description_safe_html": "\u003cp\u003eWe\u2019ll take you on two thrilling tank dives.\u003c\/p\u003e",
          "headline": "",
          "image_cdn_url": "https:\/\/d1a2dkr8rai8e2.cloudfront.net\/api\/file\/lYsz2SeTaS8s5oRMxO6b",
          "location": "",
          "name": "Wreck & Reef Dive",
          "pk": 28
        }
      ]
    }

## Availabilities endpoint

### Retrieve a list of availabilities for an item 

Request:

    $ curl -H "X-FareHarbor-API-App: APP-KEY" -H "X-FareHarbor-API-User: USER-KEY" https://fareharbor.com/api/external/v1/companies/xyz/items/85/availabilities/date/2015-02-01/

Response:

    {
      "availabilities": [
        {
          "capacity": 20,
          "customer_type_rates": [
            {
              "capacity": null,
              "customer_type": {
                "note": "",
                "pk": 29,
                "plural": "Certified Divers Needing Rental Equipment",
                "singular": "Certified Diver Needing Rental Equipment"
              },
              "pk": 8964452,
              "total": 12900
            }
          ],
          "end_at": "2015-02-01T10:30:00-1000",
          "item": {
            "name": "Wreck & Reef Dive",
            "pk": 28
          },
          "pk": 3267113,
          "start_at": "2015-02-01T07:00:00-1000"
        }
      ]
    }

Request:

    $ curl -H "X-FareHarbor-API-App: APP-KEY" -H "X-FareHarbor-API-User: USER-KEY" https://fareharbor.com/api/external/v1/companies/xyz/items/85/availabilities/date-range/2015-02-01/2015-02-15/

Response:

    {
      "availabilities": [
        {
          "capacity": 20,
          "customer_type_rates": [
            {
              "capacity": null,
              "customer_type": {
                "note": "",
                "pk": 29,
                "plural": "Certified Divers Needing Rental Equipment",
                "singular": "Certified Diver Needing Rental Equipment"
              },
              "pk": 8964452,
              "total": 12900
            }
          ],
          "end_at": "2015-02-01T10:30:00-1000",
          "item": {
            "name": "Wreck & Reef Dive",
            "pk": 28
          },
          "pk": 3267113,
          "start_at": "2015-02-01T07:00:00-1000"
        },
        {
          "capacity": 20,
          "customer_type_rates": [
            {
              "capacity": null,
              "customer_type": {
                "note": "",
                "pk": 29,
                "plural": "Certified Divers Needing Rental Equipment",
                "singular": "Certified Diver Needing Rental Equipment"
              },
              "pk": 8966452,
              "total": 12900
            }
          ],
          "end_at": "2015-02-13T10:30:00-1000",
          "item": {
            "name": "Wreck & Reef Dive",
            "pk": 28
          },
          "pk": 3267913,
          "start_at": "2015-02-13T07:00:00-1000"
        }
      ]
    }

## Bookings endpoint

### Create a booking for an availability

Request:

    $ curl -X POST \
    -H "X-FareHarbor-API-App: APP-KEY" \
    -H "X-FareHarbor-API-User: USER-KEY" \
    -d \
    '{
       "contact": {
         "name": "John Doe", 
         "phone": "415-789-4563", 
         "email": "johndoe@example.com"
       }, 
       "customers": [
         {
           "customer_type_rate": 8964453
         }
       ],
       "voucher_number": "V-35791209"
    }' \
    https://fareharbor.com/api/external/v1/companies/xyz/availabilities/10780/bookings/
    
Response:

    {
      "booking": {
        "availability": {
          "capacity": 20,
          "customer_type_rates": [
            {
              "capacity": null,
              "customer_type": {
                "note": "",
                "pk": 29,
                "plural": "Certified Divers Needing Rental Equipment",
                "singular": "Certified Diver Needing Rental Equipment"
              },
              "pk": 8964452,
              "total": 12900
            }
          ],
          "end_at": "2015-02-01T10:30:00-1000",
          "item": {
            "name": "Wreck & Reef Dive",
            "pk": 28
          },
          "pk": 3267113,
          "start_at": "2015-02-01T07:00:00-1000"
        }
        "contact": {
          "phone": "415-789-4563",
          "name": "John Doe",
          "email": "johndoe@example.com"
        },
        "customers": [
          {
            "customer_type_rate": {
              "capacity": null
              "customer_type": {
                "note": "",
                "pk": 1497,
                "plural": "Certified Divers with Your Own Equipment",
                "singular": "Certified Diver with Your Own Equipment"
              },
              "pk": 8964453,
              "total": 10900
            }
          }
        ],
        "invoice_price": 9393,
        "pk": 566107,
        "uuid": "9e61f8f3-a43f-4cb5-994e-71816301c2db",
      }
    }

### Retrieve a booking

Request:

    $ curl -H "X-FareHarbor-API-App: APP-KEY" -H "X-FareHarbor-API-User: USER-KEY" https://fareharbor.com/api/external/v1/companies/xyz/bookings/9e61f8f3-a43f-4cb5-994e-71816301c2db/`

Response:

    {
      "booking": {
        "availability": {
          "capacity": 20,
          "customer_type_rates": [
            {
              "capacity": null,
              "customer_type": {
                "note": "",
                "pk": 29,
                "plural": "Certified Divers Needing Rental Equipment",
                "singular": "Certified Diver Needing Rental Equipment"
              },
              "pk": 8964452,
              "total": 12900
            }
          ],
          "end_at": "2015-02-01T10:30:00-1000",
          "item": {
            "name": "Wreck & Reef Dive",
            "pk": 28
          },
          "pk": 3267113,
          "start_at": "2015-02-01T07:00:00-1000"
        }
        "contact": {
          "phone": "415-789-4563",
          "name": "John Doe",
          "email": "johndoe@example.com"
        },
        "customers": [
          {
            "customer_type_rate": {
              "capacity": null
              "customer_type": {
                "note": "",
                "pk": 1497,
                "plural": "Certified Divers with Your Own Equipment",
                "singular": "Certified Diver with Your Own Equipment"
              },
              "pk": 8964453,
              "total": 10900
            }
          }
        ],
        "invoice_price": 9393,
        "pk": 566107,
        "uuid": "9e61f8f3-a43f-4cb5-994e-71816301c2db",
      }
    }
