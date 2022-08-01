# Frequently Asked Questions

## Question: 500s and 40x responses from webhooks

I have FareHarbor webhooks configured. I am seeing things in my
FareHarbor dashboard that indicate that the webhooks are failing with
error status (500 or 40x). The message says:

    Error: request unsuccessful: 500 Server Error: Internal Server Error for url: https://my.webhook.url/
    
(or something like that).

What should I do?

### Answer

This response indicates that FareHarbor sent a webhook to
`https://my.webhook.url/`, but the server RECEIVING the webhook (i.e.,
your server) experienced an error. To resolve this, contact whoever is
responsible for your server, and ask them to look through the server
logs around the time when that webhook was sent. This should reveal
the problem.

It is up to folks on your side to resolve the problem. It may involve
a reconfiguration or modification of your server software.

It is unlikely that the problem lies with FareHarbor. As a general
policy, FareHarbor does not make changes to the API and webhooks that
would break existing partner implementations. 

## Question: Missed bookings

FareHarbor failed to send me webhooks for some bookings. What should I do?

### Answer

FareHarbor tries very hard to send webhooks for new or changed
bookings. If FareHarbor fails on the first attempt, it will retry
repeatedly over some window of time.  If the server RECEIVING the
webhooks (your server) is down for a long time for some reason, due to
a time-consuming update or a bug or whatever, there is a chance that
the webhooks won't be delivered.

In this case, the missing bookings can be retrieved using the
Availability Bookings endpoint, to retieve a list of all bookings for
each Availability. See `/external-api/endpoints.md`. If you need more
details than are provided by this endpoint, then you can call the Retrieve
Booking Endpoint to retrieve the full details for each one.

## Question: Slow /availabilities/ endpoint

The `/availabilities/date-range/<start-date>/<end-date>/` endpoint
takes too long to return, or times out. What should I do?

### Answer

There are a few potential causes of this endpoint being slow. But the
easiest solution to this problem is to DECREASE THE DATE RANGE for
which you are requesting availability data. For instance, if
start-date and end-date are 60 days or 30 days apart, try decreasing
the interval to 15 days or even 10 days.

# FH Webhook/API Integration Best Practices

This section describes some best practices for integrating with FH
using webhooks and APIs.

## Consider using Zapier, or a similar service.

Before writing software to integrate with FareHarbor webhooks, look
into using Zapier, IFTTT, or something similar. In many cases, doing
an integration this way will be quicker, easier, more reliable, and
less expensive than doing it yourself with your own servers and custom
software.

In order to integrate with FareHarbor webhooks and API directly, you
will need time from experienced software engineers. If you do not have
these on staff, you may need to contract them and manage them. This is
not always easy.

## Understand what kinds of events trigger webhooks

A wide variety of events on the FareHarbor side trigger webhooks. Some
examples include changes to contact details, check-ins, text message
reminders sent, and so on. Many of these may not be relevant to your
particular integration. Each webhook contains complete data about the
booking.

## The data model

### The Booking UUID

The most important field in the booking schema is the "uuid" field. IF
YOU RECEIVE TWO WEBHOOKS WITH THE SAME UUID, THEY ARE TALKING ABOUT
THE SAME BOOKING. This is the most important thing to understand about
bookings.

You will likely receive multiple webhooks for the same Booking. For
instance, you will receive one when it's created, and you may receive
another if the contact information is updated, or if a customer
checkin occurs.

### The Customer PK

Another important field is the "customers" field. This field contains
a list of customers. Each customer will have its own "pk". The PK is a
globally-unique identifier for the customer. 

As long as the booking is not rebooked, the pk will not change, and
can be used as an ID within your system, directly or indirectly. 

If you receive a new webhook for a booking that is already
represented in your system, this new webhook may contain updated
information. Using the PK, you can check each customer's data to see
if any piece of that customer's data has changed--the contents of a
custom field, for instance.

When a rebooking occurs, customer PKs are reassigned. For most
practical purposes, you can treat a rebooking event the same as a
cancellation and a new booking. Data associated with the old booking
are no longer relevant.




