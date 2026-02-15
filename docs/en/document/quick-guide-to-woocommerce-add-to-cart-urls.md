---
title: Creating WooCommerce add-to-cart URLs
url: https://woocommerce.com/document/quick-guide-to-woocommerce-add-to-cart-urls/
---

Below, we’ll cover how to create specific, clickable links that add a product(s) to your customer’s cart via custom URLs. Using this URL or link, you can add items to the cart, specify the quantity, and even redirect to another page.

Add-to-cart URLs require the WooCommerce product ID to work. You can find a product’s ID in your store’s WP Admin dashboard via `WooCommerce > Products` by hovering over the product title — the product’s ID will then appear under the product title (see image below).

To add a [simple product](https://woocommerce.com/document/managing-products/add-product/#adding-a-simple-product) to the cart, use the URL structure shown below. Replace `example.com` with your site’s URL, and `PRODUCT_ID` and `QUANTITY` with your specific product’s details:

```
https://example.com/?add-to-cart=PRODUCT_ID&quantity=QUANTITY
```

To add a specific [variable product](https://woocommerce.com/document/variable-product/) to the cart, use the `variation ID` found in the Variations tab when editing the product. For example, if you wanted to use the blue variation with a logo, it would be ID #39 (see the image below).

```
https://example.com/?add-to-cart=VARIATION_ID&quantity=QUANTITY
```

For [grouped products](https://woocommerce.com/document/managing-products/add-product/#adding-a-grouped-product), include the product ID and quantities of each sub-product.

For one sub-product:

```
https://example.com/?add-to-cart=GROUPED_PRODUCT_ID&quantity[SUB_PRODUCT_ID]=QUANTITY
```

Repeat the following for each additional sub-product:

```
https://example.com/?add-to-cart=GROUPED_PRODUCT_ID&quantity[SUB_PRODUCT_ID]=QUANTITY&quantity[SUB_PRODUCT_ID]=QUANTITY
```

After a product is added to the cart, you can choose where to **redirect the customer**. By default, they will remain on the same page, unless WooCommerce’s settings are configured to redirect to your cart or checkout page.

To customize the redirect location, append the URL where you want the customer to land. For example, to redirect to the **checkout** page after adding a product to the cart, use the following:

```
https://example.com/checkout/?add-to-cart=PRODUCT_ID&quantity=QUANTITY
```

As another example, to redirect to the **cart** page after adding a product to the cart, use the following:

```
https://example.com/cart/?add-to-cart=PRODUCT_ID&quantity=QUANTITY
```

To **prevent a page from reloading** when items are added to the cart, enable AJAX via `WooCommerce > Settings > Products > General` in your store’s WP Admin dashboard.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

