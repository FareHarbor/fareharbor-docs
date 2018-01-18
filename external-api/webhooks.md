# Webhooks

FareHarbor can notify you of updates via a simple webhook. At this time you can
provide two URLs, one for production notifications and one for test notifications, by contacting
<support@fareharbor.com>. In production, SSL certificates will be verified.

Note: companies in demo mode will not trigger webhook requests.

## Booking notifications

Anytime a booking that you have created via the API changes you will be
notified by a `POST` request to this URL. The body of this request will contain an up-to-date
representation of the booking (with the structure descriped in `/external-api/endpoints.md`. Webhook requests listen for HTTP success codes. If the request receives an error response, it will be retried 3 times at 60 second intervals.

 ```
    {
      "booking": { ... }
    }
 ```
