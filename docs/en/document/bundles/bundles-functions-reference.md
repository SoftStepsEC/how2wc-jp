---
title: Functions Reference
url: https://woocommerce.com/document/bundles/bundles-functions-reference/
---

This page is written for WooCommerce developers looking to extend or customize WooCommerce Product Bundles. It requires an advanced understanding of [PHP](http://php.net/) and [WordPress development](http://codex.wordpress.org/Developer_Documentation).

This guide introduces some of the most useful functions available in Product Bundles. It does not include tutorials on how to achieve certain tasks.

We recommend reading [Data Structures and Storage](https://woocommerce.com/document/bundles/bundles-data-structures-storage/) before consulting this reference. Take time to familiarize yourself with the plugin architecture and the the `WC_PB_Cart`, `WC_PB_Order`, `WC_PB_DB` and `WC_Bundled_Item_Data` objects.

**Global Cart Functions**

| Name | Description |
| --- | --- |
| wc_pb_is_bundled_cart_item | Checks if a cart item is part of a bundle. Instead of relying solely on cart item data, the function also checks that a parent cart item actually exists. |
| wc_pb_get_bundled_cart_item_container | Finds and returns the container cart item (parent) that a bundled cart item (child) belongs to. |
| wc_pb_is_bundle_container_cart_item | Checks if a cart item is a bundle container cart item. |
| wc_pb_get_bundled_cart_items | Finds and returns the bundled cart items (children) associated with a bundle container cart item (parent). |

**Cart API Methods**

| Name | Description |
| --- | --- |
| add_bundle_to_cart | Validates and adds a bundle to the cart. Expects a bundle configuration array to be constructed and passed into the method. |
| validate_bundle_configuration | Validates a bundle configuration array. |

**Global Order Functions**

| Name | Description |
| --- | --- |
| wc_pb_is_bundled_order_item | Checks if an order item is part of a bundle. Instead of relying solely on order item meta, the function also checks that a parent order item actually exists. |
| wc_pb_get_bundled_order_item_container | Finds and returns the container order item (parent) that a bundled order item (child) belongs to. |
| wc_pb_is_bundle_container_order_item | Checks if an order item is a bundle container order item. |
| wc_pb_get_bundled_order_items | Finds and returns the bundled order items (children) associated with a bundle container order item (parent). |

**Order API Methods**

| Name | Description |
| --- | --- |
| add_bundle_to_order | Validates and adds a bundle to an order. Expects a bundle configuration array to be constructed and passed into the method. |
| get_order_items | Modifies bundle parent/child order items depending on their shipping setup. Used to reconstruct an accurate physical representation of a bundle, typically as a callback conditionally attached to the woocommerce_order_get_items filter when exporting order data to external fulfillment, shipping or inventory management services. |
| get_product_from_item | Modifies products constructed from bundle parent/child order items. Used to reconstruct an accurate physical representation of a bundle, typically as a callback conditionally attached to the woocommerce_get_product_from_item filter when exporting order data to external fulfillment, shipping or inventory management services. |

**Global Database Functions**

| Name | Description |
| --- | --- |
| wc_pb_get_bundled_product_map | Returns a map of bundled item IDs to product bundle IDs associated with a (bundled) product. Commonly used to find which bundles a product belongs to. |

**Database API Methods**

| Name | Description |
| --- | --- |
| query_bundled_items | Fetches bundled item data from the database. Results can be returned in multiple formats/types. Includes support for meta queries. |
| add_bundled_item | Creates a bundled item in the database. |
| get_bundled_item | Gets a bundled item from the database. |
| update_bundled_item | Updates a bundled item in the database. |
| delete_bundled_item | Deletes a bundled item from the database. |
| add_bundled_item_meta | Adds a bundled item meta field to the database. |
| get_bundled_item_meta | Gets a bundled item meta field from the database. |
| update_bundled_item_meta | Updates a bundled item meta field in the database. |
| delete_bundled_item_meta | Deletes a bundled item meta field from the database. |

**Bundled Item CRUD Methods**

| Name | Description |
| --- | --- |
| get_data | Gets all bundled item data stored in a WC_Bundled_Item_Data object. |
| get_meta_data | Gets all bundled item meta data stored in a WC_Bundled_Item_Data object. |
| set_all | Sets/updates all bundled item data stored in a WC_Bundled_Item_Data object using the supplied data. |
| set_meta_data | Sets/updates bundled item meta data stored in a WC_Bundled_Item_Data object using the supplied data. |

The extension provides the following global utility functions that allow you to identify and work with the parent/child cart items associated with a bundle:

#### wc_pb_is_bundled_cart_item

**Description**

`boolean wc_pb_is_bundled_cart_item( array $cart_item [, array $cart_contents = false ] )`

Checks if a cart item is part of a bundle. Instead of relying solely on cart item data, the function also checks that a parent cart item actually exists.

**Arguments**

`array $cart_item` – Cart item to check. `array $cart_contents` – Cart contents array to search in (optional).

**Return Values**

`boolean` – See description.

**Usage**

```
$result = wc_pb_is_bundled_cart_item( $cart_item );
```

#### wc_pb_get_bundled_cart_item_container

**Description**

`mixed wc_pb_get_bundled_cart_item_container( array $cart_item [, array $cart_contents = false ] [, boolean $return_id = false ] )`

Finds and returns the container cart item (parent) that a bundled cart item (child) belongs to. If the passed cart item is not a bundled cart item, a `false` value is returned.

**Arguments**

`array $cart_item` – The (bundled) cart item whose container is searched. `array $cart_contents` – Cart contents array to search in (optional). `boolean $return_id` – When set to `true`, the function returns the cart ID of the found container item, instead of the item itself (if found) (optional).

**Return Values**

`array|string|false` – If the passed cart item is actually a bundled (child) cart item and a container item is found, the function returns the container item (or a `string` corresponding to its cart ID when the `$return_id` argument is `true`). Otherwise, a boolean `false` value is returned.

**Usage**

```
$container_item = wc_pb_get_bundled_cart_item_container( $cart_item );
```

#### wc_pb_is_bundle_container_cart_item

**Description**

`boolean wc_pb_is_bundle_container_cart_item( array $cart_item )`

Checks if a cart item is a bundle container cart item. Does not check for the existence of any bundled cart items — in some cases, a bundle configuration may not include any bundled items.

**Arguments**

`array $cart_item` – Cart item to check.

**Return Values**

`boolean` – See description.

**Usage**

```
$result = wc_pb_is_bundle_container_cart_item( $cart_item );
```

#### wc_pb_get_bundled_cart_items

**Description**

`array wc_pb_get_bundled_cart_items( array $cart_item [, array $cart_contents = false ] [, boolean $return_ids = false ] )`

Finds and returns the bundled cart items (children) associated with a bundle container cart item (parent). If the passed cart item is not a bundle container cart item, an empty `array` is returned.

**Arguments**

`array $cart_item` – The (container) cart item whose children are searched. `array $cart_contents` – Cart contents array to search in (optional). `boolean $return_ids` – When set to `true`, the function returns the cart IDs of the found bundled cart items (children), instead of the actual items (if found) (optional).

**Return Values**

`array` – If the passed cart item is actually a container (parent) cart item and a collection of bundled cart items (children) associated with it exists, the function returns an `array` with the discovered cart items (or their cart IDs when the `$return_ids` argument is `true`). Otherwise, an empty `array` is returned.

**Usage**

```
$bundled_items = wc_pb_get_bundled_cart_items( $cart_item );
```

In addition to the globally accessible utility methods documented in the previous section, the cart API of the extension is rounded off with **methods for validating and adding an entire bundle to the cart programmatically**. The methods documented in this section are callable on the `WC_PB_Cart` instance accessible via `WC_PB()->cart`.

#### add_bundle_to_cart

**Description**

`mixed add_bundle_to_cart( integer $product_id , integer $quantity [, array $configuration = array() ] [, array $cart_item_data = array() ] )`

Validates and adds a bundle to the cart. Expects a bundle configuration array to be constructed and passed into the method.

**Arguments**

`integer $product_id` – Product ID of the bundle to add to the cart. `integer $quantity` – Quantity of the bundle. `array $configuration` – Bundle configuration data. An array of bundled item configuration data indexed by bundled item ID. Bundled item configuration data values are also arrays that must conform to the following schema:

| Field Key | Field Type | Description |
| --- | --- | --- |
| product_id | integer | ID of bundled product. |
| quantity | integer | Quantity of bundled product. |
| variation_id | integer | ID of selected variation, applicable to variable-type bundled items only. |
| attributes | array | Index of variation attribute names and values, applicable when the bundled item is associated with a variable-type product. |
| optional_selected | string | Applicable to optional bundled items, indicates whether the bundled item should be included in the bundle or not. Values: yes | no. |
| discount | float | Bundled item discount, overrides the original bundled item meta value. Applicable when the Priced Individually option is enabled. |
| title | string | Bundled item title, overrides the original bundled item meta value. Applicable when the Override Title bundled item option is enabled. |

Example:

```
$args = array(
    81 => array(
        'product_id' => 1543,
        'quantity' => 3,
    ),
    84 => array(
        'product_id' => 1386,
        'quantity' => 1,
        'variation_id' => 3535,
        'attributes' => array(
            'attribute_pa_attribute-1' => 'value-1b',
            'attribute_pa_attribute-2' => 'value-2b',
        ),

    )
);

$added = WC_PB()->cart->add_bundle_to_cart( 3520, 1, $args );
```

The Product Bundle of this example contains 2 bundled items with IDs `81` and `84`, associated with product IDs `1543` and `1386`, respectively. Note that the latter one is a variable product, requiring the presence of a `variation_id` and an `attributes` field.

Passing a configuration array into `add_bundle_to_cart` is **not always required**. In many cases, `add_bundle_to_cart` will gracefully attempt to construct a valid bundle configuration itself, based on the type and meta of the associated bundled items. For instance, you can safely add a bundle to the cart without defining a configuration array if the bundle contains non-variable, non-optional items. In the same spirit, bundled item quantities will always default to the saved Min Quantity meta values.

`array $cart_item_data` – Cart item data fields to pass into `WC_Cart::add_to_cart` (optional).

**Return Values**

`string|WP_Error` – If validation is successful, the method returns the cart item ID of the added bundle container item. If not, it returns a `WP_Error` object, populated with all generated validation errors. Note that any WooCommerce notices generated during validation are not automatically cleared and will be displayed in the next front-end request. If needed, clear them from the WC session by calling `wc_clear_notices()`.

**Usage**

```
$result = WC_PB()->cart->add_bundle_to_cart( $bundle_id, $quantity, $configuration );
```

#### validate_bundle_configuration

**Description**

`boolean validate_bundle_configuration( mixed $product , integer $quantity, array $configuration [, string $context = 'add-to-cart' ] )`

Validates a bundle configuration. Expects a bundle configuration array to be constructed and passed into the method.

**Arguments**

`integer|string|WC_Product $product` – Product bundle (or ID of) to use for validating. `integer $quantity` – Quantity of the bundle to use during validation. `array $configuration` – Bundle configuration array. Contains bundled item configuration data indexed by bundled item ID. For details, refer to [add_bundle_to_cart](https://woocommerce.com/document/bundles/bundles-functions-reference/#add_bundle_to_cart). `string $context` – Validation context (optional, internal use only).

**Return Values**

`boolean` – Validation result.

**Usage**

```
$result = WC_PB()->cart->validate_bundle_configuration( $bundle, $quantity, $configuration );
```

The extension provides the following global utility functions that allow you to identify and work with the parent/child order items associated with a bundle:

#### wc_pb_is_bundled_order_item

**Description**

`boolean wc_pb_is_bundled_order_item( array $order_item , WC_Order $order )`

Checks if an order item is part of a bundle. Instead of relying solely on order item meta, the function also checks that a parent order item actually exists.

**Arguments**

`array $order_item` – Order item to check. `WC_Order $order` – WooCommerce order object.

**Return Values**

`boolean` – See description.

**Usage**

```
$result = wc_pb_is_bundled_order_item( $order_item, $order );
```

#### wc_pb_get_bundled_order_item_container

**Description**

`mixed wc_pb_get_bundled_order_item_container( array $order_item , WC_Order $order [, boolean $return_id = false ] )`

Finds and returns the container order item (parent) that a bundled order item (child) belongs to. If the passed order item is not a bundled order item, a `false` value is returned.

**Arguments**

`array $order_item` – The (bundled) order item whose container is searched. `WC_Order $order` – WooCommerce order object to search in. `boolean $return_id` – When set to `true`, the function returns the order item ID of the found container item, instead of the item itself (if found) (optional).

**Return Values**

`array|integer|false` – If the passed order item is actually a bundled (child) order item and a container item is found, the function returns the container item (or an `integer` corresponding to its order item ID when the `$return_id` argument is `true`). Otherwise, a boolean `false` value is returned.

**Usage**

```
$container_item = wc_pb_get_bundled_order_item_container( $order_item, $order );
```

#### wc_pb_is_bundle_container_order_item

**Description**

`boolean wc_pb_is_bundle_container_order_item( array $order_item )`

Checks if an order item is a bundle container order item. Does not check for the existence of any bundled order items – in some cases, a bundle configuration may not include any bundled items at all.

**Arguments**

`array $order_item` – Order item to check.

**Return Values**

`boolean` – See description.

**Usage**

```
$result = wc_pb_is_bundle_container_order_item( $order_item );
```

#### wc_pb_get_bundled_order_items

**Description**

`array wc_pb_get_bundled_order_items( array $cart_item , WC_Order $order [, boolean $return_ids = false ] )`

Finds and returns the bundled order items (children) associated with a bundle container order item (parent). If the passed order item is not a bundle container order item, an empty `array` is returned.

**Arguments**

`array $order_item` – The (container) cart item whose children are searched. `WC_Order $order` – WooCommerce order object to search in. `boolean $return_ids` – When set to `true`, the function returns the order item IDs of the found bundled order items (children), instead of the actual items (if found) (optional).

**Return Values**

`array` – If the passed order item is actually a container (parent) order item and a collection of bundled order items (children) associated with it exists, the function returns an `array` with the discovered order items (or their order item IDs when the `$return_ids` argument is `true`). Otherwise, an empty `array` is returned.

**Usage**

```
$bundled_items = wc_pb_get_bundled_order_items( $order_item, $order );
```

In addition to the globally accessible utility methods documented in the previous section, the order API of the extension is rounded off with `add_bundle_to_order`, a **method for validating and adding an entire bundle to an order programmatically**. This is callable on the `WC_PB_Order` instance accessible via `WC_PB()->order`.

#### add_bundle_to_order

**Description**

`mixed add_bundle_to_order( WC_Product_Bundle $product , WC_Order $order , integer $quantity [, array $args = array() ] )`

Validates and adds a bundle to an order. Expects a bundle configuration array to be passed to the method as a `configuration` field of the `$args` argument. Validation of the specified bundle configuration is done via `WC_PB_Cart::validate_bundle_configuration`, which is documented [here](https://woocommerce.com/document/bundles/bundles-functions-reference/#validate_bundle_configuration).

**Arguments**

`WC_Product_Bundle $product` – Product bundle to add to the order. `WC_Order $order` – Order to which the bundle is added. `integer $quantity` – Quantity of the bundle. `array $args` – Fields to be passed into the `$args` argument of `WC_Order::add_product`, when the bundle container order item is added. Bundle configuration data is passed into the method as a `configuration` field of this argument. Details about its schema are provided in the [add_bundle_to_cart](https://woocommerce.com/document/bundles/bundles-functions-reference/#add_bundle_to_cart) method of the Cart API. Additionally, a `silent` field is used to control whether validation errors are displayed in the next front-end request. Refer to the **Return Values** section below for more information.

Example:

```
$args = array(
    'configuration' => array(
        81 => array(
            'product_id' => 1543,
            'quantity'   => 3,
            'args'       => array()
        ),
        84 => array(
            'product_id'   => 1386,
            'quantity'     => 1,
            'variation_id' => 3535,
            'attributes'   => array(
                'attribute_pa_attribute-1' => 'value-1b',
                'attribute_pa_attribute-2' => 'value-2b'
            )
        )
    ),
    'silent' => false
);

$bundle = wc_get_product( 3520 );
$order  = wc_get_order( 3539 );

$added = WC_PB()->order->add_bundle_to_order( $bundle, $order, 1, $args );
```

Passing a configuration array into `add_bundle_to_order` is **not always required**. In many cases, `add_bundle_to_order` will gracefully attempt to construct a valid bundle configuration itself, based on the type and meta of the associated bundled items. For instance, you can safely add a bundle to an order without defining a configuration array if the bundle contains non-variable, non-optional items. In the same spirit, bundled item quantities will always default to the saved Min Quantity meta values.

When a bundle container item (parent) is added to an order, the entire `$args` array is passed into `WC_Order::add_product`. If you need to pass any custom fields into the `$args` argument of `WC_Order::add_product`, include them in the `$args` argument of `add_bundle_to_order`.

You can also pass custom fields into the `$args` argument of `WC_Order::add_product` when the method is called to add any bundled items (children) to the order. This is possible by adding an `args` field to the bundled item configuration data passed into the method. This is demonstrated in the example above, where an `args` field is added to the configuration of the bundled item with ID `81`.

**Return Values**

`integer|WP_Error` – If validation is successful, the method returns the order item ID of the added bundle container item. If not, it returns a `WP_Error` object, populated with all generated validation errors.

When validation fails, the method returns a `WP_Error` object without displaying any WooCommerce notices in the front-end. To have all validation notices displayed in the next front-end request, set the `$args[ 'silent' ]` field to `false` when calling the method.

**Usage**

```
$result = WC_PB()->order->add_bundle_to_order( $bundle, $order, $quantity, $args );
```

#### get_order_items

**Description**

`mixed get_order_items( array $order_items , WC_Order $order )`

Modifies bundle parent/child order items depending on their shipping setup. Useful for reconstructing an accurate physical representation of a bundle, typically as a callback conditionally attached to the `woocommerce_order_get_items` filter when exporting order data to external fulfillment, shipping or inventory management services.

The method:

- sets the totals of assembled bundled items to zero, and
- adds their original totals to the totals of their bundle container.

Note that “assembled” in this context refers to items that are not [Shipped Individually](https://woocommerce.com/document/bundles/bundles-configuration/#shipping).

**Arguments**

`array $order_items` – Unmodified collection of order items. `WC_Order $order` – Order object.

**Return Values**

`array` – Modified collection of order items.

**Usage**

The method is used in the `WC_PB_Shipstation_Compatibility` class included in Product Bundles, which contains compatibility code for the [WooCommerce Shipstation Integration](https://woocommerce.com/products/shipstation-integration/) extension.

For details, please refer to [this note](https://woocommerce.com/document/bundles/bundles-configuration/#external-order-fulfilment-note).

```
$result = WC_PB()->order->get_order_items( $order_items, $order );
```

#### get_product_from_item

**Description**

`mixed get_product_from_item( WC_Product $product , array $order_item , WC_Order $order )`

Modifies products constructed from bundle parent/child order items. Used to reconstruct an accurate physical representation of a bundle, typically as a callback conditionally attached to the `woocommerce_get_product_from_item` filter when exporting order data to external fulfillment, shipping or inventory management services.

The method applies the following modifications:

- If the product object is associated with a bundle container item, then its weight is modified to include the weight of all assembled children.
- If the product object is associated with an assembled bundled/child item, then it is marked as virtual.

Note that “assembled” is used in this context to refer to items that are not [Shipped Individually](https://woocommerce.com/document/bundles/bundles-configuration/#shipping).

**Arguments**

`WC_Product $product` – Unmodified product object. `array $order_item` – Order item that the product object was created from. `WC_Order $order` – Order object.

**Return Values**

`WC_Product` – Modified product object.

**Usage**

The method is used in the `WC_PB_Shipstation_Compatibility` class included in Product Bundles, which contains compatibility code for the [WooCommerce Shipstation Integration](https://woocommerce.com/products/shipstation-integration/) extension.

For details, please refer to [this note](https://woocommerce.com/document/bundles/bundles-configuration/#external-order-fulfilment-note).

```
$result = WC_PB()->order->get_product_from_item( $product, $order_item, $order );
```

The extension provides `wc_pb_get_bundled_product_map` as global database utility function that allows you to quickly find which bundles a product belongs to, without using the database API.

#### wc_pb_get_bundled_product_map

**Description**

`array wc_pb_get_bundled_product_map( mixed $product [, boolean $allow_cache = true ] )`

Returns a map of bundled item IDs to product bundle IDs associated with a (bundled) product. Useful for:

- Finding which bundles a product belongs to.
- Getting all bundled item IDs that a product ID has been associated with.

**Arguments**

`WC_Product|integer $product` – Product whose records are being searched (or ID of). `boolean $allow_cache` – When set to false, the internal transients cache is bypassed and a database query is executed (optional).

**Return Values**

`array` – Array of bundle IDs indexed by bundled item ID. A product may be found in a single bundle more than one time, and of course may exist in multiple bundles, as well.

**Usage**

```
$results = wc_pb_get_bundled_product_map( $product );
```

The extension provides a Database API for working with its [tables](https://woocommerce.com/document/bundles/bundles-data-structures-storage/#database-level), which includes:

- `query_bundled_items`, a utility function for database queries which includes support for meta queries and
- a number of utility functions for creating, updating and deleting bundled items and meta which rely on the `WC_Bundled_Item_Data` CRUD class (documented in the next section).

Note that all Database API functions are static and called on the `WC_PB_DB` type directly.

#### query_bundled_items

**Description**

`array query_bundled_items( array $args )`

Fetches bundled item data from the database. Results can be returned in multiple formats/types. Includes support for meta queries.

**Arguments**

`array $args` – Query parameters:

| Key | Type | Description |
| --- | --- | --- |
| return | string | Controls the indexing/content/type of the returned results array.
Values:

'all' – Returns all woocommerce_bundled_items columns in array form. Results are numerically indexed.
'ids' – Returns bundled item IDs only. Results are numerically indexed.
'id=>bundle_id' – Returns a map of bundled item IDs to bundle IDs.
'id=>product_id' – Returns a map of bundled item IDs to bundled product IDs.
'objects' – Returns results as WC_Bundled_Item_Data objects, numerically indexed. |
| bundled_item_id | integer|array | Bundled item ID(s) to include in the query. |
| product_id | integer|array | Bundled product ID(s) to include in the query. |
| bundle_id | integer|array | Bundle ID(s) to include in the query. |
| meta_query | array | Meta query parameters. Refer to the WP_Meta_Query documentation for schema details. |

**Example #1**: Get a map of bundled item IDs – product IDs contained in a bundle with ID `99`:

```
$results = WC_PB_DB::query_bundled_items( array(
    'return'    => 'id=>product_id',
    'bundle_id' => array( 99 )
) );
```

**Example #2**: Get all bundle IDs that a product with ID `41` has been added to with a Min Quantity higher than 1:

```
$results = WC_PB_DB::query_bundled_items( array(
    'return'     => 'id=>bundle_id',
    'product_id' => array( 41 ),
    'meta_query'      => array(
        array(
            'key'     => 'quantity_min',
            'value'   => 1,
            'compare' => '>'
        ),
    )
) );
```

**Example #3**: Get a map of all bundled item IDs – product IDs that do not have enough stock to purchase the bundles that contain them:

```
$results = WC_PB_DB::query_bundled_items( array(
    'return'     => 'id=>product_id',
    'meta_query' => array(
        array(
            'key'     => 'stock_status',
            'value'   => 'out_of_stock',
            'compare' => '='
        ),
    )
) );
```

**Return Values**

`array` – Array of results, with index/contents controlled by the `return` parameter (documented in the **Arguments** section above).

**Usage**

```
$results = WC_PB_DB::query_bundled_items( $args );
```

#### add_bundled_item

**Description**

`mixed add_bundled_item( array $data )`

Creates a bundled item in the database.

**Arguments**

`array $data` – Bundled item data and meta to assign to the created bundled item. Schema:

| Key | Type | Description |
| --- | --- | --- |
| bundle_id | integer | ID of the bundle that the bundled item belongs to. |
| product_id | integer | Bundled product ID associated with the bundled item. |
| menu_order | integer | Sort order of the bundled item relative to other items in the same bundle. |
| meta_data | array | Array of meta field keys/values. Refer to the Bundled Item CRUD Methods section for details. |

**Return Values**

`integer|false` – Returns the ID of the created bundled item if the item was saved in the database successfully, or `false` otherwise.

**Usage**

```
$result = WC_PB_DB::add_bundled_item( $data );
```

#### get_bundled_item

**Description**

`mixed get_bundled_item( mixed $item )`

Instantiates and returns a `WC_Bundled_Item_Data` object after fetching its data from the database.

**Arguments**

`integer|WC_Bundled_Item_Data $item` – ID of the bundled item that needs to be instantiated, or an existing `WC_Bundled_Item_Data` object to copy data from.

**Return Values**

`WC_Bundled_Item_Data|false` – Returns the instantiated bundled item, or `false` if the supplied arguments are invalid.

**Usage**

```
$item = WC_PB_DB::get_bundled_item( $item_id );
```

#### update_bundled_item

**Description**

`boolean update_bundled_item( mixed $item , array $data )`

Instantiates a `WC_Bundled_Item_Data` object and uses its CRUD API to update its database entries based on the fields of the supplied data array.

**Arguments**

`integer|WC_Bundled_Item_Data $item` – ID of the bundled item that needs to be updated, or an existing `WC_Bundled_Item_Data` object to copy data from (and update). `array $data` – Fields that need to be updated, or an existing `WC_Bundled_Item_Data` object to copy data from. Refer to the [add_bundled_item](https://woocommerce.com/document/bundles/bundles-functions-reference/#add_bundled_item) method arguments for details.

**Return Values**

`boolean` – Result of update operation.

**Usage**

```
$result = WC_PB_DB::update_bundled_item( $item_id, $data );
```

#### delete_bundled_item

**Description**

`void delete_bundled_item( mixed $item )`

Instantiates a `WC_Bundled_Item_Data` object and uses its CRUD API to delete its database entries.

**Arguments**

`integer|WC_Bundled_Item_Data $item` – ID of the bundled item that needs to be deleted, or an existing `WC_Bundled_Item_Data` object to copy data from (and delete).

**Return Values**

`void`

**Usage**

```
WC_PB_DB::delete_bundled_item( $item_id );
```

#### add_bundled_item_meta

**Description**

`integer add_bundled_item_meta( integer $item_id , string $meta_key , mixed $meta_value )`

Adds a bundled item meta field to the database. Relies on [add_metadata](https://codex.wordpress.org/Function_Reference/add_metadata).

**Arguments**

`integer $item_id` – ID of bundled item to which the meta field is added. `string $meta_key` – Meta field key. `mixed $meta_value` – Meta field value.

**Return Values**

`integer` – Returns the ID of the created meta field if the operation was successful, or `0` otherwise.

Only **unique bundled item meta keys** are allowed in the database.

**Usage**

```
$result = WC_PB_DB::add_bundled_item_meta( $item_id, $meta_key, $meta_value );
```

#### get_bundled_item_meta

**Description**

`mixed get_bundled_item_meta( integer $item_id [, string $meta_key = '' ] )`

Gets a bundled item meta field value from the database (or all meta field values indexed by key if the `$meta_key` argument is omitted). Relies on [get_metadata](https://codex.wordpress.org/Function_Reference/get_metadata).

**Arguments**

`integer $item_id` – ID of the bundled item. `string $meta_key` – The meta key whose value is requested (optional).

**Return Values**

`mixed|array|false` – Returns the value of the specified meta key, or all meta field values indexed by key if the `$meta_key` argument is omitted. If the search yields no results, a boolean `false` value is returned.

**Usage**

```
$value = WC_PB_DB::get_bundled_item_meta( $item_id, $meta_key );
```

#### update_bundled_item_meta

**Description**

`boolean update_bundled_item_meta( integer $item_id , string $meta_key , mixed $meta_value [, mixed $prev_value = '' ] )`

Updates a bundled item meta field value in the database. Relies on [update_metadata](https://codex.wordpress.org/Function_Reference/update_metadata).

**Arguments**

`integer $item_id` – ID of the bundled item. `string $meta_key` – The meta key whose value is updated. `mixed $meta_value` – The new meta value.

**Return Values**

`boolean` – Result of update operation.

**Usage**

```
$result = WC_PB_DB::update_bundled_item_meta( $item_id, $meta_key, $meta_value );
```

#### delete_bundled_item_meta

**Description**

`boolean delete_bundled_item_meta( integer $item_id , string $meta_key [, mixed $meta_value = '' ] [, boolean $delete_all = false ] )`

Deletes a bundled item meta field from the database. Relies on [delete_metadata](https://codex.wordpress.org/Function_Reference/delete_metadata).

**Arguments**

`integer $item_id` – ID of the bundled item. `string $meta_key` – The meta key to delete. `mixed $meta_value` – If specified, only delete meta fields with this value (optional). `mixed $meta_value` – If specified, delete all matched meta fields for all bundled item IDs, ignoring the `$item_id` argument (optional).

**Return Values**

`boolean` – Result of operation.

**Usage**

```
$result = WC_PB_DB::delete_bundled_item_meta( $item_id, $meta_key );
```

The extension uses the `WC_Bundled_Item_Data` class as an object wrapper for bundled item data. Once instantiated, a `WC_Bundled_Item_Data` object is also able to handle all database CRUD operations for the bundled item it represents.

Under most circumstances, you will not need to instantiate `WC_Bundled_Item_Data` objects or call any methods on them directly. If you absolutely have to work with the bundled items database, it is recommended to use the Database API Methods for CRUD operations that involve bundled items.

However, due to the extensive use of `WC_Bundled_Item_Data` objects by the Database API methods, it is useful to document some of the methods used for exchanging data with `WC_Bundled_Item_Data` objects.

Make sure that you understand the difference between the `WC_Bundled_Item_Data` type vs. the `WC_Bundled_Item` type. The former one is a data wrapper that handles database CRUD operations, as well as a data provider to the latter one. The latter one is a product wrapper that provides a set of methods useful in bundle context, and is probably the one to look into if you are working with the extension at the application layer.

This is not meant to be an exhaustive reference of the `WC_Bundled_Item_Data` type methods. The methods documented here are only the ones used to set/get object data in bulk: Understanding the structure of the exchanged data is necessary for using the Database API methods associated with creating and updating bundled items.

#### get_data

**Description**

`array get_data()`

Returns all data present in the object.

**Return Values**

`array` – The data contained in the object. If instantiated using a bundled item ID, the object will contain all associated bundled item data written in the database, including all meta fields associated with it. Schema:

| Key | Type | Description |
| --- | --- | --- |
| bundle_id | integer | ID of the bundle that the bundled item belongs to. |
| product_id | integer | Bundled product ID associated with the bundled item. |
| menu_order | integer | Sort order of the bundled item relative to other items in the same bundle. |
| meta_data | array | Array of meta field keys/values. Refer to get_meta_data for schema details. |

**Usage**

```
$data = $object->get_data();
```

#### get_meta_data

**Description**

`array get_meta_data()`

Returns all meta data present in the object.

**Return Values**

`array` – The meta data contained in the object. If the object was instantiated using a bundled item ID, the method returns all associated meta fields written in the database. Schema:

| Key | Type | Description |
| --- | --- | --- |
| quantity_min | integer | Minimum quantity of the bundled item. |
| quantity_max | integer | Maximum quantity of the bundled item. |
| override_title | string | Indicates whether to override the bundled product title.

Values: yes | no |
| title | string | Title to use when overriding the default bundled product title. |
| override_description | string | Indicates whether to override the bundled product description.

Values: yes | no |
| description | string | Description to use when overriding the default bundled product description. |
| optional | string | Indicates whether the bundled item is optional.

Values: yes | no |
| hide_thumbnail | string | Indicates whether to hide the bundled item thumbnail in the single-product template.

Values: yes | no |
| discount | mixed | Discount to apply when the Priced Individually option is enabled. |
| override_variations | string | Indicates whether to filter the variations available by default.

Values: yes | no |
| allowed_variations | array | Array of active/available variation IDs when filtering is enabled. |
| override_default_variation_attributes | string | Indicates whether to override the default variation attribute values.

Values: yes | no |
| default_variation_attributes | array | Array of default variation attribute keys/values to use when overriding the ones defined at product level. |
| cart_visibility | string | Visibility of the bundled item in cart templates.

Values: visible | invisible |
| order_visibility | string | Visibility of the bundled item in order/e-mail templates.

Values: visible | invisible |
| single_product_visibility | string | Visibility of the bundled item in the single-product template.

Values: visible | invisible |

**Usage**

```
$meta_data = $object->get_meta_data();
```

#### set_all

**Description**

`array set_all()`

Sets/updates all data of the object using the fields of the supplied `$data` array.

**Arguments**

`array $data` – Data to set/update on the object. Refer to [get_data](https://woocommerce.com/document/bundles/bundles-functions-reference/#get_meta_data) for schema details.

**Return Values**

`void`

**Usage**

```
$object->set_all( $data );
```

#### set_meta_data

**Description**

`void set_meta_data( array $data )`

Sets/updates all meta data of the object using the fields of the supplied `$data` array.

**Arguments**

`array $data` – Meta data to set/update on the object. Refer to [get_meta_data](https://woocommerce.com/document/bundles/bundles-functions-reference/#get_meta_data) for schema details.

**Return Values**

`void`

**Usage**

```
$object->set_meta_data( $meta_data );
```

Have a question before you buy? Please fill out this [pre-sales form](https://woocommerce.com/contact-us/#sales-form). Already purchased and need assistance? [Get in touch with us](https://woocommerce.com/my-account/marketplace-ticket-form/) via the Help Desk!

