---
title: WooPayments: Fraud Protection
url: https://woocommerce.com/document/woopayments/fraud-and-disputes/fraud-protection/
---

From version 5.9.0, WooPayments offers a more configurable fraud protection experience for merchants. This helps you avoid disputes by setting the security and fraud protection risk level that best suits your business.

This page explains how fraud protection works, what the various settings do, and how they interact with incoming orders from your customers.

When a new order is placed, it is first evaluated by the fraud protection rules you’ve configured. Those rules determine if the order will be allowed or blocked.

- **Allowed:** The customer will be charged and the order will succeed. In short, these orders will behave just the same as orders that use any other payment gateway.
- **Blocked:** The customer’s payment method is not charged, and the order is set to the Pending Payment status. Optionally, you can [remove these](https://woocommerce.com/document/woopayments/fraud-and-disputes/fraud-protection/#removing-blocked-orders) after a set time.

Allowed orders will be shown in their normal locations, e.g. **Payments > Transactions** and **WooCommerce > Orders**. We have also added a **Blocked** tab to the **Payments > Transactions** page, which shows the orders that were automatically cancelled.

Fraud protection rules are configured on the **Payments > Settings** page, in the *Fraud Protection* section. There are two options:

- **Basic:** Similar to the protection WooPayments had before version 5.9.0. Orders will only be blocked if the card’s issuing bank can’t verify the card security code.
- **Advanced:** This option allows you to customize the fraud protection rules as needed.

If you want more control than the **Basic** risk level offers, you can select the **Advanced** risk level and configure additional rules. The rules you can add are the following:

- **AVS Mismatch :** Compares postcode submitted by the customer to the postcode on file with their card’s issuing bank. Orders will be blocked if the two do not match up.
- **International IP Address:** Blocks the order if the customer’s [IP address](https://simple.wikipedia.org/wiki/IP_address) is outside [the countries you sell to](https://woocommerce.com/document/configuring-woocommerce-settings/general/), even if the billing country entered *is* one you sell to.
- **IP Address Mismatch:** Compares the customer’s billing country to the country that their IP address seems to originate from. Blocks the order if those do not match.
- **Address Mismatch:** Blocks orders if the billing country and shipping country differ.
- **Purchase Price Threshold:** Compares the total order price to the minimum and maximum that you’ve allowed. Blocks orders if the total is outside the range.
- **Order Items Threshold:** Blocks orders if the total number of items in the order is lower than or greater than the range you’ve allowed.

Enabling a rule will block orders if they meet that rule’s conditions. For example, the following configuration will automatically block orders with over 20 products:

The CVC Verification rule at the bottom cannot be disabled. Card payments that fail CVC verification will always be blocked. Please see [this document](https://woocommerce.com/document/woopayments/fraud-and-disputes/card-verification-checks/#cvc-checks) to learn more.

Incoming orders are evaluated according to the rules you’ve configured. The outcome is noted on the order details page under **WooCommerce > Orders**. Clicking either of the **View more details** links will take you to the transaction details page.

You can also get to the transaction details page directly, by going to **Payments > Transactions** and clicking a transaction. As noted above, blocked transactions will be added to the **Blocked** tab, instead of the main **Transactions** list.

By clicking a blocked transaction to see its timeline, you can find the fraud protection rule(s) that were triggered for that specific transaction.

In order to avoid revealing your specific fraud protection rules to customers, WooPayments will show a generic error message when the rules block a transaction.

Customers who see this message will be able to retry the order if they wish.

If you wish, you can automatically delete blocked orders after a period of time by configuring the “Retain pending orders” setting under **WooCommerce > Settings > Accounts & Privacy**.

Note, however, that this will affect **all** Pending Payment orders, not just those that were blocked by the WooPayments fraud protection rules.

