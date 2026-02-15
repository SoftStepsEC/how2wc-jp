---
title: WooCommerce System Tools
url: https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/tools/
---

WooCommerce includes a set of built-in tools to help troubleshoot issues, optimize performance, and manage key settings in one place. The WooCommerce system tools, including database cleanup and clearing your site’s cache, can help WooCommerce run smoothly.

You can access these settings from **WooCommerce > Status > Tools**.

A transient is a type of caching where data is stored in the database for a fixed period before it gets automatically deleted. This data can be quickly accessed, helping to save time and enhance the performance of your website.

A common example is the shopping cart contents. These are stored using transients so that a customer can leave the cart page and return later to find their items still there.

The below tools are available by default when WooCommerce is installed and active.

**Delete all shop and product transient data**: Clears temporary data related to shop and products.

**Delete all WordPress transient data**: Removes expired temporary data.

**Delete variations without a parent product**: These are product variations that no longer have an associated main product, which can cause errors such as incorrect product counts.

**Delete expired download permissions**: Removes permissions for downloads that have either expired or reached the limit of allowed downloads.

**Regenerate product lookup tables**: These tables store product data for quick access, speeding up the database. If they become out of sync with the products, incorrect product details may show up. Regenerating them ensures they match the actual product data.

**Reset product count cache**: This updates the cache for the number of products in each category or attribute. This can help correct any inaccurate product counts displayed on the site after settings have changed.

**Reset user capabilities to defaults**: Use this to reset user roles and permissions to the default settings. This is helpful if these a plugin or custom code has changed these, which can cause issues such as users losing access to admin pages they should be able to see.

**Delete active customer session data**: Clear data from all ongoing customer sessions, including cart contents.

**Reset template cache**: Clear the cache for theme templates. This helps when theme customizations aren’t showing up on the front end.

**Create missing WooCommerce pages**: Generate any missing default [WooCommerce pages](https://woocommerce.com/document/woocommerce-pages/) without overwriting the existing ones. This can be helpful if you find your cart of checkout pages are not assigned or are missing.

**Remove all tax rates**: Delete all configured tax rates, which is useful if you need to start over with a clean tax setup.

**Recreate shop images**: After you change the image size settings in the customizer or theme, this regenerates the shop images to ensure old sizes are updated. This process runs in the background and may take some time.

**Update the WooCommerce database**: This updates the WooCommerce database to the latest version. This can be useful if you suspect version mismatches may be causing issues. **Remember to always backup the database before running this update**.

This tool will recreate the full text search index for order addresses, which can help when trying to find order information based on a customer address.

You can find out more about FTS search [here](https://woocommerce.com/document/high-performance-order-storage/#full-text-search-indexes).

**Check for missing WooCommerce tables**: This ensures all required WooCommerce tables are present in the database.

**Reset WooCommerce Analytics cache**: This clears the analytics cache, which can be helpful if analytics appear inaccurate. You can then re-import data afterward from the Analytics ➔ Settings page.

The **Refresh Remote Inbox Notifications**tool allows you to update and fetch new notifications from the WooCommerce Marketplace. These notifications provide timely information, product updates, promotions, and other important messages.

To enable remote notifications in WooCommerce, the following setting must be enabled:

1. Navigate to **WooCommerce > Settings > Advanced > WooCommerce.com**.
2. Enable **Marketplace Suggestions**.

Once enabled, WooCommerce will display notifications relevant to the products and services available through the WooCommerce Marketplace, keeping you informed of useful suggestions and updates.The *Refresh Remote Inbox Notifications* tool allows you to refresh and synchronize new notifications from WooCommerce.com, ensuring that you are up-to-date with the latest marketplace suggestions, including relevant product updates, and best practices.

The **Delete an Inbox Notification**tool in WooCommerce allows you to remove specific notifications from your inbox using “slug.” This feature is useful for managing your inbox and keeping only relevant or important notifications visible.

Each inbox notification has a unique identifier known as a “slug.” You can find the slug of the notification you wish to delete and enter the **notification slug** in the textbox labeled **Search for inbox notification** and delete the specific inbox notification.

This tool triggers a fresh scan of the product catalog. When downloadable product paths are discovered that are not already covered by existing Approved Download Directory rules, they are added to the list, but are initially disabled.

[You can find out more about this here](https://woocommerce.com/document/approved-download-directories/#additional-tools).

This tool is used to delete the existing Approved Download Directory list entirely.

[You can find out more about this here](https://woocommerce.com/document/approved-download-directories/#additional-tools).

This tool helps to migrate old coupon data associated with orders to a new, simplified format. Specifically, it converts the existing `coupon_data` entries in order item meta to `coupon_info` entries, optimizing data storage and retrieval. This conversion process runs in the background using Action Scheduler, making it seamless and efficient without interrupting store operations.

This tool will only be enabled if there are coupon entries that can be converted (eg: it will show a notice in the description like “There are currently no entries to convert”)

For more detailed information on the transition from `coupon_data` to `coupon_info`, please refer to [Changes in Order Coupons Line Item Storage](https://developer.woocommerce.com/2024/02/08/changes-in-order-coupons-line-item-storage/).

This tool is used to schedule the action to delete expired transient files for running immediately. The expired transient files are cleaned every 24 hours.

If [High Performance Order Storage (HPOS)](https://woocommerce.com/document/high-performance-order-storage/) is enabled, some further tools become available.

The **Clean Up Order Data from Legacy Tables** tool is designed to clear old order data from legacy tables once HPOS is fully operational. This process optimizes database performance by removing outdated order information from legacy tables, provided that **HPOS is set as the authoritative table for order storage**and**compatibility mode is turned off.**

In the background, WooCommerce runs the command: `wc hpos cleanup all`.

This command removes old order data from legacy tables, verifying each order before removal to ensure that the legacy post data does not contain newer information than HPOS.

**NOTE:** The tool won’t remove placeholder records (posts with type `shop_order_placehold`) from the posts table.

The **Delete the Custom Orders Tables** tool allows for the complete deletion of custom orders tables, freeing up database space if you decide to revert from HPOS to legacy order storage.

This tool should be used when HPOS is not set as authoritative order storage and sync between HPOS and legacy tables is disabled.

Some extensions will add extra tools to this tab that are specific to their function:

- WooCommerce Square
  - Background Processing test
  - Clear Square Sync
  
- WooCommerce Smart Coupons
  - WooCommerce Smart Coupons Cache
  
- WooCommerce Bookings
  - Clean unused Person Types from DB
  - Clear expired In Cart bookings
  
- WooPayments
  - Clear WooPayments account cache
  
- WooCommerce Subscriptions
  - Generate Related Order Cache
  - Delete Related Order Cache
  - Generate Customer Subscription Cache
  

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

