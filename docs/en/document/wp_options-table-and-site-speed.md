---
title: WP_options table and site speed
url: https://woocommerce.com/document/wp_options-table-and-site-speed/
---

When a WordPress site runs slowly, the `wp_options` table is often overlooked. This table stores key site data, like permalinks, site settings, scheduled posts, and widget details.

If you have already tried the most common steps for [troubleshooting a slow WooCommerce site](https://woocommerce.com/document/troubleshooting-a-slow-site/), reviewing the `wp_options` table would be a good next step.

Almost every page — whether on the front end or in the admin dashboard — runs the following query:

```
SELECT option_name, option_value FROM wp_options WHERE autoload = 'yes'
```

If this query isn’t optimized, it can slow down your site.

**Note:**This document is meant to serve as a helpful guide for advanced troubleshooting; however, the procedures described are beyond the scope of our [support policy](https://woocommerce.com/support-policy/) and we cannot provide direct assistance with implementing them. If you would like to seek assistance from a qualified WordPress/WooCommerce developer, we highly recommend [Codeable](https://codeable.io/?ref=z4Hnp) or a [Woo Agency Partner](https://woocommerce.com/development-services/).

The `wp_options` table in WordPress stores essential settings and site data, such as:

- Site URLs
- Active extensions and plugins
- Widget settings
- Cached information

Many extensions, plugins, and themes use `wp_options` to save their settings, making it a critical part of WordPress operations.

In WordPress, **autoload** is a setting in the `wp_options` table that controls whether specific data loads automatically on every page.

When an option has *autoload* set to **yes**, WordPress retrieves this data **every time a page loads**, which helps speed up access to frequently used settings. However, if too many options have *autoload* enabled, it can slow down the site by loading unnecessary data.

The `wp_options` table struggles with scaling because it isn’t designed to handle large amounts of data. As more records pile up, especially from extensions, plugins, or themes, it can become overloaded.

The *autoload* setting plays a big role in this. When options have autoload set to **yes**, WordPress loads this data on every page, which can slow down the site if there’s too much data marked for autoload. This constant loading of excessive data **increases page load times**, making it difficult for the site to scale efficiently.

A database index improves data retrieval speed in tables like `wp_posts`. It functions like a book index, enabling the database to quickly find specific information without searching through every record. For the `wp_posts` table, indexes on fields such as `post_date` or `post_type` allows WordPress to locate and load only the relevant posts more efficiently. Without these indexes, the database must examine each record individually, which can slow down page loads, particularly as the table grows larger.

The `wp_options` table does not have an index on the *autoload* field by default, since `wp_options` was originally intended to store only a limited number of settings. However, as sites grow and more plugins or themes store data in `wp_options`, the lack of an index on *autoload* can slow down queries, impacting site performance.

Object caching can help improve site performance by reducing the need to load data from the `wp_options` table on every page. When object caching is enabled, WordPress stores frequently used `wp_options` data in memory instead of retrieving it from the database each time. This **reduces database load** and **speeds up page load times**.

To set up object caching, you can use a third-party caching tool like [Redis](https://redis.io/solutions/caching/) or [Memcached](https://www.memcached.org/) and install a WordPress caching plugin that supports your chosen tool. After installation, configure the caching tool to work with WordPress, often by adding settings in the site’s `wp-config.php` file or using plugin settings. This setup allows WordPress to automatically cache and retrieve `wp_options` data from memory, improving overall site speed.

Contact your hosting provider for guidance on setting up caching on your site if you are not familiar with how to do this. They will know your site’s server environment and will be able to make the most tailored recommendations.

To prevent performance issues from the `wp_options` table, follow these recommendations:

- **Monitor table size**: Regularly check the size of `wp_options` to ensure it isn’t growing too large, ideally less than 500 rows. Large amounts of stored data can slow down queries.
- **Use proper storage**: Store extension, plugin, or theme-specific data in more suitable tables, like `wp_postmeta` for post-specific information, rather than in `wp_options`.
- **Remove unused data**: Delete outdated or unused options from `wp_options`, especially after uninstalling extensions, plugins, or themes, to keep the table lean.

Do you still have questions and need assistance?

- [Get in touch](https://woocommerce.com/my-account/create-a-ticket/) with a Happiness Engineer via our Help Desk. We provide support for extensions developed by and/or sold on WooCommerce.com, and Jetpack/WordPress.com customers.
- If you are not a customer, we recommend finding help in the [WooCommerce support forum](https://wordpress.org/support/plugin/woocommerce/) or hiring a Woo Agency Partner. These are trusted agencies with a proven track record of building highly customized, scalable online stores.[Learn more about Woo Agency Partners](https://woocommerce.com/development-services/).

