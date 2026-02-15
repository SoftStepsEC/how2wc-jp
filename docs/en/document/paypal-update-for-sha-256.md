---
title: Paypal Update for SHA-256
url: https://woocommerce.com/document/paypal-update-for-sha-256/
---

This document is for anyone who has received an email from PayPal with the subject : IMMEDIATE ATTENTION REQUIRED: PayPal service upgrades

PayPal is upgrading the certificate for www.paypal.com to SHA-256. This endpoint is also used by merchants using the Instant Payment Notification (IPN) product.

The WooCommerce PayPal Standard Gateway itself requires no changes. You should however check that your hosting provider supports the new certificates.

In the event that your host does not support SHA-256, customers will still be able to make payments, but the PayPal IPN will not be able to update orders from ‘pending’ to ‘processing’ without manual intervention.

The PayPal Sandbox has already been updated to SHA-256. You can test your own site by placing an order using the PayPal Sandbox or you can use [this tool](https://gist.github.com/mikejolley/0941e0882efcad64ea40) which will confirm if PayPal IPN will continue to work on your site after PayPal makes the change on the Live environment.

To use the tool just click the “Download ZIP” button in the bottom right corner

and install as you would any other plugin. Once installed just click the link

and you will see either a Success or a Fail message

If the check fails you will need to contact your host about this, this is not a WooCommerce or WordPress issue.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

