---
title: Troubleshooting errors loading data
url: https://woocommerce.com/document/android-ios-apps-troubleshooting-error-fetching-orders/
---

If you are having trouble loading data in the WooCommerce Mobile App — such as your store stats, orders, products, or reviews — here are some potential issues that could be causing this problem and how to solve them:

If data in the app isn’t loading as expected, you’ll first want to make sure that the WooCommerce database doesn’t need an update. You can verify the WooCommerce database version by going to WooCommerce>Status from your site’s dashboard and ensuring the WooCommerce database version matches the version of WooCommerce installed on the site:

If the WooCommerce database version differs from the version of WooCommerce, make a complete backup of the site, then head to WooCommerce> Status> Tools, and click the `Update Database` button.

If the WooCommerce database is updated, one of the plugins on your site may be causing the issues you’re experiencing. In that case, we recommend disabling all of your plugins **except** for WooCommerce and Jetpack (if you’re using the Jetpack connection within the app) and then testing the app. If it works, turn on the plugins one at a time and test the app after each activation to find the plugin blocking the mobile app. We suggest starting with caching or security plugins, as they typically cause issues.

You may consider if the app stopped working when you recently installed a new plugin on your site or ran an update. It can help narrow down the issue so it’s easier to troubleshoot where the error is coming from.

If you find a plugin that is causing an issue, you can try reaching out to the plugin developers’ support team and let them know that it’s causing conflicts with the app. This way they can try to resolve any issues related to their plugin. Please also let our support team know so we can prevent conflicts on our end as well.

[Learn more about running a conflict test and best practices](https://woocommerce.com/document/how-to-test-for-conflicts).

**Note:** Sometimes a third-party plugin alters the type of a field in the app, then the app fails to recognize the value. We also can’t prevent other plugins from modifying our responses in the app. If a plugin is shown to be submitting invalid data, the best thing that we can suggest is to reach out to the plugin developers and ask them for assistance.

What may be happening is that the app or Jetpack is having difficulty maintaining a consistent connection to your site because the server doesn’t respond consistently to our requests.

This is sometimes due to the site performing poorly or the server being overloaded. There are a few things we can recommend to help with this.

First, make sure you have an updated version of PHP that matches WordPress’ requirements. You should reach out to your host if you need help getting this updated.

Next, ensure you don’t have any security blocks that may be preventing the app or Jetpack from communicating with your site. We’d suggest checking if you have any security plugins active on the site, thencontacting your hosting provider and searching server logs for any blocked requests to your WordPress installation’s REST API (or from our servers if you’re using the Jetpack plugin). Some hosts have a `fail2ban` log or `access.log`, for example.

If you’re using the Jetpack plugin,requests from our servers look like the following:

- File: https://yourgroovydomain.com/xmlrpc.php
- User-agent header: Jetpack by WordPress.com
- IPs: https://jetpack.com/support/hosting-faq/#jetpack-whitelist

Please ask your host to whitelist the IP addresses listed above. Note that these IP addresses could change (or more could be added) at any time, which could break your connection to Jetpack. For this reason, we discourage whitelisting specific IPs, although it may be the only option with some hosts.

If the issue remains, you can install a plugin like [Query Monitor](https://wordpress.org/plugins/query-monitor)to check which plugin or theme is the most taxing on your site’s performance. This will also let you find and remove any plugins that may not be entirely necessary but still have a negative impact onyour site.

Even if this doesn’t help with the connection issue, it will still have a positive impact on the site so it’s worth going through the process.

If your orders aren’t loading, it’s possible that some of the dates of your orders may not be in a valid format. To check this, please go to your site’s WP Admin > WooCommerce > Orders and verify your order creation date. They should all display a valid date format.

If you’re using the Jetpack plugin to connect the app to your site, make sure that the Jetpack connection is active and working correctly. You can verify some[known issues](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)or try[reconnecting your site](https://jetpack.com/support/reconnecting-reinstalling-jetpack/).

If you’re still having difficulty, please fill out our contact form to reach our support team from within the app by going to Menu > Settings > Help & Support > Contact Support.

