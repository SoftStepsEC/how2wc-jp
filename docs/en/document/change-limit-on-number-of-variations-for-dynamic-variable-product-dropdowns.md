---
title: Change Limit on Number of Variations for Dynamic Variable Product Dropdowns
url: https://woocommerce.com/document/change-limit-on-number-of-variations-for-dynamic-variable-product-dropdowns/
---

Customizations are not covered under our [support policy](https://woocommerce.com/support-policy/), so this isn’t something we can help implement or troubleshoot on your site.

By default, if a Variable product has fewer than 30 variations, the dropdowns for selecting variations on the frontend will be dynamic. For example, with a T-shirt that has “Size” and “Color” attributes, after the customer selects a Size, the Color dropdown will be updated via AJAX to only display options that are available with the chosen Size.

However, if there are more than 30 variations, the dropdowns will be static and will display all attributes. Following the example above, if the T-shirt has more than 30 variations, the Color dropdown will continue showing *all of the color options* even if they are not available for the selected Size. Instead, after they select an unavailable combination, they will see the message “Sorry, no products matched your selection. Please choose a different combination.”

This is done to improve performance on the site. For large numbers of variations, if it has to calculate the available combinations after each selection, it can slow things down quite a bit.

However, this limit can be changed from 30 to another number if desired using the `woocommerce_ajax_variation_threshold` filter:

|  | function custom_wc_ajax_variation_threshold( $qty, $product ) { |
|  | return 10; |
|  | } |
|  |  |
|  | add_filter( 'woocommerce_ajax_variation_threshold', 'custom_wc_ajax_variation_threshold', 10, 2 ); |

