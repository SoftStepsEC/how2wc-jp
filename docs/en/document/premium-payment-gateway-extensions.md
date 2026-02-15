---
title: Which payment option is right for me?
url: https://woocommerce.com/document/premium-payment-gateway-extensions/
---

There is a large range of [payment gateway options](https://woocommerce.com/product-category/woocommerce-extensions/payment-gateways) for WooCommerce to provide payment options for your customers. Read on to learn about how to choose a payment method, including [WooPayments](https://woocommerce.com/document/premium-payment-gateway-extensions/#woocommerce-payments) (available in selected locations).

On this page you’ll learn:

- What a payment gateway is.
- What to look for when choosing a payment gateway.
- How many payment gateways you need.
- How to consider free vs. premium gateways.
- Privacy considerations of payment gateways.

A payment gateway, in WooCommerce terms, is a WordPress plugin that enables WooCommerce to connect a customer to a payment processor so that they can pay for goods and services.

- All processors require an account, normally called a merchant account.
- Each payment processor has terms and fees (separate to the cost of the plugin itself). Contact the payment processor directly with questions about account requirements, terms, and fees.
- Some have multiple options based on different account types, transaction types, or redirect methods.

When selecting and setting up a payment gateway, it’s important to consider:

- **Cost**
- **Location**
- **Security**
- [Support for](https://woocommerce.com/document/premium-payment-gateway-extensions/#support-for-subscriptions) [Woo Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/) (if applicable)

Startup and ongoing costs are different for each payment processor and can consist of:

- The cost of the payment gateway extension/plugin, if it’s not free.
- Signup fees charged by the payment gateway company/processor.
- Monthly or yearly subscription fees.
- Transaction fees.

Shop location and currency are factors. A payment gateway company/processor may only serve merchants based in certain countries. If, for example, it only supports U.S. dollars and accepts U.S. shop owners, then shop owners in Canada and Europe cannot use it.

However, customers from all over the world can use the gateway to check out and pay. More info at: [What to Consider about Payments when Selling Internationally](https://woocommerce.com/2016/09/international-payment-tips/) and [How to Choose a Payment Gateway](https://woocommerce.com/posts/how-to-choose-payment-gateway/).

- **Redirect**: Customer is forwarded to the Payment Gateway site to process payment, then redirected back to your site to complete checkout.
- **Direct**: Customer purchases and pays directly on your site, requiring an [SSL certificate](https://woocommerce.com/document/ssl-and-https/) as part of [PCI Compliance](https://woocommerce.com/document/pci-dss-compliance-and-woocommerce/).

Shop owners accepting payments have a responsibility to protect sensitive customer information, such as email addresses, shipping addresses, and billing information.

To do this, most payment gateways require an SSL certificate. This encrypts communications between your site and customers, and your site and the payment processor. More info at: [SSL FAQ](https://woocommerce.com/document/ssl-faq/).

Other steps to secure your site are covered by the Payment Card Industry Data Security Standard (PCI-DSS), which applies to anyone storing, processing, or transmitting credit card data. More info at: [PCI-DSS compliance and WooCommerce](https://woocommerce.com/document/pci-dss-compliance-and-woocommerce/).

If you’d like to read more about payment gateway security, check out our [WooCommerce site and data security FAQ](https://woocommerce.com/document/woocommerce-security-faq/#section-5).

Should you wish to sell recurring payments on your site, for example using the [Woo Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/) extension (separate purchase), you must choose a payment gateway that supports manual or automatic recurring payments. More info at: [Subscription payment methods and gateways](https://woocommerce.com/document/subscriptions/payment-gateways/).

You need at least one payment method to collect payment on your site even if this is a manual payment gateway such as on of the WooCommerce defaults, like [Direct Bank Transfer](https://woocommerce.com/document/bacs/). Offering a carefully selected choice of payment options increases the possibility that customers can always check out and complete payment.

Many payment gateways offer standard credit card fields as well as “express” payment buttons to allow checkout with Apple Pay and Google Pay.

However, offering too many payment gateways and methods can overwhelm customers with choices and make your site administration more complex. Choose what you offer carefully according to shop requirements, business needs, and customer preferences.

When going through the [WooCommerce setup](https://woocommerce.com/document/woocommerce-setup-wizard/#set-up-payments), you are offered different payment gateways based on your store location, which includes [Core Payment Options](https://woocommerce.com/documentation/plugins/woocommerce/getting-started/sell-products/core-payment-options/) and [WooPayments](https://woocommerce.com/products/woocommerce-payments/).

Should you wish to use something different, you can select and purchase a **Premium** gateway.

**Core payment options** are free payment methods built into WooCommerce and include [Cash on Delivery](https://woocommerce.com/document/cash-on-delivery/), [Check Payments](https://woocommerce.com/document/cheque/), and [Direct Bank Transfers (BACS)](https://woocommerce.com/document/bacs/). The gateways themselves have no associated activation or usage costs.

**WooCommerce.com offers our own WooPayments**! WooPayments is free to install, with no setup fees or monthly fees. Pay-as-you-go fees start from just 2.9% + $0.30 per transaction for US-issued cards, [detailed in about transaction fees](https://woocommerce.com/document/woopayments/fees-and-debits/fees/). WooPayments is available in [17 other countries](https://woocommerce.com/document/payments/countries/) and growing. Read more about [WooPayments](https://woocommerce.com/payments/) and if you’re not in any of the supported countries, [let us know where you are](https://woocommerce.com/payments/#request-invite) so we know which countries to look into next!

Paid payment options are available via [Premium Payment Gateway extensions](https://woocommerce.com/product-category/woocommerce-extensions/payment-gateways). These require an annual subscription to WooCommerce.com for support and updates, along with the processor’s standard transaction fees. In the left sidebar of the search page, you can filter further by a range of options.

If selling to customers in Europe, the European General Data Protection Regulation (GDPR) framework should be part of your decision on which payment gateway to choose. For more information on the GDPR and its concerns for user privacy see [WooCommerce and the GDPR](https://woocommerce.com/gdpr/).

Customer information collected during checkout depends on the payment gateway. If you’re working with a manual payment gateway such as [BACS](https://woocommerce.com/document/bacs/), your site won’t process the payment itself, since you will check your bank account, independently of your site. Other payment gateways, such as Stripe or PayPal, require information to be passed from your site to that payment processor. It’s up to you to choose a trusted processor, as well as consider the impact on customer data.

- Be aware of what information is being sent.
- Inform customers on what happens to their data.
- Understand what the payment processor does with that information.

For example, the [WooCommerce Stripe extension](https://woocommerce.com/products/stripe/) sends certain customer information to Stripe (see [Stripe](https://stripe.com/) documentation for specifics). You need to disclose this process in your site’s Privacy Policy.

Any payment gateway you choose should have information about how to handle customer data. Check the payment processor’s website to learn more about their privacy policies and GDPR.

For more information on how payment gateways apply GDPR, see [Privacy Considerations when Using Official Payments Extensions](https://woocommerce.com/document/privacy-payments/).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

