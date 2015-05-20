# Webhooks

FareHarbor can notify you of updates via a simple webhook. At this time you can
provide two URLs, one for production notifications and one for test notifications, by contacting
<support@fareharbor.com>.

## Booking notifications

Anytime a booking that you have created via the API changes you will be
notified by a `POST` request to this URL. The body of this request will contain an up-to-date
representation of the booking (with the structure descriped in `/external-api/endpoints.md`.

 ```
    {
      "booking": { ... }
    }
 ```
