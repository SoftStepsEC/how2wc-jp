---
title: WooCommerce REST API
url: https://woocommerce.com/document/woocommerce-rest-api/
---

The WooCommerce REST API is a powerful tool for connecting your WooCommerce shop to external systems and resources. Unless you’re a developer, in most cases the integration you’re working with will only require you to generate API keys for you to enter in their system, and you’ll be connected to the external service!

This document covers the basics of using the REST API from a merchant perspective. With links to developer documentation for more advanced topics.

**Note**:

You can find the [technical documentation](https://woocommerce.github.io/woocommerce-rest-api-docs/) for the REST API on GitHub.

WordPress permalinks must be set to something that is easily human-readable at: **Settings > Permalinks**.

**Day and name** is a great default, but anything aside from **Plain** should work

The WooCommerce REST API works on a key system to control access. These keys are linked to a user on your site.

To create or manage keys for a specific WordPress user:

1. Go to: **WooCommerce > Settings > Advanced > REST API**.
2. Select **Create an API key** OR**Add Key**. You’ll be taken to the **Key Details** screen.
3. Add a **Description**.
4. Select the **User** you would like to generate a key for in the dropdown.
5. Select a level of access for this API key:
  - **Read** access,
  - **Write** access, or;
  - **Read/Write** access.
  
6. Select **Generate API Key**, and WooCommerce creates API keys for that user.
7. Now that keys have been generated, you should see **Consumer Key** and **Consumer Secret**keys, a **QR****Code**, and a “**Revoke Key**” link in red text.
8. The **Consumer Key** and **Consumer Secret** may be entered in the application you’ll be connecting to using the WooCommerce REST API. The app may also request your site’s URL.

The legacy REST API is deprecated and has been removed from WooCommerce. We’ve now integrated WooCommerce directly with the WordPress REST API. If you do still need to use the Legacy REST API for an integration your site needs, you need to install the [WooCommerce Legacy REST API](https://developer.woocommerce.com/2024/01/17/the-woocommerce-legacy-rest-api-extension-is-now-available-in-wordpress-org/) plugin.

This also means that webhooks configured to use the Legacy REST API will also stop working unless the dedicated extension is installed.

With the Legacy REST API plugin installed and activated, you can then enable the legacy REST API under **WooCommerce > Settings > Advanced** >**Legacy API** and select the **Enable the legacy REST API** checkbox.

From here, use our developer doc instructions on how to test the REST API on your site to confirm it’s working. The [make a basic request section](https://developer.woocommerce.com/docs/apis/rest-api/#make-a-basic-request) outlines how to request orders from your site.

You can also find the complete REST API documentation at: [WooCommerce REST API Docs](https://woocommerce.github.io/woocommerce-rest-api-docs/).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

