<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [What is a webhook](#what-is-a-webhook)
- [Configuring webhooks](#configuring-webhooks)
    - [Booking notifications](#booking-notifications)
    - [Third-party servers](#third-party-servers)

<!-- markdown-toc end -->
# What is a webhook

A webhook is an HTTPS request sent from FareHarbor to a server of your
choice as a result of an event.

FareHarbor can send webhooks when bookings are created, updated,
rebooked, or cancelled, when a contact changes, when a checkin occurs,
etc.

For ideas about how to use webhooks in concert with the External API,
see [/external-api/faqs-and-best-practices.md](/external-api/faqs-and-best-practices.md).

# Configuring webhooks

You can provide two webhook URLs to FareHarbor: one for production
webhooks and one for test webhooks.

Contact <support@fareharbor.com> to configure these.

(Note: The server for the production webhook URL must have a valid SSL
certificate. It doesn't have one, then the webhook will not be
delivered. It is up to you to ensure that your SSL certificates get
renewed as needed.)

(Note: Companies in demo mode do not trigger webhooks.)

## Booking notifications

When a booking-related event occurs, FareHarbor sends a `POST` request to
the webhook URL that you have provided.

Depending on how your webhooks are configured, these `POST` requests will be sent for:

* all changes to bookings (including creations, modifications, and cancellations);
* creations only; or
* cancellations only.

The body of this request contains an up-to-date JSON representation of
the booking.

Some of the fields are described here: [/external-api/endpoints.md](/external-api/endpoints.md) and
here: [/external-api/data-types.md#booking](/external-api/data-types.md#booking).

Depending how your webhook is configured and what fields you are
allowed to view, there may also be a `payments` property:

    {
      "booking": {
        "pk": 456,
        "payments": [
          {
            "amount_paid": 1939,
            "amount_paid_display": "19.39",
            "created_at": "2020-07-23T14:43:30-1000",
            "currency": "usd",
            "initial_amount_paid": 2154,
            "initial_amount_paid_display": "21.54",
            "pk": 6234,
            "refunds": [
              {
                "amount_refunded": 215,
                "amount_refunded_display": "2.15",
                "created_at": "2020-07-23T14:43:41-1000",
                "is_cancelled": false,
                "pk": 1123
              }
            ],
            "status": "succeeded",
            "type": "affiliate",
            "in_store_payment_type": {
               "pk": 137,
               "name": "Cash"
            }
          }
        ],
        ...
      }
    }

When the payment is `type: "in-store"`, the `in_store_payment_type` in
the response has the pk and name of the in-store payment type.

When the payment is `type: "affiliate"` and the payment is an
affiliate in-store payment, the `in_store_payment_type` in the
response has the pk of the in-store payment type and may have the name
as well.

When the payment is not an in-store payment, the
`in_store_payment_type` in the response is `null`.

Your server should respond to the webhook with an HTTP success
response code. If FareHarbor receives an HTTP error response or no
response at all, then the webhook will be retried some number of
times, with a significant pause between attempts. 

## Third-party servers

If you do not have your own servers, you can use third-party services
that receive webhooks on your behalf.

## Failing webhooks

Sometimes FareHarbor sends a webhook to your server and there is a
failure of one sort or another. (See
[/external-api/faqs-and-best-practices.md#question-500s-and-40x-responses-from-webhooks](/external-api/faqs-and-best-practices.md#question-500s-and-40x-responses-from-webhooks)
for a discussion of why this might happen and how you can fix it.)

If FareHarbor detects too many failures within a short period of time,
we may deactivate the webhook and contact you.

Ultimately, it is your responsibility to make sure that your webhook
is working.
