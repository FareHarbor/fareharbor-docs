# Getting Started

To get started as a FareHarbor External API partner, first contact <support@fareharbor.com>
and request access. Access is currently limited to select partners as we develop our initial
API.

## Determining User Keys

You'll want to request a user key from each affiliate you would like to make bookings on behalf of.
You'll use this key for each request you make on behalf of the associated affiliate.
Alternatively, contact <support@fareharbor.com> for help identifying the relevant user keys.

## Structuring Requests and Responses

All requests and responses are simple JSON objects; see `/external-api/format.md`.

## Interacting with the API

### Retrieve a list of available companies

The first thing you might want to do is retrieve the list of companies that a given affiliate has access
to in FareHarbor:

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

This indicates that the affiliate in question (given by `USER-KEY`) can access "XYZ Scuba".

### Retrieve a list of bookable items

Next you can identify all of the items on a particular provider that a given affiliate can book.  Continuing the
above example, we can determine which items on "XYZ Scuba" the user identified by `USER-KEY` can book:

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

### Retrieve a list of availabilities for an item
 
Having found an item to book, you can access its availability on a per-day basis:

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

You can also access availability for a given range:

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

### Create a booking for an availability

Once you've found a bookable availability you can book it by simply `POST`ing to the availability's
booking collection:

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

You'll want to hold onto the booking's `uuid` (if not the rest of the booking) so that you can access
it later.

### Retrieve a booking

Given a booking by `uuid` it's straightforward to access: 

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
