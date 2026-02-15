---
title: Paying for Orders
url: https://woocommerce.com/document/managing-orders/paying-for-orders/
---

Taking payment for an order is an important step where many pieces come together to offer your shoppers a smooth, easy experience that is also secure and promotes customer privacy.

In WooCommerce, each order can only accept one payment. Orders can be paid in a several different ways:

- Payment can be made upon order creation in the cart and checkout process. This is the standard flow, and will likely cover most orders.
- With some payment gateways, payment can be [made in person](https://woocommerce.com/in-person-payments/) via a supported card reader or using the [Tap to Pay functionality and the Woo Mobile app](https://woocommerce.com/tap-to-pay/).
- Orders in the Draft or Pending payment status can be paid via other order payment flows which can be entered via the:
  - [Pay for this order link](https://woocommerce.com/document/managing-orders/paying-for-orders/#pay-for-order-email-link) included in the Order Invoice email.
  - [Pay action button](https://woocommerce.com/document/managing-orders/paying-for-orders/#pay-button-my-account) In the Customer’s Account area in the Orders tab.
  - [Customer payment page → link](https://woocommerce.com/document/managing-orders/paying-for-orders/#customer-payment-page-link) found in the order’s detail page in the admin area. You can manually copy and share this link with the customer.
  

Below we’ll explore the details of the different ways **Pending payment** and **Draft** status orders can be paid. As well as customer verification methods that exist to protect customer privacy.

From the **Edit order** screen, select **Order actions** > **Send order details to customer** to email order details to the customer with payment instructions.

There will be a link accompanying their invoice in the email your customer receives. They can follow the link to enter the order payment flow.

If the customer is a registered user of your site, any unpaid orders assigned to will show a **Pay** option in the **Orders** tab of their My Account area.

If you are testing customer payment flows and wish to pay as the customer, consider using the [User Switching plugin](https://wordpress.org/plugins/user-switching/) (not made or endorsed by WooCommerce) to log in to the customer’s account and complete the payment as them.

On an individual order page in the admin area, you’ll see a link titled **Customer payment page →.**You can share this link with the customer for them to follow and complete payment. Sending an [order note to your customer](https://woocommerce.com/document/managing-orders/view-edit-or-add-an-order/#order-notes) is a great way to share these payment links if you want to include a custom message along with it.

The payment link may be specific to a customer. See **Customer Verification** for details.

WooCommerce has measures in place to ensure your shoppers’ orders are private. However, the behavior depends on whether an order belongs to a **Guest** or a customer that has an account on your site. It works as follows:

- If the order is **assigned to a registered customer** and they follow a payment link while **logged out**, the customer will be prompted to log in to their account to continue to the payment form.

- I f the order is assigned to the Guest customer , anyone who follows a payment link more than 10 minutes after the order was created will be prompted to verify the email address on the order to continue to the payment form.
  - **If no email address is associated with a guest order**, anyone with the payment link will be able to pay for the order.
  

**Developers:** The length of this “Grace Period” where orders can be accessed without verification is 10 minutes by default. This time period can be altered via the`woocommerce_order_email_verification_grace_period` filter [in WooCommerce’s codebase](https://woocommerce.github.io/code-reference/files/woocommerce-includes-shortcodes-class-wc-shortcode-checkout.html#source-view.407).

Order email verification is in place as a privacy feature ​​to prevent malicious actors from viewing order details of guest orders. However, we acknowledge that custom use cases exist which may work best without this feature enabled. If you’d like to disable guest order email verification, you can do so using the `woocommerce_order_email_verification_required` filter as demonstrated in the following code snippet.

```
add_filter( 'woocommerce_order_email_verification_required', '__return_false' );
```

**Note:**If you’re not comfortable modifying your site using code snippets we recommend working with a qualified developer. We highly recommend [Codeable](https://codeable.io/?ref=z4Hnp), or a [Certified WooExpert](https://woocommerce.com/experts/).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

