---
title: Filters Reference
url: https://woocommerce.com/document/bundles/bundles-filters-reference/
---

This page is written for developers looking to extend or customize WooCommerce Product Bundles. It requires an advanced understanding of [PHP](http://php.net/) and [WordPress development](http://codex.wordpress.org/Developer_Documentation).

This guide documents the most useful filter hooks available in Product Bundles. It is not an exhaustive reference of all available filters and does not include tutorials on how to achieve certain tasks.

We recommend reading [Data Structures and Storage](https://woocommerce.com/document/bundles/bundles-data-structures-storage/) and keeping the [Functions Reference](https://woocommerce.com/document/bundles/bundles-functions-reference/) handy. Take time to familiarize yourself with the plugin architecture and the objects relevant to the hook you want to use.

#### woocommerce_bundle_requires_input

**Description**

Modifies the output of `WC_Product_Bundle::requires_input`, which indicates whether a product bundle has fields that require configuration in order to be added to the cart.

**Arguments**

`array $quantities_array` – Array of min/max bundled item quantities to use. Quantities are first indexed by the string values `min` and `max` and then by bundled item ID. `WC_Product_Bundle $bundle` – Product bundle object.

#### woocommerce_bundled_items

**Description**

Modifies the collection of bundled items available to a `WC_Product_Bundle` instance and returned by `WC_Product_Bundle::get_bundled_items`.

**Arguments**

`array $bundled_items` – Array of `WC_Bundled_Item` objects associated with the bundle, indexed by bundled item ID. `WC_Product_Bundle $bundle` – Product bundle object.

#### woocommerce_bundle_is_editable_in_cart

**Description**

Use this filter to control whether a Bundle that has been added to the cart can be edited from the cart page.

**Arguments**

`array $is_editable_in_cart` – Indicates whether the bundle can be edited from the cart page. `WC_Product_Bundle $bundle` – Product bundle object. `array|false $cart_item` – Container cart item associated with the bundle when `WC_Product_Bundle::is_editable_in_cart` is called in cart context.

#### woocommerce_bundle_cart_permalink_args

**Description**

Use this filter to modify the arguments added to the permalink of a Bundle when editing its configuration from the cart.

**Arguments**

`array $args` – Parameter name/values to add to the permalink. `array|false $cart_item` – Container cart item associated with the bundle when `WC_Product_Bundle ::is_editable_in_cart` is called in cart context. `WC_Product_Bundle $bundle` – Product bundle object.

#### woocommerce_bundled_item_discount_from_regular

**Description**

Use this filter to change the reference price used for calculating bundled item discounts.

**Arguments**

`boolean $calc_discounts_from_regular` – Indicates whether to calculate discounted item prices using regular prices as reference. `False` by default. `WC_Bundled_Item $bundled_item` – Bundled item object.

**Example**

In [this snippet](https://woocommerce.com/document/bundles/bundles-snippets/#discount_over_sale_prices), the filter is used to calculate discounted prices over regular prices.

#### woocommerce_bundled_item_group_of_quantity

**Description**

Use this to override the bundled items’ ‘Group of’ quantity.

**Arguments**

`integer $group_of_quantity` – The default quantity value. `WC_product $product` – The bundled product object. `WC_Bundled_Item|int $bundled_item_or_product` – Bundled item or product object.

**Example**

```
add_filter( 'woocommerce_bundled_item_group_of_quantity', 'filter_group_of', 10, 3 );

function filter_group_of( $group_of_quantity, $product, $bundled_item_or_product ) {
    return 1;
}
```

#### woocommerce_bundled_item_is_optional_checked

**Description**

Filters the default checkbox state of optional bundled items.

**Arguments**

`integer $quantity_value -`The default quantity value.`WC_Bundled_Item $bundled_item` – Bundled item object.

**Example**

In [this snippet](https://woocommerce.com/document/bundles/bundles-snippets/#optional_checked), the filter is used to make optional bundled items selected by default.

#### woocommerce_bundled_item_classes

**Description**

Filters the html classes assigned to bundled item container elements in the single-product template.

**Arguments**

`array $classes` – Class names. `WC_Bundled_Item $bundled_item` – Bundled item object.

#### woocommerce_bundled_product_quantity

**Description**

Modifies the default bundled product quantity value, which is equal to the minimum quantity by default.

**Arguments**

`integer $quantity_value` – The default quantity value. `integer $quantity_min` – The default quantity value. `integer $quantity_max` – The default quantity value. `WC_Bundled_Item $bundled_item` – Bundled item object.

#### woocommerce_bundles_optional_bundled_item_suffix

**Description**

Modifies the “optional” suffix appended to optional bundled items.

**Arguments**

`WC_Bundled_Item $bundled_item` – Bundled item object. `WC_Product_Bundle $bundle` – Product bundle object.

**Example**

In [this snippet](https://woocommerce.com/document/bundles/bundles-snippets/#remove_optional_suffix), the filter is used to remove the title suffix of optional bundled items.

#### woocommerce_bundle_front_end_params

**Description**

Use this filter to modify the parameters passed to the single-product add-to-cart script.

**Arguments**

`array $params` – Array of parameters passed to the front-end script.

#### woocommerce_force_show_bundled_dropdown_variation_attribute_options

**Description**

Use this filter to always render the attribute options of bundled variable products in drop-down menus. By default, if a bundled variable product has only one active variation with well-defined attribute values, then its attribute selection drop-downs are hidden and replaced by pre-selected value descriptions.

**Arguments**

`boolean $force_dropdowns` – Indicates whether to force the display of drop-down menus for attribute value selection. `array $args` – Array of parameters passed to the front-end script.

#### woocommerce_bundle_show_bundled_product_attributes

**Description**

Controls whether to show the attributes of a bundled product in the single-product page of the bundle that contains it.

By default, if a bundled product is set to be visible in the single-product template of its bundle, its attributes are displayed after the attributes of the bundle.

**Arguments**

`boolean $include` – Indicates whether to display the attributes of the bundled product. `WC_Product_Bundle $bundle` – Product bundle object. `WC_Bundled_Item $bundle` – Bundled item object.

#### woocommerce_bundled_item_add_to_cart_validation

**Description**

Applied when performing add-to-cart validation for bundle-type products, this filter can be used to run custom validation logic at bundled item level.

**Arguments**

`boolean $passes_validation` – Validation result. `WC_Product $bundle` – Product object associated with the bundled item being validated. `WC_Bundled_Item $bundled_item` – `WC_Bundled_Item` object. `integer $quantity` – Bundled product quantity. `integer|''|false $variation_id` – Variation ID, if applicable. `array $configuration` – Bundle configuration array.

#### woocommerce_add_to_cart_bundle_validation

**Description**

Applied when performing add-to-cart validation for bundle-type products, this filter provides a last chance to modify a successful validation result.

**Arguments**

`boolean $passes_validation` – Validation result. `integer $bundle_id` – Product bundle ID. `WC_PB_Stock_Manager $stock_mgr` – Stock manager object used for validating bundled product stock quantities. `array $configuration` – Bundle configuration array.

#### woocommerce_bundled_item_has_bundled_weight

**Description**

When creating an **Assembled** bundle, you can use the **Assembled Weight** option to control how to calculate its weight. If the assembly has a static weight, you can choose the **Ignore** option, while if you prefer to calculate its weight dynamically, you can choose the **Preserve** option. When **Preserve** is selected, the weight of the assembly is calculated by adding:

- the specified container **Weight**; and
- the weight of all **assembled** bundled items.

With this filter, it is possible to control whether to add or ignore individual bundled item weights programmatically.

**Arguments**

`boolean $add_weight_to_container` – Indicates whether the weight of this bundled product should be appended to the weight of the parent. Defaults to `false`. `WC_Product $product` – The bundled product object. `integer $bundled_item_id` – The ID of the bundled item that the product is associated with. `WC_Product_Bundle $bundle` – The product bundle object.

#### woocommerce_bundled_cart_item

**Description**

Use this filter to modify the cart item data of bundled products, which is re-applied on session load.

**Arguments**

`array $cart_item` – Cart item data of bundled product. `WC_Product_Bundle $bundle` – The parent product bundle object.

#### woocommerce_bundle_container_cart_item

**Description**

Use this filter to modify the cart item data of bundle containers, which is re-applied on session load.

**Arguments**

`array $cart_item` – Cart item data of bundle container product. `WC_Product_Bundle $bundle` – The product bundle object.

#### woocommerce_bundled_item_cart_item_identifier

**Description**

Use this filter to add custom fields to the configuration data of a product bundle when it is added to the cart. Commonly used when adding custom configuration input fields to bundled products.

**Arguments**

`array $item_configuration` – Bundled item configuration array. `integer $bundled_item_id` – Bundled item ID. `integer $bundle_id` – Product bundle ID.

**Examples**

The use of this filter is demonstrated in the `WC_PB_Addons_Compatibility` class included in Product Bundles, which contains compatibility code for the [Product Add-Ons](https://woocommerce.com/products/product-add-ons/) extension. The filter is used to read posted data associated with bundled Product Add-Ons fields before adding the bundle to the cart, in order to pass them to the hashing function used to generate the cart ID of the bundle.

#### woocommerce_bundled_item_cart_data

**Description**

Provides an opportunity to modify bundled/child cart item data by copying data that is already stored in the container/parent cart item. Commonly used to copy data added using the [woocommerce_bundled_item_cart_item_identifier](https://woocommerce.com/document/bundles/bundles-filters-reference/#woocommerce_bundled_item_cart_item_identifier) filter.

**Arguments**

`array $bundled_item_cart_data` – Custom fields to add to the cart item data of a bundled product when it gets added to the cart. `integer $cart_item_data` – Cart item data of the container/parent, which has just been added in the cart.

**Examples**

The use of this filter is demonstrated in the `WC_PB_Addons_Compatibility` class included in Product Bundles, which contains compatibility code for the [Product Add-Ons](https://woocommerce.com/products/product-add-ons/) extension. The filter is used to copy bundled Product Add-Ons fields from the container cart item.

#### woocommerce_add_bundled_order_item_subtotals

**Description**

By default, the order item subtotal of a bundle container item is calculated as the sum of the: i) base bundle subtotal, and ii) the subtotals of any bundled items that are priced individually. Additionally, the subtotals of individually-priced items are displayed with a ‘Subtotal:’ prefix. The filter can be used to prevent this.

**Arguments**

`boolean $add_subtotals` – Indicates whether to modify the way subtotals appear. Defaults to `true`. `array $container_item_data` – Container/parent order item. `WC_Order $order` – Order object.

**Example**

[This snippet](https://woocommerce.com/document/bundles/bundles-snippets/#prevent_subtotals_modifications) demonstrates how to prevent the extension from modifying item subtotals in the cart/orders.

#### woocommerce_bundle_container_order_item_sku

**Description**

Use this filter to alter the SKU of an **assembled** product bundle object modified using the [get_product_from_item](https://woocommerce.com/document/bundles/bundles-functions-reference/#get_product_from_item) method, based on a list of the bundled products and quantities assembled in the bundle (any bundled items that are not [Shipped Individually](https://woocommerce.com/document/bundles/product-bundles-store-owners-guide/#shipping)).

**Arguments**

`string $sku` – The bundle SKU. `WC_Product $product` – The product bundle object. `WC_Order_Item_Product $container_item` – Container/parent order item. `array $assembled_items` – Bundled order items physically assembled in the bundle for shipping. `WC_Order $order` – Order object.

#### woocommerce_bundles_process_bundled_item_admin_data

**Description**

Use this filter to intercept and process custom posted fields associated with bundled item admin options. Any custom fields added here will be saved as custom bundled item meta.

**Arguments**

`array $processed_data` – Array of parameters to be used for adding/updating a specific bundled item. `array $posted_data` – Array of posted data associated with a specific bundled item. `integer|'' $bundled_item_id` – ID of the bundled item when updating, or empty when creating it for the first time. `integer $bundled_id` – ID of the product bundle.

#### woocommerce_bundled_product_admin_html_tabs

**Description**

Use this filer to create extra tabs to display custom admin options for bundled items, in addition to the default **Basic Settings** and **Advanced Settings** tabs.

**Arguments**

`array $tabs` – Array tab sections to display.

Have a question before you buy? Please fill out this [pre-sales form](https://woocommerce.com/contact-us/#sales-form). Already purchased and need assistance? [Get in touch with us](https://woocommerce.com/my-account/marketplace-ticket-form/) via the Help Desk!

