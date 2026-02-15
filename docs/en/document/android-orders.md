---
title: Orders
url: https://woocommerce.com/document/android-orders/
---

The **Orders** tab allows access to a list of orders, gives you the option to filter it by status, search for a specific order, and view and manage orders. To access this view, tap the **Orders icon** on the navigation bar, bottom-left.

#### Order Filter

Orders can be filtered by **Order Status** and/or **Date Range**.

1. Tap the **Filter icon** in the top toolbar
2. Select **Order Status** to filter by: All, Pending payment, Processing, On hold, Failed, Canceled, Completed, or Refunded.
3. Select **Date Range** to filter by: All, Today, Last 2 Days, Last 7 Days, Last 30 Days, Custom Range (select a Start Date and End Date)
4. After each filter selection, tap **Show Orders** to apply the filters
5. While filters are active a filter count is shown on the **Orders** page, and **CLEAR** appears as an option in the **Filters view**. Tap **CLEAR**followed by **Show Orders** to reset all Order filters.

#### Order Search

To **search** for a specific order or orders:

1. Tap the Search icon in the top toolbar.
2. Begin typing. The search will look for matching terms by first name, last name, product, and order number.

#### View and Manage Orders

**View Orders**

To view an order in detail, select an individual order in the list or tap the order displayed in the New Order notification.

The **Order Detail** screen provides details on:

- Order date, number, customer name, and order status
- A list of products ordered, quantity, attributes, and prices
- Payment details
- A button relative to the order status (e.g. **Mark order complete** for **Processing**, or **Issue refund** if available for **Completed**)
- Customer notes
- Shipping Details
- Billing info, including customer name, address, and email
- Order notes – private, system, and public

As of version 9.7, if an order has custom fields, the order details screen in the app will show a **View custom fields** button below the products on the order. Tapping the button opens a list of the custom fields.

**Fulfill an Order**

1. Open an order with a **Processing** status to display the **Order detail** screen.
2. Tap **Mark order complete**. The **Review Order** screen appears.
3. Verify the product details and shipping information, then tap **Mark order complete**.

Marking an order complete with the app triggers a **Completed Order** email to the customer, the same as if the order was fulfilled on your site. More info at [Email Notifications](https://woocommerce.com/document/configuring-woocommerce-settings/emails/#email-notifications).

**View Product Details**

Open the detailed view of any product in the order by tapping on the product.

**Add an Order Note**

1. Open an order and scroll down to the **Order Notes**section.
2. Tap **+ ADD A NOTE**
3. Type to add a note.
4. The note is private by default, but can be made visible to the customer by toggling the **Email note to customer** setting.
5. Tap **ADD** in the top-right corner to save the note.

**Contact the Customer**

1. Open an order and scroll down to the **Customer** section and select **SHOW BILLING.**
2. If a valid phone number was added during checkout, it will be visible underneath the billing address. Tapping the **ellipsis menu** to its right reveals options to **Call** or **Message** the customer (messages are sent to all numbers, but only succeed to mobile numbers).
3. If a valid email address was added during checkout, it will be visible with an **envelope icon** to its right. Tap the icon to email the customer.

**Refund an order**

- Open the order you’d like to refund (or partially refund) and scroll down to the **Issue Refund** button. Please note only orders with a **Completed** status will have the refund button option.
- Enter the quantity of each item you’d like to refund or press **Select All** in the top-right to select all products in the order
- To refund shipping charges, slide the **Refund Shipping** toggle to the right
- Press **Next**, and optionally leave an order note related to the refund
- Press **Refund** and a confirmation screen will appear
- Press **Refund** to confirm or **Cancel** to go back. After pressing **Refund** and the refund is processed, a notification will appear

If you’re using the Jetpack plugin to connect the app to your site, make sure that the Jetpack connection is active and working correctly. You can verify some[known issues](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)or try[reconnecting your site](https://jetpack.com/support/reconnecting-reinstalling-jetpack/).

If you’re still having difficulty, please fill out our contact form to reach our support team from within the app by going to Menu > Settings > Help & Support > Contact Support.

