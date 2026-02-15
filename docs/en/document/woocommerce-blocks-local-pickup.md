---
title: WooCommerce Blocks: Local Pickup
url: https://woocommerce.com/document/woocommerce-blocks-local-pickup/
---

Local Pickup in Blocks is a new enhanced delivery method that allows you to easily offer one or more pickup locations to your customers. We’ve made it easier for you to setup local pickup options by providing a new, simple to use Local Pickup settings page.

This new method provides a streamlined customer experience by:

- Not requiring a buyer to enter a shipping address to select a pickup location
- Allowing you to include directions and/or pickup instructions for one or more locations
- Calculating taxes based on the pickup location rather than the store address
- Delivering a clean, modern UI that allows a buyer to easily toggle between the shipping and delivery methods you offer

1. To enable and use Local Pickup, your checkout must be using the [Checkout block](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/). You can [follow this guide](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/#using-the-cart-and-checkout-blocks) to replace your old Checkout.

2. Once that’s done, you can navigate to **WooCommerce -> Settings -> Shipping**, there, you will see the new Local Pickup tab.

3. Enable local pickup by clicking the “Enable local pickup” checkbox.

4. (Optional) You can rename the method name from Local pickup to anything else in the Title input.

5. (Optional) Choose how much to charge for Local pickup by enabling the “Add a price for customers who choose local pickup” checkbox, this will show a cost and tax status inputs.

**Note**: Since Local Pickup is not set within shipping zones, it will be available at checkout regardless of customer location. To restrict local pickup to only some shipping zones, use the [legacy local pickup shipping method](https://woocommerce.com/document/local-pickup/).

In order for Local Pickup to show up at checkout, you must add at least one location.

1. In the Local Pickup page, you can see the locations section below

2. Click on “Add pickup location” to open the modal.

3. A pickup location supports a name, a full address, and a dedicated details section. All of those fields are visible to the customer, who can use them to find the location. The address is also used to calculate taxes for the order if the customer chooses that location.

4. After you’re done adding locations, click “Save changes”.

Once Local Pickup is enabled, you will see 2 new blocks in Checkout, Shipping Methods block and Pickup Options block.

The Delivery block is clickable and allows you to toggle between Pickup options and Shipping options. This is the same behavior that customers will see.

All block titles and descriptions are customizable, as well as having some additional settings in the block settings sidebar to control the block’s appearance:

- **Show icon** – Toggling this option shows an icon of a delivery van on the “Ship” button, and an icon of a storefront on the “Pickup” button.
- **Show Costs** – When this option is enabled, dynamic subtitles will display that change depending on the cheapest shipping option a customer can select. When all options in that method are free, then “FREE” will show on the button.

The Pickup Method block supports adding text, separators, or images as inner blocks as well as adding a description and editing the title.

**(Optional)** You can also edit the delivery option labels, “Ship” and “Pickup” to any wording you prefer by clicking them and typing.

Local Pickup is different from the legacy local pickup options you enable in shipping zones, using both at the same time might cause a confusing experience for your customers. You will see a notice at the Local Pickup page if you have both enabled:

Unlike the shipping zones’ method, the new local pickup will always surface to customers even if they didn’t provide an address, and will not attempt to collect a shipping address.

The new local pickup will show up in its own step in Checkout block, and is visible if you select in from the shipping methods selector. This will provide you with more customization options and makes the distinction easier for customers.

The legacy local pickup bases taxes on the store address if selected (not customer address), the new one will base taxes on the selected location address, allowing better taxes reporting.

As it stands right now, there are some limitations with the new Local Pickup feature:

- Pickup locations won’t surface in Checkout if you have the shipping option “Hide shipping costs until an address is entered” enabled.
- When you have multiple packages in Checkout, those packages would be visually combined into a single package for Pickup options, this is so that the same selection is made to all packages so that taxes for that order use the same address.
- When you have multiple packages in which one of them isn’t collectible (doesn’t support local pickup), Local Pickup will be disabled.
- Local Pickup is offered to all customers regardless of shipping zones or address. If you need to restrict local pickup to certain shipping zones, we recommend using the [legacy local pickup method](https://woocommerce.com/document/local-pickup/).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

