---
title: Plugin conflicts with the WooCommerce Mobile App
url: https://woocommerce.com/document/conflicting-plugins-with-woocommerce-mobile-apps/
---

You may occasionally experience conflicts with extensions and plugins that can prevent the WooCommerce Mobile App from fetching and displaying data correctly.

These conflicts can occur due to the various ways third-party plugins and extensions interact with the core WooCommerce plugin. To ensure a smooth experience, it’s important to be aware of potential conflicts and know how to troubleshoot them effectively.

Below is a list of plugins and extensions with known compatibility issues:

- [Solid Security](https://wordpress.org/plugins/better-wp-security/) (formerly iThemes Security): In this plugin, ensure the **Filter Long URL Strings** option under *System Tweaks* is disabled.
- [Booster for WooCommerce](https://wordpress.org/plugins/woocommerce-jetpack/): Causes connection issues.
- [WP Go Maps](https://wordpress.org/plugins/wp-google-maps/) (formerly WP Google Maps): Causes issues when uploading product images.
- [Weglot](https://wordpress.org/plugins/weglot/): In this plugin, ensure that `/xmlrpc.php` is [excluded from automatic translation](https://support.weglot.com/article/95-how-to-exclude-urls-blocks-words-from-translation).
- [Product Labels for WooCommerce (Sale Badges)](https://wordpress.org/plugins/aco-product-labels-for-woocommerce/): Causes connection issues.
- [Disable Bloat for WordPress & WooCommerce](https://wordpress.org/plugins/disable-dashboard-for-woocommerce/): Disables WooCommerce Stats.
- [WPML](https://wpml.org/): Causes login issues.
- [Spam protection, Anti-Spam, FireWall by CleanTalk](https://wordpress.org/plugins/cleantalk-spam-protect/): Causes problems when retrieving orders in the mobile app.
- [Woody Code Snippets](https://wordpress.org/plugins/insert-php/): Snippets added via this plugin may cause issues in the mobile app.
- [WooCommerce addon for Envira Gallery](https://enviragallery.com/addons/woocommerce-addon/): May cause issues when adding products to orders.
- [Speed Booster Pack](https://speedboosterpack.com/) – Causes issues in the mobile app and on the checkout page of a Woo site.
- [Product Dynamic Pricing and Discounts](https://woocommerce.com/products/product-dynamic-pricing-and-discounts/): Causes products to not load in the mobile app.
- [wePOS – Point of Sales (POS) for WooCommerce](https://wordpress.org/plugins/wepos/): Causes products to not load in the mobile app.
- [WP Blog Post Layouts](https://wordpress.org/plugins/wp-blog-post-layouts/): Causes products to not load in the mobile app.
- [FOX – Currency Switcher Professional for WooCommerce](https://wordpress.org/plugins/woocommerce-currency-switcher/): Displays the incorrect currency in Stats.
- [CURCY – Multi-Currency for WooCommerce](https://wordpress.org/plugins/woo-multi-currency/): Displays the incorrect currency in the mobile app.
- [ElasticPress](https://wordpress.org/plugins/elasticpress/): Prevents the search functionality from working; only searching by SKU will work.
- [Airlift](https://airlift.net/): Breaks site connection by injecting comments into Jetpack API responses.
- [All-In-One Security (AIOS) – Security and Firewall](https://wordpress.org/plugins/all-in-one-wp-security-and-firewall/): The “Login Lockout” causes connection issues.
- [Payment Plugins for PayPal WooCommerce](https://wordpress.org/plugins/pymntpl-paypal-woocommerce/): Disrupts payment gateway functionality when using the app. *NOTE: Our official PayPal Payments plugin does not have any compatibility issues.*
- [WP 2FA – Two-factor authentication for WordPress](https://wordpress.org/plugins/wp-2fa/): blocks REST API and XML-RPC login attempts for users who have 2FA enabled, unless `two_factor_user_api_login_enable` filter returns true.

- [Checkout Field Editor](https://woocommerce.com/products/woocommerce-checkout-field-editor/): At checkout, custom fields (such as custom billing address information) are not visible in the mobile app.
- [Product Vendors](https://woocommerce.com/products/product-vendors/): Only Shop Managers and Admins can access the store via the mobile app. Vendors created using this extension cannot use the mobile app.

- [iBid Theme](https://modeltheme.com/portfolio/ibid-multi-vendor-wordpress-auction-theme/): Causes products to not load in the mobile app.
- [Lafka Theme](https://themeforest.net/item/lafka-fast-food-restaurant-woocommerce-theme/23969682): Causes products to not load in the mobile app, as well as incorrect variable product order quantities.
- See a list of [known issues with Jetpack](https://jetpack.com/support/getting-started-with-jetpack/known-issues/).

### In-Person Payments conflicts

- [Dokan](https://dokan.co/wordpress/): Prevents merchants from connecting an M2 Card Reader.
- [YITH Point Of Sale For WooCommerce (POS)](https://yithemes.com/themes/plugins/yith-point-of-sale-for-woocommerce/): Unsupported.

If you’re using the Jetpack plugin to connect the mobile app to your site, ensure that the Jetpack connection is active and functioning correctly. [Review common issues](https://jetpack.com/support/getting-started-with-jetpack/known-issues/) or [reconnect your site](https://jetpack.com/support/reconnecting-reinstalling-jetpack/).

If you’re still having difficulty, contact support from within the app by going to *Menu > Settings > Help & Support > Contact Support*.

