---
title: Creating Sharable Checkout URLs in WooCommerce
url: https://woocommerce.com/document/creating-sharable-checkout-urls-in-woocommerce/
---

Sharable Checkout URLs make it easier to share ready-to-buy bundles with a coupon code through email campaigns, social media, or landing pages.

Below, we’ll cover how to create custom links that automatically add specific products and coupons to the cart then, redirect customers to the checkout page. You can include simple products with no additional options, individual variations, and coupons.

**Sharable Checkout URL Example:**

https://example.com/checkout-link/?products=123:2,456:1&coupon=SPRING10

Sharable Checkout URLs require the WooCommerce product ID to add the correct product to the cart.

To add a specific [simple product](https://woocommerce.com/document/simple-product/) to the cart, find the product ID in your store’s WP Admin dashboard via **WooCommerce > Products**. Hover over the product title. The product’s ID will appear under the product title.

To add a specific [variable product](https://woocommerce.com/document/variable-product/) to the cart, use the variation ID found in the Variations section of the Product data when editing the product. For example, to add the green, small variation in the following screenshot, it would be ID 83.

Use the following URL structure to add a single product to the cart:

```
https://example.com/checkout-link/?products=PRODUCT_ID:QUANTITY
```

Replace `example.com` with your store’s URL, and `PRODUCT_ID` and `QUANTITY` with your specific product’s ID and the quantity of the product to add to the cart. The product ID and quantity are separated by a colon.

Use a comma to separate additional products:

```
https://example.com/checkout-link/?products=
PRODUCT_ID_1:QUANTITY_1,PRODUCT_ID_2:QUANTITY_2,PRODUCT_ID_3:QUANTITY_3
```

**Note:**

Products that are limited to 1 product per order will only add a single product to the cart, regardless of the quantity added to the sharable URL.

Including a [coupon](https://woocommerce.com/document/coupon-management/) code will automatically apply the coupon to the customer’s cart.

```
https://example.com/checkout-link/?products=PRODUCT_ID:QUANTITY&coupon=COUPONCODE
```

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

