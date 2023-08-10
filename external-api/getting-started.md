<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Getting Started](#getting-started)
    - [Rate Limits](#rate-limits)
    - [TLS Version](#tls-version)
    - [Determining User Keys](#determining-user-keys)
    - [Structuring Requests and Responses](#structuring-requests-and-responses)
    - [Interacting with the API](#interacting-with-the-api)
        - [Retrieve a list of available companies](#retrieve-a-list-of-available-companies)
        - [Retrieve a list of bookable items](#retrieve-a-list-of-bookable-items)
        - [Retrieve a list of availabilities for an item](#retrieve-a-list-of-availabilities-for-an-item)
        - [Create a booking for an availability](#create-a-booking-for-an-availability)
        - [Retrieve a booking](#retrieve-a-booking)

<!-- markdown-toc end -->

# Getting Started

To get started as a FareHarbor External API partner, first contact <support@fareharbor.com>
and request access. Access is currently limited to select partners as we develop our initial
API.

## Rate Limits

We enforce two different rate limits. Requests to the FareHarbor External API must comply with both limits.

We allow at most 30 request per second. Going over this limit will result in an HTTP response with 429 status ("Too Many Requests") or a 403 ("Forbidden") for the remainder of the second.

In addition, we allow at most 3000 requests per 5-minute period. Going over this limit will similarly result in a 429 or a 403 for the remainder of the 5-minute period.

If you are currently running a lot of daily requests all at once,
please consider spreading them out more evenly over the course of the
day.

## TLS Version

As of 2020-09-01 we require clients that connect to our API to make use of TLS1.2 in order to ensure a speedy and secure connection. You can test this by running a curl command against our API and if you see something like `SSL_ERROR_SYSCALL in connection to fareharbor.com:443` or `Unknown SSL protocol error in connection` you are trying to use a TLS version we do not support. If that is the case it is likely that you will need to upgrade your local openssl version, which is outside the scope of this document.

## Determining User Keys

FareHarbor will provide approved API partners with User Keys that can be used to make requests and create bookings for suppliers.
The supplier must confirm their approval of your API access before you are able to make bookings for them via API.
If you are using the FareHarbor API to book for suppliers across multiple countries/currencies, you may be provided with one User Key per currency.
You can find more information about the authentication process [here](authentication.md). Alternatively, you may contact <support@fareharbor.com> for assistance with User Keys.

## Structuring Requests and Responses

All requests and responses are simple JSON objects; see [`format.md`](external-api/endpoints/format.md).

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
          "pk": 28,
          "health_and_safety_policy": "",
          "health_and_safety_policy_safe_html": ""
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
          "headline": "Epic Wreck & Reef Dive",
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
          "headline": "Epic Wreck & Reef Dive",
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
          "headline": "Epic Wreck & Reef Dive",
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
         "phone": "+1-415-789-4563",
         "email": "johndoe@example.com"
       },
       "customers": [
         {
           "customer_type_rate": 8964453
         }
       ],
       "note": "Optional booking note.",
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
          "phone": "+1-415-789-4563",
          "phone_country": "US",
          "normalized_phone": "+14157894563",
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
        "dashboard_url": "https://fareharbor.com/hawaiianadventures/dashboard/?overlay=/contacts/7/bookings/9e61f8f3-a43f-4cb5-994e-71816301c2db/",
        "customer_count": 1,
        "is_subscribed_for_sms_updates": false
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
          "phone": "+1-415-789-4563",
          "phone_country": "US",
          "normalized_phone": "+14157894563",
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
        "dashboard_url": "https://fareharbor.com/hawaiianadventures/dashboard/?overlay=/contacts/7/bookings/9e61f8f3-a43f-4cb5-994e-71816301c2db/",
        "customer_count": 1,
        "is_subscribed_for_sms_updates": false
      }
    }
