---
title: Single Order Page and Manually Adding an Order
url: https://woocommerce.com/document/managing-orders/view-edit-or-add-an-order/
---

The single order page in WooCommerce gives you a detailed view of an order made by a customer on your store. Admins and shop managers can also add and edit orders from this page.

This document explains:

- The information found on the single-order page.
- How to edit an order.
- The different kinds of [order notes](https://woocommerce.com/document/managing-orders/view-edit-or-add-an-order/#order-notes) and how to add them.
- How to [manually add an order.](https://woocommerce.com/document/managing-orders/view-edit-or-add-an-order/#manually-adding-an-order)

From the **Single Order** page, you can view edit, and update order data. Some options are:

- Change the order status.
- Edit order items, like adjusting the products, quantity, prices, and taxes.
- Perform order actions, like email order details to the customer or regenerate download permissions
- Modify product **Meta** to edit product variations by removing and adding meta
- Apply coupons.
  - You will need to know the coupon code to apply to the order.
  - Coupon usage counts are tracked, and coupons can also be removed from orders.
  - The order must be unpaid for coupons to have an affect
  
- Add a fee. You can enter an amount or percentage to add a fee to an order.
  - Negative fees will apportion taxes between all other items, and will not make the cart total go below zero
  

**Note:** Changing order details like product meta, fees, coupons, shipping, etc. can only be done on existing orders that are in the “**pending**” or “**on hold**” status. Once orders are in “**processing**” or further along in the [order status flow](https://woocommerce.com/document/managing-orders/order-statuses/#visual-diagram-to-illustrate-order-status-flow) they are no longer editable.

The Order Details panel contains:

- Order number
- Payment details
- Order date and time
- Order status
- Customer details:
  - Username and email, together with a link to view their profile and other purchases the customer may have had in the past
  - Billing details
  - Shipping details
  

Most of the details in this section can be updated and/or changed.

- To change the date and time, use the dropdown date selector and the quantity selectors for the time.
- To change the status, choose the right status in the dropdown.
- To change the customer, select the current customer and search for the new customer.

Under “Billing” and “Shipping”, several other details can be changed. In order to do so, select the pencil icon next to each of them.

- Under “Billing”, the following things can be changed:
  - Billing address — this can also be loaded from the customer’s profile by selecting “Load billing address”
  - Email
  - Phone number
  - Payment method and details
  
- Under “Shipping”, the following things can be changed:
  - Shipping address — this can also be loaded from the customer’s profile or copied from the billing address
  - Customer provided note
  

Once you’ve made any necessary changes, press the **Update** button in the **Order actions** metabox to update the order.

The next panel on the order page is the **Order Items** panel. This contains the product items, the shipping details, and the order summary.

- Each product item row lists:
  - Product image
  - Product name
  - Single product Cost
  - Quantity
  - Total (Cost x Quantity, with discounts taken into consideration)
  - Taxes
  
- Below that, the shipping details are displayed. This will include:
  - Shipping method
  - Boxed items
  - Total cost
  - Taxes
  
- The last section contains an overview of the order costs . This section will change if an order is refunded. By default, it will include:
  - Items subtotal: the cost excluding tax
  - Coupon(s): the amount deducted based on the use of coupons; the coupons used are displayed left in this section
  - Shipping: the shipping cost for the order
  - Taxes: the amount of taxes for the whole order, which will be replaced by the tax code applied to the order
  - Order total: the total of the above costs
  - An overview of what is paid and the fees taken by the payment gateway
  

**Note:**In WooCommerce each order can only accept one payment. If an order has already been paid and your customer needs additional items, rather than adding new items to their existing order, [create a new order](https://woocommerce.com/document/managing-orders/view-edit-or-add-an-order/#manually-adding-an-order). You can then send your customer an [invoice with a link to pay](https://woocommerce.com/document/managing-orders/paying-for-orders/#pay-for-order-email-link).

Apart from refunding, order items cannot be edited, unless the order status is “**Pending payment”**, or “**On hold**.”

Product items are edited by selecting the pencil icon next to a product line to edit.

The following product items can be edited:

- **Add Meta**: Add and remove meta to change product variable options.
- **Quantity**: Number of items the customer is purchasing.
- **Total**: Line price and line tax **before** pre-tax discounts.
- **Tax**: Tax cost. For example, if a customer is tax-exempt you may want to remove the taxes.

**Other actions.** There are four more actions at the bottom of this window:

- Add item(s) will show you six new options:
  - Add product(s): Add additional products to the order.
  - Add fee: Add an additional fee, such as gift wrapping.
  - Add shipping: Add a shipping cost. When you’ve done this, select the pencil icon to update the name, the method, the cost, and the tax.
  - Add tax: Add an additional tax code to every section in the order.
  - Cancel: Cancel if you do not want to make any changes.
  - Save: Save once the changes are made.
  

- **Apply coupon**: If your customer forgot to add their coupon could or you want to reward the customer before they pay, selecting this option will show a modal that allows you to apply a coupon code.
- **Refund**: Refunds the customer. For more information about Manual and Automatic Refunds, see [WooCommerce Refunds](https://woocommerce.com/document/woocommerce-refunds/).
- **Recalculate**: After you’ve made changes to an order’s items, you can select “Recalculate” if you want to automatically perform new tax calculations based on store settings. This can be handy if you are adding or removing products, coupons, shipping methods, etc. Note that any tax changes that you’ve manually made will be removed as the tax settings in your store will apply based on the customer address.

To add custom meta fields, use the **Custom Fields** metabox. This is a [core WordPress functionality](https://wordpress.org/documentation/article/assign-custom-fields/) that can be very useful in the context of WooCommerce if you need to include additional data with your orders.

The **Order Notes** panel displays notes attached to the order and can be used for storing event details, such as payment results or reducing stock levels, or adding notes to the order for customers to view. Some payment gateways also add notes for debugging.

The following note types are added to orders:

- **System notes** (purple): Automatically added by WooCommerce or extensions, such as details of payment success or failure. If an order status changes as a result of a system process (e.g. checkout), the note will be purple. System notes are not visible to the customer. However, some order status changes will [trigger a notification](https://woocommerce.com/document/configuring-woocommerce-settings/emails/#email-notifications) to the store admin or customer.
- **General notes** (gray): Added by store admins or extensions for internal reference. These include manual order status changes made by admins, or private notes. Customers do not see these notes, but may receive notification of them. (e.g., when a shop manager changes the order’s status from processing to completed, an email may be sent depending on your [email settings](https://woocommerce.com/document/configuring-woocommerce-settings/#email-settings)).
- **Customer notes** (blue): Notes added manually to an order intentionally for the customer. Customers receive notes via email and are visible when viewing order details via the “My account” area. However, email notifications for customer notes can be disabled in the email settings

Notes can be a powerful tool for communicating with customers or other store managers. Need to add a tracking number for shipping? Is stock delayed? Add a customer note, and they are automatically notified.

To add a note:

1. **Add the content** of the note to the text area. (Some HTML is accepted, including <a> tags for hyperlinking.)
2. Select **Private note** or **Note to customer** in the dropdown.
3. Press the **Add** button.

Notes that are the result of an admin or shop manager action are grey or blue, and have “by {username}” after the timestamp.

To add an order:

1. Go to **WooCommerce > Orders**.
2. Select **Add order** at the top of the page. The Single Order page appears.
3. **Input** customer details, add line items, apply coupons, apply fees, and calculate totals. These are the same as [Editing or Adding Order Items.](https://woocommerce.com/document/managing-orders/view-edit-or-add-an-order/#editing-or-adding-order-items)
4. **Set a status** for the new order, e.g., If it needs to be paid, use “Pending payment.”
5. Click **Save**.

Use the Order Actions dropdown to Email order details to the customer with payment instructions.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

