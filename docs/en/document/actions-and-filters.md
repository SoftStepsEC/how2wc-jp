---
title: Hooks, actions and filters
url: https://woocommerce.com/document/actions-and-filters/
---

Hooks, actions and filters are powerful tools that allow you to modify and extend the capabilities of your WooCommerce site without altering the core code. This document will give you a brief overview of these and an example of how to apply them to your WooCommerce site.

**Note:**This document is meant to serve as a helpful guide for advanced troubleshooting; however, the procedures described are beyond the scope of our [support policy](https://woocommerce.com/support-policy/) and we cannot provide direct assistance with implementing them. If you would like to seek assistance from a qualified WordPress/WooCommerce developer, we highly recommend [Codeable](https://codeable.io/?ref=z4Hnp) or a [Woo Agency Partner](https://woocommerce.com/development-services/).

Hooks are a broad category that encompasses both actions and filters.

They provide a way for your code to interact with WordPress by ‘hooking into’ the underlying processes of the platform. Hooks are the points to which you attach your custom code.

Here’s an example of a hook used in WooCommerce:

- **Hook: woocommerce_thankyou**
- **Purpose**: This action hook executes after an order is completed on the WooCommerce checkout page.
- **Example Usage**: If you want to perform an action right after a customer completes a purchase, like sending a custom order confirmation message, you could hook a function to `woocommerce_thankyou`.

```
function custom_thankyou_action($order_id) {
    // Send a custom confirmation message or perform other actions
}

add_action('woocommerce_thankyou', 'custom_thankyou_action');
```

In this example, `custom_thankyou_action` is triggered by the `woocommerce_thankyou` hook and executes your custom code using the order ID provided by WooCommerce.

Actions are a specific type of hook. When you hook a function to an action, that function executes at a specific point in the WordPress execution cycle or when a specific event occurs.

For instance, you might use an action to send a welcome email when a new user registers on your site. Actions are about doing something extra or different at the time the action hook runs.

Here’s another simple example of using an action hook in WooCommerce:

- **Hook: woocommerce_before_cart**
- **Purpose**: This action hook executes just before the shopping cart contents display on the WooCommerce cart page.
- **Example Usage**: If you want to add a custom message or notification at the top of the cart page, you could use this action hook.

```
function display_custom_cart_message() {
    echo '<p>Don't forget to apply your discount code before checkout!</p>';
}

add_action('woocommerce_before_cart', 'display_custom_cart_message');
```

This snippet attaches the `display_custom_cart_message` function to the `woocommerce_before_cart` hook, which outputs a custom message to users at the beginning of the cart page.

Filters are another type of hook, focused on modifying data. When data passes through a filter, all functions attached to the filter hook process it before returning or displaying it.

This allows you to change outputs or values, such as customizing how you display product prices, modify titles, or alterithe default text of buttons. Filters modify or adjust data rather than triggering additional actions.

- **Filter: woocommerce_sale_flash**
- **Purpose**: This filter allows you to customize the sale badge text that appears on products when they are on sale.
- **Example Usage**: If you want to change the text of the sale badge on product listings to something more specific, like “Limited Offer,” you can use this filter.

```
function customize_sale_flash() {
    return '<span class="onsale">Limited Offer</span>';
}

add_filter('woocommerce_sale_flash', 'customize_sale_flash');
```

In this example, the `customize_sale_flash` function is hooked to the `woocommerce_sale_flash` filter to replace the default “Sale!” badge with “Limited Offer” on all products that are on sale. This allows for a simple customization that directly targets customer attention during promotional periods.

Adding custom actions and filters to your WooCommerce site requires an advanced knowledge of WooCommerce, hooks and PHP. You can refer to our [developer documentation on adding actions and filters](https://developer.woocommerce.com/docs/extensions/core-concepts/adding-actions-and-filters/)for further information on this topic.

If you need to further customize your site or extend its functionality, we highly recommend [Codeable](https://codeable.io/?ref=z4Hnp), or a [Certified WooExpert](https://woocommerce.com/experts/).

Do you still have questions and need assistance?

- [Get in touch](https://woocommerce.com/my-account/create-a-ticket/) with a Happiness Engineer via our Help Desk. We provide support for extensions developed by and/or sold on WooCommerce.com, and Jetpack/WordPress.com customers.
- If you are not a customer, we recommend finding help in the [WooCommerce support forum](https://wordpress.org/support/plugin/woocommerce/) or hiring a Woo Agency Partner. These are trusted agencies with a proven track record of building highly customized, scalable online stores.[Learn more about Woo Agency Partners](https://woocommerce.com/development-services/).

