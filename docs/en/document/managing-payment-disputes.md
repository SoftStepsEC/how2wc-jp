---
title: Managing Payment Disputes
url: https://woocommerce.com/document/managing-payment-disputes/
---

Payment disputes are one of the more challenging aspects of running an online store. Let’s have a look at a few best practices for how to increase your chances of success when approaching and challenging disputes:

- [What is a payment dispute?](https://woocommerce.com/document/managing-payment-disputes/#what-is-a-payment-dispute)
- [Receipts as dispute evidence](https://woocommerce.com/document/managing-payment-disputes/#receipts-as-dispute-evidence)
- [Proof required to challenge chargebacks](https://woocommerce.com/document/managing-payment-disputes/#proof-required-to-challenge-chargebacks)
- [Contact your customer](https://woocommerce.com/document/managing-payment-disputes/#contact-your-customer)
- [Dispute types](https://woocommerce.com/document/managing-payment-disputes/#dispute-types)

## What is a payment dispute?

A payment dispute is when a customer’s card issuer comes back to you, the merchant, via your payment gateway with either a query or a chargeback. It happens when a customer questions transactions on their bank or credit card statements.

In the world of eCommerce, a receipt is the online order receipt or confirmation. It’s the foot and finger prints of a transaction, and as such, very important when it comes to challenging a payment dispute.

It’s not just to inform the customer of what they’re buying and from who, but also, in case it’s required, evidence when responding to a dispute. Here are some receipt requirements to consider for businesses where the card is not present during purchase:

- Merchant name and location
- Transaction date
- Merchant’s internet address
- Description of goods or services
- Payment method used
- Suppressed account number or token
- Transaction type (purchase or credit)
- Authorization code
- Transaction amount
- Return/refund policy

In an ideal world, as much as possible of the above would appear on the receipt. The receipt can also reiterate your store’s terms and conditions, refund policy, and cancelation policy.

When a transaction receipt is submitted for the purpose of challenging a dispute, it becomes evidence that the buyer was aware of what they were purchasing and under what conditions.

When a payment dispute comes knocking at your online’s store door, it usually requires the following proof:

- There were no deceptive practices, which means your store did not mislead the buyer on price, and they were aware of what they were purchasing.
- That the buyer consented to the purchase and terms, which could be through acceptance of the terms and conditions.
- It was the buyer who made the actual purchase, there was no fraud, and the card was not stolen.
- You fulfilled the product via shipping. Or, in the case of digital or downloadable goods, the product was provisioned, and you can prove the buyer accessed, partially used or engaged with the service (e.g. logged into the site multiple times, downloaded the product, etc.)

With any dispute, we recommend that you contact your customer to discuss the claim. Sometimes, customers may mistakenly dispute a charge and once reminded of the transaction, they can withdraw the dispute with their card issuer.

Importantly, even if your customer does withdraw the dispute, you still need to challenge the dispute in order for the transaction to be refunded and dispute fee returned. It will also still take approximately 75 days to be closed by the card issuer.

Card issuers categorize disputes in one of the following ways, base on the claim by the card holder:

- **Credit not processed**: card holder claims they are owed a refund or other credit that has not been received. For example, if your customer returns a product, but the charge has not been refunded to the card.
- **Duplicate**: customer claims multiple charges were placed on their card for the same product or service. For example, if your customer paid for a service when booking via your website, as well as in person after receiving the service.
- **Fraudulent**: card holder, not necessarily the customer with your store, claims they did not authorize the payment with your store. For example, if your customer used a stolen credit card number to place an order, the holder of that card may later see the transaction and dispute it as it is not recognized.
- **General or Unrecognized :** the card holder notifies their card issuer that they do not recognize the charge on their card statement.
- **Product not received**: the good or service for which the charge was processed has not been received by the customer. For example, a shipment from your business has not been received by your customer.
- **Product unacceptable**: the card holder claims the product or service they received in return for the payment was defective, damaged, or not as described. For example, your customer was shipped a different item to the one purchased.
- **Subscription cancelled**: after cancelling a subscription plan, the customer was charged a recurring payment for that subscription. For example, if a customer calls your business to request cancellation, but the subscription is not cancelled within WooCommerce.

Because each type of dispute represents a different claim by the customer, each requires different evidence to be submitted when challenging the dispute. The rest of this document outlines the different types of disputes, and evidence required to challenge each. This information is based on guidance from Stripe, our [payments partner](https://woocommerce.com/document/payments/powered-by-stripe/), on [dispute evidence for each category](https://stripe.com/docs/disputes/categories).

To overturn a **credit not processed** dispute, you need to demonstrate either that:

1. Your customer is not entitled to a refund based on your store’s refund policy; or
2. You have refunded your customer outside of the card network, e.g., via store credit.

#### Additional details text

In the **Additional Details** text field of the **Payments > Disputes > Challenge Dispute** screen, your response should include the following information:

- **Disclosure of refund policy**: explain how and when your refund policy was disclosed to the customer prior to purchase.
- **Reason for refund refusal**: if you have refused to refund the customer, explain to the bank why the customer is not entitled to a refund. Reference terms in your refund policy, uploaded in the **additional details file** field.

#### Additional details file

In the **Additional Details** file upload field of the **Payments > Disputes > Challenge Dispute** screen, upload a PDF of your refund policy, as presented to the customer. Do not link to the refund policy within your response, as links will not be visited by the card issuer evaluating the dispute.

To overturn a **duplicate** charge dispute, you need to demonstrate that each payment was for a separate product or service.

#### Additional details text

In the **Additional Details** text field of the **Payments > Disputes > Challenge Dispute** screen, your response should include:

- **Duplicate charge ID:** the charge ID for the previous payment that appears to be a duplicate of the one that is disputed. This ID is available on the transaction from the **WooCommerce > Edit Order** screen, or the **Payments > Transactions** screen.
- **Duplicate charge explanation**: explain to the bank the difference between the disputed payment and the prior one that appears to be a duplicate, referencing documentation uploaded in the **additional details file** field.

#### Additional details file

In the **Additional Details** file upload field of the **Payments > Disputes > Challenge Dispute** screen, upload a document for the prior payment that can uniquely identify it, such as a separate receipt. This document should be paired with a similar document from the disputed payment that proves the two are separate.

If the dispute is on a charge for a **physical product**, this should also include a separate shipping label for both this charge and the other payment. If multiple products were shipped together, provide a packing list that shows each purchase.

If the dispute is on a charge for an **offline service**, provide a copy of the service agreement.

To overturn a **fraudulent** charge dispute, you need to prove to the card issuer that the cardholder authorized the transaction. The cardholder may not be the same person as the customer with your store.

When challenging a Fraudulent charge dispute, you must include [compelling evidence](https://woocommerce.com/document/managing-payment-disputes/#compelling-evidence) in order for Visa to consider the dispute if the transaction was processed on the Visa network. We recommend you always include compelling evidence, regardless of card network.

For this dispute type, you also need to include different information depending on the type of product associated with the disputed transaction.

For Fraudulent disputes, you must include at least one piece of [compelling evidence](https://woocommerce.com/document/managing-payment-disputes/#compelling-evidence) in order for Visa to consider your response.

Compelling evidence for fraudulent disputes on **physical products and offline services** includes:

- Customer signature: Upload a file to prove the person who signed for the products upon delivery was the cardholder, is known to the cardholder or authorized by the cardholder to sign. If the products are collected from a physical location, you must provide:
  - Cardholder signature on the pickup form
  - A copy of identification presented by the cardholder
  - Details of identification presented by the cardholder
  
- **Customer communication:** Evidence such as photographs or emails to prove a link between the person receiving products and the cardholder, or proving that the cardholder disputing the transaction is in possession of the products.

**For all product types**, the information listed below in the **Additional details file** section is also compelling evidence and you should submit any available.

#### Additional details text

For a dispute on a transaction involving a physical product, the **Additional Details** text field of the **Payments > Disputes > Challenge Dispute** screen, your response should include:

- **Shipping date**: the date on which the package began its route to the shipping address, in a clear human-readable format.
- **Shipping carrier**: include the name of the delivery service that shipped the package, such as Fedex, UPS, USPS, etc. If multiple carriers were used for this purchase, include the names of all carriers.
- **Shipment tracking number**: include the tracking number for a physical product, obtained from the shipping carrier or delivery service. Please include all tracking numbers for all packages associated with this transaction.

#### Additional details file

For a dispute involving a physical product, using the **Additional Details** file upload field on the **Payments > Disputes > Challenge Dispute** screen, upload a file with the following:

- Shipping documentation: upload a PDF showing:
  - The address to which a physical product was shipped. The shipping address must match a billing address verified with AVS. (A signature is not required as evidence of delivery).
  - Proof that the package was shipped to the cardholder at the same address the cardholder provided to you. This could include a copy of the shipment receipt or label, and show the full shipping address of the cardholder, if possible.
  - Detailed delivery information from the carrier, like confirmation of delivery.
  
- Other evidence : in the following situations, you should also include additional documentary evidence:
  - If the customer has purchased the same products from you previously without lodging a dispute on those transactions, provide details of those transactions.
  - If the package was shipped to a business address, provide evidence that the customer works there.
  - If the transaction was completed by a member of the cardholder’s family or household, provide evidence of the connection between the two.
  

#### Additional details file

For a dispute involving a digital product or service, the file uploaded with the **Additional Details** file upload field on the **Payments > Disputes > Challenge Dispute** screen, must contain at least two of the following pieces of information in order to fulfill [compelling evidence](https://woocommerce.com/document/managing-payment-disputes/#compelling-evidence) requirements:

- Customer’s IP address and their device’s geographical location at the time of purchase.
- Device ID and name of the device used to complete the transaction.
- Customer name and email address linked to their customer profile.
- Evidence that the customer logged into their account for your business before the transaction date.
- Evidence that your website or app was accessed by the cardholder for purchase or services on or after the transaction date.
- Evidence that the same device and card used in the disputed payment was used in a previous payment that was not disputed.

#### Additional details file

For a dispute involving an offline service, using the **Additional Details** file field on the **Payments > Disputes > Challenge Dispute** screen, upload a file with the following:

- **Service date:** evidence of the date on which the cardholder received or began receiving the purchased service, which should be before the dispute date.
- **Service documentation:**Documentation showing proof that a service was provided to the cardholder. This could include a copy of a signed contract, work order, or other form of written agreement.
- Other evidence:
  - If the customer has purchased the same service from you previously without lodging a dispute, provide details of those transactions.
  - If the transaction was completed by a member of the cardholder’s family or household, provide evidence of the connection between the two.
  

In a **General** or an **Unrecognized** dispute, the customer doesn’t recognize the payment appearing on their card statement. To overturn the dispute, you need your customer to withdraw the dispute. You can achieve this by helping them identify the payment.

When challenging a dispute of this type, you should also include different information depending on the type of product associated with the disputed transaction.

#### Additional details text

For a dispute on a transaction involving a physical product, the **Additional Details** text field of the **Payments > Disputes > Challenge Dispute** screen, your response should include:

- **Shipping date**: the date on which the package began its route to the shipping address, in a clear human-readable format.
- **Shipping carrier**: include the name of the delivery service that shipped the package, such as Fedex, UPS, USPS, etc. If multiple carriers were used for this purchase, include the names of all carriers.
- **Shipment tracking number**: include the tracking number for a physical product, obtained from the shipping carrier or delivery service. Please include all tracking numbers for all packages associated with this transaction.

#### Additional details file

For a dispute involving a physical product, using the **Additional Details** file upload field on the **Payments > Disputes > Challenge Dispute** screen, upload a file with the following:

- Shipping documentation: upload a PDF showing:
  - The address to which a physical product was shipped. The shipping address must match a billing address verified with AVS. (A signature is not required as evidence of delivery).
  - Proof that the package was shipped to the cardholder at the same address the cardholder provided to you. This could include a copy of the shipment receipt or label, and show the full shipping address of the cardholder, if possible.
  - Detailed delivery information from the carrier, like confirmation of delivery.
  
- Other evidence : in the following situations, you should also include additional documentary evidence:If the customer has purchased the same products from you previously without lodging a dispute on those transactions, provide details of those transactions.
  - If the package was shipped to a business address, provide evidence that the customer works there.
  - If the transaction was completed by a member of the cardholder’s family or household, provide evidence of the connection between the two.
  

For a dispute involving a digital product or service, the file uploaded with the **Additional Details** file upload field on the **Payments > Disputes > Challenge Dispute** screen, must contain at least two of the following pieces of information in order to fulfill [compelling evidence](https://woocommerce.com/document/managing-payment-disputes/#compelling-evidence) requirements:

- Customer’s IP address and their device’s geographical location at the time of purchase.
- Device ID and name of the device used to complete the transaction.
- Customer name and email address linked to their customer profile.
- Evidence that the customer logged into their account for your business before the transaction date.
- Evidence that your website or app was accessed by the cardholder for purchase or services on or after the transaction date.
- Evidence that the same device and card used in the disputed payment was used in a previous payment that was not disputed.

In the **additional details** file, your response should include a file with:

- **Service date:** evidence of the date on which the cardholder received or began receiving the purchased service, which should be before the dispute date.
- **Service documentation:**Documentation showing proof that a service was provided to the cardholder. This could include a copy of a signed contract, work order, or other form of written agreement.

To overturn a **product not received** dispute, you need to prove a customer received a physical product or offline service, or made use of a digital product or online service prior to the date of the dispute.

When challenging a **product not received** dispute, you must include [compelling evidence](https://woocommerce.com/document/managing-payment-disputes/#compelling-evidence) in order for Visa to consider the dispute.

For this dispute type, you also need to include different information depending on the type of product associated with the disputed transaction.

For **product not received** disputes, you must include at least one piece of [compelling evidence](https://woocommerce.com/document/managing-payment-disputes/#compelling-evidence). Compelling evidence for disputes involving **physical products**, and **offline services** includes:

- Customer signature: upload a file to prove the person who signed for the products upon delivery was the cardholder, is known to the cardholder or authorized by the cardholder to sign. If the products are collected from a physical location, you must provide:
  - Cardholder signature on the pickup form
  - A copy of identification presented by the cardholder
  - Details of identification presented by the cardholder
  
- **Customer communication:** Evidence such as photographs or emails to prove a link between the person receiving products and the cardholder, or proving that the cardholder disputing the transaction is in possession of the products.

For all product types, the information listed below in the **Additional Details** file section is also compelling evidence. You should submit any such file evidence available.

#### Additional details text

For a dispute on a transaction involving a physical product, the **Additional Details** text field of the **Payments > Disputes > Challenge Dispute** screen, your response should include:

- **Shipping date**: the date on which the package began its route to the shipping address, in a clear human-readable format.
- **Shipping carrier**: include the name of the delivery service that shipped the package, such as Fedex, UPS, USPS, etc. If multiple carriers were used for this purchase, include the names of all carriers.
- **Shipment tracking number**: include the tracking number for a physical product, obtained from the shipping carrier or delivery service. Please include all tracking numbers for all packages associated with this transaction.

#### Additional details file

For a dispute involving a physical product, using the **Additional Details** file upload field on the **Payments > Disputes > Challenge Dispute** screen, upload a file with the following:

- Shipping documentation: upload a PDF showing:
  - The address to which a physical product was shipped. The shipping address must match a billing address verified with AVS. (A signature is not required as evidence of delivery).
  - Proof that the package was shipped to the cardholder at the same address the cardholder provided to you. This could include a copy of the shipment receipt or label, and show the full shipping address of the cardholder, if possible.
  - Detailed delivery information from the carrier, like confirmation of delivery.
  
- Other evidence : in the following situations, you should also include additional documentary evidence:If the customer has purchased the same products from you previously without lodging a dispute on those transactions, provide details of those transactions.
  - If the package was shipped to a business address, provide evidence that the customer works there.
  - If the transaction was completed by a member of the cardholder’s family or household, provide evidence of the connection between the two.
  

#### Additional details file

For a dispute involving a digital product or service, the file uploaded with the **Additional Details** file upload field on the **Payments > Disputes > Challenge Dispute** screen, must contain at least two of the following pieces of information in order to fulfill [compelling evidence](https://woocommerce.com/document/managing-payment-disputes/#compelling-evidence) requirements:

- Customer’s IP address and their device’s geographical location at the time of purchase.
- Device ID and name of the device used to complete the transaction.
- Customer name and email address linked to their customer profile.
- Evidence that the customer logged into their account for your business before the transaction date.
- Evidence that your website or app was accessed by the cardholder for purchase or services on or after the transaction date.
- Evidence that the same device and card used in the disputed payment was used in a previous payment that was not disputed.

#### Additional details file

For a dispute involving an offline service, using the **Additional Details** file upload field on the **Payments > Disputes > Challenge Dispute** screen, upload a file with the following:

- **Service date:** evidence of the date on which the cardholder received or began receiving the purchased service, which should be before the dispute date.
- **Service documentation:**Documentation showing proof that a service was provided to the cardholder. This could include a copy of a signed contract, work order, or other form of written agreement.
- Other evidence:
  - If the customer has purchased the same service from you previously without lodging a dispute, provide details of those transactions.
  - If the transaction was completed by a member of the cardholder’s family or household, provide evidence of the connection between the two.
  

To overturn a **product unacceptable** dispute, you need to demonstrate that the product or service was provided to the customer as advertised to the customer at the time of purchase.

For this dispute type, you should include different information depending on the type of product associated with the disputed transaction.

For all product types:

- If the product or service was delivered as described to the cardholder, provide evidence of that, e.g., a contract, service agreement, or screenshot of the product page at the time of purchase as part of the **Additional Details** file upload field.
- If you have processed a credit or reversal for this transaction, provide a document evidencing this as part of the **Additional Details** file upload field.
- If your customer made no attempt to return the product or cancel the service, or if you provided a replacement product or service, make sure to note that as well.

For disputes on products that have been repaired or replaced, as part of the **Customer Communication** file upload, provide evidence that:

- The cardholder agreed to a repair or replacement;
- It has been received by the customer, and
- The repair or replacement has not since been disputed.

#### Additional details text

For a dispute on a transaction involving a physical product, the **Additional Details** text field of the **Payments > Disputes > Challenge Dispute** screen, your response should include:

- **Shipping date**: the date on which the package began its route to the shipping address, in a clear human-readable format.
- **Shipping carrier**: include the name of the delivery service that shipped the package, such as Fedex, UPS, USPS, etc. If multiple carriers were used for this purchase, include the names of all carriers.
- **Shipment tracking number**: include the tracking number for a physical product, obtained from the shipping carrier or delivery service. Please include all tracking numbers for all packages associated with this transaction.

#### Additional details file

For a dispute involving a physical product, using the **Additional Details** file upload field on the **Payments > Disputes > Challenge Dispute** screen, upload a file with the following:

- Shipping documentation: upload a PDF showing:
  - The address to which a physical product was shipped. The shipping address must match a billing address verified with AVS. (A signature is not required as evidence of delivery).
  - Proof that the package was shipped to the cardholder at the same address the cardholder provided to you. This could include a copy of the shipment receipt or label, and show the full shipping address of the cardholder, if possible.
  - Detailed delivery information from the carrier, like confirmation of delivery.
  
- Other evidence : in the following situations, you should also include additional documentary evidence:If the customer has purchased the same products from you previously without lodging a dispute on those transactions, provide details of those transactions.
  - If the package was shipped to a business address, provide evidence that the customer works there.
  - If the transaction was completed by a member of the cardholder’s family or household, provide evidence of the connection between the two.
  

For a dispute involving a digital product or service, the file uploaded with the **Additional Details** file upload field on the **Payments > Disputes > Challenge Dispute** screen, should include access or activity logs.

This should include IP addresses, corresponding timestamps, and any detailed recorded activity.

The file needs to prove that the cardholder accessed or downloaded the digital product or service after the purchase.

For a dispute involving an offline service, using the **Additional Details** file upload field on the **Payments > Disputes > Challenge Dispute** screen, upload a file with the following:

- **Service date:** Evidence of the date on which the cardholder received or began receiving the purchased service, which should be before the dispute date.
- **Service documentation:**Documentation showing proof that a service was provided to the cardholder. This could include a copy of a signed contract, work order, or other form of written agreement.

With this type of dispute, the customer is claiming that you continued to charge them recurring payments after they had cancelled the associated subscription agreement.

To overturn a **subscription canceled** dispute, you need to prove to the bank that the subscription was still active as the customer had not followed your cancellation procedure.

You should also prove that the customer was aware of your cancellation policies and procedure. For example, demonstrate that the customer accepted the cancellation terms at the time of sign-up.

Using the **Customer Communication** file upload field on the **Payments > Disputes > Challenge Dispute** screen, provide the bank with a file showing:

- Any notifications sent to the customer of a renewal or continuation of the subscription, for example, pre-renewal email notifications, or
- Acknowledgement from the customer of their continued use of the product or service after the date they claim they canceled the subscription (if available).

#### Additional details text

In the **Additional Details** text field of the **Payments > Disputes > Challenge Dispute** screen, your response should include:

- **Disclosure of cancelation policy**: explain how and when your cancelation policy was disclosed to the customer prior to purchase.
- **Reason for cancelation refusal**: if you have refused to cancel the customer’s subscription, explain to the bank why why the customer’s subscription was not canceled. Reference terms in your cancelation policy, uploaded in the **Additional Details** file upload field.

#### Additional details file

Using the **Additional Details** file upload field on the **Payments > Disputes > Challenge Dispute** screen, upload a PDF of your cancellation policy, as presented to the customer.

Do not link to the cancellation policy in your response, as links will not be visited by the card issuer evaluating the dispute.

For **digital products or services**, the file uploaded in the additional details field should also provide server or other activity logs showing proof that the cardholder accessed or downloaded the digital product or service after the disputed cancelation date. This information should include IP addresses, corresponding timestamps, and any detailed recorded activity.

For **offline services**, you should also include in the file:

- **Service date:** evidence of the date on which the cardholder received or began receiving the purchased service, which should be before the dispute date.
- **Service documentation:**Documentation showing proof that a service was provided to the cardholder. This could include a copy of a signed contract, work order, or other form of written agreement.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

