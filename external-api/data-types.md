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

All currency amounts are returned as an integer number of the smallest
negotiable unit of money in the company's currency. In the case of
USD, this means USD cents. So, for instance, `1425` means $14.25 USD.

Some amount fields may have corresponding fields whose names are
suffixed with `_display`. These fields will contain strings
representing the same amount of money, but using the customary
formatting for the company's country. For instance, in the case of
US/USD, this will be the string `14.25`. Note that some countries may
use a comma rather than a period as the decimal point.

* `field`: `number`
* `field_display`: `string`

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

#### Minimal Representation

A `Company` object represent an affiliate or provider.

* `shortname`: `string`

  The company's ID.

* `name`: `string`

  The company's name.

* `currency`: `string`

  The company's currency.

Example:

    {
      "shortname": "hawaiianadventures",
      "name": "Hawaiian Adventures",
      "currency": "usd"
    }

#### Extended Representation

The extended representation provides additional information about the company (see below).

* `about`: `markdown`

  About page content for the company.

* `booking_notes`: `markdown`

  General notes for booking customers.

* `faq`: `markdown`

  FAQ page content for the company.

* `intro`: `markdown`

  Homepage content for the company.

* `summary`: `string`

  A short tagline or summary for the company.

* `url`: `string`

  The company's website address.

* `facebook_url`: `string`

  The company's Facebook address.

* `instagram_url`: `string`

  The company's Instagram address.

* `tripadvisor_url`: `string`

  The company's TripAdvisor address.

* `twitter_url`: `string`

  The company's Twitter address.

* `yelp_url`: `string`

  The company's Yelp address.

* `youtube_url`: `string`

  The company's Youtube address.

* `pinterest_url`: `string`

  The company's Pinterest address.

* `address`: `Address`

  The company's physical address.

* `billing_address`: `Address`

  The company's billing address.

* `health_and_safety_policy`: `markdown`

  The company's health and safety policy.

Example:

    {
      "company": {
        "shortname": "hawaiianadventures",
        "name": "Hawaiian Adventures",
        "currency": "usd",
        "about": "Hawaiian Adventures offers several water activities that you are sure to enjoy.",
        "about_safe_html": "<p>Hawaiian Adventures offers several water activities that you are sure to enjoy.</p>",
        "booking_notes": "Weather conditions will be evaluated at the time of check-in.\n\n-If using a voucher, please bring the voucher with you.",
        "booking_notes_safe_html": "<p>Weather conditions will be evaluated at the time of check-in.\n\n-If using a voucher, please bring the voucher with you.</p>",
        "faq": "# What should I bring?\n\nWe suggest that you bring a swimming suit, a towel, and sunscreen.",
        "faq_safe_html": "<h1>What should I bring?</h1>\n<p>We suggest that you bring a swimming suit, sunscreen, and a towel.</p>",
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
        "billing_address": {
          "city": "Honolulu",
          "country": "US",
          "postal_code": "96821",
          "province": "HI",
          "street": "123 Wailupe Cir"
        },
        "health_and_safety_policy": "# Company Health & Safety Policy Statement\nThe safety and health of our employees is this company’s most important business consideration.\n\nThe company pledges to do the following:\n\n*  Strive to achieve the goal of zero accidents and injuries.\n* Train all employees in safe work practices and procedures.",
        "health_and_safety_policy_safe_html": "<h1>Company Health &amp; Safety Policy Statement</h1>\n<p>The safety and health of our employees is this company’s most important business consideration.</p>\n<p>The company pledges to do the following:</p>\n<ul>\n<li>Strive to achieve the goal of zero accidents and injuries.</li>\n<li>Train all employees in safe work practices and procedures.</li>\n</ul>"
      }
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

### Location

* `pk`: `number`

  The location's unique ID.

* `type`: `string`

  The location's type.

* `note`: `markdown`

  A brief note about this location that can be displayed to end users.

* `address`: `Address`

  The location's physical address.

* `longitude`: `number | null`

  The location's longitude.

* `latitude`: `number | null`

  The location's latitude.

* `google_place_id`: `string`

  The location's Google Place ID.

* `tripadvisor_url`: `string`

  The location's TripAdvisor URL.

### Cancellation Policy

* `type`: `string`

  The cancellation policy's type. Supported types:

  * `hours-before-start`

      Bookings are eligible for cancellation some number of hours before availability start time.

  * `hours-before-midnight`

      Bookings are eligible for cancellation some number of hours before midnight on availability start date.

  * `always`

      Bookings are eligible for cancellation up until a cutoff that is determined by the availability (usually the availability start time).

  * `never`

      Bookings are never eligible for cancellation (e.g. no effective cancellation policy, insufficient privileges, cancellation disallowed by policy).

* `cutoff_hours_before`: `number`

  The number of hours for the `hours-before-start` and `hours-before-midnight` types.

  Note: this value can be negative indicating that bookings can be cancelled some number of hours after availability start time (when type is `hours-before-start`) or some number of hours after midnight on availability start date (when type is `hours-before-midnight`). The `cutoff_hours_before` property will provide `null` when no cutoff is applicable (when bookings are never elgible for cancellation).

### Tag

* `name`: `string`

  The tag's display name.

* `short_name`: `string`

  The tag's short name. The short name is unique per company and is limited to lowercase letters (a-z), digits (0-9), and the dash character.

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

* `description_text`: `string`

  The item's plain-text description.

* `description_bullets`: `[ string ]`

  An array containing plain-text descriptive bullet points for the item.

* `cancellation_policy`: `markdown`

  The item's cancellation policy.

* `location`: `string`

  The location of the item; generally where the activity takes place
  or where the tour leaves from, but can be anything. Unstructured.

* `locations`: `[ Location ]`

  An array of `Location` objects associated with the item.

* `is_pickup_ever_available`: `bool`

  Indicates whether the item is configured to provide pickups.

* `image_cdn_url`: `string`

  A URL to the item's primary image.

* `images`: `[ Image ]`

  An array of `Image` objects associated with the item.

* `customer_prototypes`: `[ CustomerPrototype ]`

  An array of `CustomerPrototype` objects associated with the item.

* `health_and_safety_policy`: `markdown`

  The item's health and safety policy.

Example:

    {
      "pk": 1867,
      "name": "Jet Ski Tour",
      "headline": "Epic Jet Ski Tour",
      "description": "We are conveniently located just 5 minutes from Waikiki and will arrange for pickup\/dropoff at or near your hotel.",
      "description_safe_html": "\u003cp\u003eWe are conveniently located just 5 minutes from Waikiki and will arrange for pickup\/dropoff at or near your hotel.\u003c\/p\u003e",
      "description_text": "We are conveniently located just 5 minutes from Waikiki and will arrange for pickup\/dropoff at or near your hotel.",
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
      "health_and_safety_policy": "Our policies are:\n\n* Bring your own googles\n* Use facemask when we met",
      "health_and_safety_policy_safe_html": "<p>Our policies are:</p>\n<ul>\n<li>Bring your own googles</li>\n<li>Use facemask when we met</li>\n</ul>"
    }

#### Item Details

When `detailed=yes` is specified as the query string for the items endpoint, additional details are provided for each item.

* `effective_cancellation_policy`: `CancellationPolicy`

  Cancellation policy data for the item.

* `tags`: `[ Tag ]`

  An array of `Tag` objects associated with the item.

Example:

    {
      "pk": 1867,
      "effective_cancellation_policy": {
        "type": "hours-before-start",
        "cutoff_hours_before": 24
      },
      "tags": [
        {
          "name": "Jet ski tour",
          "short_name": "jet-ski-tour"
        },
        {
          "name": "Water activity",
          "short_name": "water-activity"
        },
        {
          "name": "Transportation included",
          "short_name": "transportation"
        },
        ...
      ],
      ...
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

### Customer Prototype

* `pk`: `number`

  The customer prototype's unique ID.

* `display_name`: `string`

  The customer prototype's display name.

* `total`: `amount`

  The price of a single customer of this type.

* `total_including_tax`: `amount`

  The price of a single customer of this type plus applicable taxes.

Example:

    {
      "pk": 2522,
      "display_name": "Adult",
      "total": 20000,
      "total_including_tax": 21550
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
          "display_name": "Adult",
          "total": 20000,
          "total_including_tax": 21550
        }
      }
    }

#### Extended Representation

The extended representation provides additional information about the customer type rate (see below).

* `total`: `amount`

  The price of a single customer of this type.

* `total_including_tax`: `amount`

  The price of a single customer of this type plus applicable taxes.

* `custom_field_instances`: `[ CustomFieldInstance ]`

  A list of custom field instances for the customer type rate.

Example:

    {
      "pk": 978,
      "total": 20000,
      "total_including_tax": 21550,
      "capacity": 10,
      "is_exclusive": false,
      "customer_type": {
        "pk": 589,
        "singular": "Adult",
        "plural"; "Adults",
        "note": "At least 18 years old.",
        "customer_prototype": {
          "pk": 2522,
          "display_name": "Adult",
          "total": 20000,
          "total_including_tax": 21550
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
              "display_name": "Adult",
              "total": 20000
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

### Order

Orders are a way of grouping collections of bookings so that they can be created or cancelled as a block.

A booking can belong to an order, but it doesn't have to. An order can include any number of bookings.

* `display_id`: `string`

  A unique identifier for the order.

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

    * `normalized_phone`: `string`

        The party's contact phone number. This will have a plus sign, the country code, and no extra characters such as commas or dashes.

    * `country_phone`: `string`

        The contact phone's country code.

    * `email`: `string`

        The contact email for the party.

    * `is_subscribed_for_email_updates`: `bool`

        Whether or not the contact would like email updates.

* `customers`: `[ Customer ]`

  A list of customers on this booking.  Customers consist of:

    * `checkin_url`: `string`

      A short URL that can be rendered as a QR code for check-in purposes (the QR code should be "type 4" with "error correction H").

    * `checkin_status`: `CheckinStatus | null`

      The customer's checkin status.  When there is no checkin status associated with the customer, `checkin_status` will be `null`.  When a checkin status is available, it consists of:

        * `name`: `string`

          The checkin status' name.

        * `type`: `string`

          The checkin status' type. Supported types are: `checked-in` and `no-show`.

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

* `order`: `Order | null`

  When there is no order associated with the booking, `order` will be `null`.

* `dashboard_url`: `string`
  The booking's dashboard URL.

* `customer_count`: `number`
  The number of customers on this booking.


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
        "phone": "+1-443-222-1100",
        "phone_country": "US",
        "normalized_phone": "+14432221100",
        "email": "surfer@dude.com"
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
              "plural"; "Adults",
              "note": "At least 18 years old.""
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
              "plural"; "Adults",
              "note": "At least 18 years old.""
            }
          }
        }
      ],
      "invoice_price": null,
      "order": null,
      "dashboard_url": "https://fareharbor.com/hawaiianadventures/dashboard/?overlay=/contacts/7/bookings/d75102be-9732-4523-90a8-c698eff2b983/",
      "customer_count": 1
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
