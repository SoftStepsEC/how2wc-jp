---
title: Order Statuses
url: https://woocommerce.com/document/managing-orders/order-statuses/
---

Every order has its current state marked by a **status**. Order statuses can provide valuable information about the state of an order at a glance. The video and table below provide an overview and more details about order statuses in WooCommerce

Order statuses let you know how far along the order is, starting with “Pending payment” and ending with “Completed.” The core WooCommerce plugin uses the following order statuses:

This flow chart illustrates how an order moves through statuses from **Pending payment** to **On Hold,** **Failed**, or **Processing** then **Completed**, **Canceled** or **Refunded**.

In WooCommerce, the default status for newly created orders is `Pending Payment` . The pending payment status is applied to orders that have been submitted, but are awaiting payment.

However, when using WooCommerce Blocks for the checkout process, orders are created when the shopper arrives to the checkout page. The pending payment status does not accurately reflect the state of these orders, which may be incomplete or unsubmitted. To accommodate for this, the `checkout-draft` status is used until the order is submitted.

- **Creation**: Initiated when a customer arrives on the checkout page using WooCommerce Blocks.
- **Content**: Includes the customer’s items, selected shipping method, and provided address information.
- **Updates**: The draft order dynamically updates as the customer modifies information in the Cart or Checkout blocks.
- **Stock Reservation**: Draft orders place a temporary 10-minute hold on the stock contained in the customer’s cart. This reservation ensures that the items are available for the customer to purchase during the checkout session, and is separate from the [Hold Stock inventory setting](https://woocommerce.com/document/configuring-woocommerce-settings/products/#inventory). (This behavior is under discussion for modification, and can be altered via snippet, see [this Github issue](https://github.com/woocommerce/woocommerce/issues/44231#issuecomment-2109777214) for details)

A scheduled daily cron job (`woocommerce_cleanup_draft_orders`) deletes all draft orders that are no longer active.

Learn more about the different order emails that are sent in the [Email Settings documentation](https://woocommerce.com/document/configuring-woocommerce-settings/emails).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

