---
title: Refunding Orders in WooCommerce
url: https://woocommerce.com/document/woocommerce-refunds/
---

In any business, at times you’ll need to refund your customers. With WooCommerce, you can quickly process refunds in two ways: Automatically or Manually.

- Automatic refunds are preferred, and when used, return customer’s money via the payment method used to pay for the order. This all happens via the “Edit Order” page in your WooCommerce admin area.
  - To process automatic refunds, your customer must have paid via a compatible payment gateway.
  
- Manual refunds record the order as refunded in your WooCommerce store, but you’ll still need to return the money manually to your customer.
  - In most cases this means accessing your merchant account and returning funds via that interface. This varies depending on the payment gateway used.
  

**Note:**Directly changing an order’s status to `Cancelled` or `Refunded` will not automatically refund your customer. Be sure to complete the refund process outlined below.

When processing refunds automatically, the order in WooCommerce has its status changed to “Refunded”, and the customer is refunded their money via the same payment method used to pay for the order, all in one process.

Once you’ve processed a refund automatically in WooCommerce, no further steps are necessary. Here are general steps to process an automatic refund via WooCommerce:

1. Go to **WooCommerce > Orders**.
2. Select the order to refund.
3. Go to the order summary, and select the **Refund** button.
4. Use the **quantity field** next to the product(s) to be refunded in the text box(es) that appear for each line item. The refund amount will automatically be calculated based on the quantities entered. If inventory is not managed, you can also enter the Refund amount for each line item, without adjusting the product quantity.
5. Add refund notes, if desired.
6. Select **Refund $[refund amount] via [payment gateway]**.
7. Check the order status. If the full order value is not refunded, the order status will not change to `Refunded` and the email that is sent to the shopper will refer to a “partial refund.”

**Note:**

Your account balance affects the way refunds are processed. The process is different for each payment gateway so for more accurate information on how the payment gateway you are using processes refunds, especially in case of a negative account balance, please refer to the payment processor documentation.

#### How do I know the payment was refunded?

When the refund has been processed via the payment method used, the payment gateway usually adds an order note indicating the funds have been returned via the payment method.

Look in the **Order notes** for a “Successfully refunded” message to verify the refund has been processed without issues. If needed, you can log into your account with the payment gateway used for the order and check there as well.

Generally the only time you’ll need to use the manual refund option is if you’ve taken payment with a payment gateway that doesn’t support automatic refunds, like [Cash On Delivery](https://woocommerce.com/document/cash-on-delivery/), or [Check Payments](https://woocommerce.com/document/cheque/). When manually refunding an order it is up to you to ensure your customer’s funds are returned outside of WooCommerce!

- Check : Consult the documentation or support of your payment gateway on whether manual refunds are available. You will either need to:
  - Log in to your payment method account and process the refund there.
  - Transfer the money from your bank account manually.
  
- **Scope**: Refunds normally extend to products, taxes, and shipping fees. However, any transaction fees charged by the payment gateway will usually be lost and not refunded.
- WooCommerce : Refunds can be processed through your Orders page. To manually refund an order:
  1. Go to: **WooCommerce > Orders.**
  2. Select the order to refund.
  3. Go to the order summary, and select “Refund” to start.
  4. Specify the **quantity of the product(s)** to be refunded in the text box(es) that appear for each line item. The refund amount will automatically adjust based on the products refunded. If inventory levels are not managed, you can also enter the Refund amount, without adjusting the product quantity.
  5. **Add refund notes**, if desired.
  6. **Select** “Refund $[refund amount] manually”.
  

**Note:**If the full order value is not refunded, the order will not have its status changed to “Refunded” and the email sent to the shopper will refer to a “partial refund.”

Items selected for a refund will be noted as refunded. Once the refund has been applied to the order, it will look like this:

While only one email template is used for “Refunded Order” emails, the phrasing in the email will differ depending on whether you have refunded the full value of the order:

- If the entire order value is not refunded, the email sent to the shopper will refer to a “partial refund.”

- If the entire order value is refunded, the email will state the order has been refunded.

Read more about [emails that WooCommerce sends](https://woocommerce.com/document/configuring-woocommerce-settings/emails).

It is possible to enter the quantity of product to be refunded as a fraction of the whole. This is useful for calculating associated taxes automatically in scenarios where a partial refund is issued.

After the refund is completed, the quantity field will always be rounded back up to the nearest whole number. However, the tax field calculations will not be affected and will continue reflecting the fraction entered prior to the refund being submitted.

In the example below, $4 of the product’s cost needed to be refunded, **along with an equivalent percentage of the taxes**. If we type the amount ($4) directly into the Total field, the taxes will not be calculated automatically, and we’ll need to work them out manually.

However, by working out what fraction our refund amount is of the total item cost, then entering that in the **Qty** field, the other tax fields are automatically calculated.

Here’s the calculation: **Refund Amount/Total = Qty** or for this example **4/15 = 0.26666667** – copy and paste the fraction into the **Qty** field and press the **Tab** key to trigger the calculation.

When processing a refund, you have the option to restock products by ticking the “Restock refunded items” box:

- Check the documentation of the payment gateway.
- If it’s a paid extension from WooCommerce.com, purchase it and give it a try! We have a [30-day money-back guarantee](https://woocommerce.com/refund-policy/) and can refund you with no hassle.
- Check with the payment gateway provider.
- [Ask us](https://woocommerce.com/my-account/contact-support/).

The best starting point is to create a page describing your policy and how a customer can request a refund.

For points to consider, we have sample refund policy page templates and a helpful reference in our [Refund Policy Page Guidelines](https://woocommerce.com/document/refund-policy-page-guidelines/). You can also review [WooCommerce.com’s Refund Policy](https://woocommerce.com/refund-policy/) for inspiration.

The next step is to share your refund policy with customers. There are several ways you might want to make it available to your shoppers:

- Adding the policy link into a menu in your store (many stores do this in their footer menu)
- Adding the policy link to order confirmation emails (More information about [how to Customize Shop Emails](https://woocommerce.com/posts/how-to-customize-emails-in-woocommerce/))

Go to [How to check if your payment gateway supports refunds](https://woocommerce.com/document/check-if-payment-gateway-supports-refunds-subscriptions-preorders/) and look up class constructor class properties.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

