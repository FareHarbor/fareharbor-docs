<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Overview](#overview)
    - [Custom Fields](#custom-fields)
    - [Custom Field Instances](#custom-field-instances)
    - [Custom Field Types](#custom-field-types)
    - [Customer and Booking Level Custom Fields](#customer-and-booking-level-custom-fields)
    - [Example](#example)
        - [Customer Level Custom Field](#customer-level-custom-field)
        - [Booking level Custom Field](#booking-level-custom-field)
        - [Booking Creation](#booking-creation)

<!-- markdown-toc end -->

# Overview

## Custom Fields

Custom fields allow an activity company to provide booking options and collect information from their customers during the booking process. For example, scuba companies often use custom fields to collect the height, weight, and shoe size of their customers during the booking process so they can set aside gear that fits properly for a dive.

## Custom Field Instances

A custom field instance represents an available booking option. Details regarding the booking option are specified by the custom field associated with the custom field instance.

## Custom Field Types

The API currently supports the following custom field types: `short`, `long`, `extended-option`, `yes-no` and `count`.  Values for `short` and `long` custom fields can be any string under 2048 characters.  Values for `extended-option` custom fields must be an `extended_option` pk defined in the `extended_options` property for the custom field.  Values for `yes-no` custom fields must be boolean. Values for `count` custom fields must be an integer.

## Customer and Booking Level Custom Fields

`custom_field_instances` under a `customer_type_rate` specify customer level custom fields (i.e. custom fields that are applicable to the `customer_type` specified by the `customer_type_rate`). `custom_field_instances` under an availability specify booking level custom fields (i.e. custom fields that are applicable to the entire booking).

## Example

Consider the following example availability response (the ellipses represent properties that have been left out for the sake of brevity):

    {
      "availabilities": [
        {
          "start_at": "2016-05-10T10:30:00-1000",
          "end_at": "2016-05-10T11:00:00-1000",
          "item": {
            "pk": 5000,
            "name": "Glider Rides"
          },
          "pk": 9999,
          "customer_type_rates": [
            {
              "pk": 555,
              "customer_type": {
                "pk": 1111,
                "plural": "Scenic Ride (1 passenger)",
                "singular": "Scenic Ride (1 passenger)"
              },
              "custom_field_instances": [
                {
                  "pk": 4321,
                  "custom_field": {
                    "pk": 1,
                    "type": "yes-no",
                    "name": "Add an extra 30 minutes of flight time?",
                    ...
                  },
                  ...
                },
                ...
              ],
              ...
            },
            ...
          ],
          "custom_field_instances": [
            {
              "pk": 1234,
              "custom_field": {
                "pk": 2,
                "type": "short",
                "name": "Hotel and Room Reservation Name",
                ...
              }
            },
            ...
          ],
          ...
        },
        ...
      ]
    }

### Customer Level Custom Field

The custom field in the above example with `pk` 1 is a customer level custom field. It is a `yes-no` type custom field, so it accepts true/false values.

### Booking level Custom Field

The custom field in the above example with `pk` 2 is a booking level custom field.  It is a `short` type custom field, so it accepts any string value (less than 2048 characters).

### Booking Creation

The example data below shows how one specifies custom field values for customer level custom fields (`pk` 1) and booking level custom fields (`pk` 2) when creating a booking.

    {
      "voucher_number": "123",
      "customers": [
        {
          "custom_field_values": [
            {
              "custom_field": 1,
              "value": true
            }
          ],
          "customer_type_rate": 555
        }
      ],
      "contact": {
        "phone": "+1-123-456-7890",
        "name": "John Doe",
        "email": "johndoe@example.com"
      },
      "custom_field_values": [
        {
          "custom_field": 2,
          "value": "Hawaiian Village Waikiki Beach Resort Room 415"
        }
      ]
    }
