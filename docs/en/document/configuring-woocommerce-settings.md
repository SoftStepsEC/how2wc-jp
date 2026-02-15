---
title: Configuring WooCommerce settings
url: https://woocommerce.com/document/configuring-woocommerce-settings/
---

When you go to **WooCommerce > Settings** in your site’s WP Admin dashboard, you’ll notice tabs relating to the different kinds of settings available:

- [General](https://woocommerce.com/document/configuring-woocommerce-settings/#general)
- [Products](https://woocommerce.com/document/configuring-woocommerce-settings/#products)
- [Tax](https://woocommerce.com/document/configuring-woocommerce-settings/#tax)
- [Shipping](https://woocommerce.com/document/configuring-woocommerce-settings/#shipping)
- [Payments](https://woocommerce.com/document/configuring-woocommerce-settings/#payments)
- [Accounts & Privacy](https://woocommerce.com/document/configuring-woocommerce-settings/#accounts-and-privacy)
- [Emails](https://woocommerce.com/document/configuring-woocommerce-settings/#emails)
- [Integration](https://woocommerce.com/document/configuring-woocommerce-settings/#integration)
- [Site visibility](https://woocommerce.com/document/configuring-woocommerce-settings/#site-visibility)
- [Advanced](https://woocommerce.com/document/configuring-woocommerce-settings/#advanced)

**Note:**

WooCommerce is highly extensible, open-source software. Extensions and plugins commonly add additional settings and tabs to the WooCommerce settings page(s). If you see additional settings to those pictured below or mentioned in the following pages, they have most likely been added by an extension/plugin, your theme, or custom code.

You’ll find your store’s general settings in WP Admin at **WooCommerce > Settings > General**.

These settings include your store’s location, where you’ll sell and ship orders, what to use as the default customer location, enabling or disabling taxes and coupons, and your store’s currency options.

For more details, see [General settings](https://woocommerce.com/document/configuring-woocommerce-settings/general/).

Find and edit product settings in WP Admin at **WooCommerce > Settings > Products**.

These settings determine which page is set as your main shop page, which units of measurement to use for product dimensions, product review settings, inventory management, stock notifications, how downloadable products are handled, and more.

For more details, see [Products settings](https://woocommerce.com/document/configuring-woocommerce-settings/products/).

**Note:**

Taxes must be enabled in **WP Admin > WooCommerce > Settings > General** for the **Tax** settings link to appear.

Find and edit tax settings in WP Admin at **WooCommerce > Settings > Tax**.

WooCommerce’s built-in tax settings let you choose how taxes are displayed and calculated in your shop. You can also add tax rates for specific areas, and add tax classes with different rates to be used for certain products or shipping costs.

For more details, see [WooCommerce tax settings](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/).

Find and edit shipping settings in WP Admin at **WooCommerce > Settings > Shipping**.

WooCommerce has several built-in shipping settings and methods that cover a wide range of use cases:

The main shipping settings screen is for **shipping zones**. Think of a shipping zone as a geographic region where a certain set of shipping methods and their rates will apply.

Learn more at [Setting up shipping zones](https://woocommerce.com/document/setting-up-shipping-zones/).

The **shipping settings** page contains the following settings:

- Calculations
  - Enable the shipping calculator on the cart page
  - Hide shipping costs until an address is entered
  - Hide shipping rates when free shipping is available
  
- Shipping destination
  - Ship to a customer’s billing or shipping address by default, or only ship to the user’s billing address.
  
- Debug mode
  - Enabling debug mode will display the customer’s matched shipping zone in a notice on the site’s front-end (see image below), and bypass the shipping rate cache. Enable for troubleshooting purposes.
  

Shipping classes can be used to enable shipping methods to provide different rates for different classes or types of products.

Learn more about [product shipping classes](https://woocommerce.com/document/product-shipping-classes/).

Local pickup allows the customer to pick up an order themselves — no shipping required. There are currently two ways to implement local pickup in the free, core WooCommerce plugin:

- A modern, streamlined experience that is natively integrated with the block version of the checkout flow. Learn more at[WooCommerce Blocks: Local pickup](https://woocommerce.com/document/woocommerce-blocks-local-pickup/).
- A legacy version that can be added to shipping zones as a WooCommerce core shipping method. This will work on either the shortcode or block version of the checkout. Learn more at[Legacy Shipping Method: Local Pickup](https://woocommerce.com/document/local-pickup/).

We recommend using only one method for local pickup to avoid confusion.

In WP Admin, navigate to **WooCommerce > Settings > Payments** to specify which payment gateways are enabled and configure their settings.

Use the **Enabled** toggle to turn a gateway on or off:

If you try to enable a payment method that needs additional configuration, you’ll be redirected to the setup screen for that payment method.

Clicking the **name of the payment gateway** will take you to a screen to set up or adjust its settings. Another way to configure its settings is to click the **Set up** or **Manage** button for that particular payment gateway.

Installed gateways are listed in the table and can be **dragged and dropped** to control the order in which they display to customers on the checkout.

See the following pages for more payment gateway information:

- [Premium payment gateway options](https://woocommerce.com/document/premium-payment-gateway-extensions/)
- [Free payment gateways included in WooCommerce](https://woocommerce.com/documentation/plugins/woocommerce/getting-started/sell-products/core-payment-options/https://woocommerce.com/documentation/woocommerce/getting-started/sell-products/core-payment-options/)

Find accounts and privacy settings in WP Admin at **WooCommerce > Settings > Accounts & Privacy**.

Here, you can enable or disable guest checkout, control customer account creation, control how personal data is retained or removed from your shop, and set your privacy policy notices.

For more details, see [Accounts & Privacy settings](https://woocommerce.com/document/configuring-woocommerce-settings/accounts-and-privacy/).

Find email settings in WP Admin at **WooCommerce > Settings > Emails**.

You can edit design elements of your store’s email template, change your store’s sending address, and configure your settings for (or disable) each email WooCommerce sends.

For more details, see [Email settings](https://woocommerce.com/document/configuring-woocommerce-settings/emails/).

Find integration settings in WP Admin at **WooCommerce > Settings > Integration**.

This is where you enter your license key for the [MaxMind geolocation integration](https://woocommerce.com/document/maxmind-geolocation-integration/). Extensions, plugins, themes, and other integrations may also add settings to this tab.

From the site visibility settings, you’ll be able to enable **Coming soon** **mode** and share your under-construction store via a private link.

Learn more about [Coming soon mode](https://woocommerce.com/document/configuring-woocommerce-settings/coming-soon-mode/).

Find advanced settings in WP Admin at **WooCommerce > Settings > Advanced**.

Advanced settings allow you to set WooCommerce pages, integrate external applications with the REST API, add custom webhooks to your store, and enable new or experimental features like High-Performance Order Storage (HPOS) and the new product editor.

For more details, see [Advanced settings](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

