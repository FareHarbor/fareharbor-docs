# Authentication

An app key and a user key are required to authenticate all requests to
the FareHarbor external API.  The app key identifies your application,
and can be used for all of your affiliates. The user key identifies a specific
user on a specific affiliate.

These keys are in UUID format. Note that these keys *must* be kept private. 
If your key is disclosed publicly please contact support@fareharbor.com to have it rotated.

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

You can - but *we recommend you do not* -- send your keys as the query parameters, passing your app key via
`api-app` and your user key via `api-user`:

```
    GET /api/external/v1/companies/?api-app=APP-KEY&api-user=USER-KEY HTTP/1.1
    Host: fareharbor.com

    $ curl https://fareharbor.com/api/external/v1/companies/?api-app=APP-KEY&api-user=USER-KEY
```

This is a permitted usage pattern but not a recommended one - in particular you must not use this as part of a browser based interaction, since keys can end up persisting in browser histories, logs, and other less secure locations. 

## Requesting Keys

Please contact <support@fareharbor.com> to request API keys.
