---
title: Testing orders
url: https://woocommerce.com/document/managing-orders/testing-orders/
---

Creating test orders is an effective way to evaluate a new payment method, review your checkout process, and assess other order-related integrations. They can also be useful for troubleshooting issues.

Like regular orders, test orders can trigger order emails and appear in WooCommerce analytics, among others.

Many payment gateways offer a sandbox or testing mode that allows you to process test payments without incurring any fees or charges. We recommend activating this mode when testing your orders and checkout.

There is currently **no visual difference or special status** for test orders. As a result, other WooCommerce extensions, plugins, or services may be unable to differentiate between these test orders and your real orders.

Be sure to review the documentation for each extension, plugin, or integration to understand how they handle test scenarios. Depending on your requirements, you may want to disable specific integrations before placing any test orders. Once you are finished, delete and remove these test orders to prevent these orders from being inadvertently handled, shipped, or appearing in your store’s analytics, etc.

**Tip:** Use a third-party plugin such as [Disable Emails](https://wordpress.org/plugins/disable-emails/) to prevent emails from being sent for test orders. This plugin may not prevent emails from being sent via an [SMTP provider](https://woocommerce.com/document/email-smtp-providers/#dedicated-smtp-provider), however.

**Important:** To avoid unintended complications with test payments on your live site, perform testing exclusively on a [staging site](https://woocommerce.com/posts/what-is-staging-site-wordpress-how-to-set-one-up/).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

