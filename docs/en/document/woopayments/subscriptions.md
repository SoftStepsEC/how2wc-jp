---
title: WooPayments: Subscriptions
url: https://woocommerce.com/document/woopayments/subscriptions/
---

WooPayments is compatible with [the WooCommerce Subscriptions extension](https://woocommerce.com/products/woocommerce-subscriptions/), which means that your customers can pay for their recurring charges using WooPayments.

Note that, although WooPayments can accept one-off orders via [alternative payment methods](https://woocommerce.com/document/woopayments/payment-methods/additional-payment-methods/), only card payments and [express checkout methods](https://woocommerce.com/document/woopayments/payment-methods/#express-checkout-methods) can be used for [automatic subscription renewals](https://woocommerce.com/document/subscriptions/renewal-process/#manual-vs-automatic-renewals).

**NOTE:** Prior to version 10.2.0, WooPayments offered a built-in subscriptions feature that did not require WooCommerce Subscriptions. That functionality [has now been removed](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/#migrating-subscribers). The Stripe Billing feature explained below is similar, but you must have the Subscriptions extension installed to use it.

If you’ve ever wondered why a customer subscription is still working even though their card is expired, this may be due to our “card account updater” feature. In short, it allows saved cards to continue processing charges even when the customer’s bank has since replaced the card first used on the subscription.

To do this, [our payments partner](https://woocommerce.com/document/woopayments/account-management/partnership-with-stripe/) works directly with the banks to automatically update card details in their system whenever a customer receives a new card. (For example, if their existing card expired or they reported it as lost or stolen.)

This allows your customers to continue their subscription without interruption, and it reduces the need for you to collect new card details whenever one is replaced.

Card account updater is widely supported in the U.S. for most American Express, Visa, Mastercard, and Discover cards. International support varies from country to country.

There is no fee for this feature, nor is there a way to disable it.

Besides basic compatibility with [the Subscriptions extension](https://woocommerce.com/products/woocommerce-subscriptions/), WooPayments also offers one more feature to Subscriptions users based in the United States: the ability to utilize a billing engine powered by our payments partner, called Stripe Billing.

With WooCommerce Subscriptions, automatic recurring payments are initiated by your WooCommerce site and then processed by the payment gateway the customer chose during checkout. This is called an “on-site” billing engine.

An alternative approach is to allow the payment gateway *itself* to initiate the recurring payment. This is called an “off-site” billing engine, and it’s how Stripe Billing works.

Please see our [full guide to the Stripe Billing setting](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/) for more information.

