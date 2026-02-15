---
title: Troubleshooting using Health Check
url: https://woocommerce.com/document/troubleshooting-using-health-check/
---

The [Health Check & Troubleshooting](https://wordpress.org/plugins/health-check/) plugin is useful for troubleshooting problems on your WooCommerce site, particularly those related to plugin and/or theme conflicts.

It allows you to do several tests in a browser session, without affecting visitors to your live site. However, keep in mind that, given a particular combination of plugins, themes, and hosting variables, **it may not always be the same as actually disabling plugins and themes**. In these circumstances, it could lead to **false positives**.

For info on testing for conflicts and other troubleshooting tips, review our [self-service guide](https://woocommerce.com/document/woocommerce-self-service-guide/).

Back up your site **before**installing and activating Health Check & Troubleshooting**.** There are two ways you can install it:

- Upload and install the .zip file to your WooCommerce site, or
- Via your site’s WordPress dashboard:
  1. Log in to your WordPress/WooCommerce site.
  2. Go to **Plugins > Add New**
  3. Search for **Health Check & Troubleshooting**.
  4. Click **Install Now** and then **Activate**.
  

Before troubleshooting, it’s best practice to make a backup of your site as a failsafe. [Learn more about backing up WordPress content](https://woocommerce.com/document/backup-wordpress-content/).

Health Check includes a **general overview** of your WordPress installation. In comparison, the [WooCommerce System Status Report](https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/) is much more in-depth.

To access your Health Check overview, go to **Tools > Site Health** (see below):

Health Check’s true power is its troubleshooting mode, allowing you to switch the theme and test plugins without impacting visitors to your site.

To troubleshoot, go to **Tools > Site Health > Troubleshooting**, then click **Enable Troubleshooting Mode** (see below).

Once in Troubleshooting Mode, you can control **which theme and plugins are enabled** in the troubleshooting session. Initially, **all** plugins are disabled.

To test WooCommerce, navigate to **Plugins**, and click **Enable while troubleshooting** (see below).

When viewing your site, you’ll see your specific session where the theme and plugins are set by Health Check. When visitors view your site, it appears normal. At this point, perform any necessary tests. If required, you can enable further plugins while troubleshooting from the Plugins page.

Note that Troubleshooting Mode does **not** put a payment gateway into sandbox mode; if an order is placed while the site is in troubleshooting mode, live payment will be taken.

To disable Troubleshooting Mode, click **Disable Troubleshooting Mode** in your site’s dashboard or via the Admin bar.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

