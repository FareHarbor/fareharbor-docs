# Frequently Asked Questions

## Question: 500s and 40x responses from webhooks

I have FareHarbor webhooks configured. I am seeing things in my
FareHarbor dashboard that indicate that the webhooks are failing with
error status (500 or 400-something). The message says:

    Error: request unsuccessful: 500 Server Error: Internal Server Error for url: https://my.webhook.url/
    
(or something like that).

What should I do?

### Answer

A 500 response indicates that FareHarbor sent a webhook to
`https://my.webhook.url/`, but the server RECEIVING the webhook (i.e.,
your server) experienced an unexpected error--informally, it
"crashed". To resolve this, contact the person who is responsible for
your server, and ask them to look through the server logs around the
time that webhook was sent. This should provide some clues about the
problem.

A 40x response indicates that the server receiving the webhook (i.e.,
your server) did not like the data for some reason. Maybe the
authentication was improper, or some fields were missing that it was
expecting, or the webhook URL was incorrect on the FareHarbor
dashboard.

In either case (500 or a 40x), it is up to folks on your side to
resolve the problem. It may involve a reconfiguration or modification
of your server software. Also, ensure that your server's SSL
certificate has not expired, and is valid for the URL in your webhook
URL.

It is unlikely that the problem lies with FareHarbor. As a general
policy, FareHarbor does not make changes to the API and webhooks that
would break existing partner implementations. 

In order to debug problems with webhooks, you may want to cause the
webhook to be resent. See below for how to do that.

## Question: Missed webhook for specific booking

I missed a webhook for a specific booking. Maybe the webhook was sent,
but it received a 400 or 500 response. Or maybe it seems like the
webhook was never sent.  What can I do?

### Answer

The easiest way to resend a webhook for a specific booking is to
change something insignificant on the booking in question. Changing
the booking note is often a good choice. The webhook should be resent
shortly after any change to the booking.

If the webhook received a 500 before and if it receives a 500 again,
then your server software likely needs to be modified or
reconfigured. Please talk to your technical staff.

If the webhook receives a 40x, then check that the webhook URL is
correct, and confirm that certificates, security keys, etc. are in
place. 

## Question: Missed bookings

FareHarbor failed to send me webhooks for some bookings, rebookings,
and/or cancellations, but I don't know which ones. What should I do?

### Answer

FareHarbor tries very hard to send webhooks for new or changed
bookings. If FareHarbor fails on the first attempt, it will retry
repeatedly over some window of time.  If the server RECEIVING the
webhooks (your server) is down for a long time for some reason, there
is a chance that the webhooks won't be delivered.

In this case, the missing bookings can be retrieved using the
Availability Bookings endpoint, which allows you to retieve a list of
all bookings for a particular Availability. See
[/external-api/endpoints.md#availability-bookings](/external-api/endpoints.md#availability-bookings). If
you need more details than are provided by this endpoint, then you can
call the Retrieve Booking Endpoint to retrieve the full details for
each booking.

## Question: Duplicate webhooks

I receive each webhook TWICE, or more.

### Answer

Is it possible that you have multiple api keys configured to send
webhooks?

Beyond that:

A wide variety of events on the FareHarbor side trigger webhooks. Some
examples include changes to contact details, check-ins, text message
reminders sent, and so on. Many of these may not be relevant to your
particular integration. Each webhook contains complete data about the
booking.

You may receive multiple identical or nearly ideantical webhooks for
the same booking. This may happen occasionally or regularly. This is
normal. Keep reading to learn how to know how to handle this situation
and stay in sync with the bookings that exist in the FareHarbor
system.

## Question: Webhook security

How can I guarantee that the webhook we receive is from FareHarbor,
and not from someone else who somehow guessed the URL?

### Answer

#### Choose a hard-to-guess path

You are free to use whatever path you like in the webhook address you
provide to FareHarbor. For instance, if you use:

    https://mycompany.com/EE5746FDB4054852/fareharbor-webhook/
    
then it will be very hard to guess.

Or if you prefer, you can use something like
    
    https://mycompany.com/fareharbor-webhook/?key=EE5746FDB4054852
    
and check that you receive the expected query parameter.

#### Call the External API to verify booking data

Another security strategy: 

Whenever you receive a webhook, call the Retrieve Booking Endpoint of
the External API to retrieve the booking data:
[/external-api/endpoints.md#retrieve-booking-endpoint](/external-api/endpoints.md#retrieve-booking-endpoint).

Then use the retrieved data rather than the webhook payload data. 

This eliminates the potential negative impact of any "forged"
webhook. So even if someone does ascertain your webhook URL, they will
not be able to compromise your data integrity.
    
## Question: Slow /availabilities/date-range/ endpoint

The Availabilities Date Range endpoint takes too long to return, or
times out and never returns. What should I do?

### Answer

There are a couple of things you can do:

1. BE SURE YOU ARE USING THE MINIMAL AVAILABILITIES ENDPOINT. This is
   the one described in the documentation:
   [/external-api/endpoints.md#availabilities](/external-api/endpoints.md#availabilities)
   
   `GET /companies/<shortname>/items/<item.pk>/minimal/availabilities/date-range/<start-date>/<end-date>/`

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

# FH Webhook/API Integration Best Practices

This section describes some best practices for integrating with FH
using webhooks and APIs.

## Consider using Zapier, or a similar service.

Before writing software to integrate with FareHarbor webhooks, look
into using Zapier or something similar. In many cases, doing an
integration this way will be quicker, easier, more reliable, and less
expensive than doing it yourself with your own servers and custom
software.

In order to integrate with the FareHarbor API and webhooks directly,
you will need time from experienced software engineers. If you do not
have them on staff, you may need to contract them and manage
them. This is not always easy.

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
the Retrive Bookings endpoint,
[/endpoints.md#bookings](/endpoints.md#bookings):

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

### Retrieving Bookings for an Availability

FareHarbor has implemented an endpoint that allows you to retrieve all
bookings on a particular availability. This can be useful if you think
you may have missed one or more webhooks (or if you are not using
webhooks at all). See the Availability Bookings endpoint in
[/external-api/endpoints.md#availability-bookings](/external-api/endpoints.md#availability-bookings).
    
