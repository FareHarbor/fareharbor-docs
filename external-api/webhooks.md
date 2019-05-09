# What is a webhook

A webhook is an HTTPS request sent from FareHarbor to a server of your
choice as a result of an event.

FareHarbor can send webhooks when bookings are created, updated,
rebooked, or deleted, or when a contact changes.

# Configuring webhooks

You can provide two webhook URLs to FareHarbor: one for production
webhooks and one for test webhooks.

Contact <support@fareharbor.com> to configure these.

(Note: SSL certificates will be validated for the production URL.)

(Note: Companies in demo mode do not trigger webhooks.)

## Booking notifications

Any time there is a booking-related event, FareHarbor sends a `POST`
request to the webhook URL you have provided.

The body of this request contains an up-to-date JSON representation of
the booking, as described here `/external-api/endpoints.md` and here
`/external-api/data-types.md#booking`.

Your server should respond to the webhook with an HTTP success
response code. (If FareHarbor receives an HTTP error response, or no
response at all, then the webhook will be retried up to 3 more times
at 60 second intervals.)

 ```
    {
      "booking": { ... }
    }
 ```

## Third-party servers

If you do not have your own servers, you can use third-party services
that receive webhooks on your behalf.

### Zapier

Zapier is an example of one such third-party service. Once they start
receiving the webhooks, you enable you to create workflows in order to
do various things with the webhook data (add them to Google Sheet
spreadsheets for instance).

If you sign up for Zapier, they provide you a webhook URL that you pass along
to FareHarbor.

You can read more about their service here:
`https://zapier.com/apps/webhook`

(Note: Zapier costs money.)

(Note: Zapier is not affiliated in any way with FareHarbor.)

(Note: FareHarbor is not responsible for helping you use third-party
services such as Zapier.)
