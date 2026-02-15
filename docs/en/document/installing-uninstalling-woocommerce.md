---
title: Installing and Uninstalling WooCommerce
url: https://woocommerce.com/document/installing-uninstalling-woocommerce/
---

WooCommerce can be installed and uninstalled the same as any other WordPress plugin. The Setup wizard provides an optional step for installing and fully configuring WooCommerce.

Take a moment to review the [server requirements](https://woocommerce.com/document/server-requirements/) before installation, or you may encounter issues when using WooCommerce. If you need a new host or don’t have one yet, see our [recommended hosts](https://woocommerce.com/hosting-solutions/) who can get you set up with WooCommerce right away.

With WooCommerce activated, several items are added to your site for it to function properly:

- New menu items, [custom post types, and taxonomies](https://woocommerce.com/document/installed-taxonomies-post-types/) for orders, products, and more.
- New [WooCommerce Pages](https://woocommerce.com/document/woocommerce-pages/)
- New widgets and shortcodes.
- User roles for shop managers and customers.

Deactivating and deleting the installed plugin **does not remove** any data in your site database, so this requires an additional destructive step.

If you have an existing site and want to install WooCommerce, using the WordPress Admin is the most straightforward option as it handles everything for you.

To install WooCommerce:

1. Go to: **Plugins > Add New** **Plugin**.
2. Search****for “WooCommerce”.
3. Select**Install Now**.
4. Select **Activate Now, a**nd you’re ready for the WooCommerce Wizard.

When WooCommerce is activated for the first time, the [WooCommerce Setup Wizard](https://woocommerce.com/document/woocommerce-setup-wizard/) will be the next screen you see after clicking “Activate”. This helps you set up and configure your site with WooCommerce functionality.

For a full walkthrough of the Setup Wizard (also known as the Onboarding Wizard), please read through the [WooCommerce Setup Wizard documentation](https://woocommerce.com/document/woocommerce-setup-wizard/).

[On a multisite network installation](https://wordpress.org/support/article/create-a-network/), WooCommerce acts like most other plugins. Each site in the network, although sharing a database, stores its information in separate tables. Each store is a separate setup.

While you can network-activate plugins (*WordPress Admin > My Sites > Network Admin > Plugins > Add New*), such as WooCommerce and its extensions, you would be unable to share product databases, checkout, and user accounts across sites in the network.

Only themes and plugins are shared across the network of sites.

We always recommend using the latest version of all plugins and extensions on your site for security reasons. Further, the latest version of our plugins and extensions will always have the advantage of any features and functionality now available. As a consequence, this section is for guidance only.

To use a previous version of WooCommerce:

1. Disable and delete the current plugin.
2. Restore a previous backup of your store’s database.
3. Download a previous version of WooCommerce under the [Advanced View](https://wordpress.org/plugins/woocommerce/advanced/).
4. Upload the previous version under **Plugins > Add New**.
5. Activate the previous version of WooCommerce.

One warning — as mentioned in step two, you need to check and see if the version of the WooCommerce database has been updated or not. More often than not, it is updated with each version of WooCommerce, so you would need to restore your database from the previous version of WooCommerce to make sure everything works as it should.

This is why we highly recommend having backups in place alongside a staging environment to test new releases of mission-critical software like WooCommerce. See [Updating WooCommerce](https://woocommerce.com/document/updating-woocommerce/) for more information.

There are two things to understand when uninstalling or removing WooCommerce.

- If you deactivate and delete the plugin from WordPress, **you only remove the plugin and its files**. Your settings, orders, products, pages, etc… will still exist in the database.
- If you need to remove **ALL** WooCommerce data, including products, order data, etc., you need to be able to modify the site’s *wp-config.php* file **before** deactivating and deleting the plugin. Read more about how to do this in the [WooCommerce Developer Documentation](https://developer.woocommerce.com/docs/code-snippets/uninstall_remove_all_woocommerce_data).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

