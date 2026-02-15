---
title: EU VAT July 2021 changes, ecommerce, and WooCommerce
url: https://woocommerce.com/document/eu-vat-july-2021-changes-ecommerce-and-woocommerce/
---

On July 1, 2021, the European Union (EU) introduced new regulations related to value-added tax (VAT). Merchants selling across borders within the EU or importing to the EU will need to comply.

In this documentation we will provide key changes and scenarios for the new changes, although this is not exhaustive. We will use the Euro (EUR) currency symbol (€) throughout.

For general advice for how to configure taxes in WooCommerce, review our [Setting up taxes](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/) and [How to configure specific tax setups](https://woocommerce.com/document/configuring-specific-tax-setups-in-woocommerce) documentation.

These changes only affect**business-to-customer (B2C) sales**. Business-to-business (B2B) rules remain the same.

**WooCommerce merchants are responsible for complying with EU regulations.** Neither WooCommerce Inc. nor WooCommerce Ireland Limited are a marketplace or facilitator as defined by the EU.

- For EU merchants, the existing thresholds for distance sales of goods within the EU have been abolished and are replaced by a new EU-wide threshold of €10,000.
- The VAT exemption at importation of small consignments of a value up to €22 has be removed. This means all goods imported in the EU are now subject to VAT.
- Merchants can now file a single VAT return versus for each European country with the new [One Stop Shop](https://ec.europa.eu/taxation_customs/business/vat/oss_en) (OSS) or [Import One Stop Shop](https://ec.europa.eu/taxation_customs/business/vat/ioss_en) (IOSS).

In this document we will focus on **three different scenarios**:

1. [EU merchant selling to another EU shopper: under the €10,000 threshold](https://woocommerce.com/document/eu-vat-july-2021-changes-ecommerce-and-woocommerce/#eu-merchant-selling-to-another-eu-shopper-under-the-10k-threshold)
2. [EU merchant selling to another EU shopper: above the €10,000 threshold](https://woocommerce.com/document/eu-vat-july-2021-changes-ecommerce-and-woocommerce/#eu-merchant-selling-to-another-eu-shopper-above-the-10k-threshold)
3. [Non-EU merchant selling into the EU](https://woocommerce.com/document/eu-vat-july-2021-changes-ecommerce-and-woocommerce/#noneu-merchant-selling-into-the-eu)

**Key changes:**

- For EU merchants, the existing thresholds for distance sales of goods within the EU has be abolished and replaced by a new EU-wide threshold of €10,000.
- Merchants who qualify for this scenario can continue to charge the VAT rate of the EU country that the shipment originates from for all EU countries they ship to, and continue remitting to their local tax authority.

**Implications for these merchants:**

- Merchants can apply the same local VAT rate for all orders to EU countries.
- Merchants need to track whether they qualify for this exemption.

**Next steps that WooCommerce merchants in this scenario could consider:**

- Update tax settings in WooCommerce to set the VAT rate for all EU countries to be the same rate as their own country.
- Merchants can continue to make use of [tax- and VAT-related reports](https://woocommerce.com/document/woocommerce-analytics/#taxes-report) in WooCommerce Analytics.
- Merchants can give the option to EU businesses to opt to not pay VAT using the [EU VAT Number](https://woocommerce.com/products/eu-vat-number/) extension.

**Key changes:**

- Current country-specific distance selling thresholds have been replaced by a new EU-wide threshold of €10,000.
- Merchants may choose to use OSS to report all of their EU-wide sales. They no longer have the requirement to register for VAT reporting in each country based on the previous country distance selling threshold.

**Implication for these merchants:**

The VAT rate to be applied is that of the customer’s country.

**Next steps that WooCommerce merchants in this scenario could consider:**

- Update their tax settings in WooCommerce to set the VAT rate of each EU country to a specific VAT rate.
- Merchants can continue to make use of [tax- and VAT-related reports](https://woocommerce.com/document/woocommerce-analytics/#taxes-report) in WooCommerce Analytics.
- Merchants can give the option to EU businesses to opt to not pay VAT using the [EU VAT Number](https://woocommerce.com/products/eu-vat-number/) extension.

**Key changes:**

- All orders shipped to the EU are be subject to VAT. The exemption of small consignments of a value up €22 will be removed.
- For purchases over €150, the customer will be required to pay the VAT on delivery.
- Merchants should use the new IOSS filing.

**Implications for these merchants:**

They will need to decide whether to collect VAT or not during checkout. VAT will be collected based on the following criteria:

- For orders below €150, merchants can collect the VAT at checkout and then file a monthly VAT return using IOSS.
- If no VAT is collected on exports at checkout, the customer will be charged VAT by the carrier on delivery.
- For orders above €150, the customer will pay VAT.

**Next steps that WooCommerce merchants in this scenario could consider:**

- Update their tax settings in WooCommerce to set the VAT rate of each EU country to that specific VAT rate.
- They may also need to set a €150 limit for charging the VAT for orders outside of their country.
- Merchants can continue to make use of [tax- and VAT-related reports](https://woocommerce.com/document/woocommerce-analytics/#taxes-report) in WooCommerce Analytics.
- Merchants can give the option to EU businesses to opt to not pay VAT using the [EU VAT Number](https://woocommerce.com/products/eu-vat-number/) extension.
- Merchants should update their store’s [terms and conditions](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#terms-and-conditions) to help make it clear to shoppers that VAT is collected on delivery and not at the time of purchase.
- Optionally, a merchant can use a service like [Avalara AvaTax Cross-Border](https://www.avalara.com/us/en/products/industry-solutions/cross-border-solutions.html) to automatically classify items, calculate VAT at checkout ,and file with the authorities.

For the United States, cross-state taxes are similarly complex. [WooCommerce Tax](https://woocommerce.com/products/tax/) handles standard use cases. Merchants are encouraged to use solutions such as [TaxJar for WooCommerce](https://woocommerce.com/products/taxjar/) and [Avalara for WooCommerce](https://woocommerce.com/products/woocommerce-avatax/) when their requirements are no longer met by WooCommerce Tax.

For the EU, there are integrations that can help; more will be added when available.

- [Avalara AvaTaxCross-Border](https://www.avalara.com/us/en/products/global-commerce-offerings/avatax-cross-border.html) is available for merchants selling into the EU. It will automatically classify items, calculate VAT at checkout, and file with the authorities.
- [TaxJar](https://woocommerce.com/products/taxjar/) is better suited to US-based merchants than those within the EU.

- EU merchant selling to another EU shopper: under the €10,000 threshold :
  - Merchants can continue to use the tax offering in WooCommerce Shipping & Tax. It will calculate the standard VAT rate based on the merchant’s EU country.
  - However, are some limitations:
    - It will not return a different VAT rate for non-standard categories.
    - It will not track if the merchant sales surpassed the €10,000 threshold.
    
  
- EU merchant selling to another EU shopper: above the €10,000 threshold
  - These merchants should **no longer use WooCommerce Shipping & Tax**, as the incorrect VAT rate will be returned.
  - This is because the extension does not consider that the merchant is above the threshold of €10,000 and continues to return the local VAT rate.
  
- Non-EU merchant selling into the EU :
  - For merchants **opting to collect** VAT during checkout, **WooCommerce Shipping & Tax cannot be used** to calculate the VAT rate for shipments to the EU, as it will return a 0% rate.
  - For merchants opting to **not** **collect** VAT, they can continue to use WooCommerce Shipping & Tax. The customer will pay these duties on delivery, plus processing fees.
  

- [How to configure specific tax setups in WooCommerce](https://woocommerce.com/document/configuring-specific-tax-setups-in-woocommerce): an additional document to the more general [Setting up taxes in WooCommerce](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/), providing instructions for setting up some of the scenarios listed above.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

