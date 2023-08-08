<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Interchange Format](#interchange-format)
- [Requests](#requests)
    - [Request Body](#request-body)
    - [Authentication](#authentication)
- [Responses](#responses)
    - [General Structure](#general-structure)
        - [Success responses](#success-responses)
        - [Error responses](#error-responses)
    - [HTTP Codes](#http-codes)

<!-- markdown-toc end -->

# Interchange Format

All interactions with the API are done via JSON.

# Requests

## Request Body

Some requests (particularly the `POST` to create a booking) require a body.
The body should consist entirely of a JSON object.

## Authentication

You'll need to authenticate every request you make the API; see [`authentication.md`](external-api/authentication.md).

# Responses

## General Structure

The body of every response is a valid JSON object (and in particular *not* a JSON array,
number, string, and so on).

### Success responses

Successful responses contain the data requested.  The structure of these responses is described in detail
in [`data-types.md`](data-types.md); however in general they follow this structure:

* `<singular type>`: `object`

or

* `<plural type>`: `array`

Examples:

```
    {
      "company": {
        "shortname": "hawaiianadventures",
        "name": "Hawaiian Adventures"
      }
    }
```

```
    {
      "companies": [
        {
          "shortname": "hawaiianadventures",
          "name": "Hawaiian Adventures"
        }
      ]
    }
```

### Error responses

* `error`: `string`

A message describing the error.

* `status`: `number`

The HTTP status code for the response.

Example:

    {
      "error": "Method not allowed",
      "status": 405
    }

Assuming that `response` contains the entire JSON response, a response is an error when `response.error`
is defined; otherwise it is a success.

## HTTP Codes

We use the usual HTTP statuses to indicate success:

* 200: Succcess

* 201: Created

A `2xx` response is always indicative of a successful request.

We also use HTTP error codes to indicate the usual sorts of errors; the following
are the ones you are most likely to encounter.

* 400: Bad Request

  The request was invalid and could not be processed.

  This is most likely to occur when attempting to create a booking,
  and can correspond to things like attempting to overbook an availability
  or providing invalid data like customer name, phone number, etc.

* 403: Forbidden

  You do not have permission to access this endpoint in this way.

  Review [`authentication.md`](external-api/authentication.md) and verify that you are sending the
  correct API keys, and that you do indeed have permission to access to
  endpoint you are attempting to access.

* 404: Not Found

  The company, item, or availability does not exist; it may have been
  deleted or otherwise become unavailable, or you may have an incorrect ID.

* 405: Method Not Allowed

  You are trying to use an unsupported HTTP method (`GET`, `POST`, and so on)
  with this endpoint.

* 420: Enhance Your Calm

  Returned when a request has been rate-limited due to too many concurrent
  connections. It is *very* unlikely that you will encounter this in normal
  usage.

* 500: Internal Server Error

  An unexpected error occured.

* 503: Service Unavailable

  FareHarbor is temporarily unavailable, but will return shortly. Try again later.

A `4xx` request is always indicative of an problem with the request being made,
while a `5xx` error indicates a server-side error.

A detailed list of error codes and messages are described in [`error-codes.md`](error-codes.md)
