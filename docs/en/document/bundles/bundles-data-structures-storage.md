---
title: Data Structures and Storage
url: https://woocommerce.com/document/bundles/bundles-data-structures-storage/
---

code, pre { font-size: 85% }

This document is written for WooCommerce developers looking to extend or customize WooCommerce Product Bundles. It requires an advanced understanding of [PHP](http://php.net/) and [WordPress development](http://codex.wordpress.org/Developer_Documentation).

Product Bundles are stored in the database as [custom post type](https://codex.wordpress.org/Post_Types) entries of the `product` post type, similar to all product types in WooCommerce core. The extension introduces the **Product Bundle** product type by adding a `bundle` term value to the `product_type` taxonomy.

All bundles are instances of the `WC_Product_Bundle` class, which extends the core `WC_Product` class. Naturally, you can use all methods of the `WC_Product` class on bundle-type product instances. In addition to these, the `WC_Product_Bundle` class provides a number of methods specific to Product Bundle objects. A detailed reference of all methods is beyond the scope of this document – please refer to the class itself for details about each method.

`WC_Product_Bundle` objects rely on their own datastore for reading/writing object properties from/to the database. The following table contains a list of properties and meta fields specific to the **Bundle** type:

| Property | Meta Key | Description |
| --- | --- | --- |
| price | _wc_pb_base_price | Base price of the bundle. |
| regular_price | _wc_pb_base_regular_price | Base regular price of the bundle. |
| sale_price | _wc_pb_base_sale_price | Base sale price of the bundle. |
| bundle_stock_quantity | _wc_pb_bundle_stock_quantity | Quantity of bundles left in stock, taking bundled product stock requirements and limitations into account. |
| bundled_items_stock_status | _wc_pb_bundled_items_stock_status | Stock status of bundled products included in the bundle.
Values: instock | outofstock |
| bundled_items_stock_sync_status | _wc_pb_bundled_items_stock_sync_status | Indicates whether the bundled_items_stock_status and bundle_stock_quantity properties need to be synchronized.The plugin manages this process in the background to ensure that the stock status and stock quantity of all bundles is always kept in sync with stock quantity/status changes of their contents.
Values: synced | unsynced |
| virtual_bundle | _wc_pb_virtual_bundle | Manages state for the Virtual checkbox. When the Virtual box is ticked, all bundled products, in addition to the Bundle itself, are treated as Virtual.When the virtual_bundle property is true, then the virtual property is also true.When the virtual_bundle property is false, the virtual property is used to control whether the bundle is an assembled or unassembled one.For more information, refer to the examples that follow this table.Values: yes | no |
| aggregate_weight | _wc_pb_aggregate_weight | When creating assembled bundles, this property controls whether bundled product weights should be aggregated and added to the weight specified under Product Data > Shipping.
Values: yes | no |
| layout | _wc_pb_layout_style | Layout option.
Values: default | tabular |
| group_mode | _wc_pb_group_mode | Item Grouping option value.
Values: parent | noindent | none |
| editable_in_cart | _wc_pb_edit_in_cart | Edit in Cart option value.
Values: yes | no |
| sold_individually_context | _wc_pb_sold_individually_context | Sold Individually option value.
Values: product | configuration |
| add_to_cart_form_location | _wc_pb_add_to_cart_form_location | Form Location option value.
Values: default | after_summary |
| min_bundle_size | _wcpb_min_qty_limit | Min Bundle Size option value. |
| max_bundle_size | _wcpb_max_qty_limit | Max Bundle Size option value. |

**Examples: Physical/Virtual Bundles**

Data associated with bundled items is not saved in the post meta table. Instead, for scalability and speed when working with bundle parent/child relationships, the extension adds three tables to the database:

- `woocommerce_bundled_items`,
- `woocommerce_bundled_itemmeta`, and
- `wc_order_bundle_lookup`.

The table names are prefixed with your WP Database Table Prefix, usually `wp_`.

The `woocommerce_bundled_items` table is used to store all bundle-to-bundled-products associations using a simple schema:

| Table Field | Description |
| --- | --- |
| bundled_item_id | Unique ID of the bundled item. |
| product_id | ID of the product associated with the bundled item. |
| bundle_id | ID of the “parent” product bundle. |
| menu_order | Sort order of the bundled item relative to other items in the same bundle. |

The `woocommerce_bundled_itemmeta` table stores all bundled item options as meta data, similar to how the `postmeta` table is used by WordPress to store meta data for the `posts` table:

| Table Field | Description |
| --- | --- |
| meta_id | Unique ID of the meta entry. |
| bundled_item_id | ID of the associated bundled item. |
| meta_key | Meta key. |
| meta_value | Meta value. |

For database schema details, refer to `/includes/class-wc-pb-install.php`

The plugin provides a [Database API](https://woocommerce.com/document/bundles/bundles-functions-reference/#database-api-methods) for working directly with these tables, which includes:

- `query_bundled_items`, a utility function for database queries which includes support for meta queries; and
- a number of utility functions for creating, updating and deleting bundled items and meta.

To retrieve and store bundled item data, you can also utilize the `WC_Bundled_Item_Data` class, which [handles all CRUD](https://woocommerce.com/document/bundles/bundles-functions-reference/#bundled-item-crud-methods) (create, read, update, delete) operations for bundled items. For details, please refer to the [Functions Reference](https://woocommerce.com/document/bundles/bundles-functions-reference/) document section that is dedicated to the [Bundled Items CRUD](https://woocommerce.com/document/bundles/bundles-functions-reference/#bundled-item-crud-methods) class.

At a higher level of abstraction, bundled items are represented as `WC_Bundled_Item` class instances. Every instance of the `WC_Bundled_Item` class relies on a `WC_Bundled_Item_Data` class instance in order to obtain the data necessary for its own initialization. Given a `WC_Product_Bundle` object, the most straightforward way to retrieve collection of `WC_Bundled_Item` objects is to call `WC_Product_Bundle::get_bundled_items`.

The `WC_Bundled_Item` class provides access to bundled product data relevant within the context of the specific bundle: For example, `is_in_stock` can be used to obtain the stock status of a bundled item, taking the Minimum Quantity option and/or the existence of Variation Filters into account. Other examples include: `is_optional`, `get_title` and `get_description`. Please refer to the `WC_Bundled_Item` class inline method documentation for details.

In cart context, `WC_Product_Bundle` objects act as a trigger for adding bundled products to the cart on the `woocommerce_add_to_cart` action, depending on the posted configuration data. The plugin does its own client-side and server-side validation to ensure that the posted configuration can be added to the cart.

In the cart, a bundle shows up as a **group of cart items**:

- A **container** cart item, associated with the product bundle itself.
- A number of **bundled** cart items, each associated with a bundled product.

When placing an order, the same group of items are stored in the created order, along with some order item meta necessary for preserving their relationship.

Thanks to this approach:

- All inventory management is relayed to WooCommerce core.
- Compatibility with 3rd party plugins/extensions is greatly simplified, since the process of adding bundled products to the cart/order does not bypass any hooks that would be normally triggered in core.
- The container cart/order item can be used to easily override the physical properties of its children at the application layer, useful in use cases with [complex shipping requirements](https://woocommerce.com/document/bundles/bundles-configuration/#shipping).
- A clear separation of bundle level and bundled product level prices in the cart makes it easier to implement advanced pricing schemes and allows each bundled item to maintain its individual tax rate.

Parent/child **cart items** are identified by appending the following fields to cart items:

| Field | Type | Item Context | Description |
| --- | --- | --- | --- |
| bundled_by | string | Bundled | Cart item ID of the container cart item that this bundled cart item belongs to. |
| bundled_items | array | Container | Cart item IDs of all bundled cart items associated with this bundle container item. |
| stamp | array | Bundled/Container | Array with bundle configuration data, used for a) identifying the entire group uniquely and b) carrying out in-cart validation. |
| bundled_item_id | string | Bundled | Bundled item ID associated with this bundled cart item. Refer to the Database schema in the Product Data section above. |

This data is used internally to **establish the parent/child relationships of cart items** associated with a bundle. The extension provides a set of global utility functions that you can use to:

- Check if a cart item is a bundled item and get its parent.
- Check if a cart item is a bundle container item and get its children.

For details, please refer to the [Cart](https://woocommerce.com/document/bundles/bundles-functions-reference/#global-order-functions) section of the [Functions Reference](https://woocommerce.com/document/bundles/bundles-functions-reference/).

Parent/child **order items** are identified by creating the following order item meta:

| Key | Type | Item Context | Description |
| --- | --- | --- | --- |
| _bundle_cart_key | string | Bundled/Container | Original cart item ID (or other unique hash) that identifies this order item. |
| _bundled_by | string | Bundled | Unique hash of the container cart item that this bundled order item belongs to. |
| _bundled_items | serialized array | Container | Unique hashes of all bundled items associated with this bundle container item. |
| _stamp | serialized array | Bundled/Container | Serialized array with bundle configuration data, used for a) identifying the entire group uniquely and b) carrying out in-cart validation when re-ordering. |
| _bundled_item_id | string | Bundled | Bundled item ID associated with this bundled order item. Refer to the Database schema in the Product Data section above. |
| _bundled_item_priced_- _individually | string | Bundled | Indicates whether the item was individually priced when the order was placed. |
| _bundled_item_needs_- shipping | string | Bundled | Indicates whether the bundled item required shipping individually from the bundle when the order was placed. |
| _bundle_weight | numeric | Container | The total per-unit weight of a bundle container when the order was placed. May differ from the value defined in the Weight field of the Shipping tab when using a variable container weight. |

This data is used internally to **establish the parent/child relationships of order items** associated with a bundle. The extension provides a set of global utility functions that you can use to:

- Check if an order item is a bundled item and get its parent.
- Check if an order item is a bundle container item and get its children.

For details, please refer to the [Order](https://woocommerce.com/document/bundles/bundles-functions-reference/#global-order-functions) section of the [Functions Reference](https://woocommerce.com/document/bundles/bundles-functions-reference/).

Have a question before you buy? Please fill out this [pre-sales form](https://woocommerce.com/contact-us/#sales-form). Already purchased and need assistance? [Get in touch with us](https://woocommerce.com/my-account/marketplace-ticket-form/) via the Help Desk!

