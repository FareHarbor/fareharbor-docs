# Authentication

An app key and a user key are required to authenicate requests all requests to
the FareHarbor external API.  The app key identifies your application,
and can be used for all of your affiliates. The user key identifies a specific
user on a specific affiliate.

These keys are UUIDs. Note that these keys *must* be kept private.

## Keys sent as headers (recommended)

The recommended approach to passing your keys is via the custom headers
`X-FareHarbor-API-App` and `X-FareHarbor-API-User`.

```
    GET /api/external/v1/companies/ HTTP/1.1
    Host: fareharbor.com
    X-FareHarbor-API-App: APP-KEY
    X-FareHarbor-API-User: USER-KEY

    $ curl -H "X-FareHarbor-API-App: APP-KEY" -H "X-FareHarbor-API-User: USER-KEY" https://fareharbor.com/api/external/v1/companies/
```

## Keys sent as parameters

You can also send your keys as the query parameters, passing your app key via
`api-app` and your user key via `api-user`:

```
    GET /api/external/v1/companies/?api-app=APP-KEY&api-user=USER-KEY HTTP/1.1
    Host: fareharbor.com

    $ curl https://fareharbor.com/api/external/v1/companies/?api-app=APP-KEY&api-user=USER-KEY
```

This should only be used in server to server scenarios.

## Requesting Keys

Please contact <support@fareharbor.com> to request API keys.
