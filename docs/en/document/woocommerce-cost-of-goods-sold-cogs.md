---
title: WooCommerce Cost of Goods Sold (COGS)
url: https://woocommerce.com/document/woocommerce-cost-of-goods-sold-cogs/
---

WooCommerce 9.9 introduces the **Cost of Goods Sold (COGS)** feature, which enables you to track the direct costs associated with the products sold in your store. This feature provides the necessary data to calculate accurate profit margins, empowering store owners to make data-driven decisions for pricing, marketing, inventory management, and more.

As of WooCommerce 10.3, the Cost of Goods Sold (COGS) feature is available as a stable release.

Cost of Goods Sold (COGS) is a key financial metric that allows you to calculate the direct costs associated with producing or purchasing the products that a business sells. By tracking COGS, store owners can determine the true profitability of their products and orders, leading to more informed business decisions.

Understanding the true cost of each product sold is fundamental to running a successful business. With COGS, store owners will be able to:

- **Accurate Profit Margins**: Calculate exact profit margins for every product and order.
- **Data-Driven Decisions**: Make data-driven decisions about pricing, marketing, and inventory management.
- **Enhanced Financial Insights**: Track and manage store performance with greater precision.

To enable the Cost of Goods Sold (COGS) feature, please follow the steps below:

1. Navigate to **WooCommerce > Settings > Advanced > Features**
2. Scroll down to the **Cost of Goods Sold** option
3. Check the box to enable**Cost of Goods Sold**
4. Click **Save changes**

Once the COGS feature is enabled, you can set the cost for individual products and variations.

For [simple products](https://woocommerce.com/document/managing-products/#simple-products), please follow the steps below:

1. Go to the Product Editor in the admin area.
2. Under the General tab, you’ll find a new field labeled **Cost of Goods**.
3. Set the cost value for the product (defaults to zero if not set).

For [variable products](https://woocommerce.com/document/managing-products/#variable-products), the Cost of Goods field in the General tab will display a default value inherited by all variations.

You can override the default value for each variation by entering a cost in the field for individual variations.

A bulk action is available to remove custom costs from all variations, reverting them to the default cost.

COGS details are also present within the order editor in the admin area. In the order editor, a new “Cost” column will display the cost of each item in an order (i.e., the individual product cost multiplied by the quantity of the line item). Additionally, the Cost Total will be shown next to the total order amount.

For orders with refunds, the Cost column will display the combined cost of the refunded items. Additionally, a tooltip is also available to show the cost per unit of each product.

If both the WooCommerce COGS feature and another COGS plugin are activated, you will see two cost totals. Since we don’t create a preference for the core feature or other extensions, you’ll need to decide which COGS source is best for your needs.

Currently, the COGS feature does not integrate with [WooCommerce Analytics](https://woocommerce.com/document/woocommerce-analytics/).

Yes, the COGS data is saved in the order item meta table. If the product’s price is updated after the order, the COGS for existing orders will not change.

Yes, the [WooCommerce core product CSV import/export tool](https://woocommerce.com/document/product-csv-importer-exporter/) has been extended to support the COGS field. You can now export the COGS values and create a CSV import file to import these values back into your store.

