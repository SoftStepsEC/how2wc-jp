---
title: How Taxes Work in WooCommerce
url: https://woocommerce.com/document/setting-up-taxes-in-woocommerce/how-taxes-work-in-woocommerce/
---

There are more challenging tax configurations where an understanding of how taxes work in WooCommerce help with configuration and troubleshooting. Let’s take a look at a few nuances.

Related guides for additional reference:

- [Setting up Taxes in WooCommerce](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/)
- [How to configure specific tax setups in WooCommerce](https://woocommerce.com/document/configuring-specific-tax-setups-in-woocommerce/)
- [Setting Up EU VAT Rates for Digital Products](https://woocommerce.com/document/setting-up-eu-vat-rates-for-digital-products/)

**Product prices** can be defined as either:

1. Including tax
2. Excluding tax

When we say **defined including tax**, we are referring to the taxes of the store’s **base country**. E.g. if your store’s base country is the United Kingdom, you would define product prices with a tax rate of 20% (**shipping prices** are always **defined excluding tax**).

It’s important to keep in mind that if your prices include tax, the price visible to customers might change based on the country in which they are located, if that country’s tax rate is different from your store’s base country.

For example, in your UK-based store where only the one tax rate configured, the experience would be like this:

- You create a product with a tax inclusive price of £120.
- Customers with UK-based addresses pay £120 (£100 + £20 VAT).
- Customers outside the UK pay £100, because no tax rates would match their location.

**OR**

Your UK-based store sells to the UK (20%), France (19%), and Norway (25%), in which case the store works like this:

- You create a product with a tax inclusive price of £120.
- Customers in the UK pay £120 (£100 + £20 VAT).
- Customers in France pay £119 (£100 + £19 Tax).
- Customers in Norway pay £125 (£100 + £25 Tax).
- Customers outside the UK, France, or Norway again pay £100, because no tax rates are applicable to them.

[Here’s a practical example of how to configure this multi-country scenario](https://woocommerce.com/document/configuring-specific-tax-setups-in-woocommerce/#tax-only-certain-countries).

Some merchants may want to charge the same price regardless of location and taxes. The base price is then dynamically adjusted to compensate for the tax variance. [Follow this link for how to enable that](https://woocommerce.com/document/configuring-specific-tax-setups-in-woocommerce/#same-price-regardless-of-location).

Tax calculations are performed **per line**, not per item. The following calculations can be used to work out how much tax is applicable to a given price.

To calculate a tax rate of 20% for products prices that **exclude tax**:

```
Tax = Line Price * 0.2
```

To calculate a tax rate of 20% for products prices that **include tax**:

```
Tax = Line Price - ( Line Price / 1.2 )
```

Note how, when prices already include tax, the tax is not exactly 20% of the total Line Price. In the example in the previous section, if we simply calculate 20% of the total line price (£120), we’ll end up with an **incorrect £24**, which includes 20% of the base product and the taxes that were already added – hence using a different calculation.

Calculating taxes across various countries for tax exclusive prices is simple; **take the tax exclusive price and multiple by the tax rate.** Prices including tax is slightly more complicated.

Let’s take an example of selling from the UK (20% tax) to Germany. The UK price of the product is 120 including tax. If UK-based sellers do not need to charge tax when selling physical goods in Germany, the German price would look like so:

- UK price = 120 / 1.2 = 100
- UK Tax = 20
- German price = 100

Let’s take the same above example, but consider a digital good where tax would apply of the rate 19%. First, we remove the UK tax, then we apply the German tax like so:

- UK price = 120 / 1.2 = 100
- UK tax = 20
- German price = 100 * 1.19 = 119

A common feature request is to charge the same amount everywhere and absorb the differences in taxes. This would result in the following, based on the previous 2 examples.

When selling from the UK (20% tax) to Germany, the price of the product is 120 including tax. If UK-based sellers do not need to charge tax for physical goods in Germany, then it works like this:

- UK price = 120
- UK tax = 20
- German price = 120
- German tax = 0

The German price is the same as the UK price, except no taxes are included for the Germans, so the base product price is higher.

For digital goods, where a 19% German tax needs to be charged, the calculation would look like this:

- UK price = 120
- UK tax = 20
- German price = 120 / 1.19 = 100.84
- German tax = 120 – (120 / 1.19) = 19.1596

The German price is still the same, but as we’re collecting taxes, we see the base product price is just a bit higher than the UK.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

