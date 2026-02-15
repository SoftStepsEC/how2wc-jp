---
title: WooCommerce pages not displaying
url: https://woocommerce.com/document/pages-not-displaying/
---

If you are having trouble with WooCommerce pages not installing or displaying content correctly, here’s how you can fix this:

1. Create a new page.
2. Add the correct page shortcode.
3. Click **Publish**.
4. If you are using a version of WooCommerce earlier than 2.1.x, navigate to *WooCommerce > Settings > *tab** to select your newly created page (*tab* is the WooCommerce section to edit).
5. If you are using a version of WooCommerce later than 2.1.x, navigate to *WooCommerce > Settings > General*.
6. Click **Save**.

**Note:** This document does not cover every imaginable case. We recommend reviewing our [troubleshooting gu](https://woocommerce.com/document/woocommerce-self-service-guide/)[i](https://woocommerce.com/document/woocommerce-self-service-guide/)[de](https://woocommerce.com/document/woocommerce-self-service-guide/) to determine whether there is a conflict on your site.

Before [WooCommerce 2.1](https://developer.woocommerce.com/2014/02/10/woocommerce-2-1-is-live/), individual pages were used for account management and order “thank you” pages. As of version 2.1, these pages became endpoints.

[Learn more about WooCommerce endpoints](https://developer.woocommerce.com/docs/woocommerce-endpoints/).

**Note:** WooCommerce has traditionally utilized shortcodes to add dynamic content and features to pages. With the evolution of WordPress, the focus has shifted from shortcodes to more interactive, visually integrated blocks. [Learn more about WooCommerce blocks](https://woocommerce.com/document/woocommerce-store-editing/blocks/). While the block editor offers interactively customizable blocks and enhanced editing capabilities, we recognize many stores still lean heavily on shortcodes. You can still use these legacy shortcodes by adding them inside a [shortcode block](https://wordpress.org/documentation/article/shortcode-block/).

If you are using WooCommerce **2.1 or later**, page shortcodes are as follows:

- `[woocommerce_cart]`: Displays the cart page.
- `[woocommerce_checkout]`: Displays the checkout page.
- `[woocommerce_order_tracking]`: Displays the order tracking form.
- `[woocommerce_my_account]`: Displays the user account page.

Previously, page shortcodes for versions of WooCommerce **earlier than 2.1** were as follows:

- `[woocommerce_edit_account]`: Displays the *Edit account* page.
- `[woocommerce_edit_address]`: Displays the user account *Edit address* page
- `[woocommerce_change_password]`: Displays the *Change password* page.
- `[woocommerce_view_order]`: Displays the user account *View order* page.
- `[woocommerce_logout]`: Displays the logout page.
- `[woocommerce_pay]`: Displays the checkout *Pay* page.
- `[woocommerce_thankyou]`: Displays the *Order received* page.
- `[woocommerce_lost_password]`: Displays the *Lost password* page.

[See which shortcodes are included with WooCommerce](https://woocommerce.com/document/woocommerce-shortcodes/).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

