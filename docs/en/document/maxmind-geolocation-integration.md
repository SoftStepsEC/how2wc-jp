---
title: MaxMind geolocation integration
url: https://woocommerce.com/document/maxmind-geolocation-integration/
---

The free, core WooCommerce plugin enables store owners to automatically geolocate customers to display tax rates and shipping methods specific to their location. To determine this, WooCommerce integrates with [MaxMind GeoLite2](https://dev.maxmind.com/geoip/geoip2/geolite2/) geolocation data.

This document covers:

- Enabling geolocation.
- Creating a MaxMind account.
- Generating a MaxMind license key.
- Adding the MaxMind license key to your site.
- How your WooCommerce site updates the MaxMind geolocation database.

To enable the MaxMind geolocation integration:

1. In your site’s WP Admin dashboard, navigate to *WooCommerce > Settings > General*.
2. Scroll down to the **General options** section.
3. From the *Default customer location* dropdown, select **Geolocate** or **Geolocate (with page caching support)**.

Once geolocation is enabled, you’ll need to create a MaxMind account and configure MaxMind via the **Integration** tab in *WooCommerce > Settings*. If you do choose the **Geolocate (with page caching support)** option, you will see `?v=$hash` query strings added to your site’s URLs. For example, your URL may look like this `https://woocommerce.com/?v=bc74b2d76824` When you select this option, WooCommerce appends a user-specific hash of the user’s IP address to the URL so that the page can be cached for their reuse. This enables location-specific data (like tax rates and shipping information) to be cached for your customers as they navigate your store.

If you’d like to prevent these query strings from being added, select the Geolocate option instead.

1. Visit MaxMind’s [GeoLite2 sign-up page](https://www.maxmind.com/en/geolite2/signup).
2. Complete the registration form. If you’re unsure about which option to select in the *Industry* and *Intended use* fields, use **eCommerce Platform** and **Content customization** respectively.
3. After successfully submitting the form, you’ll receive an email containing a link to set your password. Click it and choose a secure password.

Now that you have a MaxMind account, you can create a license key.

1. Log in to MaxMind and navigate to [https://www.maxmind.com/en/account](https://www.maxmind.com/en/account).
2. Click the **Manage License Keys** tab in your user account dashboard.
3. Click the **Generate new license key** button.
4. Next, fill in the form to generate a license key.
5. Add a description (this can be the name of your store).
6. Select the **Confirm** button.
7. You will be presented with a new license key.**Copy and save this key somewhere safe immediately, as it will be shown only once.**

**Note:**

While you can only generate a maximum of 25 license keys on MaxMind, the same license can be used on multiple sites.

Finally, you need to add your license key to your store’s WooCommerce settings.

1. In your WP Admin dashboard, navigate to *WooCommerce > Settings > Integration > MaxMind Geolocation*.
2. Paste your license key into the *MaxMind License Key* field.
3. Click the **Save changes** button.

Your WooCommerce store is now ready to geolocate customers using MaxMind.

- The system automatically updates every 15 days, using WordPress’s built-in WP-Cron to trigger `woocommerce_geoip_updater`.
- If the MaxMind Database file on your server doesn’t seem to be updated correctly after this time, you can install the third-party [WP Crontrol](https://wordpress.org/plugins/wp-crontrol/) plugin to troubleshoot scheduled cron events in WordPress.
- Once this plugin is installed and active, you can go to **Tools > Cron Events** and check the next scheduled time for this event—or choose to run it manually.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

