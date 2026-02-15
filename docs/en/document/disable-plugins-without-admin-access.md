---
title: Disable plugins without admin access
url: https://woocommerce.com/document/disable-plugins-without-admin-access/
---

Normally, you can disable plugins — including WooCommerce — on your WordPress site from the **Plugins > Installed Plugins** section of your admin area.

If you can’t access this part of your site’s admin area for any reason, there are other ways to disable plugins.

**Note:**This document is meant to serve as a helpful guide for advanced troubleshooting; however, the procedures described are beyond the scope of our [support policy](https://woocommerce.com/support-policy/) and we cannot provide direct assistance with implementing them. If you would like to seek assistance from a qualified WordPress/WooCommerce developer, we highly recommend [Codeable](https://codeable.io/?ref=z4Hnp) or a [Woo Agency Partner](https://woocommerce.com/development-services/).

Changing the name of a plugin’s folder in your site’s files will cause the plugin to be disabled. Follow these steps to disable a plugin via the plugin folder:

1. Log in to your site’s files using the file manager provided by your web hosting company or using a program such as Filezilla. Please reach out to your host for help with these steps.
2. Navigate to the `/wp-content/plugins/` directory.
3. Find the folder for the plugin you would like to deactivate.

1. Rename the folder, adding `-disabled` at the end. For example, if you are disabling the WooCommerce plugin with this method, you would rename the `woocommerce` folder to `woocommerce-disabled`.

1. Repeat steps 3–4 as necessary.

Another more advanced option is to disable a plugin through your site’s database.

Many hosts offer a tool called phpMyAdmin for accessing a site’s database, and it is used in the example below.

**Please note that making changes to your site’s database can have major effects on the entire site. Always back up your site before making any database changes, and contact your hosting provider for guidance if you’re unsure.**

1. Log into your site’s database.
2. Find the table called `wp_options`.

1. Find the row with the option called `active_plugins`.

1. Click on the pencil icon.

1. On the next screen, find the line with the name of the plugin that you want to deactivate. For example: `a:1:{1:0;9:19:"woocommerce/woocommerce.php";}`.

1. At the start of the line for that plugin, change `a:1` to `a:0`.
2. Click on “Go” in the bottom right corner to save your changes.

If you want to deactivate all of the plugins at once, you can click on the red X. This won’t delete the plugins from your site — it will only deactivate them.

[WP-CLI](https://wp-cli.org/) is a command-line tool for managing WordPress websites. It allows users to perform tasks, like updating plugins, configuring settings, and managing content directly from the command line, without needing to log into the WordPress dashboard.

If you’re not sure how to access WP-CLI for your site, reach out to your hosting provider to see if it is something they offer and how you can access it.

Once you access WP-CLI, you can apply the [commands to deactivate plugins](https://developer.wordpress.org/cli/commands/plugin/deactivate/).

Please note that WP-CLI is a third-party resource and our Happiness Engineers aren’t able to provide support with these commands. If you are using WP-CLI and have any questions, please reach out to your hosting provider.

Do you still have questions and need assistance?

- [Get in touch](https://woocommerce.com/my-account/create-a-ticket/) with a Happiness Engineer via our Help Desk. We provide support for extensions developed by and/or sold on WooCommerce.com, and Jetpack/WordPress.com customers.
- If you are not a customer, we recommend finding help in the [WooCommerce support forum](https://wordpress.org/support/plugin/woocommerce/) or hiring a Woo Agency Partner. These are trusted agencies with a proven track record of building highly customized, scalable online stores.[Learn more about Woo Agency Partners](https://woocommerce.com/development-services/).

