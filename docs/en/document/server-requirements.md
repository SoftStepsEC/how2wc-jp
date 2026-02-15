---
title: WooCommerce Server Recommendations
url: https://woocommerce.com/document/server-requirements/
---

WooCommerce Server Recommendations are a guide to setting your site up for success and longevity. If the server running your WordPress site doesn’t meet our minimum requirements, then many plugins, including WooCommerce itself, won’t function as expected. Read over the WooCommerce Server Recommendations and additional items below.

The first step in setting up your WooCommerce-powered online store is to install WordPress and the WooCommerce plugin.**But before doing so, you should check your hosting environment. If they don’t meet these requirements, the security and performance of your site will suffer.

**To run WooCommerce, it’s recommended your host supports:**

- The latest version of [WordPress](https://href.li/?http://WordPress.org)
- [PHP](https://href.li/?https://www.php.net/) version 8.3 or greater
- [MySQL](https://href.li/?https://www.mysql.com/) version 8.0 or greater OR [MariaDB](https://href.li/?https://mariadb.org/) version 10.6 or greater.
- [HTTPS](https://href.li/?https://wordpress.org/news/2016/12/moving-toward-ssl/) support
- WordPress [memory limit](https://href.li/?https://woocommerce.com/document/increasing-the-wordpress-memory-limit/) of 256 MB or greater

[Apache](https://href.li/?https://httpd.apache.org/) or [Nginx](https://href.li/?https://nginx.org/) is recommended as the most robust and featureful server for running WooCommerce, but any server that supports PHP and MySQL will do. You can also read more about the [WordPress requirements here](https://href.li/?https://wordpress.org/about/requirements/).

**Note:** If you are in a legacy environment where you only have older PHP or MySQL versions, WooCommerce also works with PHP 7.4+ and MySQL version 5.67 or greater (or MariaDB version 10.4 or greater). However, these versions have reached their official End of Life and may expose your site to security vulnerabilities.

Other optional things that may be required include:

- cURL or fsockopen support, used by WooCommerce and by several of our integrations, e.g., [PayPal IPN](https://woocommerce.com/document/paypal-standard/#section-6)
- Some WooCommerce.com extensions require SOAP support
- Multibyte String support if you’re running a non-English store.
- Additional requirements listed at [Using Permalinks](https://wordpress.org/support/article/using-permalinks/#using-pretty-permalinks), if you want WordPress “pretty” permalinks.
- [Global SQL](https://href.li/?https://dev.mysql.com/doc/refman/8.0/en/sql-mode.html) mode options: `ERROR_FOR_DIVISION_BY_ZERO`, `NO_ENGINE_SUBSTITUTION`, `NO_ZERO_DATE`, `NO_ZERO_IN_DATE`, `STRICT_ALL_TABLES`

After installing WooCommerce, check if your server has the items listed using [the System Status page.](https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/)

Before you update your server settings for your WooCommerce site, it’s crucial to back up your site and files. Changes to the server environment can significantly affect your site’s performance and functionality.

Start by contacting your hosting provider if you need to change your server settings. They might update these settings for you or guide you on using their tools to make changes yourself.

You can also manually adjust PHP settings like `post_max_size`, `max_input_vars`, and `max_execution_time` in the `.htaccess` file. Access this file through your hosting provider’s file manager or via an FTP client like FileZilla. For assistance accessing or modifying this file, please contact your hosting provider.

Need a new host to meet the WooCommerce server recommendations? [Check out our hosting partners here](https://woocommerce.com/hosting-solutions/) or [dedicated WordPress web hosts listed here](https://wordpress.org/hosting/).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

