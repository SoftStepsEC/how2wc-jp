---
title: Completed Order Email doesn’t Contain Download Links
url: https://woocommerce.com/document/completed-order-email-doesnt-contain-download-links/
---

On some WooCommerce installs you can experience the following issue: when a customer purchases a downloadable product, the **Complete Order Email** **doesn’t contain any download link** for the customer to download purchased products. Here is how the email looks like in that case:

While it should look like this:

This happens because a SQL table called **wp_woocommerce_downloadable_product_permissions** is missing in your database.

When activating WooCommerce, a few new SQL tables are added in your database. You can find the list of all tables [here](https://woocommerce.com/document/installed-database-tables/). But this process can fail sometimes if the WordPress SQL tables prefix is too long: **the table name can’t contain more than 64 characters**.

The following table describes the maximum length for each type of identifier in the database. Please note that the maximum length for table is 64:

| Identifier | Maximum Length (characters) |
| --- | --- |
| Database | 64 |
| Table | 64 |
| Column | 64 |
| Index | 64 |
| Constraint | 64 |
| Stored Program | 64 |
| View | 64 |
| Alias | 256 |
| Compound Statement Label | 16 |

The WordPress SQL Table prefix is defined during WordPress install, and is stored in the file called **wp-config.php**.

To solve this issue, there’s only one single solution: renaming the WordPress SQL table prefix.

You can do this using a plugin from the [WordPress.org plugin directory](https://wordpress.org/plugins/search/DB+Prefix/).

Or you can do it manually. In that case you need to rename all tables names using a tool like phpMyAdmin, reduce the table’s prefix, and update the prefix value in **wp-config.php**. When you’ve done this, deactivate WooCommerce and re-activate it. Don’t worry you won’t lose any data, and re-enabling WooCommerce should force it to create missing SQL tables.

If you’re not familiar with how this is done, you can search for a guide on changing the WordPress database Prefix.

**Please create a backup of your database and of your site before doing such actions.**

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

