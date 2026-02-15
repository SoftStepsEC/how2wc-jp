---
title: Understanding the WooCommerce System Status Report
url: https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/
---

The WooCommerce System Status report is useful for troubleshooting issues with your store. Containing a wide variety of information and tools, you can check software versions, server settings, and more from within.

We’d encourage you to use the info below, before opening a support request with Woo Support. But we’re here to help if needed. To view your System Status report and copy it for support:

1. Go to: **WooCommerce > Status**.
2. Select**Get System Report** and then either **Copy for support** to copy and paste it into your [Support Request](https://woocommerce.com/my-account/create-a-ticket/) or **Download for support** to upload as a file attachment. The information included will help our support team narrow down the issue much quicker.

This provides general information about your site and WordPress installation and features you have enabled.

This provides general information about your server.

This tells you your current database version, and lists all database tables and whether or not they exist.

This shows what post types exist in your store and how many posts exist within each type. Varies according to what plugins you have installed.

Displays whether your connection is protected. Errors should be hidden from untrusted visitors trying to view your information.

This displays all plugins installed and active on your site. You can view current version numbers of your software and if any extensions have updates available.

This displays all plugins installed but inactive on your site. You can view current version numbers of your software and if any extensions have updates available.

These are in the `wp-content` but only specific file names. They replace/augment very specific functionality within WordPress.

This shows general settings for your site.

This shows page IDs and Permalinks designated as [WooCommerce pages](https://woocommerce.com/document/woocommerce-pages/).

For example: If your site is `https://example.com`, a user would get to the Cart page by going to `https://example.com/cart/`

This displays information about the current theme running on your installation.

This could be a more problematic area of a site, as there is no standard on what themes should and should not do, and non-Woo themes can cause conflicts with WooCommerce or one of its extensions.

If you’re experiencing issues with your site, we recommend temporarily switching to the free [Storefront Theme](https://woocommerce.com/storefront). If your problem is resolved while the Storefront theme is active, then the issue is with the theme. To resolve, check for updates or contact the theme developer to see if there is a fix.

This section shows any files that are overriding the default WooCommerce template pages, and also notes if the templates are outdated.

If you are experiencing trouble with any of the pages displayed, switching to the [Storefront](https://woocommerce.com/storefront/) theme will ensure that the original template files are used. For more information, see [Fixing Outdated WooCommerce Template Files](https://woocommerce.com/document/fix-outdated-templates-woocommerce/). For a long-term fix, you need to contact the theme developer.

See the documentation here for details on [what the WooCommerce Subscriptions extension adds to the System Status Report.](https://woocommerce.com/document/subscriptions-system-status-report/)

This shows scheduled action counts with previous and most recent dates. For more technical information about the Action Scheduler and FAQ, please see [ActionScheduler.org](https://actionscheduler.org/).

If you’re not able to access your site’s System Status Report for any reason, you have a couple of alternatives.

You can try accessing the relevant page directly by going to `[example.com]/wp-admin/admin.php?page=wc-status`, replacing `example.com` with your site’s domain.

Or you can navigate from your admin homepage to **Tools > Site Health > Info** and share the information from there. Much like the System Status report, the Site Health report also has a copy to clipboard button for easy sharing.

The Tools tab is where you will find WooCommerce system tools. These settings can assist with troubleshooting site issues, optimizing your site’s performance, and managing settings.

[Learn more about WooCommerce system tools.](https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/tools/)

The Logs tab is where WooCommerce keeps logs of all events happening in your store. Some logs, like `fatal-errors` are kept automatically, while others, like those for payment gateways, first need to be enabled in the relevant extension’s settings.

From this tab, you can click on the logs you would like to view in order to open the full log file. Or you can search within all log files by entering the term you are searching for in the search box.

If your site experiences a **fatal error**, they may be logged here under a log named `fatal-errors`. This is useful when debugging.

[Learn more about navigating and understanding WooCommerce error logs.](https://woocommerce.com/document/finding-php-error-logs/)

Users of WooCommerce Shipping & Tax have a fifth tab that allows them to check the health of the extension, specific Services in use, a debugging section, and more.

Health displays the status of connected parts – if anything with WooCommerce or Jetpack needs attention, and if Services is up or down.

Services display how specific Services are doing. Perhaps they’re unused, have an error needing attention, or working fine. You can enable debug logging to capture issues, and also contact our Support team to help configure your printer for printing shipping labels.

The Scheduled Actions tab allows you to view a log of processes that are run in the background on your site and include tasks such as subscription renewals, some customer emails, and checking for theme or plugin updates. You will be able to see the status for each task and which were completed, which are pending, and more detailed error information for any that failed to run.

[Learn more about WooCommerce scheduled actions.](https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/scheduled-actions/)

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

