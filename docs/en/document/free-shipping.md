---
title: Free Shipping
url: https://woocommerce.com/document/free-shipping/
---

Free shipping is a WooCommerce core shipping method that allows you to add a “free shipping” option for customer orders if they either meet certain criteria (e.g. a minimum order spend amount) or if you want to offer free shipping to all customers within a certain geographical area.

On this page you’ll learn how to:

- Add free shipping as a shipping method.
- Configure free shipping.

Setting up free shipping starts by adding it as a [shipping method](https://woocommerce.com/document/setting-up-shipping-zones/#adding-shipping-methods-to-zones) to a shipping zone. Follow these steps to add free shipping:

**Note:**

This shipping method has to be added to a **Shipping zone**. If you haven’t configured your Shipping zones yet, please check our [Setting up Shipping Zones guide](https://woocommerce.com/document/setting-up-shipping-zones/) before proceeding.

1. Go to **WooCommerce > Settings > Shipping > Shipping zones**.

2. Click the **Edit** button on the shipping zone where you want to offer this method.

3. Inside the shipping zone, click the **Add shipping method** button.

4. Then, select the shipping method and click the **Continue** button.

5. Enter a **Name** that displays to customers in the cart and checkout pages.

6. Select the requirement that users must meet to receive free shipping from the “**Free Shipping Requires**” dropdown:

- **No requirement** — Offer Free Shipping to all customers in that shipping zone.
- **A valid free shipping coupon** — Free Shipping is available if the customer uses a coupon that offers free shipping (*see below: Create Free Shipping Coupons*).
- **A minimum order amount** — Free Shipping is available if the customer spends a minimum amount. Set this amount in the **Minimum Order Amount** field, which will appear if you choose this option.
- **A minimum order amount OR a coupon** — Free shipping is available if the customer spends a minimum amount *or* the customer uses a coupon that offers free shipping.
- **A minimum order amount AND a coupon** — Free shipping is available only if the customer spends a minimum amount *and* the customer uses a coupon that offers free shipping.

1. **Free Shipping – Minimum Order Amounts:** If you select one of the **minimum order** amount options, a checkbox will appear: **Apply minimum order rule before coupon discount**.

- **Box**is **unchecked :** WooCommerce determines if an order meets the “minimum order amount” for free shipping by using the order amount after applying a coupon discount (e.g., if an order is $30 and a customer applies a $10 coupon, the order amount of $20 is used to check eligibility for free shipping).
- **Box is****checked****:** the order amount **before** a coupon discount will be used to determine if the minimum order amount for free shipping is met (**ex**: if an order is $30 and the customer applies a $10 coupon, the undiscounted order amount of $30 is used to determine if the order is eligible for free shipping).

2. **Free Shipping with a Coupon:**If you offer your customers free shipping with a coupon, follow these steps to create and configure a free shipping coupon:

1. Go to **WooCommerce > Marketing > Coupons**
2. Select **Add Coupon**
3. Select Allow Free Shipping
4. Click the **Publish** button on the right to save

Customers can now use the coupon to get free shipping.

Click here if you need more information about creating and configuring coupons: [Coupon Management](https://woocommerce.com/document/coupon-management/)

These additional Advanced Settings/Customization are possible via code snippets as explained in the [WooCommerce Developer Documenation](https://developer.woocommerce.com/docs/free-shipping-customizations/):

- Enabling or Disabling Free Shipping via Hooks
- How to show only show Free Shipping
- How to show only Local Pickup and Free Shipping
- Only show free shipping in all states except…
- Take a look at our [premium Shipping Method extensions](https://woocommerce.com/product-category/woocommerce-extensions/shipping-methods/) for more options.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

