---
title: Managing Coupons in WooCommerce
url: https://woocommerce.com/document/coupon-management/
---

WooCommerce comes with built-in coupon creation and management tools. WooCommerce core offers fixed-cart, fixed-product, and percentage-based coupons. On this page, you’ll learn how to:

- Activate coupons in your store.
- Create a coupon.
- Set “Usage Restrictions” and “Usage Limits” for coupons.

Before creating your first coupon, you’ll need to enable coupon use in your store.****Enable coupons by following these instructions:

1. Navigate to: **WooCommerce > Settings > General > Enable coupons**
2. Tick the checkbox to**Enable the use of coupon codes**.
3. **Save Changes**.

(*More info at*:[Configuring WooCommerce – General options](https://woocommerce.com/document/configuring-woocommerce-settings/general/).)

The first step to offering coupons to your customers is to create one. Follow these instructions to create a coupon in WooCommerce:

1. Navigate to: Marketing >Coupons .
  - If no coupons exist in your store yet, you’ll see a screen prompting you to create your first coupon.
  - There’s also a button to learn more about coupons, which is how you might’ve ended up reading this document.
  - If you’ve made a coupon previously, you will see a list of coupons, their type, discount, etc…
  
2. Create a new coupon by selecting the **Add new coupon** button at the top of the screen.
3. Enter or generate a Coupon code . This is the code your customers use on the cart or checkout pages to apply the discount. You have two options for generating a code:
  - **Create/Enter a code**— Enter a coupon code in the Coupon Code field. You can include letters, numbers, and special characters (such as &, $, -, or @). Coupon codes aren’t case-sensitive, so “SAVE10” and “save10” will both work.
  - **Generate a** **Random Cod**e — Select the **Generate coupon code** button if you want WooCommerce to auto-create a coupon code for you.
  

1. **Enter** a Description (optional). This is information about the coupon for internal use (not seen by customers) like name of promotion/event, dates the coupon is valid, ticket number, customer name, etc.
2. Select the “Discount Type” from the dropdown menu. There are three choices:
  - **Percentage discount**— A percentage discount for selected products only. For example, if the cart contains three (3) t-shirts @ $20 each = $60, a coupon for 10% off applies a discount of $6.
  - **Fixed cart discount**— A fixed total discount for the entire cart. For example, if the cart contains three (3) t-shirts @ $20 each = $60, a coupon for $10 off gives a discount of $10.
  - **Fixed product discount**— A fixed total discount for selected products only. Customers receive a set amount of discount per item. For example, three (3) t-shirts @ $20 each with a coupon for $10 off applies a discount of $30.
  
3. **Enter** the coupon amount. Enter the amount without currency (i.e. : $, £) or percent (%) signs, regardless of the discount type you chose in the previous step. If you want to offer a discount of 10%, you’ll enter `10` in the field.
4. Check the box for “Allow Free Shipping” if applicable. You use this box when creating a “free shipping” coupon to use with the free shipping method. [You can learn more about this option here](https://woocommerce.com/document/free-shipping/#section-2).
5. Set a coupon expiry date (optional). Coupons expire/cannot be used on the date that is set.
6. Click the “Publish” button on the right-hand side if you do not need to add any usage restrictions or usage limits (covered in the next section).

Coupons have two other settings tabs used for the configuration of coupons: Usage Restrictions and Usage Limits. Below, we provide detailed descriptions of each of the options in these tabs.

In the usage restrictions menu are options to restrict the use of the coupon to certain cart totals, products, and customers. Below, we describe each type of restriction that you can apply to a coupon:

- **Minimum spend —** Set the minimum subtotal needed to use the coupon. **Note**: WooCommerce uses the sum of cart subtotal + tax to determine the minimum amount.
- **Maximum spend —** Set the maximum subtotal allowed when using the coupon.
- **Individual use only —** Tick the box if the coupon cannot be used in combination with other coupons.
- **Exclude sale items**— Tick the box if the coupon does not apply to products on sale. Per-cart coupons don’t work when a sale item is added afterward.
- **Products** **—** The coupon can be applied to these specific products, or these products must be in the cart for the coupon discount to apply.
- **Exclude products** **—** You cannot apply the coupon to these specific products, or these products cannot be in the cart for the coupon discount to apply.
- **Product categories** **—** The coupon applies to only these categories or requires specific categories in the cart for the discount to apply.
- **Exclude categories** **—** The coupon does not apply to these categories, or specific categories must not be in the cart for the coupon discount to apply.
- **Allowed Emails/Email restrictions**— These are email addresses that can use a coupon. Verified against customer’s billing email. WooCommerce also allows you to include a wildcard character (*) to match multiple email addresses, for example, `*@gmail.com` would allow any @gmail.com email address to use the coupon.

**Note:**

Leaving “Products” and “Exclude Products” empty allows the coupon to be applied to all products in your store.

Usage limits specify how many times customers can use a coupon. There are three ways to limit coupon usage:

- **Usage limit per coupon** **—** Each coupon has a usage limit indicating how many times all customers can use it before it becomes invalid.
- **Limit usage to X items —** Customers can apply the coupon to a maximum of X items before it becomes invalid. **Note:** This field only works if specific products are added to the `products` field in “Usage Restrictions”.
- **Usage limit per user** **—** Each customer can use the coupon a certain number of times before it becomes invalid specifically for that customer.

Once you’ve configured all settings, select **Publish** and your coupon is ready to use.

If you do not want the coupon to be immediately available, you can schedule it to become available on a future date/time using the option in the Publish settings:

Customers must add coupon codes to their cart or at checkout to receive the coupon discount. There is no functionality in WooCommerce core to automatically apply coupon codes for customers, so you need to send them via email, social media, or other marketing methods. If you are looking for ways to boost your store’s marketing campaigns and send coupons via emails to your customers, check out these two plugins to extend WooCommerce:

Powerful marketing automation for WooCommerce. AutomateWoo has the tools you need to grow your store and make more money.

The official email marketing solution every new WooCommerce store needs to get started without a fuss. Make beautiful emails that reach the…

Customers apply coupon codes on the cart/checkout pages by clicking the “Add Coupon” link. They then enter the coupon into the box and click “Apply” to add the discount to their order.

Customers will see an error message appear indicating why the coupon cannot be applied if it is not valid..(i.e. When a coupon expires).

Store managers can also add coupons to manually created orders by clicking the “Apply coupon” button at the bottom of the order details. These same steps also apply to an “unpaid” customer order.

Here are a few important notes about coupon discounts and how they are applied:

- **Taxes:**Coupons apply to product prices before tax calculation to ensure accurate tax calculation, preventing rounding errors by splitting the discount between each product in the cart. This behavior is more noticeable with Fixed Cart Discounts.
- **Shipping:** Coupons do not affect shipping since they can only apply to cart items. Shipping is not a cart item. Therefore, if a customer has a coupon covering the entire cost of the products in their cart but your store charges a $10 shipping fee, they will still pay the $10 shipping fee. The only exception is when you create a coupon for [free shipping](https://woocommerce.com/document/free-shipping/#section-2).

**Scope of support:**

We are unable to provide support for customizations under our**Support Policy**. If you need to customize a snippet or extend its functionality, we recommend working with a [Woo Agency Partner](https://woocommerce.com/development-services/) or a WooCommerce developer on [Codeable](https://www.codeable.io/partners/woocommerce/?ref=qGefA6#tiers).

Yes, if you are a developer, it’s possible to customize the Javascript driven Generate coupon code functionality by specifying length of code, and add a prefix and/or suffix. The WooCommerce core team intentionally excluded characters that could be ambiguous or difficult to read.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

