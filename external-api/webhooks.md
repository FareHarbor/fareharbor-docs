# What is a webhook

A webhook is an HTTPS request sent from FareHarbor to a server of your
choice as a result of an event.

FareHarbor can send webhooks when bookings are created, updated,
rebooked, or cancelled, or when a contact changes.

# Configuring webhooks

You can provide two webhook URLs to FareHarbor: one for production
webhooks and one for test webhooks.

Contact <support@fareharbor.com> to configure these.

(Note: SSL certificates will be validated for the production URL.)

(Note: Companies in demo mode do not trigger webhooks.)

## Booking notifications

When a booking-related event occurs, FareHarbor sends a `POST` request to
the webhook URL you have provided.

Depending on how your webhooks are configured, these `POST` reqeusts will be sent for:

* all changes to bookings (including creations, modifications, and cancellations);
* creations only; or
* cancellations only.

The body of this request contains an up-to-date JSON representation of
the booking.

Some of the fields are described here `/external-api/endpoints.md` and
here `/external-api/data-types.md#booking`.

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
                "is_cancelled": False,
                "pk": 1123
              }
            ],
            "status": "succeeded",
            "type": "affiliate"
          }
        ],
        ...
      }
    }

Your server should respond to the webhook with an HTTP success
response code. (If FareHarbor receives an HTTP error response or no
response at all, then the webhook will be retried up to 3 more times
at 60 second intervals.)

## Third-party servers

If you do not have your own servers, you can use third-party services
that receive webhooks on your behalf.
