---
title: Setting Up EU VAT Rates for Digital Products
url: https://woocommerce.com/document/setting-up-taxes-in-woocommerce/configuring-specific-tax-setups-in-woocommerce/setting-up-eu-vat-rates-for-digital-products/
---

**VAT Updates starting in 2026:** Several European countries are updating their tax rules in the new year, most taking effect on January 1:

- VAT-related changes in Lithuania, the Netherlands, Slovakia, Finland, Germany, and Austria.
- Spain is requiring businesses to follow VERI*FACTU standards for invoice tracking by 2027. To ease the transition, we recommend using one of these handy extensions:
  - [Verifactu](https://quaderno.io/es/integraciones/verifactu/) by Quaderno
  - [FacturaDirecta Integration for WooCommerce](https://woocommerce.com/products/facturadirecta-integration/) by Kamalyon
  

To learn about these changes and how to prepare your Woo store, check our blog post: [Prepare your business for 2026 EU tax change](https://woocommerce.com/posts/2026-eu-tax-changes/)

EU VAT laws for digital goods changed on 1 January 2015, affecting B2C transactions only. VAT on digital goods must be calculated based on customer location, and you’re required to collect evidence of this via an IP address and/or Billing Address. In addition, you need to set up VAT rates in your WooCommerce store to charge the correct amount.

This guide is provided as-is and shows you how to set up rates specific to Digital Goods in this scenario. For general tax setup, please see:

- [Setting up Taxes in WooCommerce](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#shipping-tax-class)
- [How Taxes Work in WooCommerce](https://woocommerce.com/document/how-taxes-work-in-woocommerce/)
- [How to configure specific tax setups in WooCommerce](https://woocommerce.com/document/configuring-specific-tax-setups-in-woocommerce/)

For more details and information about setting up EU VAT rates for digital products, please see the [European Commission Taxation and Customs Union website](https://ec.europa.eu/taxation_customs/business/vat/telecommunications-broadcasting-electronic-services/content/guide-vat-mini-one-stop-shop-moss_en) for VAT MOSS (mini One-Stop Shop).

This documentation covers how to set up tax rates in WooCommerce, as well as how the platform handles taxes/VAT/GST based on these settings — **not** when or what to charge.

**We are not tax professionals**; our advice only applies to how to use our software. For advice on what — or when — to charge tax/VAT/GST etc., we recommend consulting a tax professional or accountant.

Every business is unique, and we are unable to cover all possibilities here.

If you’re only selling digital goods, VAT rates can be added under **Standard rates** in WooCommerce.

If you’re selling/distributing both digital and regular products, you can create and use a new **Additional tax class**, for example, **Digital Goods**.

To set up EU VAT rates in a new tax class:

1. Go to: **WooCommerce > Settings > Tax**.
2. Select the **Additional tax classes** setting.
3. Add a new tax class to the list, for example, **Digital Goods**.
4. Scroll down and click **Save changes**.

After saving the tax options changes, tax rates need to be assigned to this tax class.

## Setting Up the EU VAT Rates

The next step is to input the EU VAT Rates into WooCommerce.

The latest VAT rates can be found at the [Europa website](https://europa.eu/youreurope/business/taxation/vat/vat-rules-rates/index_en.htm#inline-nav-6). If VAT rates change, you need to update the VAT rates for your store.

1. **Go to**: **WooCommerce > Settings > Tax > Digital Goods**.
2. **Enter** rates for all EU member states. See our guide on [Setting Up Tax Rates in WooCommerce](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#setting-up-tax-rates).

At the time of the last update, Standard VAT rates are:

Alternatively, if you have a CSV file in the correct format, you can import the VAT rates to save time. Here are the above rates in CSV format with tax class **Digital Goods**: [vat_rates.csv](https://woocommerce.com/wp-content/uploads/2021/01/vat_rates.csv)

To import this file:

1. Go into the tax rate in this example, the**Digital Goods rates** section.
2. select the **Import CSV** button to the bottom right below the tax rates table
3. The importer appears with a **Browse…** button allowing file section.
4. Select the downloaded CSV file, and click the **Upload file and import** button

Once rates are uploaded, imported or input in the tax rate screen, the table is populated with the respective data. This has the country code in the **Country code** column, the respective rate in that country’s **Rate %** column, **VAT** as the **Tax name**, a **Priority** of **1**, and **Shipping** checked for all the rates.

With EU VAT rates set up, customers buying a product with the Digital Goods tax class are charged tax based on their location, not the store location. This is provided the **Tax options > Calculate tax based on** setting is set to **Customer shipping address**or **Customer billing address**.

To apply this tax class to digital products in WooCommerce:

1. Go to: **Products > All Products**.
2. Edit a product.
3. Go to **Product data > General section > Tax class**, and select the respective class from the dropdown.
4. **Update** the product to save the change.

You can also bulk-edit products:

1. Go to **Products > All Products**.
2. **Tick** the box to the left of each of the products you want to bulk-edit.
3. Select **Edit** from the bulk actions dropdown.
4. Click the **Apply** button to the dropdown’s right.

After clicking **Apply** the bulk edit view appears:

1. Choose the tax class from the **Tax class** dropdown.
2. Click **Update** to the bottom-left of the **bulk edit view** to apply the tax class to the selected products.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

