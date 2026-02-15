---
title: Checkout block
url: https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/
---

The Checkout block is part of a simplified, conversion-optimized checkout flow. It’s where a customer completes their purchase by entering shopping and payment information.

This page provides an overview of the structure of the Checkout block, its settings, and customization options to control your store’s brand identity — and create a visually appealing checkout journey for your customers.

- [Checkout block structure](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#checkout-block-structure)
- [Checkout block settings](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#checkout-block-settings)
- [Checkout Fields](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#checkout-fields-block)
- [Checkout Totals](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#checkout-totals-block)
- [Local Pickup delivery option](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#blocks-local-pickup)

**Note:**You can add the Checkout block to any page, but, for everything to function properly, you’ll need to first **designate your chosen checkout page** in your store’s [advanced settings](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/) via **WooCommerce > Settings > Advanced.**

The Checkout block contains two main inner blocks, [Checkout Fields](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#checkout-fields-block) and [Checkout Totals](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#checkout-totals) — two key components of the checkout experience. Use the [List View](https://woocommerce.com/document/woocommerce-store-editing/the-editor/#list-view) to see how these blocks fit together.

Many of the inner blocks that make up the Checkout block are completely dynamic and behave based on how your other settings in WooCommerce are configured. For example, the Payment Options block displays all payment methods that are:

- Available in your store, and
- [Compatible with the Checkout block](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/#compatible-extensions), according to their configuration in your [payment gateway’s settings](https://woocommerce.com/document/configuring-woocommerce-settings/#payments).

These inner blocks, which have no settings to configure in the block editor, are not listed in this documentation. You can click through them using the [List View](https://woocommerce.com/document/woocommerce-store-editing/the-editor/#list-view) to see a description of each inner block in the [settings sidebar.](https://woocommerce.com/document/woocommerce-store-editing/blocks/#block-settings)

Where possible, in the Settings sidebar, these blocks will point you to the relevant settings in WooCommerce so you can configure them.

The checkout block only has one setting to configure via the block settings sidebar: **Dark Mode Inputs**. Toggle this setting to style the checkout form fields and other inputs appropriately for pages and sections with dark backgrounds.

The **Checkout Fields** block contains the fields where a customer enters their information to complete their purchase. It contains inner blocks for each field; most of these inner blocks are dynamic. Their behavior is based on:

- The current customer’s order, and
- How your [WooCommerce settings](https://woocommerce.com/document/configuring-woocommerce-settings/) are configured.

The Checkouts Fields block is the **first block** nested inside the main Checkout block, It contains the following settings, which are shared with the Shipping and Billing Address blocks. Changing these settings in one block will also change them in the others.

- **Form Step Options**: Toggle this setting to add numbers to section headings and create a guided checkout flow.
- **Address Fields**: Use this setting to toggle the visibility of the Company, Address Line 2, and Phone fields. You can also set whether Address and Phone fields are required to complete checkout.

Additional blocks are nested inside the Checkout Fields block, all of which can be repositioned or renamed via the [List View](https://woocommerce.com/document/woocommerce-store-editing/the-editor/#list-view). Some contain additional settings, which are outlined below.

The Express Checkout block displays content only if a payment gateway that supports express checkouts ([WooPay](https://woocommerce.com/woopay/), ApplePay, Google Pay, etc.) is active. This block has no additional settings. To enable express checkout methods, we recommend using [WooPayments](https://woocommerce.com/payments/) (if it’s available in your area).

The Delivery block is where customers can choose between shipping their order or picking it up locally. It includes options in the Settings sidebar for customizing its appearance.

This block and the **Pickup Method** block will only display if:

- The [block version of Local Pickup](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#blocks-local-pickup) has been enabled via **WooCommerce > Settings > Shipping > Local Pickup**.
- The checkout page being edited is designated as the Checkout page via **WooCommerce > Settings > Advanced**.

#### Appearance

- **Show Icon**: Displays an icon next to the delivery options to visually differentiate them.
- **Show Costs**: Includes delivery costs alongside each option to provide customers with transparent pricing information.

The settings in this block are the same as those found in the [Checkout Fields block](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#checkout-fields-block). These settings are **linked**, meaning a change in one location changes it in the other.

The Terms and Conditions block facilitates customer acknowledgment of your store policies before a purchase can be completed.

- **Require Checkbox**: Toggle this setting to make it mandatory for customers to check a box confirming their agreement to the terms and conditions before they can proceed with their order.

Automatically link to your store’s policies in the block’s content by specifying your Terms and Conditions**and Privacy Policy pages.

[Learn more about page setup](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#page-setup) and [privacy policy options](https://woocommerce.com/document/configuring-woocommerce-settings/accounts-and-privacy/#privacy-policy).

The Actions block provides additional navigation options for customers during checkout.

- **Navigation Options**: Toggles the **Show a Return to Cart link** setting to show or hide a link that takes customers back to their cart to make changes.
- **Return to Cart Button**: When the return to cart link is enabled, a drop-down menu displays where you can select which page the link should return shoppers to.

The Checkout Totals block contains inner blocks displaying an order summary, a coupon entry form, and a list of the costs that make up the order total. All but one of these inner blocks are [locked](https://woocommerce.com/document/woocommerce-store-editing/blocks/#locked-blocks). These inner blocks can be moved up or down from their default location, but **not** removed.

The **Coupon Form** is the only block in the checkout totals section that is unlocked and **can** be removed.

Once the Checkout block is in place on your site’s [designated checkout page](https://woocommerce.com/document/woocommerce-pages/#tell-woocommerce-what-pages-to-use), local pickup settings become available.

[Local Pickup in WooCommerce blocks](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/woocommerce-blocks-local-pickup/) allows you to offer one or more pickup locations to your customers. Enabling this option (and configuring a pickup location via **WooCommerce > Settings > Shipping > Local Pickup**) displays the [Delivery and Pickup Method blocks](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#delivery-block) in your site’s Checkout block — a more streamlined way for shoppers to select a pickup location for their order.

This is different from the [legacy local pickup options](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/woocommerce-blocks-local-pickup/#difference-from-legacy-local-pickup) that were previously configurable when setting up shipping zones.

[Review options for Local Pickup in WooCommerce blocks](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/woocommerce-blocks-local-pickup/).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

