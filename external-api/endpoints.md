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

## Planned: Lodgings

Note: this functionality is not available yet.

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
          "fax": "",
          "address": "440 Olohana St Honolulu, HI 96815",
          "url": "https:\/\/www.extraholidays.com\/honolulu-hawaii\/royal-garden-at-waikiki.aspx"
        }
      ]
    }

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
          "cancellation_policy": "A full refund will be issued if notice is given at least 24 hours before start time.",
          "cancellation_policy_safe_html": "\u003cp\u003eA full refund will be issued if notice is given at least 24 hours before start time.\u003c\/p\u003e",
          "location": "Honolulu, HI",
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
              "display_name": "Adult"
            }
          ]
        },
        { 
          "pk": 1963,
          "name": "Surfing 101",
          "headline": "Learn to surf!",
          "description": "This is an introductory lesson.",
          "description_safe_html": "\u003cp\u003eThis is an introductory lesson.\u003c\/p\u003e",
          "cancellation_policy": "A full refund will be issued if notice is given at least 24 hours before start time.",
          "cancellation_policy_safe_html": "\u003cp\u003eA full refund will be issued if notice is given at least 24 hours before start time.\u003c\/p\u003e",
          "location": "Honolulu, HI",
          "image_cdn_url": "",
          "images": []
        }
      ]
    }

## Availabilities

* `GET /companies/<shortname>/items/<item.pk>/availabilities/date/<date>/`
* `GET /companies/<shortname>/items/<item.pk>/availabilities/date-range/<start-date>/<end-date>/`

Returns possibly-bookable availabilities for `date`, or for the range `start-date` through `end-date`.
Note that possibly-bookable availabilies include those for which customers are requested to "call to book".
Note that `date`, `start-date`, and `end-date` should be in the format YYYY-MM-DD.

Returns an array of `Availability` objects.

Example request:

    $ curl -H "X-FareHarbor-API-App: YOUR-APP-KEY" -H "X-FareHarbor-API-User: YOUR-USER-KEY" https://fareharbor.com/api/external/v1/companies/hawaiianadventures/items/1867/availabilities/date/2015-01-22/

Example response:

    {
      "availabilities": [
        {
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
                "plural"; "Adults",
                "note": "At least 18 years old."
              },
              "customer_prototype": {
                "pk": 2522,
                "display_name": "Adult"
              }
            }
          ]
        },
        {
          "pk": 4787,
          "start_at": "2015-01-22T13:30:00-1000",
          "end_at": "2015-01-22T15:30:00-1000",
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
                "plural"; "Adults",
                "note": "At least 18 years old."
              },
              "customer_prototype": {
                "pk": 2522,
                "display_name": "Adult"
              }
            }
          ]
        }
      ]
    }

## Bookings

Create a booking:

* `POST /companies/<shortname>/availabilities/<Availability.pk>/bookings/`

Retrieve a booking:

* `GET /companies/<shortname>/bookings/<Booking.uuid>/`

Cancel a booking:

* `DELETE /companies/<shortname>/bookings/<Booking.uuid>/`

The result of both creating, retrieving, and cancelling a booking is a `Booking` object.

Example request:

    $ curl -X POST \
    -H "X-FareHarbor-API-App: YOUR-APP-KEY" \
    -H "X-FareHarbor-API-User: YOUR-USER-KEY" \
    -d \
    '{
       "contact": {
         "name": "John Doe", 
         "phone": "415-789-4563", 
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
                "plural"; "Adults",
                "note": "At least 18 years old."
              },
              "customer_prototype": {
                "pk": 2522,
                "display_name": "Adult"
              }
            }
          ]
        },
        "contact": {
          "name": "John Doe",
          "phone": "415-789-4563",
          "email": "johndoe@example.com"
        },
        "customers": [
          {
            "customer_type_rate": {
              "pk": 65675,
              "total": 20000,
              "capacity": 10,
              "is_exclusive": false,
              "customer_type": {
                "pk": 978,
                "singular": "Adult",
                "plural"; "Adults",
                "note": "At least 18 years old."
              },
              "customer_prototype": {
                "pk": 2522,
                "display_name": "Adult"
              }
            }
          },
          {
            "customer_type_rate": {
              "pk": 65675,
              "total": 20000,
              "capacity": 10,
              "is_exclusive": false,
              "customer_type": {
                "pk": 978,
                "singular": "Adult",
                "plural"; "Adults",
                "note": "At least 18 years old."
              },
              "customer_prototype": {
                "pk": 2522,
                "display_name": "Adult"
              }
            }
          }
        ]
      },
      "invoice_price": null
    }

### Request Schema

When creating bookings use the customer type rate and custom field instance information
contained in the availability to construct a request of the following form:

* `note`: `string`
* `voucher_number`: `string`
* `contact`: `object`
    * `name`: `string`
    * `phone`: `string`
    * `email`: `string`
* `customers`: `array`
    * `customer_type_rate`: `CustomerTypeRate.pk`

Example:

    {
      "note": "Optional booking note.",
      "voucher_number": "VLT-1123",
      "contact": {
        "name": "John Doe",
        "phone": "443-222-1100",
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

#### Custom Field Values

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
         "phone": "415-789-4563",
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
         "phone": "415-789-4563",
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

* The booking must be cancelled at least 48 hours prior to start time (availability `start_at` property).
* Any affiliate collected payments for the booking must be fully refunded.
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

Initially all companies will use a "48 hours prior, 100% refund" policy; however, we expect to expand support for various kinds of cancellation policies in the future.

#### Planned: Rebooking

Note: this functionality is not available yet.

If it is necessary to change a booking to another date/time or change customer types/count, the booking must be cancelled and a new booking must be created.  Rebooking is a shortcut for that process.

To rebook an existing booking, specify the existing booking's UUID value for the `rebooking` property when creating a booking.

Example request:

    $ curl -X POST \
    -H "X-FareHarbor-API-App: YOUR-APP-KEY" \
    -H "X-FareHarbor-API-User: YOUR-USER-KEY" \
    -d \
    '{
       "rebooking": "d75102be-9732-4523-90a8-c698eff2b983",
       "contact": {
         "name": "John Doe",
         "phone": "415-789-4563",
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

#### Planned: Transportation

Note: this functionality is not available yet.

To request transportation for a booking, specify a `Lodging` pk for the `lodging` property when creating the booking as shown in the example below.

Example booking request body with a lodging specified:

    {
      "contact": {
         "name": "John Doe",
         "phone": "1234567890",
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

##### Planned: Pickup Information

When a lodging is specified during booking creation and transportation is available, the booking response will include a `pickup` property as shown in the example below.

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

##### Planned: Arrival Information

When a lodging is NOT provided during booking creation and arrival information is available, the booking response will include an `arrival` property as shown in the example below.

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

* `map_url`: `string`

  A URL to a map showing the arrival location; may not be provided.

* `display_text`: `string`

  A formatted string that can be shown to customers.
