FareHarbor External Integration API
-----------------------------------

# Requests

## Request Body

Some requests (particularly the `POST` to create a booking) require a body.
The body should be JSON.

## Authentication

Each FareHarbor user has a revocable API key associated with them, viewable
in a the Dashboard > Settings > Users section.  We suggest you create a
new user for your company (perhaps named "api"), and use the API key
for that user with all requests. This will allow you to track all API
actions via the user's history.

To authenticate a particular request, simply set the `X-FareHarbor-API` header
to your API key.

# Responses

## General Structure

All successful responses have the following form:

* `data`: `json`

The descriptions of schemas below assume that the request was successful
and describe the content of `data`.
 
All error responses have the following form:

* `error`: `string`
* `status`: `number`

Where `error` contains a message describing the error, and `status` is the same
as the HTTP status code.

## Error Codes

We use HTTP error codes to indicate the usual sorts of errors; the following
are the ones you are most likely to encounter.

* 400: Bad Request

  The request was invalid and could not be processed.

  This is most likely to occur when attempting to create a booking,
  and can correspond to things like attempting to overbook an availability
  or providing invalid data like customer name, phone number, etc.

* 403: Forbidden

  You do not have permission to access this endpoint in this way.
  
  Review the "Authentication" section and verify you are sending the
  correct API key, and that you do indeed have permission to access to
  endpoint you are attempting to access.
  
* 404: Not Found

  The company, item, or availability does not exist; it may have been
  deleted or otherwise become unavailable, or you may have an incorrect ID.

* 405: Method Not Allowed

  You are trying to use an unsupported HTTP method (`GET`, `POST`, and so on)
  with this endpoint.
  
* 429: Too Many Requests

  Returned when a request has been rate-limited. It is *very* unlikely
  that you will encounter this in normal usage.

* 500: Internal Server Error

* 503: Service Unavailable

  FareHarbor is temporarily unavailable, but will return within a few minutes.
  Try again later.

## Markdown

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

## Amounts

All currency amounts are returned as an integer number of USD cents. So, for instance,
`1425` means $14.25 USD.

## Datetimes

All datetimes are returned in ISO8601 format; for example `2013-02-04T06:21:36+0000`

## Schemas

### Company

* `shortname`: `string`

  The company's ID.

* `name`: `string`

  The company's name.

Example:

    {
      "shortname": "hawaiianadventures",
      "name": "Hawaiian Adventures"
    }
    
### Items

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

* `image_cdn_url`: `string`

  A URL to the item's primary image.

### Availabilities

Availability objects represent particular datetimes that an item goes out.
 
* `item`: `Item`

  The availability's item.

* `start_at`: `datetime`
* `end_at`: `datetime`

  The availability's start and end time; note that this time can be arbitrarily long or short,
  and that `start_at` can equal `end_at` for "point" availabilities.

* `available_capacity`: `number`

  The overall maximum number of customers that can currently book this availability;
  this number will change over time as other customers book. 

* `customer_type_rates`: `[ CustomerTypeRate ]`

  Pricing information for available customer types.

### Customer Type Rates

Customer type rates set capacity, pricing information, and custom fields
for customer types on a particular availability. 

* `pk`: `number`

  The customer type rate's unique ID.

* `customer_type`: `CustomerType`

The customer type being priced.

* `total`: `amount`

  The price of a single customer of this type.

* `available_capacity`: `number | null`

  The maximum number of customers of this type that can currently booking this availability;
  this number will change over time as other customers book. 

* `is_exclusive`: `bool`

  Indicates that this customer type rate is "exclusive"; see below for how exclusivity
  affects bookability.


### Customer Types

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

### Bookings

* `pk`: `number`

  The booking's unique ID; this is the customer's "ticket number", and is used
  only for rendering.

* `uuid`: `string`

  The booking's universally unique identifier; used to access the booking via the API.

* `availability`: `Availability`

  The availability to which this booking corresponds.
 
* `item`: `Item`

  The item to which this booking corresponds.

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

* `invoice_price`: `amount | null`

  The invoice price of this booking.  Assuming that the user of the API is a reseller this will
  be the amount that the user of the API owes the vendor on this booking, if the vendor has opted
  to set up that information; otherwise it will be `null`.

### Capacities

Note that availabilities have both an overall capacity, and customer type rates have an (optional) capacity.
Both capacities, if specified, cannot be exceeded, despite the fact that the sum of available
capacities of the customer type rates may not match the available capacity of the availability
itself. 

# Endpoints

All endpoints are rooted at `https://fareharbor.com/api/external/v1`.

## Companies

`GET /companies/`

Returns a list of all companies for which you have permission to create bookings;
note that this may include companies that have no bookable availabilities.

Returns an array of `Company` objects.

## Items

`GET /companies/<shortname>/items/`

Returns a list of items for which you have permission to create bookings; again,
note that this may include items that have no bookable availabilities.

Returns an array of `Item` objects.

## Availabilities

* `GET /companies/<shortname>/items/<item.pk>/availabilities/date/<date>/`
* `GET /companies/<shortname>/items/<item.pk>/availabilities/date/<start-date>/<end-date>/`

Returns possibly-bookable availabilities for `date`, or for the range `start-date` through `end-date`.
Note that possibly-bookable availabilies include those for which customers are requested to "call to book".
Note that `date`, `start-date`, and `end-date` should be in the format YYYY-MM-DD.

Returns an array of `Availability` objects.

## Bookings

* `POST /companies/<shortname>/availabilities/<Availability.pk>/bookings/`
* `GET /companies/<shortname>/bookings/<Booking.uuid>/`

The result of both creating and retrieving a booking is a `Booking` object.
 
### Request Schema

When creating bookings use the customer type rate and custom field instance information
contained in the availability to construct a request of the following form:

* `voucher_number`: `string` (required)
* `contact`: `dict`
    * `name`: `string` (required)
    * `phone`: `string` (required)
    * `email`: `string` (required)
* `customers`: `array`
    * `customer_type_rate`: `CustomerTypeRate.pk`

Example:

    {
      "voucher_number": "VLT-1123"
      "contact": {
        "name": "Surfer Dude",
        "phone": "443-222-1100",
        "email": "surfer@dude.com"
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
