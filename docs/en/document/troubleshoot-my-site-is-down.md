---
title: Troubleshoot “My site is down”
url: https://woocommerce.com/document/troubleshoot-my-site-is-down/
---

WordPress sites occasionally go down; this guide is meant to help you get started with troubleshooting. This is when your site can no longer load or respond properly to requests due to an error.

You may be seeing any of the following:

- White screen displaying an error message (usually a critical or fatal error),
- White screen displaying no text at all (this is known as the “White Screen of Death” or WSOD).

**First, identify the error.**If an error is already showing directly on the page, copy/paste it to a safe place for troubleshooting later. Otherwise, there are a few ways to find out more information:

- **Check the site admin email**. WordPress may have sent a debug email when the fatal error occurred which contains the error details.
- **Check PHP logs.**These can be accessed through most hosting service’s control panel or via File Transfer Protocol (FTP). If you aren’t sure, check with your host for more information.
- **Enable debug mode.**WordPress has a debug mode which displays the error message instead of a blank page; see [Debugging in WordPress](https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/) for more information. Note that you’ll want to disable debug mode once you’ve solved the problem.

**Next, search for solutions or seek help.**Once you know what the error is, there are a variety of next steps to choose from:

- Starting with an online search may help you diagnose the issue, but be careful when following advice you find on the internet — especially if it advises technical fixes or database changes you don’t fully understand.
- If the error indicates a recently added or updated plugin/extension, you can try [manually removing it](https://wordpress.org/documentation/article/manage-plugins/#manual-uninstallation). If you aren’t sure how, check with your host for help. If that brings your site back online, consider contacting the plugin’s developer about the error.
- If the issue appears to be related to WooCommerce core or one of our extensions, [check the forums](https://wordpress.org/support/plugin/woocommerce/) or [contact support](https://woocommerce.com/my-account/contact-support/).

Once your site is back online, many problems are caused by conflicts which can help you narrow down the root issue. Once your site is fully backed up, consider reviewing our [conflict testing guide](https://woocommerce.com/document/how-to-test-for-conflicts/).

Check out our [Troubleshoot PHP errors](https://woocommerce.com/document/troubleshoot-php-errors/) article for more general information on errors pertaining to WooCommerce.

If you’d like to know more about the different PHP and other errors affecting WordPress, check out [Common WordPress errors](https://developer.wordpress.org/advanced-administration/wordpress/common-errors/) in WordPress.org’s [Advanced Administration Handbook](https://developer.wordpress.org/advanced-administration/).

