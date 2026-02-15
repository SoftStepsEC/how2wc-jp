---
title: Local Pickup
url: https://docs.woocommerce.com/document/local-pickup/
---

**Note:**

This document is referring to the legacy WooCommerce local pickup options. If you’re using a WooCommerce Blocks-based checkout, you can find [configuration instructions for the local pickup block here.](https://woocommerce.com/document/woocommerce-blocks-local-pickup/)

Local Pickup is a WooCommerce core shipping method that allows the customer to pick up an order themselves. On this page, you’ll learn how to:

- Add Local Pickup as a shipping method.
- Configure Local Pickup.

Setting up Local Pickup starts by adding it as a [shipping method](https://woocommerce.com/document/setting-up-shipping-zones/#adding-shipping-methods-to-zones) to a shipping zone. Follow these steps to add the Local Pickup option:

**Note:**

This shipping method has to be added to a **Shipping zone**. If you haven’t configured your Shipping zones yet, please check our [Setting up Shipping Zones guide](https://woocommerce.com/document/setting-up-shipping-zones/) before proceeding.

1. Go to **WooCommerce > Settings > Shipping > Shipping zones**.

2. Click the **Edit** link in the Shipping Zone where you want to offer this method.

3. Inside the Shipping Zone, click the **Add shipping method** button.

4. Once you see the “Create shipping method” pop-up, select the “Local Pickup” shipping method and then click the **Continue** button.

5. Enter a **Name** that displays to customers in the cart and checkout pages.

6. Select the **Tax Status** to determine whether tax is applied to the Local Pickup **Cost**.

- By default, when selecting local pickup, the store address will be used to calculate taxes regardless of the customer’s address.

8. **(Optional)** Enter the Cost for this option. This is applied to the entire cart.

9. Click the **Create** button to finish.

Customers can select “local pickup” as an option in the cart/checkout if they reside in the shipping zone that includes it. This is what customers see in the cart and checkout:

**Cart view**:

**Checkout view**

**Note:** If customers aren’t seeing the local pickup option, but they reside in the shipping zone that includes local pickup, it may be an issue with the order of shipping zones. As explained in [Setting up Shipping Zones](https://woocommerce.com/document/setting-up-shipping-zones/), zones need to be sorted from the smallest geographical area to the largest. Make sure that the shipping zone that includes local pickup is listed above any other shipping zones that overlap (**ex.** If you offer shipping to the state of California but offer local pickup specifically to the postal code 90201, then the shipping zone for local pickup needs to be above the one for California state).

Developers can configure the following via the [WooCommerce Developer Documentation](https://developer.woocommerce.com/docs/legacy-local-pickup-advanced-settings-and-customization/):

- [Disable local taxes when using local pickup](https://developer.woocommerce.com/docs/legacy-local-pickup-advanced-settings-and-customization/#0-disable-local-taxes-when-using-local-pickup)
- [Changing the location for local taxes](https://developer.woocommerce.com/docs/legacy-local-pickup-advanced-settings-and-customization/#1-changing-the-location-for-local-taxes)
- [Custom emails for local pickup](https://developer.woocommerce.com/docs/legacy-local-pickup-advanced-settings-and-customization/#2-custom-emails-for-local-pickup)
- [Adding custom emails for local pickup](https://github.com/godaddy-wordpress/woocommerce-expedited-order-email) (3rd-party tutorial)

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

