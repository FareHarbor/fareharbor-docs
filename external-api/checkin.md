<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Checkin via QR Code](#checkin-via-qr-code)
- [Check-in via Booking UUID](#check-in-via-booking-uuid)

<!-- markdown-toc end -->

# Checkin via QR Code

```
PUT https://fareharbor.com/api/external/v1/companies/<shortname>/checkin/
```

The body should be as follows:

```
{
  "qr_code": string,  // required
  "is_whole_booking": bool,  // defaults to false if not provided
  "checkin_status": string|number|null  // defaults to "auto" if not provided; null clears checkin status
}
```

`qr_code` - `string`: the customer's QR code data.

`is_whole_booking` - `bool`: whether whole booking checkin is desired. If `true`,
the checkin status for all customers associated with the booking will be
updated. If `false`, the checkin status for the customer associated with the QR
code (customer checkin URL) will be updated. Defaults to `false` if the property
is not provided.

`checkin_status` - `string|number|null`: the string "auto" indicates that checkin status
should be automatically determined. The string "unchanged" will leave the checkin
status unchanged. Other string values may be supported in the
future. When a checkin status `pk` is provided, the associated checkin status
will be used. When `null` is provided, the checkin status will be reset. Defaults
to `"auto"` if the property is not provided.

The result is the booking as described here: https://github.com/FareHarbor/fareharbor-docs/blob/master/external-api/data-types.md#booking

When "auto" check-in is used, an HTTP 400 will be returned if the customer
(or, in the case of whole booking checkin, any customer) is already checked in.


Examples:

1. Customer checkin, auto status

```
{
  "qr_code": "https://fhchk.co/abc"
}
```

2. Whole booking checkin, auto status

```
{
  "qr_code": "https://fhchk.co/abc",
  "is_whole_booking": true
}
```

3. Customer checkin, specific status

```
{
  "qr_code": "https://fhchk.co/abc",
  "checkin_status": 386865
}
```

4. Customer checkin, reset status

```
{
  "qr_code": "https://fhchk.co/abc",
  "checkin_status": null
}
```

If instead of automatically selecting the checkin status you would like to specify it
directly via `pk`, you can pull a list of available checkin statuses here:

```
GET https://fareharbor.com/api/external/v1/companies/<shortname>/checkin-statuses/
```

Response:
```
{
  "checkin_statuses": [
    {
      "pk": 45786797,
      "type": "checked-in",
      'name': "Checked in"
    },
    {
      "pk": 89766887,
      "type": "no-show",
      "name": "No show"
    }
  ]
}
```

Note that checkin statuses are unique per company. They have the form described here under
"Customers": https://github.com/FareHarbor/fareharbor-docs/blob/master/external-api/data-types.md#booking

# Check-in via Booking UUID

If instead of checking in via the QR code you would like to use a booking directly to check-in, you may do so as follows:

```
PUT https://fareharbor.com/api/external/v1/companies/<shortname>/bookings/<Booking.uuid>/checkin/
```

Body:

```
{
  "checkin_status": string|number|null,  // defaults to "auto" if not provided
  "customer": number|null  // defaults to null (whole booking) if not provided
}
```

`checkin_status` - `string|number|null`: as above.

`customer` - `number|null`: when a customer `pk` is specified, the associated customer
will be checked in. When `null` is specified, all customers associated with the
booking will be checked in. Defaults to `null` if the property is not provided.

Examples:

1. Whole booking checkin, auto status

No request body.

2. Whole booking checkin, specific status

```
{
  "checkin_status": 68575
}
```

3. Customer checkin, specific status

```
{
  "checkin_status": 785897,
  "customer": 9868574
}
```

4. Whole booking checkin, reset status

```
{
  "checkin_status": null
}
```

5. Customer checkin, reset status

```
{
  "checkin_status": null,
  "customer": 6857686
}
```
