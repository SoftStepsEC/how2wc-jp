---
title: Removing personal data from orders
url: https://woocommerce.com/document/managing-orders/removing-personal-data-from-orders/
---

WooCommerce has several settings that allow you to remove customer data from orders:

- Via **bulk editing**, useful if you need to manually anonymize orders in bulk.
- Via **account erasure requests**, a core WordPress function.
- Via **personal data retention settings** which automatically clear personal data after a chosen amount of time.

Once this option is activated, you can use bulk editing to manually anonymize many orders at once.

To enable this option:

1. In your store’s WP Admin dashboard, navigate to *WooCommerce > Settings* and click the **Accounts & Privacy** tab.
2. From this page, select the checkbox marked **Allow personal data to be removed in bulk from orders**.
3. Click **Save changes.**

The option to remove personal data will then be available for orders.

1. Navigate to *WooCommerce > Orders* in your store’s WP Admin dashboard.
2. Select the orders that need personal data removed.
3. From the **Bulk actions** dropdown field, choose **Remove personal data**.
4. Click the **Apply** button.

Once personal data has been removed, orders will appear on the *Orders* screen with removed information replaced with **[deleted]**, as shown in the image below.

On an individual order, personal data is removed as shown in the image below:

- The order is assigned to a **Guest** customer.
- Billing details are replaced with **[deleted]**.
- The email address is now [deleted@site.invalid](mailto:deleted@site.invalid).
- The phone number has changed to **+ 0 000 000 0000**.

Orders are anonymized this way so that sales stats are unaffected.

WordPress permits user detail deletion upon request via *Tools > Erase Personal Data*. This data removal can also be associated with the orders of this user.

WooCommerce includes a setting for whether personal data within orders should be retained or removed when processing account erasure requests. For details, [review accounts and privacy settings in WooCommerce](https://woocommerce.com/document/configuring-woocommerce-settings/accounts-and-privacy/).

WooCommerce lets you decide how long to keep order data on your store. You should specify how long your site will retain data in your privacy policy; consider what makes sense for local laws.

For details on the scheduled personal data removal options in WooCommerce and how to use them, [review personal data retention options in WooCommerce](https://woocommerce.com/document/configuring-woocommerce-settings/accounts-and-privacy/#personal-data-retention).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

