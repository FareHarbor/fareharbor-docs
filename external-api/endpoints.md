# Endpoints

All endpoints are rooted at `https://fareharbor.com/api/external/v1/`.

## Companies

`GET /companies/`

Returns a list of all companies for which you have permission to create bookings;
note that this may include companies that have no bookable availabilities.

Returns an array of `Company` objects.

Example request:

    $ curl -H "X-FareHarbor-API-App: APP-KEY" -H "X-FareHarbor-API-User: USER-KEY" https://fareharbor.com/api/external/v1/companies/

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

## Items

`GET /companies/<shortname>/items/`

Returns a list of items as for which you have permission to create bookings; again,
note that this may include items that have no bookable availabilities.

Returns an array of `Item` objects.

Example request:

    $ curl -H "X-FareHarbor-API-App: APP-KEY" -H "X-FareHarbor-API-User: USER-KEY" https://fareharbor.com/api/external/v1/companies/hawaiianadventures/items/

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

    $ curl -H "X-FareHarbor-API-App: APP-KEY" -H "X-FareHarbor-API-User: USER-KEY" https://fareharbor.com/api/external/v1/companies/hawaiianadventures/items/1867/availabilities/date/2015-01-022/

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
                "note": "At least 18 years old.""
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
                "note": "At least 18 years old.""
              }
            }
          ]
        }
      ]
    }

## Bookings

* `POST /companies/<shortname>/availabilities/<Availability.pk>/bookings/`
* `GET /companies/<shortname>/bookings/<Booking.uuid>/`

The result of both creating and retrieving a booking is a `Booking` object.

Example request:

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
                "note": "At least 18 years old.""
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
                "note": "At least 18 years old.""
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
                "note": "At least 18 years old.""
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

#### Planned: Custom Field Values 

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

#### Validation

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

## Planned: Validation

Checks bookability and provides booking level pricing information.
