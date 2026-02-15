---
title: Advanced Settings
url: https://woocommerce.com/document/configuring-woocommerce-settings/advanced/
---

The “Advanced” settings area is where you set WooCommerce pages like the cart and checkout, create access tokens to integrate external applications with the REST API, add custom webhooks to your store, and enable new or experimental features like high performance order storage and the new product editor. Find them at: **WooCommerce > Settings > Advanced**.

The different sections of Advanced settings can accessed via the submenu:

- [Page setup](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#page-setup)
- [REST API](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#rest-api)
- [Webhooks](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#webhooks)
- [Legacy API](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#legacy-api)
- [WooCommerce.com](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#woocommerce-com)
- [Features](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#features)

Pages need to be set so WooCommerce knows where to send users to perform certain actions:

- **Cart Page**– This page shows items in your customers cart.
- **Checkout Page** – This page is where your customer will enter their payment information and submit orders.
- **My Account page**– This page is where registered customers will go to view their orders or update their account details.
- **Terms and Conditions**– This page shows terms and conditions.

On sites that aren’t served via HTTPS, the page setup area also shows the **Force Secure Checkout** setting. See more details about that setting in our [SSL and HTTPS documentation](https://woocommerce.com/document/ssl-and-https/#woocommerce-force-ssl-setting)

You don’t need to use the exact pages WooCommerce created when it was installed, but you must have a page set for the Cart and Checkout pages. Otherwise your customers cannot buy and pay for your products. These pages are normally created and set when installing/setting up WooCommerce. See. [WooCommerce Pages](https://woocommerce.com/document/woocommerce-pages/) for more details.

#### Terms and conditions

To use a**Terms and Conditions** page, create a new page for it at **Pages > Add New**, then select the page in the dropdown.

When using the `[woocommerce_checkout]` [shortcode](https://woocommerce.com/document/woocommerce-shortcodes/page-shortcodes/#checkout) the Terms and Conditions appear inline during checkout. They are expanded and displayed when the customer clicks the “Terms & Conditions” link. Then the customer can scroll through content and tick the checkbox to accept.

On the [Block version of the Checkout](https://woocommerce.com/checkout-blocks/), shoppers will see a message saying: “By proceeding with your purchase you agree to our **Terms and Conditions** and **Privacy Policy**” with links to the respective pages if they’ve been set. You can edit this message to fit your needs in the block editor.

#### Checkout Endpoints

Endpoints are an extra part in the website URL that WooCommerce uses to show different content when it detects them.

The checkout endpoints are appended to page URLs to handle specific actions during the checkout and order payment process. They should be unique, and are generally don’t need to be modified unless you have a specific reason. The checkout endpoints are as follows:

- Pay
- Order Received
- Add Payment Method
- Delete Payment Method
- Set Default Payment Method

Learn more about [WooCommerce endpoints](https://developer.woocommerce.com/docs/woocommerce-endpoints/) in our developer documentation.

#### My Account Endpoints

These endpoints handle specific actions on the accounts pages. They should be unique, and generally shouldn’t need to be modified unless you have a specific reason. The “my account” endpoints are as follows:

- Orders
- View Order
- Downloads
- Edit Account
- Addresses
- Payment Methods
- Lost Password
- Logout

Learn more about [WooCommerce endpoints](https://developer.woocommerce.com/docs/woocommerce-endpoints/) in our developer documentation.

These settings are at: **WooCommerce > Settings > Advanced > REST API**.

In the REST API settings you can create API keys to connect to your store via the WooCommerce REST API. More info at: [Generate API Keys](https://woocommerce.com/document/woocommerce-rest-api/#generate-api-keys).

The REST API is generally for developers to use. Though in some cases a service may ask you to create API keys so they can connect to your store. The REST API enables access to store data from outside WordPress, so create and use keys with caution. Learn more at: [WooCommerce REST API.](https://woocommerce.com/document/woocommerce-rest-api/)

A Webhook is an event notification sent to a URL of your choice. They can be used to integrate with third-party services that support them. Learn more in our developer documentation at: [Working with Webhooks in WooCommerc](https://developer.woocommerce.com/docs/working-with-webhooks-in-woocommerce/)e

Enable the Legacy REST API which is no longer maintained and [will be removed in WooCommerce 9.0](https://developer.woocommerce.com/2023/10/03/the-legacy-rest-api-will-move-to-a-dedicated-extension-in-woocommerce-9-0/), which is scheduled for release on June 11, 2024. If you need to use the Legacy REST API please see [this post on our developer blog](https://developer.woocommerce.com/2024/05/14/goodbye-legacy-rest-api/) for details.

In the WooCommerce.com section you can enable WooCommerce [usage tracking](https://woocommerce.com/usage-tracking/) so we can make WooCommerce even better. There’s also a setting to display contextual suggestions for official extensions that may be helpful to your store.

These settings are at: **WooCommerce > Settings > Advanced > Features**. You can enable stable and experimental WooCommerce features here.

- **Order Data Storage** – Choose which order data storage method to use. More details in our documentation about [High Performance Order Storage](https://woocommerce.com/document/high-performance-order-storage/).
- **Analytics** – Enable or disable [WooCommerce Analytics](https://woocommerce.com/document/woocommerce-analytics/)
- **Order Attribution** – Enable or disable [Order Attribution Tracking](https://woocommerce.com/document/order-attribution-tracking/)

#### Experimental Features

Features here are either experimental or incomplete, enable them at your own risk!

- **New Product Editor** (Beta) – Enable or disable the [New Product Editor (Beta)](https://woocommerce.com/document/new-product-editor-beta/)

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

