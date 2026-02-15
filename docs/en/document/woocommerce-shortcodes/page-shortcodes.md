---
title: Page Shortcodes
url: https://woocommerce.com/document/woocommerce-shortcodes/page-shortcodes/
---

WooCommerce cannot function properly without a cart, checkout, and account area configured somewhere on your site. These shortcodes add those areas to pages on your site.

Starting with WooCommerce version 8.3, the Cart and Checkout Blocks are the default for new installations. Currently there is not a block based alternative for displaying the My Account area.

**Note:** We now recommend using the new conversion optimized [cart and checkout blocks](https://woocommerce.com/document/cart-checkout-blocks-status/) that are available as WooCommerce Blocks. Though in some cases the shortcode versions will have better compatibility with extensions.

**woocommerce_cart** – shows the cart page **woocommerce_checkout** – shows the checkout page **woocommerce_my_account** – shows the user account page **woocommerce_order_tracking** – shows the order tracking form

In most cases, the necessary shortcodes will be added to pages automatically via our [setup wizard](https://woocommerce.com/document/woocommerce-onboarding-wizard/) and do not need to be added manually.

Used on the cart page, the cart shortcode displays cart content, interface for coupon codes and other basic order information.

```
[woocommerce_cart]
```

Used on the checkout page, the checkout shortcode displays the checkout process.

```
[woocommerce_checkout]
```

Shows the ‘my account’ area where the currently logged in customer can view past orders and update their information. Guests who aren’t logged in will see a sign in form. As well as a registration form if you have it enabled in your [accounts & privacy settings](https://woocommerce.com/document/configuring-woocommerce-settings/#accounts-and-privacy-settings). Currently there is not a block based alternative for displaying the My Account area.

```
[woocommerce_my_account]
```

Lets a user see the status and details of an order by entering their order number and billing email. This is helpful for guest who don’t have an account on with your store but unlike the `cart`, `checkout`, and `my account` shortcodes (or blocks), it is not required. Here is an example of it being used on the `My Account` page for guests:

```
[woocommerce_order_tracking]
```

Show a full single product page by ID or SKU. This is helpful if you want to add a product to a page other than the shop page, for example, a post about a new product *(replace xx and xxx with the actual product number or sku)*:

```
[product_page id="xx"]
```

```
[product_page sku="xxx"]
```

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

