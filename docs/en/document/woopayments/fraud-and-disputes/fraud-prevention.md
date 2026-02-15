---
title: Does WooPayments have built-in fraud prevention?
url: https://woocommerce.com/document/woopayments/fraud-and-disputes/fraud-prevention/
---

WooPayments is built [in partnership with Stripe](https://woocommerce.com/document/woopayments/account-management/partnership-with-stripe/) and uses their fraud prevention system, called [Radar](https://stripe.com/radar). It provides real-time fraud detection and risk evaluation for orders placed via WooPayments, and it will block those that Radar determines are likely fraudulent.

[Card verification checks](https://woocommerce.com/document/woopayments/fraud-and-disputes/card-verification-checks/) are also run for every credit or debit card transaction.

WooPayments also has its own [fraud protection settings](https://woocommerce.com/document/woopayments/fraud-and-disputes/fraud-protection/), which can be used to block orders that meet certain criteria. You can of course customize the detection rules to suit the needs of your particular store.

Sometimes WooPayments flags a transaction as *Elevated* risk. This occurs if it has *some* suspicious signals, but isn’t quite risky enough to be blocked automatically.

- Order page showing a charge with Elevated risk
- Transactions table showing a charge with Elevated risk
- Transaction details page showing a charge with Elevated risk

For *Elevated* risk transactions, you should try to contact the customer before fulfilling the order. If you can’t reach them, consider refunding the order as a precaution.

However, keep in mind that no fraud prevention system is perfect. Although it is rare, sometimes merchants may be affected by card testing attacks. You can learn more about card testing, and how to respond to such attacks, in [this document](https://woocommerce.com/document/woopayments/fraud-and-disputes/card-testing/).

As WooPayments continues to enhance the merchant experience, we will be looking to add more fraud detection functionality for stores using our plugin. Please feel free to submit feedback or other ideas on our [Ideas Board](https://woocommerce.com/feature-requests/woopayments/).

