---
title: Product shortcodes
url: https://woocommerce.com/document/woocommerce-shortcodes/products/
---

While WooCommerce primarily [uses blocks](https://woocommerce.com/document/woocommerce-store-editing/)to offer interactive and customizable display settings for products, you can still use legacy **product shortcodes** on your store by adding them to a shortcode block. This document lists and explains the available WooCommerce product-related shortcodes.

**Note:**

The core WooCommerce plugin includes several product blocks which can be more powerful and flexible compared to shortcodes, [learn more about WooCommerce Blocks](https://woocommerce.com/document/woocommerce-blocks/).

The `[products]` shortcode is one of WooCommerce’s most robust shortcodes. It allows you to display products by post ID, stock-keeping unit (SKU), categories, and attributes, with support for pagination, random sorting, and product tags.

This removes the previous need for multiple shortcodes, including:

- `[featured_products]`
- `[sale_products]`
- `[best_selling_products]`
- `[recent_products]`
- `[product_attribute]`
- `[top_rated_products]`

The following attributes are available to use with the `[products]` shortcode.

These attributes alter the way products are displayed, ordered, and arranged within the `[products]` shortcode:

- `limit`: The number of products to display. Defaults to `-1` (display all) when listing products, and `-1` (display all) for categories.
- `columns`: The number of columns to display. Defaults to `4`.
- `paginate`: Toggles pagination. Use in conjunction with `limit`. Defaults to `false` ; set to `true` to enable pagination.
- orderby : Sorts the products displayed by one or more options. Multiple options can be passed by adding both slugs with a space between them. Available options include:
  - `title`: The product title. This is the default `orderby` mode if no other attribute is used.
  - `date`: The date the product was published.
  - `id`: The post ID of the product.
  - `menu_order`: The menu order, if set (lower numbers display first).
  - `popularity`: The number of purchases.
  - `rand`: Randomly orders products when the page loads (may not work with sites that use caching, as it could save a specific order).
  - `rating`: The average product rating.
  
- `order`: States whether the product order is ascending (`ASC`) or descending (`DESC`), using the method set in `orderby`. Defaults to `ASC`.
- `skus`: Comma-separated list of product SKUs.
- `category`: Comma-separated list of category slugs.
- `tag`: Comma-separated list of tag slugs.
- `class`: Adds an HTML wrapper class that you can target and modify using custom CSS.
- `on_sale`: Retrieve products on sale; not to be used in conjunction with `best_selling`or `top_rated`.
- `best_selling`: Retrieve the best-selling products; should not be used in conjunction with `on_sale` or `top_rated`.
- `top_rated` Retrieve top-rated products; should not be used in conjunction with `on_sale`or `best_selling`.

If you do not include the `orderby` attribute, the system will display products in the default sorting order — first by [menu order](https://woocommerce.com/document/managing-products/#advanced-section), then by title.

These attributes determine which products are displayed in the `[products]` shortcode:

- `attribute`: Retrieves products using the specified attribute slug.
- `terms`: Comma-separated list of attribute terms to be used with `attribute`.
- terms_operator : Operator to compare attribute terms. Available options are:
  - `IN`: Displays products with the chosen attribute. This is the default `terms_operator` value.
  - `NOT IN`: Displays products that are not in the chosen attributes.
  - `AND`: Displays products from all the chosen attributes.
  
- tag_operator : Used to compare tags. Available options include:
  - `IN`: Displays products with the chosen tags; this is the default `tag_operator` value.
  - `NOT IN`: Displays products that are not in the chosen tags.
  - `AND`: Displays products from all the chosen tags.
  
- visibility : Displays products based on the selected visibility. Available options include:
  - `visible`: Products visible on shop and search results. This is the default `visibility` option.
  - `catalog`: Products visible on the shop only, but not search results.
  - `search`: Products visible in search results only, but not on the shop.
  - `hidden`: Products that are hidden from both shop and search, accessible only by direct URL.
  - `featured`: Products that are marked as Featured Products.
  

- `category`: Retrieves products using the specified category slug.
- `tag`: Retrieves products using the specified tag slug.
- cat_operator : Operator to compare category terms. Available options are:
  - `IN`: Will display products within the chosen category. This is the default `cat_operator` value.
  - `NOT IN`: Will display products that are not in the chosen category.
  - `AND`: Will display products that belong in all the chosen categories.
  

- `ids`: Displays products based on a comma-separated list of Post IDs.
- `skus`: Displays products based on a comma-separated list of SKUs.

**Note:**

If the product should be shown but isn’t at the moment, make sure it is not set to “Hidden” in the “Catalog Visibility” settings.

To find a product’s ID, go to the Products screen and hover over the product row. The Product ID appears beneath the product title as shown below.

These attributes cannot be used with the product content attributes listed above, as they will likely cause a conflict and not display. You should **only use one** of the following special attributes.

- `best_selling`: Displays your best-selling products when set to `true`.
- `on_sale`: Displays products on sale when set to `true`.

Below you’ll find a few examples of how to use the `[product]` shortcode along with attributes (`args`).

Here’s how to display four sale products at random:

```
[products limit="4" columns="4" orderby="popularity" class="quick-sale" on_sale="true" ]
```

This shortcode explicitly states four products with four columns (which will be one row), showing the most popular on-sale items. It also adds the `quick-sale` CSS class, which we can target and modify using custom CSS.

Here’s how to display featured products, two per row, with a maximum of four items:

```
[products limit="4" columns="2" visibility="featured" ]
```

This shortcode specifies that up to four products will load in two columns and that they *must* be featured. We did not use the `orderby` attribute, so the shortcode will display products in the default sorting (by [menu order](https://woocommerce.com/document/managing-products/#advanced-section), then by title, listed A to Z by default as `order` is not used).

Here’s how you would display three top best-selling products in one row:

```
[products limit="3" columns="3" best_selling="true" ]
```

#### Scenario 4: Newest products

In this example, we’ll display the newest products first — four products across one row. To accomplish this, we’ll use `Post ID` (which increases incrementally with new posts, and is generated when the product page is created), along with the order and `orderby` command. Since you can’t see the Post ID from the front end, the ID numbers have been superimposed over the images.

```
[products limit="4" columns="4" orderby="id" order="DESC" visibility="visible"]
```

Here’s how to display hoodies and shirts, but not accessories. We’ll configure it to display in two rows of four:

```
[products limit="8" columns="4" category="hoodies, tshirts" cat_operator="AND"]
```

Alternatively, if you only want to display products that are *not* in those categories, update the `cat_operator` to `NOT IN`.

```
[products limit="8" columns="4" category="hoodies, tshirts" cat_operator="NOT IN"]
```

**Note:** Even though the limit is set as `8`, only four products that fit that criteria, so four products are displayed.

Each item of clothing has an attribute — either “Spring/Summer” or “Fall/Winter”, depending on the appropriate season — with some accessories having both as they can be worn all year. In this example, there are three products per row, displaying all of the “Spring/Summer” items. The attribute slug is `season`; the attribute’s terms are `warm` and `cold`. We’ve also sorted the products from newest to oldest.

```
[products columns="3" attribute="season" terms="warm" orderby="date"]
```

Alternatively, if we want to display everything but warm-weather products, we could add `NOT IN` as my `terms_operator`:

```
[products columns="3" attribute="season" terms="warm" terms_operator="NOT IN"]
```

**Note:** By using `NOT IN`, we exclude products that are both in “Spring/Summer” and “Fall/Winter”. If we want to show all cold-weather appropriate gear including these shared accessories, we would change the term from `warm` to `cold`.

```
[products tag="hoodie"]
```

**Scope of support:**

We are unable to provide support for customizations under our**Support Policy**. If you need to customize a snippet or extend its functionality, we recommend working with a [Woo Agency Partner](https://woocommerce.com/development-services/) or a WooCommerce developer on [Codeable](https://www.codeable.io/partners/woocommerce/?ref=qGefA6#tiers).

When using the `[products]` shortcode, you can choose to order products by the pre-defined values above. You can also sort products by **custom meta fields** using the code below (in this example we order products by price):

```
add_filter( 'woocommerce_shortcode_products_query', 'woocommerce_shortcode_products_orderby' );

function woocommerce_shortcode_products_orderby( $args ) {

    $standard_array = array('menu_order','title','date','rand','id');

    if( isset( $args['orderby'] ) && !in_array( $args['orderby'], $standard_array ) ) {
        $args['meta_key'] = $args['orderby'];
        $args['orderby']  = 'meta_value_num'; 
    }

    return $args;
}
```

You’ll need to place this snippet in the `functions.php` file in your theme folder and then customize it by editing the `meta_key`.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

