---
title: Orders Overview and Bulk Order Management
url: https://woocommerce.com/document/managing-orders/overview-and-bulk-management/
---

The **Orders** page found at **WooCommerce > Orders** displays a list of your store’s orders, which fills up as customers start making purchases in your shop. This page is a central location for finding and managing your shop’s orders.

This document explains:

- How to [review orders](https://woocommerce.com/document/managing-orders/overview-and-bulk-management/#orders-overview) placed by customers.
- How to change the information shown on the**Orders Page** with [Screen Options](https://woocommerce.com/document/managing-orders/overview-and-bulk-management/#screen-options).
- How to [search, filter, and arrange orders.](https://woocommerce.com/document/managing-orders/overview-and-bulk-management/#filter-and-arrange-orders)
- How to [preview an order.](https://woocommerce.com/document/managing-orders/overview-and-bulk-management/#previewing-orders)
- How to use [bulk actions](https://woocommerce.com/document/managing-orders/overview-and-bulk-management/#bulk-actions) to manage order statuses or remove personal data on multiple orders at once.

When a shop starts taking orders, they can be found on the **Orders** admin page. Navigate to **WooCommerce > Orders** to view your orders.

Each row displays several details. Some information is visible by default, and others can be added. WooCommerce extensions can add additional options as well. These are the default options available in WooCommerce:

- **Order** – order number and customer name
- **Date** – the date the order was created
- **Status** – the current status of the order
- **Total**– the purchase total of the order
- **Origin** – the traffic source of the order (Only available if [Order Attribution](https://woocommerce.com/document/order-attribution-tracking/) is enabled)

Some other options that can be enabled but are not pictured above are:

- **Billing** – the customer’s billing address
- **Ship to** – where the order will ship to
- **Actions** – shortcuts for changing the order status depending on its current state

**Note:** WooCommerce is highly extensible, open source software. Extensions commonly add additional data to WooCommerce orders. If you see additional information to what’s pictured and mentioned here, it may be added by an extension, your theme, or custom code.

The information visible in the Orders table can be altered via the “Screen Options” settings.

To change the columns of data that are visible on the Orders table:

1. Go to **WooCommerce > Orders**.
2. Select**Screen Options** in the upper right corner.
3. Select which **Columns**to show.
4. Check the boxes of items you want to be displayed.
5. Select **Apply**.

In the Screen Options settings, there’s also a setting to increase the number of Orders visible per page. Increasing this can be an effective way to edit many orders at a time. However, setting the number of orders visible on a single page too high can significantly increase load times for the page.

**Order Statuses** are color-coded and descriptive. Hovering over an order status will display the full description of the status in a tooltip.

- **Canceled**: Grey
- **Completed**: Blue
- **Failed**: Red
- **On Hold**: Orange
- **Pending payment**: Grey
- **Processing**: Green
- **Refunded**: Grey

If enabled in the [screen options](https://woocommerce.com/document/managing-orders/overview-and-bulk-management/#screen-options), the orders table will include shortcut buttons to quickly mark orders as **Processing** or **Completed**.

Orders can be filtered by **date (month/year)**, **registered customer**, or **order status**.

To filter orders:

1. Select a **month**, search for a **registered customer**, or both.
2. Press****the**Filter** button.

You can also filter the list by using the **order status links**.

To sort orders, select one of the linked headings, **Order** number, **Date**, or **Total**. To change whether the column is sorted in **ascending** or **descending** order, select the linked heading again.

**Note:**

The **Total** column does not take the refunded amount into consideration when sorting.

Orders can be found using the search box at the top right of the order list. Enter an order number, customer name, or other information shown in the order list such as address. Use the “**Search orders**” button or press return on your keyboard to display a list of matching orders.

You can preview an order by selecting the eye icon next to the order.

The eye icon opens a preview modal that allows you to change the order status. Additionally, the preview modal contains information about the order, such as:

- Order number
- Status
- Billing details
- Payment method
- Shipping details
- Items ordered

Much like other WordPress post types that let you alter multiple post statuses at once, WooCommerce Orders also have a bulk editing feature.

**Bulk Actions** can be used to move orders to the trash, or update their status in a group.

To update multiple orders at once:

1. Check the boxes on the left-hand side of the rows you wish to edit, or check the box next to the Orders heading to select all rows on the page.
2. Use the **Bulk Actions** dropdown to display available options.
3. Choose the action you’d like to take on the selected orders.
4. Select the **Apply** button.

Available options include:

- Move to Trash
- Change status to processing
- Change status to on-hold
- Change status completed
- Change status to cancelled
- Remove personal data (if [remove personal data with bulk editing](https://woocommerce.com/document/managing-orders/removing-personal-data-from-orders/#remove-personal-data-with-bulk-editing) is enabled)

If you run a multi-site network, there is a widget available on the Dashboard that shows order information from across all sites. Selecting an order will take you to the full order details on the store where the order was placed.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

