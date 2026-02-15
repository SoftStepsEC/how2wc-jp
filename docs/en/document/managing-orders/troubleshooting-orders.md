---
title: Troubleshooting Orders
url: https://woocommerce.com/document/managing-orders/troubleshooting-orders/
---

Order-related challenges in WooCommerce, such as pending payments, inventory mismanagement, or incorrect order statuses, can disrupt your store’s functionality and customer experience. This guide simplifies the troubleshooting process, helping you identify common issues such as orders stuck in “Processing” or “On Hold” status, duplicate orders, or stock discrepancies.

If you are not familiar with order statuses, make sure to review our [order status documentation](https://woocommerce.com/document/managing-orders/order-statuses/), a dedicated page with detailed information on the expected order status at each stage of the ordering process.

Typically, one of the first things you need to know when troubleshooting issues related to order statuses is what payment method and gateway were used. That information can usually be found in one of two places.

In the **general order details** section, following the order number:

In the screenshot above, the order screen shows that the payment was made via a credit card and the transaction ID. In some cases, the specific payment gateway used will appear at the top of the order details, alongside the method used. As this isn’t always the case, we’ll show you how to find this information in the **order notes** below:

When an order status does not automatically update, it could be an expected behavior, a configuration issue, or due to something else altogether. Let’s go over the most common causes.

#### Orders Stuck in Processing Status

The **Processing** order status means that the payment was successful, and it’s time to prepare to fulfill orders. It’s expected that orders will not automatically change from the **Processing** to the **Completed** status, as the store administrator is responsible for fulfilling the order and should manually update the order status to **Completed** once the product(s) have been shipped. All orders require processing except those in which all products are both[Virtual and Downloadable](https://woocommerce.com/document/managing-products/virtual-downloadable/).

#### Order Stuck in On Hold Status

If an order was placed and you received the payment, but the order didn’t automatically change from the **On Hold** to **Processing** status, it could be due to one of the following scenarios, as outlined in the[Order Statuses table](https://woocommerce.com/document/managing-orders/order-statuses/#order-statuses-in-woocommerce).

##### Offline Payment Methods

Orders paid using an “offline” payment method, such as the [Direct Bank Transfer (BACS)](https://woocommerce.com/document/bacs/), don’t provide immediate payment confirmation, so it’s expected that the order will remain On Hold. Instead, offline payment methods require you to manually verify the payment was processed; once you confirm payment has been received, you can change the status of the order.

##### Delayed Notification Payment Method

If the order was paid using a delayed notification payment method, like SEPA Direct Debit, it’s expected that it will remain in **On Hold** status temporarily. Depending on the payment gateway in use on your site, the order may be moved automatically from **On hold** to a different status once the payment clears. Check the order notes on the order and the documentation of your payment gateway for details.

##### Authorize and Capture

Make sure the payment gateway is set to both **Authorize and Capture** the charge, and not just authorize it. An authorization is a hold on funds, requiring the store owner to manually “capture” the charge before any money is transferred. Authorize and Capture is much more common, and is a single-step process that immediately transfers funds from your customer to your payment gateway. You can check if this is the case by looking at the order notes and checking that the payment was authorized, but not captured:

For detailed information about this setting, please refer to your payment gateway’s documentation. Below, you’ll find additional details about the Authorize and Capture setting for some commonly used payment gateways:

- [WooPayments](https://woocommerce.com/document/woopayments/settings-guide/authorize-and-capture/)
- [Stripe](https://woocommerce.com/document/stripe/admin-experience/authorize-and-capture/)
- [Square](https://woocommerce.com/document/woocommerce-square/payment-settings/#payment-settings)
- [PayPal Payments](https://woocommerce.com/document/woocommerce-paypal-payments/#general-settings)

##### Order Notes

Order notes can reveal specific issues such as insufficient funds, expired cards, authentication failures, or gateway timeouts. Look for entries that include error codes, decline reasons, or status updates from your payment gateway. These messages typically appear with timestamps showing when each event occurred during the payment process.

##### Logs

If you can’t find anything useful or insightful in the order notes, check WooCommerce logs for errors or any clues about issues with the communication between the payment gateway and your store. If logging is enabled in your payment gateway’s settings, you can find the logs in **WooCommerce > Status > Logs**. You will want to look for the logs of the payment gateway used in the affected order for the day the order was placed. Please know that once logging is enabled, the system will only **capture new transactions**. This means you may need to place a test order to generate logs. If you find any logs for the payment being initiated, but not finished, this could indicate that the process was interrupted or failed silently after the initial request. If you find this is the case, you may want to contact your payment gateway’s support or [contact our support](https://woocommerce.com/my-account/contact-support/) for WooCommerce-developed payment gateways.

The `Pending Payment` order status in WooCommerce indicates that an order has been received, but payment has not yet been confirmed. Certain payment gateways, such as[Direct Bank Transfer (BACS)](https://woocommerce.com/document/bacs/) or[check payments](https://woocommerce.com/document/cheque/), require the store owner to manually verify the payment has been received before moving the order to the `Processing` or `Completed` status.

However, most payment gateways will automatically update the order status to `Processing` status once the payment has been received. If they aren’t automatically updating, here are a few things you can check.

Note: If you are still using the now deprecated and hidden-by-default PayPal Standard functionality and orders are staying in the Pending Payment status after successful payment, you may have an IPN issue. See the troubleshooting section at [Debugging IPN Issues](https://woocommerce.com/document/paypal-standard/#debugging-ipn-issues)

##### Check Order Notes

Payment gateway messages often appear in order notes and can reveal specific issues such as insufficient funds, expired cards, authentication failures, or gateway timeouts. Look for entries that include error codes, decline reasons, or status updates from your payment gateway. These messages typically appear with timestamps showing when each event occurred during the payment process.

**When order notes are missing:**

If you see no order notes related to the payment attempt, this itself indicates a potential problem. Missing notes often suggest that the payment gateway failed to communicate properly with WooCommerce or the payment process was interrupted before completing. In cases where order notes are absent, you should verify that your payment gateway is configured correctly. If you have debug logging enabled in your payment gateway settings, review the logs and see if any clues appear there.

##### Check Webhooks

A webhook acts as a real-time notification system that allows your payment gateway to instantly communicate with your WooCommerce store when a payment status changes. Some payment gateways require you to manually set up webhooks, while others handle this automatically in the background.

One example of a payment gateway that requires manual configuration of webhooks is [Stripe for WooCommerce](https://woocommerce.com/products/stripe/). If you’re using [Stripe for WooCommerce](https://woocommerce.com/products/stripe/) and seeing pending payment issues, you may want to[Reconfigure Webhooks](https://woocommerce.com/document/stripe/setup-and-configuration/stripe-webhooks/#reconfiguring).

If you observe duplicate orders in your WooCommerce store, there are several potential causes that you should investigate. Here’s a detailed breakdown of each point:

##### Customer Communication:

If you identify suspected duplicate orders, contact the customer to verify their intent. Ask if they intended to place multiple orders. In many cases, seemingly duplicate orders were the result of a second purchase by the customer.

##### Browser/Network Issues:

Duplicate orders can sometimes happen if a customer accidentally double-clicks the “Place Order” button or refreshes the checkout page while waiting for the transaction to complete. This can create multiple order attempts, which may lead to the same item being purchased more than once. We suggest asking your customer if they experienced any delays or errors that led them to refresh the checkout page or click the “Place Order” button more than once.

##### Order Number Verification:

Do the suspected duplicate orders share the exact same order number? If the order numbers are unique, it’s possible that the customer placed separate, legitimate orders. It is not uncommon for a customer to make multiple purchases, especially if they forgot to add items to their initial order.

##### Order Note Examination:

Thoroughly review the order notes for each of the suspected duplicates. Comparing information such as customer details, payment methods, discrepancies, or similarities in this data can offer clues. Pay particular attention to any payment gateway-specific notes that might be included. If the payment went through at the same time in both orders (or with a really short span between them), it’s possible that it was an error, indeed, and the second order is not legitimate.

##### Staging Site Influence:

If you maintain a[staging or development](https://woocommerce.com/posts/what-is-staging-site-wordpress-how-to-set-one-up/) version of your WooCommerce site, ensure that the staging site is completely isolated from your production environment. An improperly configured staging site might be processing live orders inadvertently, leading to apparent duplicates. Be especially wary of possible staging site issues if you use an extension that creates recurring orders automatically on a schedule.

##### Payment Gateway Dashboard Review:

Login in to your payment gateway’s dashboard. Locate the corresponding transaction for the potentially duplicate order(s) in question. If there are two transactions, it can indicate a customer making the same purchase twice, especially if WooCommerce also shows two transactions. If only one transaction is listed in the gateway, further troubleshooting in WooCommerce is required.

##### Recent Changes Audit:

If the duplicate order issue surfaced recently, consider any recent changes to your store. This includes plugin installations, updates, gateway configurations, or theme modifications. Reverting recent changes may resolve the issue or may highlight the source of the problem.

##### Server and Hosting Evaluation:

Slow server response times or hosting issues can lead to duplicate orders. If a customer experiences delays during checkout, they might resubmit the order form multiple times. Contact your hosting provider to investigate server performance and check for any known issues with their services. Consult our[WooCommerce Server Recommendations](https://woocommerce.com/document/server-requirements/) to ensure your environment is properly configured.

##### Log Review:

Check WooCommerce logs for duplicate webhook calls or responses. If logging is enabled in your payment gateway’s settings, you can find the logs in **WooCommerce > Status > Logs**. You will want to look for the logs of the payment gateway used in the affected order for the day the order was placed.

##### Plugin Conflict Diagnosis:

Plugin conflicts are a common source of unexpected behavior. If you can reproduce the issue, in a testing environment like a local or staging site, temporarily deactivate all plugins except for WooCommerce and your active payment gateways. Test placing an order. If the duplicates disappear, reactivate each plugin one by one, testing after each activation to identify the culprit. See our [WooCommerce Plugin Conflict Testing Guide](https://woocommerce.com/document/how-to-test-for-conflicts/) for more details.

WooCommerce automatically tracks and updates product inventory as customers make purchases in your store. When functioning correctly, this system reduces stock levels during the checkout process and maintains accurate inventory counts across your entire product catalog.

To prevent overselling, it’s important to keep track of your inventory carefully. You can do this by turning on the stock management option in your products and product settings. This will help ensure that the amount you show online matches what you have on hand.

To ensure Stock Management is enabled in WooCommerce, please navigate to **WooCommerce > Settings > Products > Inventory**:

1. “Enable stock management” is **checked**
2. “Hold stock” duration is set appropriately (recommended: 60 minutes)

For additional information, please see[Product Settings: Inventory](https://woocommerce.com/document/configuring-woocommerce-settings/products/#inventory).

WooCommerce might not reduce stock levels after orders if stock management is not enabled in both the global WooCommerce settings and the settings for individual products. Ensure that stock management is active in both locations. If either setting is disabled, automatic stock reduction will not occur upon order placement.

#### Simple Products

By following these steps, you can ensure that you successfully add and manage stock for your simple products in WooCommerce.

1. **Go** to Products.
2. **Select** a Product to edit.
3. **Go** to the Product data section.
4. Enable **Track stock quantity for this product**.

1. Set the Stock **quantity.**

Note: If you want customers to be able to order items even if they’re currently out of stock, you can select Allow backorders from the dropdown options.

#### Variable Products

You can manage inventory for variable products at the product level, variation level, or a mixture of the two.

- Product Level Inventory Management
- Variation Level Inventory Management
- Combining Inventory Management Systems: Variation Level + Product Level Management

For additional information, please see[Inventory Management for Variable Products](https://woocommerce.com/document/variable-product/#inventory-management).

#### Incorrect Stock Display

If customers cannot view stock inventory on your website, verify the stock display format in your WooCommerce settings under **WooCommerce > Settings > Products > Inventory**.

Select one of the following options for how the number of products in stock is displayed, or choose not to display it:

- Always show stock — “12 in stock”.
- Only show stock when low — “Only 2 left in stock” vs. “In stock”.
- Never show the amount.

Additional information regarding this and related considerations can be found in[Product Settings: Inventory](https://woocommerce.com/document/configuring-woocommerce-settings/products/#inventory).

While every order uses a unique order ID, they won’t necessarily be sequential. Order numbers are non-sequential because they share the wp_post database table. This database table is shared with other post types in WordPress — like pages, blog posts, comments, product reviews, and coupons. Each time a new post of any kind is created, it increments the ID number used in the database table by one. So if items of other post types are created between orders, the order IDs will “skip” those IDs that have been used by other posts.

To assign your orders sequential order numbers, you can use an extension like [Sequential Order Numbers Pro](https://woocommerce.com/es/products/sequential-order-numbers-pro/).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

