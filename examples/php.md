<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Setup](#setup)
    - [Dependencies](#dependencies)
    - [Request headers](#request-headers)
    - [Root URL](#root-url)
- [Listing companies](#listing-companies)
- [Listing items for a company](#listing-items-for-a-company)
- [Listing availabilities for an item](#listing-availabilities-for-an-item)
- [Listing customer type rates for an availability](#listing-customer-type-rates-for-an-availability)
- [Creating a booking for an availability](#creating-a-booking-for-an-availability)
- [Retrieving a booking](#retrieving-a-booking)
- [Entire script](#entire-script)

<!-- markdown-toc end -->

# Setup

## Dependencies

Httpful PHP library. See the [installation instructions](http://phphttpclient.com/) for more information. 

    include("./httpful.phar");

## Request headers

    $api_app = "your app key";
    $api_user = "your user key";

## Root URL

    $root_url = "https://test.fareharbor.com/api/external/v1";

# Listing companies

    $companies_url = "$root_url/companies/";

    $response = \Httpful\Request::get($companies_url)
        ->addHeader("X-FareHarbor-API-App", $api_app)
        ->addHeader("X-FareHarbor-API-User", $api_user)
        ->send();

    $companies = $response->body->companies;

    echo "<h1>Companies</h1>";
    echo "<h2>$companies_url</h2>";
    echo "<ul>";
    foreach ($companies as $company) {
        echo "<li>";
        echo $company->shortname;
        echo "</li>";
    }
    echo "</ul>";

# Listing items for a company

    $company = array_values($companies)[0];

    $items_url = "$root_url/companies/$company->shortname/items/";

    $response = \Httpful\Request::get($items_url)
        ->addHeader("X-FareHarbor-API-App", $api_app)
        ->addHeader("X-FareHarbor-API-User", $api_user)
        ->send();

    $items = $response->body->items;

    echo "<h1>Items</h1>";
    echo "<h2>$items_url</h2>";
    echo "<ul>";
    foreach ($items as $item) {
        echo "<li>";
        echo "$item->pk ($item->name)";
        echo "</li>";
    }
    echo "</ul>";

# Listing availabilities for an item

    $item = array_values($items)[0];

    $availabilities_url = "$root_url/companies/$company->shortname/items/$item->pk/availabilities/date/2015-12-01/";

    $response = \Httpful\Request::get($availabilities_url)
        ->addHeader("X-FareHarbor-API-App", $api_app)
        ->addHeader("X-FareHarbor-API-User", $api_user)
        ->send();

    $availabilities = $response->body->availabilities;

    echo "<h1>Availabilities</h1>";
    echo "<h2>$availabilities_url</h2>";
    echo "<ul>";
    foreach ($availabilities as $availability) {
        echo "<li>";
        echo "$availability->pk ($availability->start_at)";
        echo "</li>";
    }
    echo "</ul>";

# Listing customer type rates for an availability

    $availability = array_values($availabilities)[0];
    $customer_type_rates = $availability->customer_type_rates;

    echo "<h1>Customer Type Rates</h1>";
    echo "<h2>Availability $availability->pk</h2>";
    echo "<ul>";
    foreach ($customer_type_rates as $customer_type_rate) {
        echo "<li>";
        echo "$customer_type_rate->pk ({$customer_type_rate->customer_type->plural})";
        echo "</li>";
    }
    echo "</ul>";

# Creating a booking for an availability

    $customer_type_rate = array_values($customer_type_rates)[0];

    $book_url = "$root_url/companies/$company->shortname/availabilities/$availability->pk/bookings/";

    $contact = array(
        "name" => "John Doe",
        "phone" => "415-098-1234",
        "email" => "johndoe@gmail.com"
    );

    $customers = array(
        array("customer_type_rate" => $customer_type_rate->pk)
    );

    $data = array(
        "contact" => $contact,
        "customers" => $customers,
        "note" => "Optional booking note.",
        "voucher_number" => "V-35791209"
    );

    $body = json_encode($data);

    $response = \Httpful\Request::post($book_url)
        ->addHeader("X-FareHarbor-API-App", $api_app)
        ->addHeader("X-FareHarbor-API-User", $api_user)
        ->sendsJson()
        ->body($body)
        ->send();

    $booking = $response->body->booking;

    echo "<h1>Create Booking</h1>";
    echo "<h2>$book_url</h2>";
    echo "Created booking $booking->uuid";

# Retrieving a booking

    $booking_url = "$root_url/companies/$company->shortname/bookings/$booking->uuid/";

    $response = \Httpful\Request::get($booking_url)
        ->addHeader("X-FareHarbor-API-App", $api_app)
        ->addHeader("X-FareHarbor-API-User", $api_user)
        ->send();

    $booking = $response->body->booking;

    echo "<h1>Retrieve Booking</h1>";
    echo "<h2>$booking_url</h2>";
    echo "Retrieved booking $booking->uuid";

# Entire script

    <?php
    include("./httpful.phar");

    $api_app = "your app key";
    $api_user = "your user key";

    $root_url = "https://test.fareharbor.com/api/external/v1";

    # COMPANIES

    $companies_url = "$root_url/companies/";

    $response = \Httpful\Request::get($companies_url)
        ->addHeader("X-FareHarbor-API-App", $api_app)
        ->addHeader("X-FareHarbor-API-User", $api_user)
        ->send();

    $companies = $response->body->companies;

    echo "<h1>Companies</h1>";
    echo "<h2>$companies_url</h2>";
    echo "<ul>";
    foreach ($companies as $company) {
        echo "<li>";
        echo $company->shortname;
        echo "</li>";
    }
    echo "</ul>";

    # ITEMS

    $company = array_values($companies)[0];

    $items_url = "$root_url/companies/$company->shortname/items/";

    $response = \Httpful\Request::get($items_url)
        ->addHeader("X-FareHarbor-API-App", $api_app)
        ->addHeader("X-FareHarbor-API-User", $api_user)
        ->send();

    $items = $response->body->items;

    echo "<h1>Items</h1>";
    echo "<h2>$items_url</h2>";
    echo "<ul>";
    foreach ($items as $item) {
        echo "<li>";
        echo "$item->pk ($item->name)";
        echo "</li>";
    }
    echo "</ul>";

    # AVAILABILITIES

    $item = array_values($items)[0];

    $availabilities_url = "$root_url/companies/$company->shortname/items/$item->pk/availabilities/date/2015-12-01/";

    $response = \Httpful\Request::get($availabilities_url)
        ->addHeader("X-FareHarbor-API-App", $api_app)
        ->addHeader("X-FareHarbor-API-User", $api_user)
        ->send();

    $availabilities = $response->body->availabilities;

    echo "<h1>Availabilities</h1>";
    echo "<h2>$availabilities_url</h2>";
    echo "<ul>";
    foreach ($availabilities as $availability) {
        echo "<li>";
        echo "$availability->pk ($availability->start_at)";
        echo "</li>";
    }
    echo "</ul>";

    # CUSTOMER TYPE RATES

    $availability = array_values($availabilities)[0];
    $customer_type_rates = $availability->customer_type_rates;

    echo "<h1>Customer Type Rates</h1>";
    echo "<h2>Availability $availability->pk</h2>";
    echo "<ul>";
    foreach ($customer_type_rates as $customer_type_rate) {
        echo "<li>";
        echo "$customer_type_rate->pk ({$customer_type_rate->customer_type->plural})";
        echo "</li>";
    }
    echo "</ul>";

    # CREATE BOOKING

    $customer_type_rate = array_values($customer_type_rates)[0];

    $book_url = "$root_url/companies/$company->shortname/availabilities/$availability->pk/bookings/";

    $contact = array(
        "name" => "John Doe",
        "phone" => "415-098-1234",
        "email" => "johndoe@gmail.com"
    );

    $customers = array(
        array("customer_type_rate" => $customer_type_rate->pk)
    );

    $data = array(
        "contact" => $contact,
        "customers" => $customers,
        "voucher_number" => "V-35791209"
    );

    $body = json_encode($data);

    $response = \Httpful\Request::post($book_url)
        ->addHeader("X-FareHarbor-API-App", $api_app)
        ->addHeader("X-FareHarbor-API-User", $api_user)
        ->sendsJson()
        ->body($body)
        ->send();

    $booking = $response->body->booking;

    echo "<h1>Create Booking</h1>";
    echo "<h2>$book_url</h2>";
    echo "Created booking $booking->uuid";

    # RETRIEVE BOOKING

    $booking_url = "$root_url/companies/$company->shortname/bookings/$booking->uuid/";

    $response = \Httpful\Request::get($booking_url)
        ->addHeader("X-FareHarbor-API-App", $api_app)
        ->addHeader("X-FareHarbor-API-User", $api_user)
        ->send();

    $booking = $response->body->booking;

    echo "<h1>Retrieve Booking</h1>";
    echo "<h2>$booking_url</h2>";
    echo "Retrieved booking $booking->uuid";
    ?>
