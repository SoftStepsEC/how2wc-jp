---
title: Search your WooCommerce site database
url: https://woocommerce.com/document/search-your-woocommerce-site-database/
---

Searching the WordPress database on your WooCommerce site can help you quickly find and manage important information, like product details, order histories, and customer data.

**Note:**This document is meant to serve as a helpful guide for advanced troubleshooting; however, the procedures described are beyond the scope of our [support policy](https://woocommerce.com/support-policy/) and we cannot provide direct assistance with implementing them. If you would like to seek assistance from a qualified WordPress/WooCommerce developer, we highly recommend [Codeable](https://codeable.io/?ref=z4Hnp) or a [Woo Agency Partner](https://woocommerce.com/development-services/).

In your WooCommerce database, specific tables organize and store key information. Here’s a quick look at where to find essential data:

- **Orders and Order Information**: If you have [HPOS (High Performance Order Storage) enabled](https://woocommerce.com/document/high-performance-order-storage/#order-data-storage) custom order tables store order information. Otherwise, order information is stored in tables like `wp_posts` (for order data) and `wp_postmeta` (for order details like item prices, order status, etc.).
- **Products and Variations**: Found in the `wp_posts` table (for product listings) and `wp_postmeta` (for details like prices, SKU, and attributes). The table also stores variations as separate entries.
- **Shipping Settings**: Typically located in `wp_options` (for general shipping settings) and `wp_postmeta` (for order-specific shipping details).
- **Tax Settings**: Stored in `wp_options`, including tax rates, rules, and other configurations.
- **Customer Information**: Found in `wp_users` (for registered users) and `wp_usermeta` (for additional user details like billing and shipping addresses).

Some WooCommerce extensions such as [WooCommerce Subscriptions](https://woocommerce.com/document/subscriptions/develop/data-structure/), [AutomateWoo](https://woocommerce.com/document/automatewoo/performance/), [Product Bundles](https://woocommerce.com/document/bundles/bundles-data-structures-storage/) and [Composite Products](https://woocommerce.com/document/composite-products-data-structures-storage/) create additional custom post types or custom tables. For more information, refer to the documentation pages of the extension you are using.

**Please note that making changes to your site’s database can have major effects on the entire site. Always back up your site before making any database changes, and contact your hosting provider for guidance if you’re unsure.**

Most hosting providers offer a tool called phpMyAdmin to access your site’s database. However, it’s a good idea to check with your hosts to confirm which tools they provide.

In this example, we are going to search for a product in the database.

In the below example, the product “T-Shirt With Logo” has a permalink `t-shirt-with-logo` and the browser address bar shows the product’s post ID is 35.

As mentioned, products are stored in the `wp_posts` table of the database.

1. When you have accessed your site’s database, find the `wp_posts` table:

1. Click on Search, enter “product” in the `post_type` and click on “Go”. This will filter your view of the rows in `wp_posts` to just products.

1. You can then enter your search query in the “Filter rows” box. For the product “T-shirt with logo”, the search term “logo” will load products with that search term in the title. Searching for the product’s post ID (35) or the permalink (“t-shirt-with-logo”) would also load this product.

4. Once you have found the product you’re looking for, you can then edit, copy or delete directly from within the database.

Do you still have questions and need assistance?

- [Get in touch](https://woocommerce.com/my-account/create-a-ticket/) with a Happiness Engineer via our Help Desk. We provide support for extensions developed by and/or sold on WooCommerce.com, and Jetpack/WordPress.com customers.
- If you are not a customer, we recommend finding help in the [WooCommerce support forum](https://wordpress.org/support/plugin/woocommerce/) or hiring a Woo Agency Partner. These are trusted agencies with a proven track record of building highly customized, scalable online stores.[Learn more about Woo Agency Partners](https://woocommerce.com/development-services/).

