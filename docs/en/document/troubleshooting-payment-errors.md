---
title: Troubleshoot payment errors
url: https://woocommerce.com/document/troubleshooting-payment-errors/
---

Troubleshooting payment errors can depend on the payment gateway you are using and how it is set up or might be specific to your site or customer.

WooCommerce comes with a number of [built-in payment options](https://href.li/?https://docs.woocommerce.com/documentation/plugins/woocommerce/getting-started/sell-products/core-payment-options/) and you can also see the [payment gateways available in the WooCommerce.com Marketplace](https://href.li/?https://woocommerce.com/product-category/woocommerce-extensions/payment-gateways/).

When encountering errors, these general guidelines can help:

- **400 Errors**: These usually happen because the contact URL is incorrect.
- **200 Errors**: These often result from incorrect credentials.
- **Blank Page Errors**: Often indicate a PHP issue. Enable debugging to find the root cause. [Learn how to debug WordPress](https://wordpress.org/support/article/debugging-in-wordpress/).

If you would like to set up a separate test environment for your WooCommerce site to troubleshoot payment errors, we [recommend setting up a staging site](https://woocommerce.com/posts/what-is-staging-site-wordpress-how-to-set-one-up/).

Many payment gateways also offer a test or sandbox mode for testing their functionality. Refer to your payment gateway’s documentation for the exact steps for activating this.

Order statuses indicate where an order stands in the payment and fulfilment process. Here’s a breakdown:

- **On Hold**: Payment is awaiting confirmation (e.g., for manual payment methods like bank transfer or cheque). For gateways set to authorize (instead of capture), this status requires manual action.
- **Pending**: The order was received but remains unpaid. This often points to issues with notification URLs or plugin conflicts.
- **Processing**: Payment has been received, and the order is awaiting shipment. This status typically applies to physical goods.
- **Completed**: The order has been fulfilled successfully.
- **Failed**: Payment was unsuccessful or declined. Common reasons include expired payment windows or abandoned orders. Refer to the order notes for any specific error information.

For detailed information on managing orders, visit [Managing Orders](https://href.li/?https://docs.woocommerce.com/document/managing-orders/).

Order notes provide a summary of what happened during a transaction. To dive deeper, enable transaction logging for your payment plugin:

1. Go to **WooCommerce > Settings > Payments > [Your Plugin]**.
2. Enable logging.
3. Access logs via **WooCommerce > Status > Logs**.

Keep in mind that logs can be lengthy and continue to grow over time. We recommend keeping them **deactivated unless troubleshooting**.

Conflicts with plugins or your theme can cause issues such as:

- missing or improperly displayed payment options at checkout,
- failure to redirect customers to the correct confirmation page, and
- Blocked API responses from the gateway.

If you encounter issues, consider:

- checking for outdated plugins or themes,
- [testing for conflicts](https://woocommerce.com/document/how-to-test-for-conflicts/) by disabling all plugins except WooCommerce and your payment gateway, then re-enabling them one by one.

Conflicts typically don’t affect API credentials. For errors like “incorrect credentials,” confirm the credentials are correct with your payment processor.

The [WooCommerce System Status Report](https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/) provides insights into potential issues. Key things to check include:

- Is the site running the latest versions of WordPress and WooCommerce?
- Is PHP up to date? Older versions can cause compatibility problems.
- Is SOAP enabled? Some gateways require it.
- Are the WooCommerce pages (like checkout) properly configured?

Payment notifications ensure your shop receives updates about transaction status. These notifications vary by gateway:

- [Stripe](https://woocommerce.com/products/stripe/): Automatically handles notifications—no setup required.
- **PayPal**: May require manual configuration for some setups.
- **Authorize.Net**: Often requires manual configuration.

If notifications aren’t working, double-check the notification URL or configuration for your specific gateway.

By understanding these troubleshooting steps, you’ll be better equipped to resolve issues quickly and maintain a smooth checkout experience for your customers.

Do you still have questions and need assistance?

- [Get in touch](https://woocommerce.com/my-account/create-a-ticket/) with a Happiness Engineer via our Help Desk. We provide support for extensions developed by and/or sold on WooCommerce.com, and Jetpack/WordPress.com customers.
- If you are not a customer, we recommend finding help in the [WooCommerce support forum](https://wordpress.org/support/plugin/woocommerce/) or hiring a Woo Agency Partner. These are trusted agencies with a proven track record of building highly customized, scalable online stores.[Learn more about Woo Agency Partners](https://woocommerce.com/development-services/).

