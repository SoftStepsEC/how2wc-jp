---
title: General settings
url: https://woocommerce.com/document/configuring-woocommerce-settings/general/
---

From your store’s general settings page, you can enter your business address, define the regions you will sell and ship orders to, enable tax calculations and coupons, and select the currency your shop will use for sales.

You can access and edit general settings via your WP Admin dashboard by navigating to *WooCommerce > Settings*. The **General** tab will be open by default, displaying the following sections:

- [Store address](https://woocommerce.com/document/configuring-woocommerce-settings/general/#store-address)
- [General options](https://woocommerce.com/document/configuring-woocommerce-settings/general/#general-options)
- [Currency options](https://woocommerce.com/document/configuring-woocommerce-settings/general/#currency-options)

Below, you’ll find explanations of the options for each.

This is where you set your business’s physical address — the location where you are based as a seller. Many tax and shipping configurations use this address for determining rates.

- Selling location(s) : Specify whether you’d like to sell to:
  - All countries
  - All countries, except for…
  - Specific countries
  
- **Shipping location(s)**: Choose to ship to only the countries you sell to or a subset of countries. You can also disable shipping and all shipping-related functionality.
- Default customer location : Choose how to determine a customer’s default location. This is used help calculate default tax and shipping rates.   Options include:
  - **Shop country/region**: This tells the system to assume customers are in the same location as your shop.
  - **No location by default**: Taxes and shipping aren’t calculated until a customer enters their address.
  - **Geolocate**: Uses [MaxMind Geolocation](https://woocommerce.com/document/maxmind-geolocation-integration/) to verify the customer’s current location and calculates taxes and shipping accordingly.
  - **Geolocate (with page caching support)**: The same as above, but using AJAX geolocation. When this option is selected, you may notice characters similar to `?v=xxxxx` appended to your website URLs. This is normal and prevents static caching of prices.
  
- **Enable taxes**: Enable or disable taxes on your store. Disabling taxes hides the [Tax settings page](https://woocommerce.com/document/configuring-woocommerce-settings/#tax).
- Enable coupons : Enable or disable coupons in your store. Coupons are applied from the admin edit order screen (for unpaid orders), cart, and checkout pages.
  - **Enable the use of coupon codes**: Select this option to enable coupon usage in your store. When coupons are enabled, you’ll see the option below concerning how discounts should be calculated.
  - **Calculate coupon discounts sequentially**: Changes the coupon calculation logic to apply coupons in sequence on top of one another, rather than basing them on the original product prices.
  

Currency options determine how prices are displayed in your store for customers; you’ll find a brief overview of the settings below. [Learn more about shop currency settings](https://woocommerce.com/document/shop-currency/).

- **Currency**: Sets your store’s default currency. Only**one currency** may be selected.
- Currency position : Choose the default position of the currency symbol for prices:
  - Left
  - Right
  - Left with space
  - Right with space
  
- Thousand separator : Choose which symbol to use for the thousand separator:
  - Comma (`,`) — this is the default option.
  - Period/full stop (`.`)
  
- Decimal separator : Similar to the option above, choose which symbol to use for the decimal separator:
  - Period/full stop (`.`) — this is the default option.
  - Comma (`,`)
  
- **Number of decimals**: Specify how many numbers to display to the right of the decimal separator when displaying prices (e.g. 100.00 or 100).

Be sure to click the **Save changes** button before leaving the general settings page.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

