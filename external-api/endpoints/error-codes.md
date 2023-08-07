<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [FareHarbor External API Error Codes](#fareharbor-external-api-error-codes)
    - [Bookability error](#bookability-error)
    - [Booking creation error](#booking-creation-error)
    - [Booking cancellation error](#booking-cancellation-error)

<!-- markdown-toc end -->

# FareHarbor External API Error Codes

This document provides more information about the following types of error codes and messages:

| status | Code | Error |
| ------- | ------ | ------- |
| 400  |availability-date-range-invalid  | Please specify an end date that comes after start date `start_date` |
| 400  |book-data-parse-error | Unable to parse request body |
| 400  |book-data-validation-error  | Validation error: `message` |
| 400  |bookability-error  | Unable to create booking: [bookability-error](#bookability-error) |
| 400  |booking-cancellation-error | Unable to cancel booking: [booking-cancellation-error](#booking-cancellation-error) |
| 400  |booking-creation-error | Unable to create booking: [booking-creation-error](#booking-creation-error) |
| 400  |booking-custom-field-value-creation-error | Unable to create custom field value for custom_field pk %s: ensure a valid value is specified|
| 400  |booking-custom-field-values-invalid  |<p>Duplicate values provided for the following custom_field pks <br>The following custom_field pk values are invalid for pk <br>The following custom_field pk values are required for pk <br> The value is not valid for custom_field pk </p>|
| 400  |booking-note-error | Unable to update booking note: `booking_note` |
| 400  |contact-error | Unable to create contact: `message`|
| 400  |content-type-invalid-error  | Invalid content-type|
| 400  |customer-custom-field-value-creation-error | Unable to create customer custom field value for customer custom_field pk %s: ensure a valid value is specified|
| 400  |customer-custom-field-values-invalid  |<p>Duplicate values provided for the following customer custom_field pks <br>The following customer custom_field pk values are invalid for pk <br>The following customer custom_field pk values are required for pk <br> The value is not valid for customer custom_field pk </p>|
| 400  |customer-type-rates-invalid | The following 'customer_type_rate' pk values are invalid for availability pk <availability_pk>: <customer_type_rate_pk> |
| 400  |invalid-checkin-already-checked-in | already checked in |
| 400  |invalid-checkin-customer | invalid customer|
| 400  |invalid-checkin-status-error  | invalid checkin status |
| 400  |invalid-qr-code-error  | invalid QR code |
| 400  |key-missing  | X-FareHarbor-API-App/X-FareHarbor-API-User header or api-app/api-user parameter is required |
| 400  |lodging-pk-invalid  | `pk` is not a valid lodging pk for company shortname|
| 400  |no-default-checkin-status-error  | no default checkin status|
| 400  |payment-error  | Unable to create payment: `message`|
| 400  |rebooking-uuid-invalid-error | `UUID` is not a valid UUID|
| 400  |resource-bookability-error | explicit_customer_count causes resources to be overused. Unable to satisfy resources. Please refresh the page and try again. |
| 400  |voucher-number-invalid  | Voucher number cannot be specified for non-affiliate bookings |
| 400  |voucher-number-not-specified | Unable to create booking: a voucher number is required|
| 403  |app-invalid | Invalid application |
| 403  |app-key-invalid  | API app key is invalid |
| 403  |invalid-checkin-permissions-error  | you do not have permissions to update checkin status|
| 403  |user-key-invalid  | API user key is invalid |
| 404  |availability-pk-invalid  | `pk` is not a valid availability pk for company shortname `shortname` |
| 404  |booking-uuid-invalid  | `UUID` is not a valid booking uuid for company shortname `shortname` |
| 404  |company-shortname-invalid  | `shortname` is not a valid company shortname |
| 404  |item-pk-invalid | <pk> is not a valid item pk for company shortname `shortname` |
| 429  |Too Many Requests | [You have sent too many requests in too short a time interval](getting-started.md#rate-limits) |


## Bookability error
| Message | Description |
| ------- | ------      |
| Auto-open time not reached  |Please contact api-support@fareharbor.com |
| Availability was removed | Availability no longer available |
| Call to book |Availability is not available for online or API booking |
| Closed | Availability is closed |
| Cutoff time reached |Availability is no longer bookable. Please contact the supplier or choose a different availability. |
| Full for all customer types| Availability is full |
| Full for customer type |Capacity is full for your selected customer type |
| Invalid customer type rate for availability |Please use a different customer_type_rate pk |
| Item is not available |Product is no longer offered for online or API booking |
| Item is private |Product is no longer offered for online or API booking |
| No bookings cutoff time reached |Availability is no longer bookable. |
| Over maximum for customer type |Your selected quantity exceeds the maximum set by the supplier |
| Party size is too large |Your selected quantity exceeds the maximum party size set by the supplier |
| Party size is too small |Your selected quantity does not meet the minimum party size set by the supplier |
| Resources are not available |Please contact api-support@fareharbor.com |
| Sorry, this date and time is not available. Please call us or choose a different date or time. Error: a-already-has-exclusive. |Please contact the supplier, or select a different availability. |
| Sorry, this date and time is not available. Please call us or choose a different date or time. Error: a-already-has-non-exclusive. |Please contact the supplier, or select a different availability. |
| The time you are trying to book is no longer available. Please call us or go back and choose a different time.|Availability is no longer bookable. Please contact the supplier or choose a different availability. |
| Under minimum for customer type |Your selected quantity does not meet the minimum set by the supplier |


## Booking creation error
| Message | Description |
| ------- | ------      |
| Affiliates cannot be changed while rebooking without first refunding all affiliate payments. |Please contact api-support@fareharbor.com |
| Availability is not bookable. |This time cannot be booked. Please try another availability. |
| Invalid order. |Please contact api-support@fareharbor.com |
| New bookings cannot be created for availabilities on archived items. |Product is no longer offered  |
| New bookings cannot be created for this contact until demo mode is disabled. |Please contact api-support@fareharbor.com |
| New bookings cannot be created for this contact until demo mode is enabled. |Please contact api-support@fareharbor.com |
| Non-test bookings cannot be rebooked because demo mode is enabled. |Please contact api-support@fareharbor.com |
| Please specify a voucher number. |Voucher field is required. |
| Please specify at least one customer. |Cannot create a booking for zero customers |
| Sorry, you are not an affiliate for this company. |Insufficient permission, please contact api-support@fareharbor.com |
| Sorry, you cannot add bookings to this contact for this company.|Please contact api-support@fareharbor.com |
| Sorry, you cannot rebook this booking to this company. |Insufficient permission, please contact api-support@fareharbor.com |
| Sorry, you cannot rebook while adding a booking to a customer. |Please contact api-support@fareharbor.com |
| Test bookings cannot be rebooked when demo mode is not enabled.|Please contact api-support@fareharbor.com |
| This booking has already been rebooked. |Cannot rebook a cancelled booking |
| Unable to add to order. |Please contact api-support@fareharbor.com |
| Unable to satisfy resources. |Insufficient inventory for supplier to operate the product for your selections |


## Booking cancellation error
| Message | Description |
| ------- | ------      |
| This booking has already been cancelled. | Cannot cancel a cancelled booking |
| You don't have permission to cancel this booking. | Insufficient permission, please contact api-support@fareharbor.com|
