---
title: How do I prevent and respond to card testing attacks?
url: https://woocommerce.com/document/how-do-i-prevent-and-respond-to-card-testing-attacks/
---

**Under attack?**See [this section](https://woocommerce.com/document/how-do-i-prevent-and-respond-to-card-testing-attacks/#how-to-respond) for how to respond to card testing.

Card testing is a type of fraud where the someone obtains a large amount of stolen credit card data, and then attempts to determine which of those cards are valid. Typically, these fraudulent attempts involve making a multiple low-value purchases, each with a different card, to avoid detection by cardholders or banks. If the purchase is successful, the attacker learns that the card is valid, allowing them to sell the card data as “validated” for higher prices, or to use it for larger fraudulent purchases.

Other terms for this activity include “carding” or “card checking.” This kind of attack may lead to increased transaction fees, chargebacks or disputes when legitimate card-holders see this unauthorized activity on their accounts, and can damage the reputation of a store.

Though rare, the potential for a card testing attack is an unavoidable part of running an online business. Our own payments solution, WooPayments, has [some built-in measures](https://woocommerce.com/document/woopayments/fraud-and-disputes/fraud-prevention/) to prevent or limit the impact of such attacks, but ultimately, merchants are responsible for their own fraud prevention techniques.

Fortunately, there are ways you can prevent card testing attacks from harming your site.

One common sign of card testing is a large increase in the number of orders being assigned the *Failed* status. These orders may contain multiple notes about cards being declined. This is because it’s common for card testers to attack a site with hundreds (or even thousands!) of stolen card numbers in a short period of time.

It’s important to note that these orders do not represent missed sales, nor are they caused by issues with your checkout that could prevent legitimate buyers from placing orders. However, card testing may cause other issues for your business, such as an increase in [disputes](https://woocommerce.com/document/payments/disputes/) and [decline](https://woocommerce.com/document/woopayments/managing-money/#failed-payments) rates, which can negatively impact your reputation, and take time and effort to resolve.

If you are using [WooPayments](https://woocommerce.com/products/woopayments/), we have specific guidance [here](https://woocommerce.com/document/woopayments/fraud-and-disputes/card-testing/) with advice on how to handle these situations.

If you are using another payment gateway:

- **Most importantly:** Review all transactions and refund any transactions that you believe to be fraudulent. This is critical to prevent disputes and should be done urgently.
- Consider installing some plugins that can help prevent card testing. These are listed in the[Preventing Card Testing section](https://woocommerce.com/document/how-do-i-prevent-and-respond-to-card-testing-attacks/#preventing-card-testing)below.
- If there are specific low-cost products that may be more susceptible to these kinds of tests, for example “donation” or “name your price” products, consider temporarily making these products private and unavailable for purchase.
- You may want to prevent [guest checkout](https://woocommerce.com/document/configuring-woocommerce-settings/accounts-and-privacy/#guest-checkout-and-accounts) on your site.
- Contact your payment provider to increase the security on their account, for example, updating or reviewing the anti-fraud measures they have in place.

Beyond responding to a card testing attack with the measures above, there are some helpful extensions and steps you can take to prevent continued card testing listed below.

**Note:**If you refund the transactions you believe to be fraudulent, your payment provider still may not refund the transactions fees for those transactions. If you would like these fees to be refunded, reach out to your payment provider and they may be able to assist.

Although we do work with the community and our payments partners to develop new strategies for preventing card testing attacks, it’s important to note that no fraud prevention system is perfect. Here are some additional things you can do to protect your store from card testing attacks.

- Implement a CAPTCHA, extensions such as [reCaptcha for WooCommerce](https://woocommerce.com/products/recaptcha-for-woocommerce/) or [Google reCaptcha for WooCommerce](https://woocommerce.com/products/google-recaptcha-for-woocommerce/) are quick and easy ways to achieve this. Either of these plugins will insert a mandatory bot detection mechanism into your checkout process, which can help prevent automated fraud. A free plugin that only supports Google’s v2 (Checkbox) reCaptcha is [available on WordPress.org](https://wordpress.org/plugins/recaptcha-woo/)
- [Cloudflare Turnstile](https://www.cloudflare.com/application-services/products/turnstile/) is a newer alternative to CAPTCHA plugins that provides a lightweight, privacy-focused solution for bot detection. By integrating Turnstile into your checkout process, you can add an extra layer of security without compromising user experience, helping to safeguard your store against automated fraud attempts. Turnstile is free to use with the [Simple Cloudflare Turnstile](https://wordpress.org/plugins/simple-cloudflare-turnstile/) plugin from WordPress.org. A [paid option](https://woocommerce.com/products/enhanced-cloudflare-turnstile/) is also available on the WooCommerce.com marketplace.
- [WooCommerce Anti-Fraud](https://woocommerce.com/products/woocommerce-anti-fraud/) is an extension that allows you to set up complex rules that, when triggered, will block the offending transactions. This extension offers even more power and flexibility than the rules built into WooPayments.
- [Anti-Fraud Shield for WooCommerce](https://woocommerce.com/products/anti-fraud-shield-for-woocommerce/) offers highly customizable fraud detection and prevention techniques. It helps you reduce card testing activities and block fraud orders manually or automatically.

If you install one of the above plugins, be sure to read the documentation thoroughly. If the plugins are not configured correctly, they will offer little or no protection!

Here are a couple more miscellaneous tips that may help:

- Avoid pay-what-you-want or donation products with no minimum. Fraudsters often use these to make small transactions that may not be noticed by the cardholder.
- If your site is under attack but you don’t see see a large number of *Failed* orders, it may help to disable the **Enable payments via saved cards** setting for your payment methods (if supported). This is sometimes effective if fraudsters are trying to validate cards by adding them to an account on your site.

By carefully monitoring transactions, implementing appropriate security measures, and responding quickly to suspicious activity, you can help protect your store from card testing attacks and maintain your customers’ trust and confidence.

