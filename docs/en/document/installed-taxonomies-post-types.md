---
title: Installed Taxonomies and Post Types
url: https://woocommerce.com/document/installed-taxonomies-post-types/
---

Here we detail the taxonomies and post types specific to WooCommerce, which are fundamental for organizing and managing different content types within a WordPress site. Understanding these elements is crucial for developers and site administrators to effectively extend, customize, and manage their WooCommerce installations.

Two major building blocks in the WordPress environment are [taxonomies](https://wordpress.org/support/article/taxonomies/) and [post types](https://wordpress.org/support/article/post-types/).

- **Taxonomy.** A grouping of post types, such as categories and tags.
- **Post types.**With post types, WordPress creates a distinction in different content types. For example, by default WordPress has different post types for “posts”, “pages”, “media”, etc.

WooCommerce creates a few different posts types and a couple of taxonomies to group those post types.

WooCommerce installs the following post types and taxonomies — the first levels are post types, and the second levels are taxonomies for their top-level post type.

- Product: product
  - Product categories: `product_cat`
  - Product tags: `product_tag`
  - Product variation: `product_variation` (these are hidden from the UI)
  - Product visibility: `product_visibility`
  
- Shop order (Legacy) : shop_order
  - Order statuses: `shop_order_status`
  - Order refunds: `shop_order_refund`
  
- Shop coupon: `shop_coupon`
- Shop webhook: `shop_webhook`

WooCommerce makes use of existing [WordPress tables](https://codex.wordpress.org/Database_Description) to store some information:

- `wp_options` is used for store settings and information about the store such as store address, countries a store sells or ships to and other information that you would configure from **WooCommerce > Settings > General**.
- `wp_posts` and `wp_postmeta` contain information around products, coupons, and shipping classes.
- `wp_terms, wp_termmeta, wp_term_taxonomy, wp_term_relationships` are used for storing taxonomies such as product [tags, categories and attributes](https://woocommerce.com/document/managing-product-taxonomies/), as well as [shipping classes](https://woocommerce.com/document/product-shipping-classes/) and [tax classes](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/).
- `wp_commentmeta` stores [product reviews](https://woocommerce.com/document/product-reviews/).
- `wp_users` stores some customer information such as username, email address, and their assigned user ID number.
- `wp_usermeta` stores additional customer information such as their name, shipping address and billing address.

In addition to the above, WooCommerce also creates some custom tables that store some additional information.

- `wp_woocommerce_payment_tokens` stores the payment tokens used by payment gateways. The way this looks will vary depending on the payment gateway(s) you are using on your site.
- `wp_woocommerce_payment_tokenmeta` shows you additional customer payment information such as the last 4 digits of a card, card type, and expiry date.
- `wp_woocommerce_sessions` allows you to see active cart sessions from your site’s visitors.
- `wp_woocommerce_shipping_zones`, `wp_woocommerce_shipping_zone_methods`, and `wp_woocommerce_shipping_zone_locations` list your configured [shipping zones](https://woocommerce.com/document/setting-up-shipping-zones/), locations for these zones and the shipping methods available for these zones.
- `wp_woocommerce_tax_rates` and `wp_woocommerce_tax_rate_locations` provide an overview of the [tax rates](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#setting-up-tax-rates) that are configured and the locations they are configured for.
- `wp_woocommerce_api_keys` is where you can see your stored [REST API](https://woocommerce.com/document/woocommerce-rest-api/)keys.
- `wp_woocommerce_attribute_taxonomies` provides an overview of all of the attributes that are stored on your WooCommerce site.
- `wp_woocommerce_downloadable_product_permissions` stores a record of which customers have download permissions for which [downloadable products](https://woocommerce.com/document/managing-products/virtual-downloadable/).
- `wp_woocommerce_log` stores logs and event data from WooCommerce.

Starting from WooCommerce 8.2, released in October 2023, [High-Performance Order Storage (HPOS)](https://woocommerce.com/document/high-performance-order-storage/#background) is officially flagged as **stable** and is enabled by default for **new installations**. Shops launched using HPOS do not use the `shop_order` post type. As orders are not stored in the `_posts` table. If your store initially installed a WooCommerce version lower than 8.2. You can read about backwards compatibility, and migrating to the more performant HPOS, in our [HPOS documentation](https://woocommerce.com/document/high-performance-order-storage/#how-to-enable-high-performance-order-storage).

HPOS introduces dedicated tables for data such as orders, order addresses, and dedicated indexes. This results in fewer read/write operations and fewer busy tables. This feature enables ecommerce stores of all shapes and sizes to **scale to their maximum potential**.

instead of being stored in the `_posts` and `_postmeta` tables, HPOS stores order data in four dedicated order tables:

- `_wc_orders`
- `_wc_order_addresses`
- `_wc_order_operational_data`
- `_wc_orders_meta`

**Developers:**For detailed information about the schema used in HPOS. Refer to the Developer blog post detailing the [HPOS database schema](https://developer.woocommerce.com/2022/09/15/high-performance-order-storage-database-schema/)

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

