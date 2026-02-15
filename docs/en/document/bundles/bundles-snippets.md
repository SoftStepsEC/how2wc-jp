---
title: Snippets
url: https://woocommerce.com/document/bundles/bundles-snippets/
---

Use these snippets to customize the appearance and functionality of WooCommerce Product Bundles.

To use a snippet, download the linked file and activate it as you would with any other plugin. Alternatively, you can copy the code to your site. We would recommend adding these snippets into a separate [snippets plugin](https://wordpress.org/plugins/search/snippets/) rather than modifying your site’s theme files or functions.php file.

**Note**: We are unable to provide support for customizations under our [Support Policy](https://woocommerce.com/support-policy/). If you need to customize a snippet, or extend its functionality, seek assistance from a qualified WordPress/WooCommerce Developer. We highly recommend [Codeable](https://codeable.io/?ref=z4Hnp), or a [Certified WooExpert](https://woocommerce.com/experts/).

By default, optional bundled item checkboxes are unticked by default. This can be changed with the following snippet:

|  | <?php |
|  | /** |
|  | * Plugin Name: WooCommerce Product Bundles – Optional Items Checked by Default |
|  | * Plugin URI: https://woocommerce.com/products/product-bundles/ |
|  | * Description: Use this plugin to have optional bundled items checked/selected by default. |
|  | * Version: 1.1 |
|  | * Author: WooCommerce |
|  | * Author URI: https://woocommerce.com/ |
|  | * Developer: Manos Psychogyiopoulos |
|  | * |
|  | * Requires at least: 4.1 |
|  | * Tested up to: 5.3 |
|  | * |
|  | * Copyright: © 2021 Automattic. |
|  | * License: GNU General Public License v3.0 |
|  | * License URI: http://www.gnu.org/licenses/gpl-3.0.html |
|  | */ |
|  |  |
|  | add_filter( 'woocommerce_bundled_item_is_optional_checked', 'wc_pb_is_optional_item_checked', 10, 2 ); |
|  |  |
|  | function wc_pb_is_optional_item_checked( $checked, $bundled_item ) { |
|  |  |
|  | if ( ! isset( $_GET[ 'update-bundle' ] ) ) { |
|  | $checked = true; |
|  | } |
|  |  |
|  | return $checked; |
|  | } |

To add an “- optional” suffix next to the title of bundled items that have been marked as optional, use the following snippet/plugin:

|  | <?php |
|  | /** |
|  | * Plugin Name: WooCommerce Product Bundles. |
|  | * Plugin URI: https://woocommerce.com/products/product-bundles/ |
|  | * Description: Use this snippet to add an “- optional” suffix next to bundled items' titles |
|  | * Version: 1.0 |
|  | * Author: WooCommerce |
|  | * Author URI: https://woocommerce.com/ |
|  | * Developer: Jason Kytros |
|  | * |
|  | * Requires at least: 2.6.0 |
|  | * Tested up to: 5.7 |
|  | * |
|  | * Copyright: © 2017-2021 Automattic. |
|  | * License: GNU General Public License v3.0 |
|  | * License URI: http://www.gnu.org/licenses/gpl-3.0.html |
|  | */ |
|  |  |
|  | "add_filter( 'woocommerce_bundles_optional_bundled_item_add_suffix', '__return_true' ); |

By default, a bundled item discount can co-exist with a sale price, reducing the final price of a bundled product even further.

Alternatively, you may prefer to ignore sale prices and apply bundled product discounts over the regular prices of bundled products. This is possible with the following snippet:

|  | <?php |
|  | /** |
|  | * Plugin Name: WooCommerce Product Bundles – Discounts over Regular Prices |
|  | * Plugin URI: https://woocommerce.com/products/product-bundles/ |
|  | * Description: Use this snippet to apply bundled item discounts on regular prices. |
|  | * Version: 1.0 |
|  | * Author: WooCommerce |
|  | * Author URI: https://woocommerce.com/ |
|  | * Developer: Manos Psychogyiopoulos |
|  | * |
|  | * Requires at least: 3.8 |
|  | * Tested up to: 5.3 |
|  | * |
|  | * Copyright: © 2021 Automattic. |
|  | * License: GNU General Public License v3.0 |
|  | * License URI: http://www.gnu.org/licenses/gpl-3.0.html |
|  | */ |
|  |  |
|  | // To use this snippet, download this file into your plugins directory and activate it, or copy the code under this line into the functions.php file of your (child) theme. |
|  |  |
|  | add_filter( 'woocommerce_bundled_item_discount_from_regular', 'wc_pb_bundled_item_discount_from_regular', 10, 2 ); |
|  |  |
|  | function wc_pb_bundled_item_discount_from_regular( $from_regular, $bundled_item ) { |
|  | return true; |
|  | } |

Ensure that you are using the latest version of Product Bundles, then use the following snippet/plugin:

|  | <?php |
|  | /** |
|  | * Plugin Name: WooCommerce Product Bundles – Prevent Range-Format Prices |
|  | * Plugin URI: https://woocommerce.com/products/product-bundles/ |
|  | * Description: Use this snippet to prevent Product Bundles from displaying bundle prices in range format. |
|  | * Version: 1.0 |
|  | * Author: WooCommerce |
|  | * Author URI: https://woocommerce.com/ |
|  | * Developer: Manos Psychogyiopoulos |
|  | * |
|  | * Requires at least: 4.1 |
|  | * Tested up to: 5.3 |
|  | * |
|  | * Copyright: © 2021 Automattic. |
|  | * License: GNU General Public License v3.0 |
|  | * License URI: http://www.gnu.org/licenses/gpl-3.0.html |
|  | */ |
|  |  |
|  | // To use this snippet, download this file into your plugins directory and activate it, or copy the code under this line into the functions.php file of your (child) theme. |
|  |  |
|  | add_filter( 'woocommerce_bundle_force_old_style_price_html', '__return_true' ); |

The following snippet demonstrates how to adjust the number of bundled item columns to 4:

|  | <?php |
|  | /** |
|  | * Plugin Name: WooCommerce Product Bundles – Bundled Items Grid Layout column count |
|  | * Plugin URI: http://woocommerce.com/products/product-bundles/ |
|  | * Description: Use this snippet to change the bundled items column count when using the 'Grid' Layout option. |
|  | * Version: 1.0 |
|  | * Author: WooCommerce |
|  | * Author URI: http://woocommerce.com |
|  | * Developer: Jason Kytros |
|  | * |
|  | * |
|  | * Copyright: © 2021 Automattic. |
|  | * License: GNU General Public License v3.0 |
|  | * License URI: http://www.gnu.org/licenses/gpl-3.0.html |
|  | */ |
|  |  |
|  | add_filter( 'woocommerce_bundled_items_grid_layout_columns', 'wc_pb_grid_layout_change_number_of_columns', 10, 2 ); |
|  |  |
|  | function wc_pb_grid_layout_change_number_of_columns( $columns, $bundle ) { |
|  | return 4; |
|  | } |

When the **Grouped** selection is active under [Item Grouping](https://woocommerce.com/document/bundles/bundles-configuration/#grouping-options), the subtotals of parent/child line items in cart/order templates are added together and the actual subtotal of the parent item is replaced by the aggregated subtotal. Additionally, the subtotals of individually-priced items are indented and displayed with a **Subtotal:** prefix.

To prevent this, use the following snippet/plugin:

|  | <?php |
|  | /** |
|  | * Plugin Name: WooCommerce Product Bundles – Prevent Subtotals Aggregation |
|  | * Plugin URI: https://woocommerce.com/products/product-bundles/ |
|  | * Description: Prevents Product Bundles from displaying aggregated item subtotals in cart/order templates. Requires v5.5+. |
|  | * Version: 1.0 |
|  | * Author: WooCommerce |
|  | * Author URI: https://woocommerce.com/ |
|  | * Developer: Manos Psychogyiopoulos |
|  | * |
|  | * Requires at least: 4.1 |
|  | * Tested up to: 5.3 |
|  | * |
|  | * Copyright: © 2021 Automattic. |
|  | * License: GNU General Public License v3.0 |
|  | * License URI: http://www.gnu.org/licenses/gpl-3.0.html |
|  | */ |
|  |  |
|  | add_filter( 'woocommerce_bundles_group_mode_options_data', 'sw_pb_group_mode_options_data' ); |
|  |  |
|  | function sw_pb_group_mode_options_data( $data ) { |
|  | $data[ 'parent' ][ 'features' ] = array( 'parent_item', 'child_item_indent' ); |
|  | return $data; |
|  | } |

By default, the stock of a Product Bundle is calculated based on the remaining stock of the bundled items.

To calculate the stock of the bundle based on the stock of parent item instead, which is defined under **Product Data > Inventory,** use the following snippet:

|  | <?php |
|  | /** |
|  | * Plugin Name: WooCommerce Product Bundles. |
|  | * Plugin URI: https://woocommerce.com/products/product-bundles/ |
|  | * Description: Use this snippet to hide the remaining stock of the parent item |
|  | * Version: 1.0 |
|  | * Author: WooCommerce |
|  | * Author URI: https://woocommerce.com/ |
|  | * Developer: Jason Kytros |
|  | * |
|  | * Requires at least: 2.6.0 |
|  | * Tested up to: 5.7 |
|  | * |
|  | * Copyright: © 2021 Automattic. |
|  | * License: GNU General Public License v3.0 |
|  | * License URI: http://www.gnu.org/licenses/gpl-3.0.html |
|  | */ |
|  |  |
|  | add_filter( 'woocommerce_bundle_display_bundled_items_stock_quantity', 'wc_sw_hide_bundled_items_stock_quantity' ); |
|  | function wc_sw_hide_bundled_items_stock_quantity() { |
|  | return false; |
|  | } |

### Hide the short description that shows up for each Bundle-Sell

To hide the short description that shows up for each Bundle-Sell, use the following snippet:

|  | <?php |
|  | /** |
|  | * Plugin Name: WooCommerce Product Bundles. |
|  | * Plugin URI: https://woocommerce.com/products/product-bundles/ |
|  | * Description: Use this snippet to hide the bundled sells short description |
|  | * Version: 1.0 |
|  | * Author: WooCommerce |
|  | * Author URI: https://woocommerce.com/ |
|  | * Developer: Jason Kytros |
|  | * |
|  | * Requires at least: 2.6.0 |
|  | * Tested up to: 5.7 |
|  | * |
|  | * Copyright: © 2021 Automattic. |
|  | * License: GNU General Public License v3.0 |
|  | * License URI: http://www.gnu.org/licenses/gpl-3.0.html |
|  | */ |
|  |  |
|  | add_filter( 'wc_pb_bundle_sell_data_item_args', 'sw_pb_hide_bundle_sells_description', 10, 3 ); |
|  |  |
|  | function sw_pb_hide_bundle_sells_description( $args, $bundle_sell_id, $product ) { |
|  | $args[ 'meta_data' ][ 'override_description' ] = 'yes'; |
|  | return $args; |
|  | } |

### Set the Bundle Sells layout to Grid

To change the default Bundle-Sells layout and make them show up in a **Grid** layout, use the following snippet:

|  | <?php |
|  | /** |
|  | * Plugin Name: WooCommerce Product Bundles. |
|  | * Plugin URI: https://woocommerce.com/products/product-bundles/ |
|  | * Description: Use this snippet to change the bundle sells layout to grid |
|  | * Version: 1.0 |
|  | * Author: WooCommerce |
|  | * Author URI: https://woocommerce.com/ |
|  | * Developer: Jason Kytros |
|  | * |
|  | * Requires at least: 2.6.0 |
|  | * Tested up to: 5.7 |
|  | * |
|  | * Copyright: © 2021 Automattic. |
|  | * License: GNU General Public License v3.0 |
|  | * License URI: http://www.gnu.org/licenses/gpl-3.0.html |
|  | */ |
|  |  |
|  | add_filter( 'wc_pb_bundle_sells_dummy_bundle', 'wc_sw_bs_change_layout' ); |
|  |  |
|  | function wc_sw_bs_change_layout( $bundle ) { |
|  | $bundle->set_layout( 'grid' ); |
|  |  |
|  | return $bundle; |
|  | } |

### Set the Bundle Sells layout to Tabular

To change the default Bundle-Sells layout and make them show up in a **Tabular** layout, use the following snippet:

|  | * Plugin URI: https://woocommerce.com/products/product-bundles/ |
|  | * Description: Use this snippet to change the bundle sells layout to tabular |
|  | * Version: 1.0 |
|  | * Author: WooCommerce |
|  | * Author URI: https://woocommerce.com/ |
|  | * Developer: Jason Kytros |
|  | * |
|  | * Requires at least: 2.6.0 |
|  | * Tested up to: 5.7 |
|  | * |
|  | * Copyright: © 2021 Automattic. |
|  | * License: GNU General Public License v3.0 |
|  | * License URI: http://www.gnu.org/licenses/gpl-3.0.html |
|  | */ |
|  |  |
|  | add_filter( 'wc_pb_bundle_sells_dummy_bundle', 'wc_sw_bs_change_layout' ); |
|  |  |
|  | function wc_sw_bs_change_layout( $bundle ) { |
|  | $bundle->set_layout( 'tabular' ); |
|  |  |
|  | return $bundle; |
|  | } |

### Display the bundled products’ full description

By default, bundled items display the short description of the corresponding Simple/Variable products.

To display the full description, use the following snippet:

|  | <?php |
|  | /** |
|  | * Plugin Name: WooCommerce Product Bundles. |
|  | * Plugin URI: https://woocommerce.com/products/product-bundles/ |
|  | * Description: Use this snippet to display the bundled products' full description |
|  | * Version: 1.0 |
|  | * Author: WooCommerce |
|  | * Author URI: https://woocommerce.com/ |
|  | * Developer: Jason Kytros |
|  | * |
|  | * Requires at least: 2.6.0 |
|  | * Tested up to: 5.7 |
|  | * |
|  | * Copyright: © 2021 Automattic. |
|  | * License: GNU General Public License v3.0 |
|  | * License URI: http://www.gnu.org/licenses/gpl-3.0.html |
|  | */ |
|  |  |
|  | add_action( 'init', 'sw_pb_wc_replace_bundled_items_description' ); |
|  |  |
|  | function sw_pb_wc_replace_bundled_items_description() { |
|  | remove_action( 'woocommerce_bundled_item_details', 'wc_pb_template_bundled_item_description', 20, 2 ); |
|  | add_action( 'woocommerce_bundled_item_details', 'wc_pb_template_bundled_item_full_description', 20, 2 ); |
|  | } |
|  |  |
|  | function wc_pb_template_bundled_item_full_description( $bundled_item, $bundle ) { |
|  | wc_get_template( 'single-product/bundled-item-description.php', array( |
|  | 'description' => $bundled_item->product->get_description() |
|  | ), false, WC_PB()->plugin_path() . '/templates/' ); |
|  | } |

By default, bundled items show up in a list in mobile screens.

However, we understand that in some cases it is preferable to display bundled items on mobile using the same layout as in desktop view. To achieve this, please use the following snippet:

```
add_filter( 'woocommerce_bundle_front_end_params', 'sw_pb_change_responsive_breakpoint' );
function sw_pb_change_responsive_breakpoint( $frontend_params ) {
	$frontend_params[ 'responsive_breakpoint' ] = 0;
	return $frontend_params;
}
```

### How to move the Add to Cart button before the bundled items on the product page

**Note**: The following solutions only work on Product Bundle pages, **not** the Bundle-Sells feature.

To display the **Add to Cart** button before all bundled items, you can use [WooCommerce Product Bundles – Top Add to Cart Button](https://href.li/?https://github.com/somewherewarm/woocommerce-product-bundles-top-add-to-cart-button#woocommerce-product-bundles---top-add-to-cart-button), a free mini-extension for [WooCommerce Product Bundles](https://href.li/?https://woocommerce.com/products/product-bundles/) that adds an extra add-to-cart button section at the top of Product Bundle pages.

Alternatively, to display **a single Add to Cart** button before all bundled items, use the following snippet:

```
add_action( 'woocommerce_before_add_to_cart_form', 'sw_pb_move_add_to_cart_button', 100 );

function sw_pb_move_add_to_cart_button() {
	global $product;

	if ( ! is_a( $product, 'WC_Product' ) ) {
		return;
	}

	if ( ! $product->is_type( 'bundle' ) ) {
		return;
	}
	
	remove_action( 'woocommerce_bundles_add_to_cart_wrap', 'wc_pb_template_add_to_cart_wrap' );
	add_action( 'woocommerce_before_bundled_items', 'wc_pb_template_add_to_cart_wrap' );
}
```

Once you install this snippet, you’ll notice that the **Add to Cart** button will show up *directly*above the bundled items form.

To add some space between them, we recommend adding the following CSS snippet as well:

```
.bundle_form .bundle_wrap {  	
    margin-bottom: 10% !important;  
}
```

By default, WooCommerce core displays **Cross-Sells** for every single cart item. When you add a Product Bundle to the cart, then one cart item is created for the parent bundle and one cart item is created for each bundled item. Therefore, both Cross-Sells linked to the Bundle itself and Cross-Sells linked to the individual bundled products will show up in the cart.

To prevent **Cross-Sells** linked to bundled products from showing up, use the following snippet:

```
add_filter( 'woocommerce_cart_crosssell_ids', 'sw_pb_remove_bunlded_item_crossells', 10, 2 );

function sw_pb_remove_bunlded_item_crossells( $cross_sells, $cart ) {

	$cross_sells = array();
	$in_cart     = array();
	if ( ! $cart->is_empty() ) {
		foreach ( $cart->get_cart() as $cart_item_key => $values ) {
			if ( $values['quantity'] > 0 ) {
				if ( wc_pb_is_bundled_cart_item( $values ) ) {
					continue;
				}
				$cross_sells = array_merge( $values['data']->get_cross_sell_ids(), $cross_sells );
				$in_cart[]   = $values['product_id'];
			}
		}
	}
	$cross_sells = array_diff( $cross_sells, $in_cart );
	return $cross_sells;
}
```

### How to resolve custom theme issues with the Tabular layout in mobile screens

In the past, we have received reports from store owners that the Tabular layout does not work well in mobile screens with their custom theme. One of the most common issues is that a part of the table is cut off or looks like it doesn’t fit entirely in the screen.

To modify the way Tabular layout works in mobile screens so that:

- it looks similar to the ‘Standard’ layout, and;
- better fits small pages;

you can use the following CSS snippet:

```
@media (max-width: 568px) {
  .woocommerce #content div.product .bundle_form div.bundled_product_summary .bundled_product_images, .woocommerce div.product .bundle_form div.bundled_product_summary .bundled_product_images, .woocommerce-page #content div.product .bundle_form div.bundled_product_summary .bundled_product_images, .woocommerce-page div.product .bundle_form div.bundled_product_summary .bundled_product_images {
    width: 100%;
    float: left;
    margin-left: 0;
    margin-right: 0; }
  .bundle_form div.bundled_product_summary:not(.thumbnail_hidden) .details {
    width: 100%;
    float: left;
    margin-left: 0;
    margin-right: 0; }
  .bundle_form div.bundled_product_summary .bundled_product_images {
    max-width: 50%; }
  .bundle_form div.bundled_product_summary .bundled_product_images img {
    margin-bottom: 1em; }
  .bundle_form table.bundled_products td {
    display: block; }
  .bundle_form table.bundled_products thead {
    display: none; }
  .bundle_form table.bundled_products tr td.bundled_item_images_col {
    width: 100%;
    padding-bottom: 0; }
  .bundle_form table.bundled_products tr td.bundled_item_images_col, .bundle_form table.bundled_products tr td.bundled_item_details_col {
    padding-bottom: 0; }
  .bundle_form table.bundled_products tr td.bundled_item_images_col {
    width: 100%; }
  .bundle_form table.bundled_products tr td.bundled_item_qty_col {
    max-width: 100%;
    text-align: left; } }
```

```
add_filter( 'woocommerce_product_is_visible', 'wc_hide_insufficient_stock_bundles_from_upsells', 10, 2 );

function wc_hide_insufficient_stock_bundles_from_upsells( $visible, $product_id ) {

	if ( ! $visible ) {
		return $visible;
	}

	$product_type = WC_Data_Store::load( 'product' )->get_product_type( $product_id );

	if ( 'bundle' === $product_type ) {

		$bundle = wc_get_product( $product_id );

		if ( 'yes' === get_option( 'woocommerce_hide_out_of_stock_items' ) && ! $bundle->is_in_stock() ) {
			$visible = false;
		}
	}
	return $visible;
}
```

To remove optional out of stock bundled items from a bundle, use the following snippet:

```
add_filter( 'woocommerce_bundled_items', 'sw_remove_out_of_stock_items', 10, 2 );

function sw_remove_out_of_stock_items( $bundled_items, $bundle ) {
    foreach ( $bundled_items as $key => $bundled_item ) {
        if ( $bundled_item->is_optional() || $bundled_item->get_quantity( 'min' ) == 0 ) {
            if ( 'outofstock' === $bundled_item->product->get_stock_status() ) {
                unset( $bundled_items[ $key ] );
            }
        }
    }
    return $bundled_items;
}
```

**Note**: it is not possible to remove mandatory out of stock products as this would trigger an add to cart validation error.

### Prevent changes to a bundled item’s quantity in the cart

To prevent customers from changing a Bundle’s configuration once it is added to their cart. use the following snippet:

```
add_filter( 'woocommerce_cart_item_quantity', 'wc_cart_item_quantity', 15, 3 );   

function wc_cart_item_quantity( $product_quantity, $cart_item_key, $cart_item ) {                                      
    if ( is_cart() && wc_pb_is_bundled_cart_item( $cart_item ) ) {
        $product_quantity = sprintf( '%2$s ', $cart_item_key, $cart_item['quantity'] );
    }
    return $product_quantity;
}
```

### Change the size of bundled item images

When you upload an image to WordPress, it automatically generates four additional image sizes:

- **Thumbnail** (150px square)
- **Medium** (up to 300px width and height)
- **Large** (up to 1024px width and height)
- **Full** (the original size you uploaded)

WooCommerce adds three more image sizes:

- **woocommerce_thumbnail** – Used in product grids, such as the shop page. Defaults to 600px width, square-cropped for consistency. The aspect ratio can be customized.
- **woocommerce_single** – Used on single product pages. Displays the full product image as uploaded, uncropped by default. Defaults to 600px width.
- **woocommerce_gallery_thumbnail** – Used for gallery navigation below the main product image. Always square-cropped and defaults to 100×100 pixels.

By default, bundled item images use the **large** image size. To change this, use the following filter:

```
add_filter( 'bundled_product_large_thumbnail_size', 'sw_wc_pb_change_thumbnail_size', 10, 1 );function sw_wc_pb_change_thumbnail_size( $thumbnail_size ) {        return 'woocommerce_gallery_thumbnail';}
```

### How to add a title / heading before bundled items

The following code snippet can be used to add a title before bundled products that are created with the **Product bundle** product type:

```
add_action( 'woocommerce_before_bundled_items', 'wc_display_bundled_items_heading' );

function wc_display_bundled_items_heading() {
	echo '<h3> Bundled items: </h3>';
}
```

Bundled items that are priced individually and have a max quantity of greater than 1, display an “each” suffix in their price string. To replace this suffix with a custom string, use the following snippet:

```
add_filter( 'woocommerce_bundled_item_price_html', 'sw_pb_remove_pc', 10, 3 );

function sw_pb_remove_pc( $price_html, $price, $bundled_item ) {
	$price_html = str_replace( 'each', 'test', $price_html );
	return $price_html;
}
```

**Note**; Before using this snippet, replace `test` with your desired custom string.

### How to use the Product Bundles JavaScript API

To start writing custom code that uses the Product Bundles JavaScript API, you can use the following template:

```
add_action( 'wp_footer', function() {
	?>
	<script type="text/javascript">
		jQuery( function( $ ) {

			$( '.bundle_data' ).on( 'woocommerce-product-bundle-initialized', function( event, bundle ) {
				// Write your custom code here. 
			} );
		} );
	</script>
	<?php
} );
```

To remove downloadable files associated with bundled items, use the following snippet:

```
 add_filter( 'woocommerce_order_get_downloadable_items', 'sw_pb_remove_bundled_items_files', 10, 2 );

function sw_pb_remove_bundled_items_files( $downloads, $order ) {

	$downloads = array();

	foreach ( $order->get_items() as $item ) {
		if ( ! is_object( $item ) ) {
			continue;
		}

		if ( wc_pb_is_bundled_order_item( $item ) ) {
			continue;
		}

		if ( $item->is_type( 'line_item' ) ) {
			$item_downloads = $item->get_item_downloads();
			$product        = $item->get_product();
			if ( $product && $item_downloads ) {
				foreach ( $item_downloads as $file ) {
					$downloads[] = array(
						'download_url'        => $file['download_url'],
						'download_id'         => $file['id'],
						'product_id'          => $product->get_id(),
						'product_name'        => $product->get_name(),
						'product_url'         => $product->is_visible() ? $product->get_permalink() : '', // Since 3.3.0.
						'download_name'       => $file['name'],
						'order_id'            => $order->get_id(),
						'order_key'           => $order->get_order_key(),
						'downloads_remaining' => $file['downloads_remaining'],
						'access_expires'      => $file['access_expires'],
						'file'                => array(
							'name' => $file['name'],
							'file' => $file['file'],
						),
					);
				}
			}
		}
	}
	return $downloads;
}
```

By default, the stock status of a Bundle gets updated only when:

- the stock of a product added as a bundled item changes or;
- then the product added as bundled item is deleted — but **not** when **trashed**.

If you’d like to also update the stock status of the Bundle when a product that is added as a bundled item gets trashed, use the following snippet:

```
add_action( 'wp_trash_post', function( $id ) {
	if ( $id > 0 ) {

		$post_type = get_post_type( $id );

		if ( 'product' === $post_type ) {
			$bundled_item_ids = array_keys( wc_pb_get_bundled_product_map( $id, false ) );

			if ( ! empty( $bundled_item_ids ) ) {
				foreach ( $bundled_item_ids as $bundled_item_id ) {
					WC_PB_DB::bulk_delete_bundled_item_stock_meta( array( $bundled_item_id ) );
				}
			}
		}
	}
} );
```

Have a question before you buy? Please fill out this [pre-sales form](https://woocommerce.com/contact-us/#sales-form). Already purchased and need assistance? [Get in touch with us](https://woocommerce.com/my-account/marketplace-ticket-form/) via the Help Desk!

