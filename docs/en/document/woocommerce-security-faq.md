---
title: WooCommerce site and data security FAQ
url: https://woocommerce.com/document/woocommerce-security-faq/
---

- What products a customer ordered and when
- Name, e-mail address, and phone number provided by the customer
- Billing (and optionally: shipping) address entered by the customer
- A note about payment method used by the customer

- A manual payment gateway, such as [BACS](https://woocommerce.com/document/bacs/), collects customer information, then provides them with your details so they can transfer payment.
- An automatic payment gateway is an application that securely requests information from customers and relays it to a third-party payment processing service, e.g., A credit card processor or PayPal.

- Verify the customer’s billing information
- Verify if funds are available
- Transfer funds from the customer to you
- Send confirmation of payment back to your WooCommerce site

- Refund all transactions that you believe to be fraudulent.
- Consider adding anti-fraud software to your site such as [WooCommerce Anti-Fraud](https://href.li/?https://woocommerce.com/products/woocommerce-anti-fraud/?aff=10486&cid=1131038).
- Consider adding reCaptcha software to your checkout [reCaptcha for WooCommerce](https://href.li/?https://woocommerce.com/products/recaptcha-for-woocommerce/?aff=10486&cid=1131038).
- Determine if there are specific products that may be more susceptible to these kinds of tests, for example “donation” or “name your price” products
- Consider preventing [guest checkout](https://woocommerce.com/document/configuring-woocommerce-settings/accounts-and-privacy/#guest-checkout-and-accounts) on your site.
- Work with your payment provider to increase the security on their account, for example, updating or reviewing the anti-fraud measures they have in place.

