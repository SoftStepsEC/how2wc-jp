---
title: High-Performance Order Storage
url: https://woocommerce.com/document/high-performance-order-storage/
---

[High-Performance Order Storage (HPOS)](https://woocommerce.com/posts/platform-update-high-performance-order-storage-for-woocommerce/) (previously known as Custom Order Tables) is a solution specifically designed for ecommerce needs that provides a simple-to-understand, solid database structure.

It uses Woo’s Create, Read, Update, Delete (CRUD) design to store order data in custom tables optimized for WooCommerce queries, with minimal impact on the store’s performance.

Bringing HPOS to WooCommerce improves three properties that are essential for ecommerce stores:

1. **Scalability** The rise in the number of customers and customer orders increases the load on your store’s database, making it difficult to handle customer order requests and deliver a seamless user experience. With High-Performance Order Storage, you get **dedicated tables** for data such as orders, order addresses, and dedicated indexes, resulting in fewer read/write operations and fewer busy tables. This feature enables ecommerce stores of all shapes and sizes to scale their business to their maximum potential, without requiring expert intervention.
2. **Reliability** HPOS makes implementing and restoring targeted data backup simpler. You no longer need to worry about losing orders, inventory numbers, or client information due to reliable backups in these custom order tables. It also facilitates implementing read/write locks and prevents race conditions.
3. **Simplicity** You no longer have to go through a single huge database to locate underlying data and WooCommerce entries. With HPOS, you can browse through the separate tables and simple-to-handle entries, independent of the `_posts` table, to find data or understand the table structure. It also lets you develop new extensions, implement designs for shops and products, and modify WooCommerce with more flexibility.

Before version 8.2, WooCommerce relied on the `_post` and `_postmeta` table structures to store order information.

HPOS introduced dedicated tables for data such as orders, order addresses, and dedicated indexes. This results in fewer read/write operations and fewer busy tables. This feature enables ecommerce stores of all shapes and sizes to **scale to their maximum potential**.

Order data is synced from the `_posts` and `_postmeta` table to four custom order tables:

- `_wc_orders`
- `_wc_order_addresses`
- `_wc_order_operational_data`
- `_wc_orders_meta`

**Note:**

Before activating High-Performance Order Storage, make sure that any extension on your site that use custom post types (eg, [Woo Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/), [WooCommerce Bookings](https://woocommerce.com/products/woocommerce-bookings/), etc), are active. Deactivating these extensions before transitioning order data to HPOS may lead to data discrepancy. [Learn more about handling custom post types during HPOS migration](https://woocommerce.com/document/high-performance-order-storage/#handling-custom-post-types-hpos).

HPOS is enabled by default for **new installations** from WooCommerce 8.2 onward. Existing stores can switch from WordPress posts storage to High-Performance Order Storage by following the steps below.

To activate HPOS, existing stores will first need to get both the posts and orders table in sync:

1. In WP Admin, navigate to **WooCommerce > Settings > Advanced > Features**
2. Tick the **Enable compatibility mode (synchronizes orders to the posts table)** checkbox.
3. Once this setting is enabled, background actions will be scheduled.
  - The `wc_schedule_pending_batch_process` action checks whether there are orders that need to be backfilled.
  - If there are, it schedules another action (`wc_run_batch_process`) to backfill these orders to post storage.
  - You can either wait for these actions to run on their own (which shouldn’t take long), or you can go to **WooCommerce > Status > Scheduled Actions**, find the actions, and click the **Run** link under the action name (which appears when the mouse cursor hovers over the name).
  - This action will backfill **25 orders at a time**. If there are more orders to be synced, further actions will be scheduled once the previous actions are completed.
  
4. After both tables are successfully synchronized, you can select the option to switch to HPOS.
  - It is advisable to maintain compatibility mode for some time to ensure a seamless transition. In case of any issues, reverting to the `_posts` table can be done instantly.
  

Alternatively, you can also use the command-line interface (CLI) command `wp wc cot sync` to copy orders from the `_posts` table to HPOS tables. This command will automatically identify the appropriate table for data transfer based on the authoritative table setting.

**Note:** Turning the **Enable compatibility mode (synchronizes orders to the posts table)** setting off and on will also schedule the backfill process again if needed.

You can switch between data stores freely to sync the data between the tables.

- If you select the **WordPress posts storage (legacy)** option, the system will save the order data within `_posts` and `_postmeta` tables. Order tables are not utilized in this scenario.

- If you select the **High-performance order storage (recommended)** option, the system will save order data within the new WooCommerce order tables.

- If you select the **WordPress posts storage (legacy)** option and tick the**Enable compatibility mode** checkbox, the system will sync order data between the `_posts`, `_postmeta`, and WooCommerce order tables.

When the **High-performance order storage (recommended)** and **compatibility mode** options are both selected, WooCommerce populates the HPOS tables with data from `_posts` and `_postmeta` tables. [Learn more about synchronization between different tables](https://developer.woocommerce.com/2022/09/29/high-performance-order-storage-backward-compatibility-and-synchronization/#synchronization).

Before activating High-Performance Order Storage, make sure that any extension on your site that use custom post types (eg. [Woo Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/), [WooCommerce Bookings](https://woocommerce.com/products/woocommerce-bookings/), etc.), are active. These extensions store data in the WordPress posts table. When HPOS is enabled, order data is moved to new, optimized HPOS tables.

If an extension is reactivated post-migration, this could create data discrepancies, as the original data remains in the posts table and is not recognized by the system, which now looks in the HPOS tables. **To prevent such issues, keep the extensions that utilize custom post types active when enabling HPOS.**

If you have already deactivated the extension and enabled HPOS, follow these steps to correctly migrate the order data:

1. Go to **WooCommerce > Settings > Advanced > Features**.
2. Switch the **High-performance order storage** back to **WordPress post storage**, and allow the sync to complete.
3. Then, switch back to **High-Performance Order Storage**.

If you are using an extension that is not compatible with HPOS, the option to switch is disabled in WP Admin under **WooCommerce > Settings > Advanced > Features**.

- Click the **View and manage** link to review the list of incompatible extensions.
- You can also visit `https://example.com/wp-admin/plugins.php?plugin_status=incompatible_with_feature&feature_id=custom_order_tables` to review the list of incompatible extensions (replace `example.com` with your site domain).

**Note:** If you are using a third-party extension that isn’t working properly with High-Performance Order Storage, please notify its developers and ask them to add HPOS support. It is up to each respective extension developer to add support for HPOS to their extension. We have [developer resources and documentation](https://developer.woocommerce.com/2022/09/14/high-performance-order-storage-progress-report/) available to help with their integration efforts.

Full-text search (FTS) for orders is available in experimental mode from WooCommerce 9.0. This feature enhances search capabilities, allowing you to quickly search using order addresses and products.

To enable the experimental “HPOS Full text search indexes” feature:

1. Navigate to **WooCommerce > Settings > Advanced > Features**.
2. Make sure**Order data storage is set to HPOS**.
3. Under the **Experimental features** section, enable the **HPOS Full-text search indexes**option

**Note:** This feature only works **when Order data storage is set to HPOS**.

If you encounter problems, or if you need to continue working with extensions that are not yet HPOS-compatible, we recommend temporarily switching the **Order data storage**setting back to **WordPress posts storage (legacy)**.

To do this, navigate to **WooCommerce > Settings > Advanced > Features** and ensure that **compatibility mode**is enabled. If this was not already enabled, you may need to wait while order data is synchronized across data stores.

Once synchronization is complete, select **WordPress posts storage (legacy)** as your preferred option; you can also disable compatibility mode at this point. Once you are ready to re-enable HPOS, simply follow the instructions posted at the [beginning of this doc](https://woocommerce.com/document/high-performance-order-storage/#section-3). Finally, remember to save this page between changes!

As noted earlier, we also strongly recommend reaching out to the support teams for any incompatible extensions so they can take corrective action.

If you or your team needs to update your store’s custom code, extensions, or anything related to HPOS, check out our [Upgrade Recipe Book](https://developer.woocommerce.com/docs/features/high-performance-order-storage/recipe-book/) to find all the technical details.

No problem! While we do encourage everyone to switch to HPOS to enjoy the full benefits of a faster checkout experience for your customers, we understand that not everyone will want to try it right away. The feature is completely **opt-in** and you will be able to switch anytime.

We have actively communicated the upcoming HPOS changes with our developer community. We have several blog posts, guides on how to update extensions in GitHub, and full documentation. Despite our best efforts to encourage extension developers to make the switch, some developers may not accommodate HPOS. If one of your extensions is incompatible, we strongly recommend that you reach out to the respective developer’s support team and ask them to make the update. You will continue to be able to use the extension without HPOS if you already have it installed.

Businesses of **all sizes** will benefit from High-Performance Order Storage.

Existing stores will **not** be migrated over to HPOS automatically. The feature is completely **opt-in**. You can enable HPOS by following the steps mentioned above.

There are **no hosting restrictions**. Any host that is able to run WordPress and WooCommerce should have no trouble running HPOS. This should even increase performance in a number of ways after it is enabled. [Learn more about server requirements for WooCommerce](https://woocommerce.com/document/server-requirements/).

For more technical insight, take a look at our [developer blog FAQ](https://developer.woocommerce.com/2022/10/11/hpos-upgrade-faqs/).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

