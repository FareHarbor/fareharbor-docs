# Data Types

## Fields

### Markdown fields

Many of the fields returned by the API contain user-defined Markdown.
We also return the rendered HTML version of the field.  In the following
schemas, fields of type `markdown` actually contain a `string`, and imply
a second field in the schema containing the rendered HTML.  So the following:

* `field`: `markdown`

Should be treated as if it were:

* `field`: `string`
* `field_safe_html`: `string`

The "safe" part of the field name indicates that only a limited subset
of HTML is allowed; all other HTML entities are escaped.

### Amount fields

All currency amounts are returned as an integer number of USD cents. So, for instance,
`1425` means $14.25 USD.

* `field`: `number`

### Datetime fields

All datetimes are returned in ISO8601 format; for example `2013-02-04T06:21:36+0000`

* `field`: `string`

## Schemas

### Address

Structured address data.

* `city`: `string`

* `country`: `string`

* `postal_code`: `string`

* `province`: `string`

* `street`: `string`

Example:

    {
      "city": "Honolulu",
      "country: "US",
      "postal_code": "96821",
      "province": "HI",
      "street": "123 Wailupe Cir"
    }

### Company

A `Company` object represent an affiliate or provider.

* `shortname`: `string`

  The company's ID.

* `name`: `string`

  The company's name.

Example:

    {
      "shortname": "hawaiianadventures",
      "name": "Hawaiian Adventures"
    }

### Agent

* `pk`: `number`

  The agent's unique ID.

* `name`: `string`

  The agent's name.


Example:

    {
      "pk": 231,
      "name": "Eddie"
    }

### Desk

* `pk`: `number`

  The desk's unique ID.

* `name`: `string`

  The desk's name.


Example:

    {
      "pk": 231,
      "name": "Windward Side"
    }

### Lodging

* `pk`: `number`

  The lodging's unique ID.

* `name`: `string`

  The Lodging's name.

* `phone`: `string`

  The lodging's phone number.

* `address`: `string`

  The lodging's address.

* `url`: `string`

  The lodging's URL.

* `is_self_lodging`: `bool`

  Whether the lodging is a customer provided, non-hotel lodging (e.g. private residence).

Example:

    {
      "pk": 231,
      "name": "Wyndham Royal Garden",
      "phone": "(808) 943-0202",
      "address": "440 Olohana St Honolulu, HI 96815",
      "url": "https:\/\/www.extraholidays.com\/honolulu-hawaii\/royal-garden-at-waikiki.aspx",
      "is_self_lodging": false
    }

### Image

* `pk`: `number`

  The image's unique ID.

* `gallery`: `string`

  The image's gallery name.

* `image_cdn_url`: `string`

  The image's URL.
  
Example:

    {
      "pk": 687,
      "gallery": "carousel",
      "image_cdn_url": "https:\/\/d1a2dkr8rai8e2.cloudfront.net\/api\/file\/rvybRyLWTgyV5w4xg42p\/"
    }

### Item

Items represent a particular kind of tour that the company offers.

* `pk`: `number`

  The item's unique ID.

* `name`: `string`
    
  The name of the item.

* `headline`: `string`

  The item's headline.

* `description`: `markdown`

  The item's description.

* `cancellation_policy`: `markdown`

  The item's cancellation policy.

* `location`: `string`

  The location of the item; generally where the activity takes place
  or where the tour leaves from, but can be anything. Unstructured.

* `is_pickup_ever_available`: `bool`

  Indicates whether the item is configured to provide pickups.

* `image_cdn_url`: `string`

  A URL to the item's primary image.

* `images`: `[ Image ]`

  An array of `Image` objects associated with the item.

Example:

    {
      "pk": 1867,
      "name": "Jet Ski Tour",
      "headline": "Epic Jet Ski Tour",
      "description": "We are conveniently located just 5 minutes from Waikiki and will arrange for pickup\/dropoff at or near your hotel.",
      "description_safe_html": "\u003cp\u003eWe are conveniently located just 5 minutes from Waikiki and will arrange for pickup\/dropoff at or near your hotel.\u003c\/p\u003e",
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
      ]
    }

### Customer Type

Customer types represent different kinds of customers that might do an activity, for
example "Adults", "Children", "Infants". Note however that FareHarbor companies use
customer types to represent a range of different sorts of customers; for instance,
some SCUBA companies use types like "Diver", "Snorkeler", and "Observer".

* `pk`: `number`

  The customer type's unique ID.

* `singular`: `string`
* `plural`: `string`

  The singular and plural forms of the name of this customer type; ex. "adult", "adults".

* `note`: `string`

  A brief note about this customer type that can be displayed to end users.

Example:

    {
      "pk": 589,
      "singular": "Adult",
      "plural"; "Adults",
      "note": "At least 18 years old."
    }

### Customer Type Rate

Customer type rates set capacity and pricing information for customer types on
a particular availability. 

#### Minimal Representation

* `pk`: `number`

  The customer type rate's unique ID.

* `customer_type`: `CustomerType`

The customer type being priced.

* `capacity`: `number`

  The maximum number of customers of this type that can currently book this availability;
  this number will change over time as other customers book. 

* `is_exclusive`: `bool`

  Indicates that this customer type rate is "exclusive"; see below for how exclusivity
  affects bookability.

Example:

    {
      "pk": 978,
      "capacity": 10,
      "is_exclusive": false,
      "customer_type": {
        "pk": 589,
        "singular": "Adult",
        "plural"; "Adults",
        "note": "At least 18 years old.",
        "customer_prototype": {
          "pk": 2522,
          "display_name": "Adult"
        }
      }
    }

#### Extended Representation

The extended representation provides additional information about the customer type rate (see below).

* `total`: `amount`

  The price of a single customer of this type.

* `custom_field_instances`: `[ CustomFieldInstance ]`

  A list of custom field instances for the customer type rate.

Example:

    {
      "pk": 978,
      "total": 20000,
      "capacity": 10,
      "is_exclusive": false,
      "customer_type": {
        "pk": 589,
        "singular": "Adult",
        "plural"; "Adults",
        "note": "At least 18 years old.",
        "customer_prototype": {
          "pk": 2522,
          "display_name": "Adult"
        }
      },
      "custom_field_instances": [
        {
          "pk": 8629,
          "custom_field": {
            "pk": 43879,
            "type": "yes-no",
            ...
          }
        }
      ]
    }

### Availability

Availability objects represent particular datetimes that an item goes out.

#### Minimal Representation

* `pk`: `number`

  The availabilities's unique ID.

* `start_at`: `datetime`
* `end_at`: `datetime`

  The availability's start and end time; note that this time can be arbitrarily long or short,
  and that `start_at` can equal `end_at` for "point" availabilities.

* `capacity`: `number`

  The overall maximum number of customers that can currently book this availability;
  this number will change over time as other customers book. 

* `customer_type_rates`: `[ CustomerTypeRate ]`

  Pricing information for available customer types (minimal version).

Example:

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
            "plural"; "Adults",
            "note": "At least 18 years old.",
            "customer_prototype": {
              "pk": 2522,
              "display_name": "Adult"
            }
          }
        }
      ]
    }

#### Extended Representation

The extended representation provides additional information about the availability (see below).

* `item`: `Item`

  The availability's item (minimal version).

* `customer_type_rates`: `[ CustomerTypeRate ]`

  Pricing information for available customer types (extended version).

* `custom_field_instances`: `[ CustomFieldInstance ]`

  A list of custom field instances for the availability.

Example:

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
          "customer_type": {
            "pk": 978,
            "singular": "Adult",
            "plural"; "Adults",
            "note": "At least 18 years old.",
            "customer_prototype": {
              "pk": 2522,
              "display_name": "Adult"
            },
            "custom_field_instances": [
              {
                "pk": 8629,
                "custom_field": {
                  "pk": 43879,
                  "type": "yes-no",
                  ...
                }
              }
            ]
          }
        }
      ],
      "custom_field_instances": [
        {
          "pk": 47974,
          "custom_field": {
            "pk": 3387,
            "type": "yes-no",
            ...
          }
        }
      ]
    }

### Booking

* `pk`: `number`

  The booking's unique ID.

* `uuid`: `string`

  The booking's universally unique identifier; used to access the booking via the API.

* `display_id`: `string`

  The customer's "ticket number;" used only for rendering.

* `availability`: `Availability`

  The availability to which this booking corresponds.
 
* `contact`: `Contact`

  Contact information for this booking.  A contact consists of:
    
    * `name`: `string`
    
        The name of the head of the party.
        
    * `phone`: `string`
    
        The contact phone number for the party.
        
    * `email`: `string`
    
        The contact email for the party.

* `customers`: `[ Customer ]`

  A list of customers on this booking.  Customers consist of:
  
    * `customer_type_rate`: `CustomerTypeRate`
    
      The customer type rate to which this customer corresponds.

    * `custom_field_values`: `[ CustomFieldValue ]`

      A list of custom field values for the customer.

* `custom_field_values`: `[ CustomFieldValue ]`

  A list of custom field values for the booking.

* `invoice_price`: `amount | null`

  The invoice price of this booking.  Assuming that the user of the API is a reseller this will
  be the amount that the user of the API owes the vendor on this booking, if the vendor has opted
  to set up that information; otherwise it will be `null`.

* `confirmation_url`: `string`

  The booking's confirmation page URL.

Example:

    {
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
        "name": "Surfer Dude",
        "phone": "443-222-1100",
        "email": "surfer@dude.com"
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
      ],
      "invoice_price": null
    }

### Capacities

Note that availabilities have both an overall capacity, and customer type rates have an (optional) capacity.
Both capacities, if specified, cannot be exceeded, despite the fact that the sum of available
capacities of the customer type rates may not match the available capacity of the availability
itself. 

### Extended Option

Extended options are applicable to custom fields of type `extended-option`.

* `pk`: `number`

  The extended option's unique ID.

* `name`: `string`

  The extended option's name.

* `description`: `markdown`

  The extended option's description.

* `modifier_kind`: `string`

  Can be `offset` or `percentage`. Determines whether an offset or percentage
  is used when the total is adjusted or set.

* `modifier_type`: `string`

  Can be `adjust` or `set`. Determines whether the total is adjusted or set.

* `offset`: `amount`

  When `modifier_type` is `adjust`: a positive or negative amount value.

  When `modifier_type` is `set`: a positive amount value.

  Only applicable when `modifier_kind` is `offset`.

* `percentage`: `number`

  When `modifier_type` is `adjust`: a number between -100 and 100 inclusive.

  When `modifier_type` is `set`: a number between 0 and 100 inclusive.

  Only applicable when `modifier_kind` is `percentage`.

* `is_always_per_customer`: `bool`

  Whether pricing should be applied to each customer (when the customer field
  is at the booking level).

* `is_taxable`: `bool`

  Whether the cost of this option should affect the taxable total of a booking.

### Custom Field

* `pk`: `number`

  The custom field's unique ID.

* `type`: `string`

  The custom field's type. Supported types: `yes-no`, `short`, `long`, and
  `extended-option`.

* `is_required`: `bool`

  Indicates whether the custom field requires a value.

* `description`: `markdown`

  The custom field's description.

* `name`: `string`

  The name of the custom field.

* `booking_notes`: `markdown`

  Notes for the customer specific to the custom field. 

* `offset`: `amount`

  A positive or negative amount value.

* `extended_options`: `[ ExtendedOption ]`

  A list the custom field's extended options. This will only be provided
  for custom fields that have type `extended-option`.

### Custom Field Instance

* `pk`: `number`

  The custom field instance's unique ID.

* `custom_field`: `CustomField`

  The custom field associated with the custom field instance.

### Custom Field Value

* `custom_field`: `CustomField.pk`

  A valid Custom Field pk.

* `value`: `string`

  A string up to 2048 characters. If the custom field is of type `yes-no`, 
  "true" or "false" must be specified. If the custom field is of type 
  `extended-option`, an extended option pk must be specified.
