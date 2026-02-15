---
title: PCI-DSS compliance and WooCommerce
url: https://woocommerce.com/document/pci-dss-compliance-and-woocommerce/
---

The Payment Card Industry Data Security Standard (PCI-DSS) is a set of actionable rules established by the [Payment Card Industry Security Standards Council](https://www.pcisecuritystandards.org/) (PCI SSC). Its primary goal is to promote consistent global data security practices and reduce credit card fraud.

These rules apply to anyone who stores, processes, or transmits cardholder data. For more information about PCI-DSS, review the [Quick Reference Guide](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Supporting%20Document/PCI_DSS-QRG-v4_0.pdf).

If you store, process, or transmit cardholder data as defined in the [PCI SSC glossary](https://www.pcisecuritystandards.org/pci_security/glossary), then **PCI-DSS applies to you**.

If you’re using a payment gateway that processes payments off-site or through hosted fields (such as Stripe, PayPal, or WooPayments), your site is not directly handling raw cardholder data. However, because your site still serves the checkout page, **PCI-DSS does still apply** — though your compliance scope may be significantly reduced.

[WooPayments](https://woocommerce.com/products/woocommerce-payments/) is the best option for merchants in eligible regions to accept PCI-compliant payments on their sites. [Learn more about PCI compliance in WooPayments](https://woocommerce.com/document/woopayments/our-policies/pci-compliance/).

The 12 core PCI-DSS requirements are as follows:

**Last updated**: 6 June 2025. This summary reflects the 12 core requirements as defined in **PCI DSS v4.0.1**. For full details and the latest documentation, visit the [PCI SSC website](https://www.pcisecuritystandards.org/document_library).

PCI compliance is often enforced by your payment processor, who may ask you to complete a self-assessment questionnaire (SAQ) or undergo scans by an [approved scanning vendor](https://listings.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors) (ASV).

PCI DSS compliance is ultimately the responsibility of the store owner. The core WooCommerce plugin is not PCI certified, as it does not handle cardholder data or process payments directly. However, once your site begins accepting card payments — even via a secure, hosted gateway like WooPayments — it falls within the scope of PCI DSS. Your site can meet compliance requirements by using a secure hosting environment, following security best practices, and integrating a PCI-compliant payment gateway.

Many PCI requirements apply to your broader environment — including your hosting provider, the plugins you use, and your policies around user access, updates, and security scans.

Here are some considerations:

1. Work with your host or network admin to configure firewalls appropriately.
2. Use strong passwords and ensure the hosting environment is secure.
3. **WooCommerce never stores card details**, and [official WooCommerce payment gateways](https://woocommerce.com/learn-more-about-official-partner-badging/) only retain partial data when using payment tokens (e.g., last 4 digits).
4. Use SSL on your checkout page, and make sure your host supports it.
5. Ask your host about malware protection and secure system maintenance.
6. Use WordPress roles and follow [security best practices](https://woocommerce.com/posts/woocommerce-security/) when managing admin users.
7. Log and review admin-level activity when possible, and restrict access to sensitive areas.
8. Coordinate with your host or developer to secure data access and storage.
9. Use an [ASV](https://listings.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors) if required by your payment processor.
10. Develop and maintain a policy around PCI-DSS, and conduct periodic risk assessments.

If you’re aiming for PCI compliance, start by:

- Choosing a [secure, PCI-aware hosting provider](https://woocommerce.com/hosting-solutions/).
- Using strong passwords and minimizing access to your admin environment.
- Never storing credit card data on your server or site.
- Using SSL to encrypt traffic on checkout and account pages.
- Keeping plugins, themes, WordPress, and WooCommerce up to date.
- Scanning your site regularly using an [ASV](https://listings.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors).

Do you still have questions and need assistance?

- [Get in touch](https://woocommerce.com/my-account/create-a-ticket/) with a Happiness Engineer via our Help Desk. We provide support for extensions developed by and/or sold on WooCommerce.com, and Jetpack/WordPress.com customers.
- If you are not a customer, we recommend finding help in the [WooCommerce support forum](https://wordpress.org/support/plugin/woocommerce/) or hiring a Woo Agency Partner. These are trusted agencies with a proven track record of building highly customized, scalable online stores.[Learn more about Woo Agency Partners](https://woocommerce.com/development-services/).

