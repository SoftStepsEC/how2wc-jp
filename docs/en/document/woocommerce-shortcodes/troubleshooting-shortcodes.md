---
title: Troubleshooting shortcodes
url: https://woocommerce.com/document/woocommerce-shortcodes/troubleshooting-shortcodes/
---

On this page, you’ll find a few common reasons why WooCommerce shortcodes may not work as expected.

If your shortcodes are correctly pasted but display incorrectly, ensure they are not enclosed between `<pre>` tags.

To remove these tags, edit the page, and click the **Text** tab:

A common problem is when **straight** quotation marks (`"`) are used instead of **curly** quotation marks (`“`). For shortcodes to function correctly, you must use straight quotation marks.

When using an SKU shortcode (such as `[products skus="sku-name"]`), do not use the variation name SKU from *Product data > Variable product > Variations > Variation name > SKU* should not be used.

The solution is to instead use an SKU from the **parent variable product**‘s *Product data* meta box — *Product data > Variable product > Inventory > SKU*.

**Note:**We are unable to provide support for customizations under our [Support Policy](https://woocommerce.com/support-policy/). If you need to customize a snippet or extend its functionality, please seek assistance from a qualified WordPress/WooCommerce developer. We highly recommend [Codeable](https://codeable.io/?ref=z4Hnp) or a [Woo Agency Partner](https://woocommerce.com/development-services/).

The **Product Categories List**block displays a list of *all* product categories, both top-level and sub-categories alike. It cannot display *only* top-level categories.

The snippet below adds a new shortcode — `[top_level_product_categories_list]` — which outputs a **bulleted list of top-level product categories** only. Add it to a [child theme](https://developer.woocommerce.com/docs/how-to-set-up-and-use-a-child-theme/)’s `functions.php` file or via a code snippets extension/plugin.

|  | <?php |
|  | /* |
|  | * The shortcode is [top_level_product_categories_list] |
|  | */ |
|  | add_shortcode('top_level_product_categories_list', 'wc_shortcode_top_level_product_categories_list'); |
|  |  |
|  | function wc_shortcode_top_level_product_categories_list() { |
|  |  |
|  | ob_start(); |
|  |  |
|  | $args = array( |
|  | 'taxonomy' => 'product_cat', |
|  | 'parent' => 0 |
|  | ); |
|  |  |
|  | $product_categories = get_categories($args); |
|  |  |
|  | echo '<ul>'; |
|  |  |
|  | foreach ($product_categories as $category) { |
|  | echo '<li><a href="' . get_term_link($category->slug, 'product_cat') . '">' . $category->name . '</a></li>'; |
|  | } |
|  |  |
|  | echo '</ul>'; |
|  |  |
|  | return ob_get_clean(); |
|  | } |

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

