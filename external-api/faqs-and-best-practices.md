<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Frequently Asked Questions](#frequently-asked-questions)
    - [-](#-)
    - [Using IP address-based ACLs or allowlists to validate the source of webhooks](#using-ip-address-based-acls-or-allowlists-to-validate-the-source-of-webhooks)
    - [Question: Slow /availabilities/date-range/ endpoint](#question-slow-availabilitiesdate-range-endpoint)
        - [Answer](#answer)
    - [Question: 403 from FareHarbor External API](#question-403-from-fareharbor-external-api)
        - [Answer](#answer-1)
    - [Question: Cancelling rebooked bookings](#question-cancelling-rebooked-bookings)
        - [Answer](#answer-2)
    - [Question: Translations](#question-translations)
        - [Answer](#answer-3)
- [FH API Integration Best Practices](#fh-api-integration-best-practices)
    - [Consider using Zapier, or a similar service.](#consider-using-zapier-or-a-similar-service)
    - [The data model](#the-data-model)
        - [The Booking UUID](#the-booking-uuid)
        - [The Customer PK](#the-customer-pk)
    - [Retrieving All Existing Bookings](#retrieving-all-existing-bookings)

<!-- markdown-toc end -->

# Frequently Asked Questions

## Question: Slow /availabilities/date-range/ endpoint

The Availabilities Date Range endpoint takes too long to return, or
times out and never returns. What should I do?

### Answer

There are a couple of things you can do:

1. BE SURE YOU ARE USING THE MINIMAL AVAILABILITIES ENDPOINT. This is
   the one described in the documentation:
   [/external-api/endpoints/endpoints.md#availabilities](/external-api/endpoints/endpoints.md#availabilities)
   
   GET /companies/<shortname>/items/<item.pk>/minimal/availabilities/date-range/<start-date>/<end-date>/

   Make sure the endpoint path contains the word `minimal`.
   
   Other versions of this endpoint are much slower, and are not
   recommended.

2. DECREASE THE DATE RANGE for which you are requesting availability
   data. For instance, if start-date and end-date are 60 days or 30
   days apart, try decreasing the interval to 15 days or even 10 days.

## Question: 403 from FareHarbor External API

I am calling the FareHarbor External API. FareHarbor is responding
with a "403 Forbidden". How can I fix this?

### Answer

Double-check that you are using the right keys in your API call.

## Question: Cancelling rebooked bookings

Say I create booking A, then I rebook it to booking B, then I want to
cancel the booking. When cancelling via API, should I cancel booking A
or booking B?

### Answer

Cancelling either one via API will cause FareHarbor to cancel the
booking. Regardless of which you cancel, booking A will wind up with
`"status":"rebooked"` and booking B will wind up with
`"status":"cancelled"`. So cancel whichever you like. In many cases,
depending how your system is set up, the path of least confusion on
your side may be to CANCEL THE MOST RECENT BOOKING.

## Question: Translations

Can I use the FareHarbor External API to retrieve translated content?

### Answer

Yes. You can retrieve translated content provided by the dashboard company in any language that is "active" in their dashboard, in the Translation Languages section, by adding a query parameter to the API request:

    GET /companies/<shortname>/items/?language=es

Doing this gives you company-provided translations. It does not translate field names etc., and it does not change currency formatting or provide other localization.

# FH API Integration Best Practices

This section describes some best practices for integrating with FH
using webhooks and APIs.

## Consider using Zapier, or a similar service.

Before writing software to integrate with FareHarbor webhooks, look
into using Zapier or something similar. In many cases, doing an
integration this way will be quicker, easier, more reliable, and less
expensive than doing it yourself with your own servers and custom
software.

In order to integrate with the FareHarbor webhooks and/or API
directly, without using Zapier or the like, you will need time from
experienced software engineers. If you do not have them on staff, you
may need to contract them and manage them. This is not always easy.

## The data model

### The Booking UUID

The most important field in the booking schema is the "uuid" field. IF
YOU RECEIVE TWO WEBHOOKS WITH THE SAME UUID, THEY ARE TALKING ABOUT
THE SAME BOOKING. This is the most important thing to understand about
bookings.

You will likely receive multiple webhooks for the same booking. For
instance, you will receive one when it's created, and you may receive
another if the contact information is updated, or if a customer
checkin occurs.

For any given uuid, the most recent webhook received will contain the
most up-to-date data.

You can always retrieve the most recent details for a booking using
the Retrieve Bookings endpoint,
[/endpoints.md#bookings](/external-api/endpoints/endpoints.md#bookings):

    GET /companies/<shortname>/bookings/<Booking.uuid>/

### The Customer PK

Another important field is the "customers" field. This field contains
a list of customers. Each customer will have its own "pk". The PK is a
globally-unique identifier for the customer. 

The details of a booking may change, but as long as it is not
rebooked, the customer PK will not change, and can be used as an ID
within your system, directly or indirectly.

If you receive a webhook from FareHarbor for a booking that is already
recorded in your system, this new webhook may contain updated
information. Using the PK, you can check each customer's data to see
if any piece of that customer's data has changed--the contents of a
custom field, for instance.

When a rebooking occurs, customer PKs are reassigned. For most
practical purposes, you can treat a rebooking event the same as
cancellation of the old booking and creation of the new booking. Data
associated with the old booking are no longer relevant.

## Retrieving All Existing Bookings

Using the External API, it is possible to retrieve all existing bookings.

In pseudocode, it looks like this:

    retrieve a list of companies via the [Companies endpoint](/endpoints.md#companies)
    for each company,
      retrieve a list of items via the [Items endpoint](/endpoints.md#items)
      for each item,
        retrieve lists of availabilities via the [Availabilities endpoint](/endpoints.md#availabilities)
        for each availability,
          retrieve a list of bookings via the [Availability Bookings endpoint](/endpoints.md#availability-bookings)

There is sample python code to retrieve all bookings [here](/external-api/examples/retrieve_bookings.py).
