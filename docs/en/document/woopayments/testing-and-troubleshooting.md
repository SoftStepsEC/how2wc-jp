---
title: WooPayments: Testing and Troubleshooting
url: https://woocommerce.com/document/woopayments/testing-and-troubleshooting/
---

**Spanish version of this page | Aquí puedes encontrar la versión en español de esta página**

WooPayments includes several tools to help you test things out in your store before taking actual payments. We also have a handy guide to help troubleshoot WooPayments errors that, although rare, do occur from time to time.

Payment failures (also called “declines”) can happen for a number of reasons. Most often, they occur because the card issuer has declined the charge, or some other system has blocked it. Only rarely do they signify an actual error with WooPayments.

To learn more about why payments might fail, please [see this document](https://woocommerce.com/document/woopayments/managing-money/#failed-payments).

WooPayments is designed to be dependable and broadly compatible with other plugins, but problems can occur in any complex piece of software. Our [self-service guide](https://woocommerce.com/document/woocommerce-self-service-guide/) explains how to resolve many common issues.

If you’re having trouble even getting WooPayments connected to WordPress.com, please see [this section of our docs](https://woocommerce.com/document/woopayments/our-policies/connection/#troubleshooting) for some helpful tips.

You can also [contact](https://woocommerce.com/my-account/create-a-ticket/)[our](https://woocommerce.com/my-account/contact-support/)[support staff](https://woocommerce.com/my-account/create-a-ticket/) for assistance. Before doing so, it may help to [enable logging](https://woocommerce.com/document/woopayments/settings-guide/#debug-mode) first, since that is a common step required to diagnose many issues.

By default, WooPayments will place real charges on real payment methods, such as credit and debit cards.

WooPayments also provides an easy-to-enable test mode, which simulates the real payment process as closely as possible. This way, you can try out the various features of WooPayments on your site without charging a live payment method.

Please see our [guide to using test mode](https://woocommerce.com/document/payments/testing/) for instructions on how to enable and use test mode.

If you want to try WooPayments on a site that does not need to process real payments, you can use [a test account](https://woocommerce.com/document/woopayments/testing-and-troubleshooting/test-accounts/). This can come in handy on staging sites and the like.

With a test account, it’s possible to create a sandbox-style account that requires no personal information. This account can then be used to process test transactions. It will only operate in test mode and cannot run any real transactions.

If you’re a WordPress developer or agency working on a site for a client, we have [a few helpful guidelines](https://woocommerce.com/document/woopayments/account-management/developer-or-agency-setup/) that you may want to consult as well.

[Safe mode](https://woocommerce.com/document/woopayments/testing-and-troubleshooting/safe-mode/) helps prevent issues in cases where duplicated sites are connected to the same WooPayments account, which may occur when you clone your site to or from a staging site to a live one. Please see guide linked above for tips on what can trigger Safe Mode, as well as how to address the issue.

Safe mode should almost never be triggered deliberately. Instead, we suggest using [test accounts](https://woocommerce.com/document/woopayments/testing-and-troubleshooting/#sandbox-mode) on staging sites.

All test orders placed using either a test account or a live account in test mode will have the `_wcpay_mode` meta key set to `test`. This can help you quickly find test orders and clean up after you finish testing WooPayments.

To improve performance, WooPayments caches some information in the WordPress database. On occasion, our support team may ask you to clear this cache. To do so:

1. Go to **WooCommerce > Status > Tools** page.
2. Scroll down to the **Clear WooPayments account cache** tool.
3. Click **Clear**.

This tool will clear the cached account details so that they are immediately refreshed from the WooPayments server.

The WooPayments plugin is designed for seamless activation and deactivation, without causing compatibility issues with other payment gateways or plugins on your site. If you wish to remove WooPayments data from your site’s database, follow these steps carefully:

1. **Uninstall the WooPayments plugin** – Start by uninstalling and deleting the WooPayments plugin from your WordPress site.
2. **Search for WooPayments data in the database** – Search your site’s database for entries in the `wp_options` table where `option_name` includes `wcpay`. You can consider deleting these entries, but proceed with caution.

**Please also note that:**

- WooPayments does not create its own database tables.
- The `wp_woocommerce_payment_tokens` and `wp_woocommerce_payment_tokenmeta` tables belong to WooCommerce core. **Do not delete these tables**, as they are essential for WooCommerce functionality, regardless of the payment gateway you use.
- WooPayments stores custom values in the `wp_postmeta` table for payment information related to orders.
- WooPayments uses entries in the `wp_options` table to manage settings and state. However, our servers, rather than your database, store transaction details (via Stripe).

- **Avoid Deleting Data** We strongly advise against deleting database records, as this can cause unintended issues.
- **Backup Your Site** Always back up your site before making any database changes. Consult your hosting provider if you’re unsure how to proceed.
- **Scope of Support** Making changes to your site’s database is beyond the scope of our [support policy](https://woocommerce.com/support-policy/). We cannot provide direct assistance with implementing these steps.

If you would like to seek assistance from a qualified WordPress/WooCommerce developer, we highly recommend [Codeable](https://codeable.io/?ref=z4Hnp) or a [Woo Agency Partner](https://woocommerce.com/development-services/).

**Something missing from this documentation? Still have questions and need assistance?**

- If you have a question about a specific extension or theme you’d like to purchase, [contact us](https://woocommerce.com/contact-us/#sales-form) to get answers.
- If you already purchased this product and need some assistance, get in touch with a Happiness Engineer via our [support page](https://woocommerce.com/my-account/create-a-ticket/) and select this product’s name from the Product dropdown.

