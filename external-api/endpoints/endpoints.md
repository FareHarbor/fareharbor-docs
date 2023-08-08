<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Endpoints](#endpoints)
    - [Companies](#companies)
    - [Company](#company)
    - [Check in with QR Code](#check-in-with-qr-code)
    - [Check in Statuses](#check-in-statuses)
    - [Agents](#agents)
    - [Desks](#desks)
    - [Lodgings](#lodgings)
    - [Availability Lodgings](#availability-lodgings)
    - [Items](#items)
    - [Availabilities](#availabilities)
    - [Availability](#availability)
    - [Bookings](#bookings)
        - [Request Schema](#request-schema)
        - [Custom Field Values](#custom-field-values)
        - [Bookability](#bookability)
        - [Party Size Restrictions](#party-size-restrictions)
            - [Availability Restrictions](#availability-restrictions)
            - [Customer Type Rate Restrictions](#customer-type-rate-restrictions)
        - [Errors](#errors)
        - [Validation](#validation)
        - [Cancellation](#cancellation)
            - [Cancellation Policies](#cancellation-policies)
                - [Effective Cancellation Policies](#effective-cancellation-policies)
                    - [Items Endpoint](#items-endpoint)
                    - [Availability Endpoints](#availability-endpoints)
                    - [Retrieve Booking Endpoint](#retrieve-booking-endpoint)
        - [Note](#note)
        - [Rebooking](#rebooking)
        - [Cancelling a Rebooked Booking](#cancelling-a-rebooked-booking)
        - [Agents and desks](#agents-and-desks)
        - [Transportation](#transportation)
            - [Pickup Information](#pickup-information)
            - [Arrival Information](#arrival-information)
        - [Orders](#orders)
    - [Availability Bookings](#availability-bookings)

<!-- markdown-toc end -->

# Endpoints

All endpoints are rooted at `https://fareharbor.com/api/external/v1/`.

## Companies

`GET /companies/`

Returns a list of all companies for which you have permission to create bookings;
note that this may include companies that have no bookable availabilities.

Returns an array of `Company` objects.

Example request:

    $ curl -H "X-FareHarbor-API-App: YOUR-APP-KEY" -H "X-FareHarbor-API-User: YOUR-USER-KEY" https://fareharbor.com/api/external/v1/companies/

Example response:

    {
      "companies": [
        {
          "shortname": "hawaiianadventures",
          "name": "Hawaiian Adventures"
        }, {
          "shortname": "surflessonshawaii",
          "name": "Surf Lessons Hawaii"
        }
      ]
    }

## Company

`GET /companies/<company-shortname>/`

Returns a `Company` object (extended representation).

Example request:

    $ curl -H "X-FareHarbor-API-App: YOUR-APP-KEY" -H "X-FareHarbor-API-User: YOUR-USER-KEY" https://fareharbor.com/api/external/v1/companies/hawaiianadventures/

Example response:

    {
      "company": {
        "shortname": "hawaiianadventures",
        "name": "Hawaiian Adventures",
        "currency": "usd",
        "about": "Hawaiian Adventures offers several water activities that you are sure to enjoy.",
        "about_safe_html": "<p>Hawaiian Adventures offers several water activities that you are sure to enjoy.</p>",
        "booking_notes": "Weather conditions will be evaluated at the time of check-in.\n\nIf using a voucher, please bring the voucher with you.",
        "booking_notes_safe_html": "<p>Weather conditions will be evaluated at the time of check-in.\n\nIf using a voucher, please bring the voucher with you.</p>",
        "faq": "# What should I bring?\n\nWe suggest that you bring a swimming suit, sunscreen, and a towel.",
        "faq_safe_html": "<h1>What should I bring?</h1>\n<p>We suggest that you bring a swimming suit, a towel, and sunscreen.</p>",
        "intro": "We offer the best water activities on Oahu",
        "intro_safe_html": "<p>We offer the best water activities on Oahu</p>",
        "summary": "Water activities 365 days a year",
        "url": "https://company-url.com",
        "facebook_url": "https://facebook.com/url",
        "instagram_url": "https://instagram.com/url",
        "tripadvisor_url": "https://tripadvisor.com/url",
        "twitter_url": "https://twitter.com/url",
        "yelp_url": "https://yelp.com/url",
        "youtube_url": "https://youtube.com/url",
        "pinterest_url": "https://pintrest.com/url",
        "address": {
          "city": "Honolulu",
          "country": "US",
          "postal_code": "96821",
          "province": "HI",
          "street": "123 Wailupe Cir"
        },
        'affiliated_since': '2020-06-17T15:44:03+0000',
        "billing_address": {
          "city": "Honolulu",
          "country": "US",
          "postal_code": "96821",
          "province": "HI",
          "street": "123 Wailupe Cir"
        },
        "health_and_safety_policy": "# Company Health & Safety Policy Statement\nThe safety and health of our employees is this company’s most important business consideration.\n\nThe company pledges to do the following:\n\n*  Strive to achieve the goal of zero accidents and injuries.\n* Train all employees in safe work practices and procedures.",
        "health_and_safety_policy_safe_html": "<h1>Company Health &amp; Safety Policy Statement</h1>\n<p>The safety and health of our employees is this company’s most important business consideration.</p>\n<p>The company pledges to do the following:</p>\n<ul>\n<li>Strive to achieve the goal of zero accidents and injuries.</li>\n<li>Train all employees in safe work practices and procedures.</li>\n</ul>",
        "open_hours": {
          "monday": {
            "open_time": "10:00",
            "close_time": "17:00"
          },
          "tuesday": {
            "open_time": "10:00",
            "close_time": "17:00"
          },
          "wednesday": {
            "open_time": "10:00",
            "close_time": "17:00"
          },
          "thursday": {
            "open_time": "10:00",
            "close_time": "17:00"
          },
          "friday": {
            "open_time": "10:00",
            "close_time": "17:00"
          },
          "saturday": null,
          "sunday": null
        }
      }
    }

## Check in with QR Code

`PUT /companies/<company-shortname>/checkin/`

Check in a booking based on QR code. Returns a `Booking` object.

Example request:

    $ curl -X PUT \
    -H "X-FareHarbor-API-App: YOUR-APP-KEY" \
    -H "X-FareHarbor-API-User: YOUR-USER-KEY" \
    -d \
    '{
       "qr_code": "https://fhchk.co/abc"
    }' \
    https://fareharbor.com/api/external/v1/companies/hawaiianadventures/checkin/

Example response:

    {
      "booking": {
        "pk": 6876876,
        "uuid": "d75102be-9732-4523-90a8-c698eff2b983",
        "status": "booked",
        "availability": {
          "pk": 4786,
          "start_at": "2015-01-22T11:30:00-1000",
          "end_at": "2015-01-22T13:30:00-1000",
          "capacity": 10,
          "item": {
            "pk": 1867,
            "name": "Jet Ski Tour"
          },
          "customer_type_rates": [
            {
              "pk": 65675,
              "total": 20000,
              "capacity": 10,
              "is_exclusive": false,
              "customer_type": {
                "pk": 978,
                "singular": "Adult",
                "plural": "Adults",
                "note": "At least 18 years old."
              },
              "customer_prototype": {
                "pk": 2522,
                "display_name": "Adult",
                "total": 20000
              }
            }
          ]
        },
        "contact": {
          "name": "John Doe",
          "phone": "+1-415-789-4563",
          "phone_country": "US",
          "normalized_phone": "+14157894563",
          "email": "johndoe@example.com"
        },
        "customers": [
          {
            "checkin_url": "https://fhchk.co/abc",
            "checkin_status": {
              "name": "checked in",
              "type": "checked-in"
            },
            "customer_type_rate": {
              "pk": 65675,
              "total": 20000,
              "capacity": 10,
              "is_exclusive": false,
              "customer_type": {
                "pk": 978,
                "singular": "Adult",
                "plural": "Adults",
                "note": "At least 18 years old."
              },
              "customer_prototype": {
                "pk": 2522,
                "display_name": "Adult",
                "total": 20000
              }
            }
          },
          {
            "checkin_url": "https://fhchk.co/def",
            "checkin_status": {
              "name": "checked in",
              "type": "checked-in"
            },
            "customer_type_rate": {
              "pk": 65675,
              "total": 20000,
              "capacity": 10,
              "is_exclusive": false,
              "customer_type": {
                "pk": 978,
                "singular": "Adult",
                "plural": "Adults",
                "note": "At least 18 years old."
              },
              "customer_prototype": {
                "pk": 2522,
                "display_name": "Adult",
                "total": 20000
              }
            }
          }
        ],
        "invoice_price": null,
        "order": null,
        "dashboard_url": "https://fareharbor.com/hawaiianadventures/dashboard/?overlay=/contacts/7/bookings/d75102be-9732-4523-90a8-c698eff2b983/",
        "customer_count": 1,
        "is_subscribed_for_sms_updates": false
      }
    }

## Check in Statuses

`GET /companies/<company-shortname>/checkin-statuses/`

Returns an array of `CheckinStatus` objects for the `Company`.

Example request:

    $ curl -H "X-FareHarbor-API-App: YOUR-APP-KEY" -H "X-FareHarbor-API-User: YOUR-USER-KEY" https://fareharbor.com/api/external/v1/companies/hawaiianadventures/checkin-statuses/

Example response:

    {
        "checkin_statuses": [
            {
                "pk": 3,
                "type": "checked-in",
                "name": "checked in"
            },
            {
                "pk": 4,
                "type": "no-show",
                "name": "no-show"
            }
        ]
    }

## Agents

`GET /companies/<affiliate-shortname>/agents/`

Returns an array of `Agent` objects.

Example request:

    $ curl -H "X-FareHarbor-API-App: YOUR-APP-KEY" -H "X-FareHarbor-API-User: YOUR-USER-KEY" https://fareharbor.com/api/external/v1/companies/hawaiianadventures/agents/

Example response:

    {
      "agents": [
        {
          "pk": 123,
          "name": "Eddie"
        }
      ]
    }

Note that `affiliate-shortname` is the shortname of the affiliate company with which your user key is associated; agents are per-affiliate, not per company.

## Desks

`GET /companies/<affiliate-shortname>/desks/`

Returns an array of `Desk` objects.

Example request:

    $ curl -H "X-FareHarbor-API-App: YOUR-APP-KEY" -H "X-FareHarbor-API-User: YOUR-USER-KEY" https://fareharbor.com/api/external/v1/companies/hawaiianadventures/desks/

Example response:

    {
      "desks": [
        {
          "pk": 123,
          "name": "Windward Side"
        }
      ]
    }

Note that `affiliate-shortname` is the shortname of the affiliate company with which your user key is associated; desks are per-affiliate, not per company.

## Lodgings

`GET /companies/<shortname>/lodgings/`

Returns an array of `Lodging` objects.

Example request:

    $ curl -H "X-FareHarbor-API-App: YOUR-APP-KEY" -H "X-FareHarbor-API-User: YOUR-USER-KEY" https://fareharbor.com/api/external/v1/companies/hawaiianadventures/lodgings/

Example response:

    {
      "lodgings": [
        {
          "pk": 231,
          "name": "Wyndham Royal Garden",
          "phone": "(808) 943-0202",
          "address": "440 Olohana St Honolulu, HI 96815",
          "url": "https:\/\/www.extraholidays.com\/honolulu-hawaii\/royal-garden-at-waikiki.aspx",
          "is_self_lodging": false
        }
      ]
    }

## Availability Lodgings

`GET /companies/<shortname>/availabilities/<availability.pk>/lodgings/`

Returns an array of `Lodging` objects that include availability specific data.

Example request:

    $ curl -H "X-FareHarbor-API-App: YOUR-APP-KEY" -H "X-FareHarbor-API-User: YOUR-USER-KEY" https://fareharbor.com/api/external/v1/companies/hawaiianadventures/availabilities/4786/lodgings/

Example response:

    {
      "lodgings": [
        {
          "pk": 231,
          "name": "Wyndham Royal Garden",
          "is_pickup_available": true
        }
      ]
    }

The `is_pickup_available` property indicates whether a pickup is offered for the lodging (for the availability specified in the request URL). This value reflects the current state of the system and can change when updates are made.

## Items

`GET /companies/<shortname>/items/`

Returns a list of items as for which you have permission to create bookings; again,
note that this may include items that have no bookable availabilities.

Returns an array of `Item` objects.

Example request:

    $ curl -H "X-FareHarbor-API-App: YOUR-APP-KEY" -H "X-FareHarbor-API-User: YOUR-USER-KEY" https://fareharbor.com/api/external/v1/companies/hawaiianadventures/items/

Example response:

    {
      "items": [
        {
          "pk": 1867,
          "name": "Jet Ski Tour",
          "headline": "Epic Jet Ski Tour",
          "description": "See Honolulu from a jet ski!",
          "description_safe_html": "\u003cp\u003eSee Honolulu from a jet ski!\u003c\/p\u003e",
          "description_text": "See Honolulu from a jet ski!",
          "description_bullets": [
            "Located just 5 minutes from Waikiki.",
            "Transportation included."
          ],
          "cancellation_policy": "A full refund will be issued if notice is given at least 24 hours before start time.",
          "cancellation_policy_safe_html": "\u003cp\u003eA full refund will be issued if notice is given at least 24 hours before start time.\u003c\/p\u003e",
          "location": "Honolulu, HI",
          "is_pickup_ever_available": true,
          "image_cdn_url": "https:\/\/d1a2dkr8rai8e2.cloudfront.net\/api\/file\/rvybRyLWTgyV5w4xg42p\/",
          "images": [
            {
              "pk": 687,
              "gallery": "carousel",
              "image_cdn_url": "https:\/\/d1a2dkr8rai8e2.cloudfront.net\/api\/file\/rvybRyLWTgyV5w4xg42p\/"
            }
          ],
          "customer_prototypes": [
            {
              "pk": 2522,
              "display_name": "Adult",
              "total": 20000
            }
          ],
          "health_and_safety_policy": "Our policies are:\n\n* Bring your own equipment\n* Please wear a facemask",
          "health_and_safety_policy_safe_html": "<p>Our policies are:</p>\n<ul>\n<li>Bring your own equipment</li>\n<li>Please wear a facemask</li>\n</ul>"
        },
        {
          "pk": 1963,
          "name": "Surfing 101",
          "headline": "Learn to surf!",
          "description": "This is an introductory lesson.",
          "description_safe_html": "\u003cp\u003eThis is an introductory lesson.\u003c\/p\u003e",
          "description_text": "This is an introductory lesson.",
          "description_bullets": [
            "Located just 5 minutes from Waikiki.",
            "Transportation included."
          ],
          "cancellation_policy": "A full refund will be issued if notice is given at least 24 hours before start time.",
          "cancellation_policy_safe_html": "\u003cp\u003eA full refund will be issued if notice is given at least 24 hours before start time.\u003c\/p\u003e",
          "location": "Honolulu, HI",
          "locations": [
            {
              "pk": 234234,
              "type": "primary",
              "note": "Next to the blue fence.",
              "note_safe_html": "<p>Next to the blue fence.</p>",
              "address": {
                "city": "Honolulu",
                "country": "US",
                "postal_code": "96821",
                "province": "HI",
                "street": "123 Wailupe Cir"
              },
              "longitude": 21.3069,
              "latitude": -157.8583,
              "google_place_id": "ChIJYZ4srGUSAHwRT1Da4amp3x",
              "tripadvisor_url": "https://www.tripadvisor.com/Attraction_Review-g60982-d184886-Reviews-Epic_Jet_Ski_Tour-Honolulu_Oahu_Hawaii.html",
            }
          ],
          "is_pickup_ever_available": true,
          "image_cdn_url": "",
          "images": []
        },
        "health_and_safety_policy": "",
        "health_and_safety_policy_safe_html": ""
      ]
    }

## Availabilities

* `GET /companies/<shortname>/items/<item.pk>/minimal/availabilities/date/<date>/`
* `GET /companies/<shortname>/items/<item.pk>/minimal/availabilities/date-range/<start-date>/<end-date>/`

Returns possibly-bookable availabilities for `date`, or for the range `start-date` through `end-date`.
Note that possibly-bookable availabilies do not include those for which customers are requested to "call to book". Note that `date`, `start-date`, and `end-date` should be in the format YYYY-MM-DD.

Returns an array of `Availability` objects (minimal representation).

Example request:

    $ curl -H "X-FareHarbor-API-App: YOUR-APP-KEY" -H "X-FareHarbor-API-User: YOUR-USER-KEY" https://fareharbor.com/api/external/v1/companies/hawaiianadventures/items/1867/minimal/availabilities/date/2015-01-22/

Example response:

    {
      "availabilities": [
        {
          "pk": 4786,
          "start_at": "2015-01-22T11:30:00-1000",
          "end_at": "2015-01-22T13:30:00-1000",
          "capacity": 10,
          "customer_type_rates": [
            {
              "pk": 65675,
              "capacity": 10,
              "customer_type": {
                "pk": 978,
                "singular": "Adult",
                "plural": "Adults",
                "note": "At least 18 years old."
              },
              "customer_prototype": {
                "pk": 2522,
                "display_name": "Adult"
              }
            },
            ...
          ]
        },
        ...
      ]
    }

## Availability

`GET /companies/<shortname>/availabilities/<availability.pk>/`

Returns an `Availability` object (extended representation).

Example request:

    $ curl -H "X-FareHarbor-API-App: YOUR-APP-KEY" -H "X-FareHarbor-API-User: YOUR-USER-KEY" https://fareharbor.com/api/external/v1/companies/hawaiianadventures/availabilities/4786/

Example response:

    {
      "availability": {
        "pk": 4786,
        "start_at": "2015-01-22T11:30:00-1000",
        "end_at": "2015-01-22T13:30:00-1000",
        "capacity": 10,
        "item": {
          "pk": 1867,
          "name": "Jet Ski Tour"
        },
        "customer_type_rates": [
          {
            "pk": 65675,
            "total": 20000,
            "capacity": 10,
            "customer_type": {
              "pk": 978,
              "singular": "Adult",
              "plural": "Adults",
              "note": "At least 18 years old."
            },
            "customer_prototype": {
              "pk": 2522,
              "display_name": "Adult",
              "total": 20000
            },
            "custom_field_instances": [
              {
                "pk": 8629,
                "custom_field": {
                  "pk": 43879,
                  "type": "yes-no",
                  ...
                }
              },
              ...
            ]
          },
          ...
        ],
        "custom_field_instances": [
          {
            "pk": 47974,
            "custom_field": {
              "pk": 3387,
              "type": "yes-no",
              ...
            }
          },
          ...
        ]
      }
    }

## Bookings

Create a booking:

* `POST /companies/<shortname>/availabilities/<Availability.pk>/bookings/`

Retrieve a booking:

* `GET /companies/<shortname>/bookings/<Booking.uuid>/`

Cancel a booking:

* `DELETE /companies/<shortname>/bookings/<Booking.uuid>/`

Update the booking note:

* `PUT /companies/<shortname>/bookings/<Booking.uuid>/note/`

The result of creating, retrieving, or cancelling a booking is a `Booking` object.

Example request:

    $ curl -X POST \
    -H "X-FareHarbor-API-App: YOUR-APP-KEY" \
    -H "X-FareHarbor-API-User: YOUR-USER-KEY" \
    -d \
    '{
       "contact": {
         "name": "John Doe",
         "phone": "+1-415-789-4563",
         "email": "johndoe@example.com"
       },
       "customers": [
         {
           "customer_type_rate": 65675
         },
         {
           "customer_type_rate": 65675
         }
       ],
       "note": "Optional booking note.",
       "external_id": "DataTracker5678",
       "voucher_number": "V-35791209"
    }' \
    https://fareharbor.com/api/external/v1/companies/hawaiianadventures/availabilities/4786/bookings/

Example response:

    {
      "booking": {
        "pk": 6876876,
        "uuid": "d75102be-9732-4523-90a8-c698eff2b983",
        "status": "booked",
        "availability": {
          "pk": 4786,
          "start_at": "2015-01-22T11:30:00-1000",
          "end_at": "2015-01-22T13:30:00-1000",
          "capacity": 10,
          "item": {
            "pk": 1867,
            "name": "Jet Ski Tour"
          },
          "customer_type_rates": [
            {
              "pk": 65675,
              "total": 20000,
              "capacity": 10,
              "is_exclusive": false,
              "customer_type": {
                "pk": 978,
                "singular": "Adult",
                "plural": "Adults",
                "note": "At least 18 years old."
              },
              "customer_prototype": {
                "pk": 2522,
                "display_name": "Adult",
                "total": 20000
              }
            }
          ]
        },
        "contact": {
          "name": "John Doe",
          "phone": "+1-415-789-4563",
          "phone_country": "US",
          "normalized_phone": "+14157894563",
          "email": "johndoe@example.com"
        },
        "customers": [
          {
            "checkin_url": "https://fhchk.co/abc",
            "checkin_status": {
              "name": "checked in",
              "type": "checked-in"
            },
            "invoice_cost": {
              "price": 32996,
              "tax": 0,
              "taxable": 0,
              "feeable": 32996,
              "tax_by_type": {
                53558: 0
              },
              "total": 32996
            },
            "total_cost": {
              "price": 38900,
              "tax": 0,
              "taxable": 38900,
              "feeable": 38900,
              "tax_by_type": {
                53558: 0
              },
              "total": 38900
            },
            "customer_type_rate": {
              "pk": 65675,
              "total": 20000,
              "capacity": 10,
              "is_exclusive": false,
              "customer_type": {
                "pk": 978,
                "singular": "Adult",
                "plural": "Adults",
                "note": "At least 18 years old."
              },
              "customer_prototype": {
                "pk": 2522,
                "display_name": "Adult",
                "total": 20000
              }
            }
          },
          {
            "checkin_url": "https://fhchk.co/def",
            "checkin_status": {
              "name": "checked in",
              "type": "checked-in"
            },
            "customer_type_rate": {
              "pk": 65675,
              "total": 20000,
              "capacity": 10,
              "is_exclusive": false,
              "customer_type": {
                "pk": 978,
                "singular": "Adult",
                "plural": "Adults",
                "note": "At least 18 years old."
              },
              "customer_prototype": {
                "pk": 2522,
                "display_name": "Adult",
                "total": 20000
              }
            }
          }
        ],
        "invoice_price": null,
        "external_id": "DataTracker5678",
        "order": null,
        "dashboard_url": "https://fareharbor.com/hawaiianadventures/dashboard/?overlay=/contacts/7/bookings/d75102be-9732-4523-90a8-c698eff2b983/",
        "customer_count": 1,
        "is_subscribed_for_sms_updates": false
      }
    }

Permissions affect the visibility of certain fields:

* The `invoice_cost` will be included if the permission *View invoice prices*
is enabled.
* The `invoice_cost` will be `null` if *View invoice prices* is disabled.
* The `total_cost` will be included if the permission *View amounts* is enabled.
* The `total_cost` will be `null` if *View amounts* is disabled.

`invoice_cost` represents the invoice price of the customer type.
`total_cost` represents the total cost of the customer type, including any
priced custom fields.

Check in a booking based on UUID:

* `PUT /companies/<shortname>/bookings/<Booking.uuid>/checkin/`

Returns a `Booking` object.


Example request:

    $ curl -X PUT \
    -H "X-FareHarbor-API-App: YOUR-APP-KEY" \
    -H "X-FareHarbor-API-User: YOUR-USER-KEY" \
    -d \
    '{
       "qr_code": "https://fhchk.co/abc"
    }' \
    https://fareharbor.com/api/external/v1/companies/hawaiianadventures/bookings/d75102be-9732-4523-90a8-c698eff2b983/checkin/

Example response:

    {
      "booking": {
        "pk": 6876876,
        "uuid": "d75102be-9732-4523-90a8-c698eff2b983",
        "status": "booked",
        "availability": {
          "pk": 4786,
          "start_at": "2015-01-22T11:30:00-1000",
          "end_at": "2015-01-22T13:30:00-1000",
          "capacity": 10,
          "item": {
            "pk": 1867,
            "name": "Jet Ski Tour"
          },
          "customer_type_rates": [
            {
              "pk": 65675,
              "total": 20000,
              "capacity": 10,
              "is_exclusive": false,
              "customer_type": {
                "pk": 978,
                "singular": "Adult",
                "plural": "Adults",
                "note": "At least 18 years old."
              },
              "customer_prototype": {
                "pk": 2522,
                "display_name": "Adult",
                "total": 20000
              }
            }
          ]
        },
        "contact": {
          "name": "John Doe",
          "phone": "+1-415-789-4563",
          "phone_country": "US",
          "normalized_phone": "+14157894563",
          "email": "johndoe@example.com"
        },
        "customers": [
          {
            "checkin_url": "https://fhchk.co/abc",
            "checkin_status": {
              "name": "checked in",
              "type": "checked-in"
            },
            "invoice_cost": {
              "price": 32996,
              "tax": 0,
              "taxable": 0,
              "feeable": 32996,
              "tax_by_type": {
                53558: 0
              },
              "total": 32996
            },
            "total_cost": {
              "price": 38900,
              "tax": 0,
              "taxable": 38900,
              "feeable": 38900,
              "tax_by_type": {
                53558: 0
              },
              "total": 38900
            },
            "customer_type_rate": {
              "pk": 65675,
              "total": 20000,
              "capacity": 10,
              "is_exclusive": false,
              "customer_type": {
                "pk": 978,
                "singular": "Adult",
                "plural": "Adults",
                "note": "At least 18 years old."
              },
              "customer_prototype": {
                "pk": 2522,
                "display_name": "Adult",
                "total": 20000
              }
            }
          },
          {
            "checkin_url": "https://fhchk.co/def",
            "checkin_status": {
              "name": "checked in",
              "type": "checked-in"
            },
            "customer_type_rate": {
              "pk": 65675,
              "total": 20000,
              "capacity": 10,
              "is_exclusive": false,
              "customer_type": {
                "pk": 978,
                "singular": "Adult",
                "plural": "Adults",
                "note": "At least 18 years old."
              },
              "customer_prototype": {
                "pk": 2522,
                "display_name": "Adult",
                "total": 20000
              }
            }
          }
        ],
        "invoice_price": null,
        "order": null,
        "dashboard_url": "https://fareharbor.com/hawaiianadventures/dashboard/?overlay=/contacts/7/bookings/d75102be-9732-4523-90a8-c698eff2b983/",
        "customer_count": 1,
        "is_subscribed_for_sms_updates": false
      }
    }

### Request Schema

When creating bookings, use the customer type rate and custom field instance information
contained in the availability to construct a request of the following form:

* `note`: `string`
* `voucher_number`: `string`
* `contact`: `object`
    * `name`: `string`
    * `phone`: `string`
    * `email`: `string`
* `customers`: `array`
    * `customer_type_rate`: `CustomerTypeRate.pk`

For best results, include the plus sign and international country code
in the contact `phone` field (E.164 format). If the country code is
not present, it may lead to unexpected behavior in some cases.

Example:

    {
      "note": "Optional booking note.",
      "voucher_number": "VLT-1123",
      "contact": {
        "name": "John Doe",
        "phone": "+14432221100",
        "email": "johndoe@example.com"
      },
      "customers": [
        {
          "customer_type_rate": 42
        },
        {
          "customer_type_rate": 42
        },
        {
          "customer_type_rate": 33
        }
      ]
    }

The following JSON schema is used to validate requests:

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "type": "object",
      "properties": {
        "contact": {
          "type": "object",
          "properties": {
            "email": {
              "type": "string",
              "maxLength": 256
            },
            "name": {
              "type": "string",
              "maxLength": 128
            },
            "phone": {
              "type": "string",
              "maxLength": 32
            }
          },
          "required": ["email", "name", "phone"],
          "additionalProperties": false
        },
        "customers": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "customer_type_rate": {
                "type": "number"
              }
            },
            "required": ["customer_type_rate"],
            "additionalProperties": false
          },
          "minItems": 1
        },
        "voucher_number": {
          "type": "string",
          "maxLength": 128
        }
      },
      "required": ["contact", "customers", "voucher_number"],
      "additionalProperties": false
    }

For more information regarding JSON schemas, see: http://json-schema.org/

### Custom Field Values

Booking custom fields:

  Values for booking custom fields are specified by including a
  `custom_field_values` property at the root level with the following form:

  * `custom_field_values`: `array`
    * `custom_field`: `CustomField.pk`
    * `value`: `string`

Customer custom fields:

  Values for customer custom fields are specified by including a
  `custom_field_values` property at the customer level with the following form:

  * `customers`: `array`
    * `custom_field_values`: `array`
      * `custom_field`: `CustomField.pk`
       * `value`: `string`

Example:

    {
       "contact": {
         "name": "John Doe",
         "phone": "+1-415-789-4563",
         "email": "johndoe@example.com"
       },
       "customers": [
         {
           "customer_type_rate": 8964453,
           "custom_field_values": [
             {
               "custom_field": 123,
               "value": "true"
             }
           ]
         }
       ],
       "custom_field_values": [
         {
           "custom_field": 456,
           "value": "6745"
         }
       ],
       "voucher_number": "V-35791209"
    }

### Bookability

When creating a booking, several properties about the availability and the booking request must hold
or the booking will not be created.

* Availability open

  The vendor may close availabilities at any time, and availabilities
  are automatically closed at various times based on the companies criteria.

* Availability capacity

  There must be available capacity on the availability for all customers

* Customer type rate capacities

  For each booked customer type rate there must be available capacity for each
  customer of that customer type.

* Exclusivity

  If any customer type rate being booked is exclusive, then it must be the *only* customer
  type rate being booked.

* Correct Customer Type Rates

  Each customer type rate being booked must actually belong to the availability being booked.

### Party Size Restrictions
#### Availability Restrictions

FareHarbor supports optional party size booking restrictions at the availability level. The following properties will be included for each availability provided by the availability endpoints to indicate applicable restrictions:

* `minimum_party_size`: minimum number of customers currently allowed on a booking.
* `maximum_party_size`: maximum number of customers currently allowed on a booking.

For example:

    {
      "availabilities": [
        {
          "pk": 47836,
          "minimum_party_size": 4,
          "maximum_party_size": 12,
          ...
        },
        ...
      ]
    }

Note: a number value will be provided for enabled restrictions; a `null` value will be provided for restrictions that are not enabled.

#### Customer Type Rate Restrictions

FareHarbor also supports optional party size booking restrictions at the customer type rate level. The following properties will be included for each customer type rate provided by availability endpoints to indicate applicable restrictions:

* `minimum_party_size`: minimum number of the associated customer type allowed in a party.
* `maximum_party_size`: maximum number of the associated customer type allowed in a party.

Note: the `minimum_party_size` restriction only applies when at least one customer of the associated customer type is in the party.

For example:

    {
      "availabilities": [
        {
          "pk": 47836,
          "customer_type_rates": [
            {
              "pk": 659086,
              "minimum_party_size": 2,
              "maximum_party_size": 6,
              "customer_type": {
                "pk": 9178,
                "singular": "Adult",
                "plural": "Adults",
                ...
              },
              ...
            },
            ...
          ]
        },
        ...
      ]
    }

Note: a number value will be provided for enabled restrictions; a `null` value will be provided for restrictions that are not enabled.

### Errors

Assuming you've properly constructed your request, the most likely error you will encounter when
booking is a `400` indicating that the availability cannot be booked, almost certainly because
it has been closed or removed, or has run out of capacity.  For example:

    {
      "error": "Availability was removed",
      "status": 400
    }

### Validation

* `POST /companies/<shortname>/availabilities/<Availability.pk>/bookings/validate/`

Checks bookability and provides booking level pricing information.

Example request:

    $ curl -X POST \
    -H "X-FareHarbor-API-App: YOUR-APP-KEY" \
    -H "X-FareHarbor-API-User: YOUR-USER-KEY" \
    -d \
    '{
       "contact": {
         "name": "John Doe",
         "phone": "+1-415-789-4563",
         "email": "johndoe@example.com"
       },
       "customers": [
         {
           "customer_type_rate": 65675
         },
         {
           "customer_type_rate": 65675
         }
       ],
       "note": "Optional booking note.",
       "voucher_number": "V-35791209"
    }' \
    https://fareharbor.com/api/external/v1/companies/hawaiianadventures/availabilities/4786/bookings/validate/

The response provides an `is_bookable` field indicating whether the booking can be created.

    {
      "is_bookable": true,
      ...
    }

When the booking can't be created, additional information regarding the error is provided:

    {
      "is_bookable":false,
      "code":"bookability-error",
      "error":"Unable to create booking: error details."
    }

### Cancellation

* `DELETE /companies/<shortname>/bookings/<Booking.uuid>/`

Cancels the specified booking.

Requirements:

* The booking must be cancelled at least 48 hours prior to start time (availability `start_at` property) to receive 100% refund.
* Any affiliate-collected payments for the booking must be fully refunded.
* Cancellations are allowed up until the start time. However, if the booking is cancelled less than 48 hours prior to start time, there is no refund.
* The requesting user must have permission to cancel bookings (granted on a per-company basis).

Example request:

    $ curl -X DELETE -H "X-FareHarbor-API-App: YOUR-APP-KEY" -H "X-FareHarbor-API-User: YOUR-USER-KEY" https://fareharbor.com/api/external/v1/companies/hawaiianadventures/bookings/d75102be-9732-4523-90a8-c698eff2b983/

Example response:

    {
      "booking": {
        "pk": 6876876,
        "uuid": "d75102be-9732-4523-90a8-c698eff2b983",
        "status": "cancelled",
        ...
    }

The ellipses in the above example represent properties that have been left out for the sake of brevity.

#### Cancellation Policies

Initially all companies will use a "48 hours prior, 100% refund" and "if less than 48 hours prior, 0% refund" policy; however, we expect to expand support for various kinds of cancellation policies in the future.

##### Effective Cancellation Policies
###### Items Endpoint

When `detailed=yes` is specified as the query string for the items endpoint, a new `effective_cancellation_policy` property will be provided for each item that specifies data regarding the effective cancellation policy as shown in the example below:

    {
        "items": [
            {
                "pk": 123,
                "name": "Surf Lesson",
                "effective_cancellation_policy": {
                    "type": "hours-before-start",
                    "cutoff_hours_before": 48
                },
                ...
            },
            ...
        ]
    }

The `type` property will specify the effective cancellation policy type. The following types will be supported:

* "hours-before-start" - bookings are eligible for cancellation some number of hours before availability start time.
* "hours-before-midnight" - bookings are eligible for cancellation some number of hours before midnight on availability start date.
* "always" - bookings are eligible for cancellation up until a cutoff that is determined by the availability (usually the availability start time).
* "never" - bookings are never eligible for cancellation (e.g. no effective cancellation policy, insufficient privileges, cancellation disallowed by policy).

The `cutoff_hours_before` property will specify the number of hours for the "hours-before-start" and "hours-before-midnight" types. Note: this value can be negative indicating that bookings can be cancelled some number of hours after availability start time (when type is "hours-before-start") or some number of hours after midnight on availability start date (when type is "hours-before-midnight"). The `cutoff_hours_before` property will provide `null` when no cutoff is applicable (when bookings are never eligible for cancellation).

###### Availability Endpoints

When `detailed=yes` is specified as the query string for the availabilities endpoints, a new `effective_cancellation_policy` property will be provided for each availability that specifies data regarding the effective cancellation policy as shown in the example below:

    {
        "availabilities": [
            {
                "pk": 8901,
                "effective_cancellation_policy": {
                    "type": "hours-before-start",
                    "cutoff": "2017-01-22T13:30:00-1000"
                },
                ...
            },
            ...
        ]
    }

The `type` property will specify the effective cancellation policy type (see the items endpoint section for more details).

The `cutoff` property will specify the last possible time (ISO8601 timestamp) bookings are eligible for cancellation. The `cutoff` property will provide `null` when no cutoff is applicable (when bookings are never elgible for cancellation).

###### Retrieve Booking Endpoint

A new `is_eligible_for_cancellation` and `effective_cancellation_policy` property will be provided as shown in the example below:

    {
        "booking": {
            "pk": 578997533,
            "is_eligible_for_cancellation": true,
            "effective_cancellation_policy": {
                "type": "hours-before-start",
                "cutoff": "2017-01-22T13:30:00-1000"
            },
            ...
        }
    }

The `is_eligible_for_cancellation` property provides a boolean value indicating whether the booking is currently eligible for cancellation.

The `type` property will specify the effective cancellation policy type (see the items endpoint section for more details).

The `cutoff` property will specify the last possible time (ISO8601 timestamp) the booking is eligible for cancellation. The `cutoff` property will provide `null` when no cutoff is applicable (when the booking is never elgible for cancellation).

### Note

The booking note can be changed by issuing a `PUT` request to the note endpoint (`/companies/<shortname>/bookings/<Booking.uuid>/note`) with the new note; to clear the booking note, pass `""`.

Example request:

    $ curl -X PUT \
    -H "X-FareHarbor-API-App: YOUR-APP-KEY" \
    -H "X-FareHarbor-API-User: YOUR-USER-KEY" \
    -d \
    '{
       "note": "This is a *note*."
     }' \
    https://fareharbor.com/api/external/v1/companies/hawaiianadventures/bookings/d75102be-9732-4523-90a8-c698eff2b983/note/

The response is the `Booking` object, with the `note` field updated.

### Rebooking

If it is necessary to change a booking to another date/time or change customer types/count, the booking must be cancelled and a new booking must be created.  Rebooking is a shortcut for that process.

To rebook an existing booking, specify the existing booking's UUID value for the `rebooking` property when creating a booking. Note: valid values for all properties required by the create booking request must be provided.

Example request:

    $ curl -X POST \
    -H "X-FareHarbor-API-App: YOUR-APP-KEY" \
    -H "X-FareHarbor-API-User: YOUR-USER-KEY" \
    -d \
    '{
       "rebooking": "d75102be-9732-4523-90a8-c698eff2b983",
       "contact": {
         "name": "John Doe",
         "phone": "+1-415-789-4563",
         "email": "johndoe@example.com"
       },
       "customers": [
         {
           "customer_type_rate": 65675
         },
         {
           "customer_type_rate": 65675
         }
       ],
       "note": "Optional booking note.",
       "voucher_number": "V-35791209"
    }' \
    https://fareharbor.com/api/external/v1/companies/hawaiianadventures/availabilities/5796/bookings/

Example response:

    {
      "booking": {
        "pk": 7974877,
        "uuid": "10414711-3d20-4f4d-8ab3-eeaea26c2be3",
        "rebooked_from": "d75102be-9732-4523-90a8-c698eff2b983",
        "status": "booked",
        ...
    }

The response includes a `rebooked_from` property that provides the source booking's UUID.

Bookings that have been rebooked have a "rebooked" status. The `rebooked_to` property provides the UUID of the new booking.

Example rebooked booking:

    {
      "booking": {
        "pk": 6876876,
        "uuid": "d75102be-9732-4523-90a8-c698eff2b983",
        "rebooked_to": "10414711-3d20-4f4d-8ab3-eeaea26c2be3"
        "status": "rebooked",
        ...
    }

### Cancelling a Rebooked Booking

If you create a booking, then rebook it, and then cancel *either the original or the rebooked booking*, you will get the same response: the `Booking` object for the rebooked booking (not the original). Assuming the cancellation succeeds, the `status` of the rebooked booking will become `cancelled`. (The status of the original booking remains `rebooked` even after you have cancelled the rebooked booking.)

### Agents and desks

When creating a booking, you can specify the booking agent by pk, by name, or not at all. It is an error to specify both an agent pk and a name.

Similarly, you can specify a desk pk, a desk name, or neither, but not both.

To specify the booking agent by pk, pass an `Agent` pk for the `agent` property. To specify the agent by name, pass an `Agent` name for the `agent_name` property. (Resp. `Desk` pk for the `desk` property, `Desk` name for the `desk_name` property).

Example booking request body with both agent and desk specified by pk:

    {
      "contact": {
         "name": "John Doe",
         "phone": "+11234567890",
         "email": "example@example.com"
       },
       "customers": [
         {
           "customer_type_rate": 933643
         }
       ],
       "voucher_number": "1233456-1",
       "agent": 123,
       "desk": 456
    }

Example booking request body with both agent and desk specified by name:

    {
      "contact": {
         "name": "John Doe",
         "phone": "+11234567890",
         "email": "example@example.com"
       },
       "customers": [
         {
           "customer_type_rate": 933643
         }
       ],
       "voucher_number": "1233456-1",
       "agent_name": "Eddie",
       "desk_name": "Windward Side"
    }

Specification of agent and desk when booking is **optional**; you can specify neither, either, or both. If you do not wish to specify one or the other, do not pass a `null` value; instead, simply omit the property.

### Transportation

To request transportation for a booking, specify a `Lodging` pk for the `lodging` property when creating the booking as shown in the example below.

Example booking request body with a lodging specified:

    {
      "contact": {
         "name": "John Doe",
         "phone": "+11234567890",
         "email": "example@example.com"
       },
       "customers": [
         {
           "customer_type_rate": 933643
         }
       ],
       "voucher_number": "1233456-1",
       "lodging": 789
    }

#### Pickup Information

When a lodging is specified during booking creation and transportation is available for the lodging, the booking response will include a `pickup` property that provides pickup information as shown in the example below.

Example booking response with `pickup` property:

    {
        "booking": {
            "pk": 123,
            "pickup": {
                "time": "2016-08-01T10:30:00-1000",
                "name": "Wyndham Royal Garden",
                "description": "Please meet us at the front entrance of your hotel and allow a 15 minute window for your driver to arrive.",
                "map_url": "https://goo.gl/maps/6QiYT",
                "display_text": "We'll pick you up at 10:30am from Wyndham Royal Garden"
            },
            ...
        }
    }

The `pickup` object provides the following properties:

* `time`: `datetime`

  The pickup time; the customer must arrive at the pickup location by this time.

* `name`: `string`

  The name of the pickup location.

* `description`: `markdown`

  Pickup instructions from the activity company; may not be provided.

* `map_url`: `string`

  A URL to a map showing the pickup location; may not be provided.

* `display_text`: `string`

  A formatted string that can be shown to customers.

Note: if a lodging is specified and transportation is not available for the specified lodging (or any lodging), the `pickup` property will have a `null` value.

#### Arrival Information

Arrival information is intended for customers who are providing their own transportation. When a lodging is not provided during booking creation or transportation is not available for the specified lodging (or any lodging), arrivial information may be provided. When arrival information is available, the booking response will include an `arrival` property that provides arrival information as shown in the example below.

Example booking response with `arrival` property:

    {
        "booking": {
            "pk": 456,
            "arrival": {
                "time": "2016-08-01T13:15:00-1000",
                "notes": "Check-in Time is at 12:15 for your 12:45 Zipline adventure time. Our check-in locations is at our KapohoKine Adventures Store: 224 Kamehameha Ave Suite 106 Hilo, HI 96720",
                "display_text": "Please arrive by 12:15pm"
            },
            ...
        }
    }

The `arrival` object provides the following properties:

* `time`: `datetime`

  The arrival time; the customer must provide their own transporation and arrive at the activity location by this time.

* `notes`: `markdown`

  Notes from the activity company regarding arrival (e.g. check-in location details, driving directions); may not be provided.

* `display_text`: `string`

  A formatted string that can be shown to customers.

Note: the `arrival` property will have a `null` value if pickup information is available.

### Orders

Orders are a way of grouping collections of bookings so that they can be created or cancelled as a block.

A booking can belong to an order, but it doesn't have to. An order can include any number of bookings.

Example of the `order` property for a booking that does not belong to an order:

    {
        "booking": {
            "pk": 456,
            "order": null,
            ...
        }
    }

Example of the `order` property for a booking that *does* belong to an order:

    {
        "booking": {
            "pk": 456,
            "order": {
                "display_id": "ABTT"
            },
            ...
        }
    }

When `order` is not `null`, `order` is an object that provides the following property:

* `display_id`: `string`

  A unique identifier for the order.

Note that there is not currently a way to create orders via the API.


## Availability Bookings

Fetch a list of all bookings (in simplified format) for an availability:

* `GET /companies/<shortname>/availabilities/<Availability.pk>/bookings/`

The result will be a list of simplified booking objects.

Example request:

    $ curl \
    -H "X-FareHarbor-API-App: YOUR-APP-KEY" \
    -H "X-FareHarbor-API-User: YOUR-USER-KEY" \
    https://fareharbor.com/api/external/v1/companies/hawaiianadventures/availabilities/4786/bookings/

Example response:

    {
      "bookings": [
        {
          "pk": 6876876,
          "uuid": "d75102be-9732-4523-90a8-c698eff2b983",
          "company": {
            "shortname": "hawaiianadventures",
            "name": "Hawaiian Adventures",
            "currency": "usd"
          },
          "affiliate_company": {
            "shortname": "joes",
            "name": "Joes",
            "currency": "usd"
          },
          "contact": {
            "name": "John Doe",
            "phone": "+1-415-789-4563",
            "phone_country": "US",
            "language": "en-us",
            "normalized_phone": "+14157894563",
            "is_subscribed_for_email_updates": false,
            "email": "johndoe@example.com",
            "is_subscribed_for_sms_updates": false
          },
          "display_id": "#12",
          "external_id": "DataTracker5678",
          "order": null,
          "status": "booked",
          "rebooked_from": null,
          "rebooked_to": null,
          "dashboard_url": "https://fareharbor.com/hawaiianadventures/dashboard/?overlay=/contacts/7/bookings/d75102be-9732-4523-90a8-c698eff2b983/"
        }
      ]
    }
