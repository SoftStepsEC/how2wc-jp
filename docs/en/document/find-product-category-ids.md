---
title: Find Product Category IDs
url: https://woocommerce.com/document/find-product-category-ids/
---

Some WooCommerce shortcodes ask for the category ID to display a list of categories. This document shows how you can locate the ID for your product categories.

More info at [Shortcodes included with WooCommerce](https://woocommerce.com/document/woocommerce-shortcodes/). Better yet, consider using the [blocks included in WooCommerce](https://woocommerce.com/document/woocommerce-store-editing/blocks/) alongside a theme that supports full site editing.

To find the product category ID:

1. Go to: **Products > Categories.**
2. **Hover** over a category name.
3. Select the **category** or the **Edit** link.
4. **Find** the address bar of your browser.
5. In that address bar, search for the `tag_ID=` part of the URL. The number after the equals symbol is the category ID. For example, in this screenshot: The section `tag_ID=16` where **16** is the ID of this Clothing category.

- **To find a product ID**, see the [Product ID section of our Adding and Managing Products documentation.](https://woocommerce.com/document/managing-products/#product-id)
- To find an order’s ID :
  - e.g. in `https://woocommerce.com/wp-admin/post.php?post=3572&action=edit` the order’s ID is `3572`
  
  1. From your Site’s admin area, navigate to **WooCommerce > Orders**.
  2. Click the order’s number to access the “**Edit Order**” page.
  3. Find the page URL.
  4. In the page URL, look for the post= query string. The number after this equals sign is the Order’s ID.
    - e.g. in `https://woocommerce.com/wp-admin/post.php?post=3572&action=edit` the order’s ID is `3572`
    
  5. This will often be the same as the order’s **number** from the order overview page, but can vary depending on your site’s configuration.
  

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

