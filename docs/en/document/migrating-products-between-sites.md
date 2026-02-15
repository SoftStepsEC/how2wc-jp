---
title: Migrating products between sites
url: https://woocommerce.com/document/migrating-products-between-sites/
---

Data portability is a fundamental advantage of platforms like WooCommerce and WordPress, WooCommerce empowers merchants to fully own and control their data. This ensures that you can freely transfer and utilize your data across different systems as needed. In the context of this documentation, we’ll cover some options for exporting and migrating WooCommerce products.

WooCommerce products are stored as a type of ‘post,’ meaning that you can migrate products between sites the same way you migrate WordPress posts.

Products are stored in your site’s database within the `_posts` table, with product meta data inside the `_postmeta` table. There are also relationships to things like terms and [organizational taxonomies](https://woocommerce.com/document/managing-product-taxonomies/), as they follow the same structure as posts. More info about WordPress’s data schema at [Database Description](https://codex.wordpress.org/Database_Description).

There are several good options to assist with the import/export of product data, or migrating your entire site and database.

To export an XML file containing product data:

1. Go to: **Tools > Export** and choose the content you wish to migrate.

1. Click the**” Download Export File**” button. An XML file is downloaded to your computer.
2. Go to the site to which you are moving the content and navigate to **Tools > Import**.
3. Select**WordPress** and follow the instructions.

More details can be found in this [WordPress.org article on Importing Content](http://codex.wordpress.org/Importing_Content#WordPress).

To import, export, change and merge product data, WooCommerce has a built-in CSV importer and exporter that covers the core product types, and many others. Check our detailed documentation on the built-in [Product CSV Importer and Exporter](https://woocommerce.com/document/product-csv-importer-exporter/).

If you have advanced product data, additional product types from extensions, or need a more efficient workflow for merging variable products, use our premium [Product CSV Import Suite](https://woocommerce.com/products/product-csv-import-suite/) extension. The premium extension includes several handy extras like a tool to delete all products on your WooCommerce store with a single click.

Both of these tools work with CSV data and can be used to migrate data, or do first-time product imports from a CSV.

## Migrating (all) data with Jetpack VaultPress Backup

[Jetpack VaultPress Backup](https://woocommerce.com/products/jetpack-backup/) is a subscription-based security and backup service for self-hosted WordPress sites. Jetpack VaultPress Backup supports live backups of WooCommerce and it can be used to migrate your WordPress website to another host. Jetpack VaultPress Backup allows you to:

- Restore your site to any past state while keeping all orders and customer data current
- Clone your entire site to a new host or server
- Protect your customer data and stay GDPR compliant
- Backup and restore custom WooCommerce tables

More info at: [Jetpack Backup: Migrate to a New Host](https://jetpack.com/support/backup/cloning/)

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

