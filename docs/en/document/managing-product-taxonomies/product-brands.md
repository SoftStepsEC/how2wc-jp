---
title: Product brands
url: https://woocommerce.com/document/managing-product-taxonomies/product-brands/
---

Brands in WooCommerce offer an additional and helpful way to create brands for your shop, with a name, description, and image assigned to each.

To start adding brands:

1. Go to: **WooCommerce >** **Products > Brands**. The interface looks and works similar to adding categories and tags — the form on the left lets you add a brand, which are then displayed on the right.
2. **Enter a Name and Description**. Image is optional. Brands can be hierarchical, specifying a ‘parent’ with ‘child’ brands under it.
3. **Select Add New Brand** to save.

Modify Brands by hovering over the Name and click **Edit** or **Delete**. Brands may also be **re-ordered**by dragging and dropping.

*Did you know?* Assigning a brand to a product also adds Brand name Schema to the product page which is helpful in SEO! That being said, assigning brands to products is the same process as adding categories and tags.

1. Go to: **WooCommerce > Products**.
2. **Select a product** to assign a brand.
3. Find the **Brands** box in the right sidebar.
4. **Tick the box of brands** you wish to assign to the product.
5. **Update or Publish** to save changes.

To display the brands in different ways across your site you can use the following Shortcodes. These shortcodes are ways to call in complicated code, giving you many options with only a few keystrokes.

To use a shortcode, copy the text starting with “[” and ending with “]”, then paste into your editor. As an example, `[product_brand]`shows a brand’s image on the single product page.

#### Product brand

Shows a single brand’s image with a link to its archive page. This only works on single product pages, not on posts or other WordPress pages. Note that showing brands on the single page with this shortcode will only pull 1 brand and not all.

```
array(
      'width' => '64px',
      'height' => '64px',
      'class' => 'aligncenter'
 )
```

**Example Shortcode:**

```
[product_brand class="alignright"]
```

#### Brand products

Show all products in a certain brand.

```
array(
      'per_page' => '12',
      'columns' => '4',
      'orderby' => 'title',
      'order' => 'asc',
      'category' => 'boots,sandals',
 )
```

**Example Shortcode:**

```
[brand_products brand="hiro-shoes" per_page="12" columns="4"]
```

#### Product brand list

Shows an A-Z index of all brands with links to their archive pages.

```
array(
      'show_top_links' => 'true',
      'show_empty_brands' => 'false'
 )
```

**Example Shortcode:**

```
[product_brand_list show_empty_brands="true"]
```

#### Product brand thumbnails

Shows a list of all product brand thumbnails with links to their archives.

```
array(
      'columns' => '12',
      'show_empty' => 'true',
      'orderby' => 'name',
      'exclude' => '2,5,8', // Category IDs to exclude
      'number' => '' // Number of brands to show.
 )
```

**Example Shortcode:**

```
[product_brand_thumbnails number="12" show_empty="false"]
```

#### Product brand thumbnails description

Shows a list of all product brand thumbnails with brand descriptions and links to their archives.

```
array(
      'columns' => '12',
      'show_empty' => 'true',
      'orderby' => 'name',
      'exclude' => '2,5,8', // Category IDs to exclude
      'number' => '' // Number of brands to show.
 )
```

**Example Shortcode:**

```
[product_brand_thumbnails_description number="12" show_empty="false"]
```

To get the shortcode to display on multiple product pages, you would want to add it into a template or onto a hook using the **do_shortcode** function, as seen here:

```
echo do_shortcode('[product_brand width="64px" height="64px" class="alignright"]')
```

In some situations, you may want to display the brand image associated with the product in your product page, as shown below:

There are two ways to implement this, either on a single product basis or applying to all products.

#### To apply to a Single Product

In the product’s body area, you can add the shortcode

```
[product_brand width="64px" height="64px" class="alignright"]
```

In that example, it would link to the brand of the product, establish the width and height in pixels (each 64), and align it to the right side. The ‘class’ field isn’t required – it’s by default set to ‘aligncenter’, but you can do left or right as well.

#### To apply to All Products

First, ensure that you’re making edits in a child theme.

This allows you to customize content without the risk of an update removing your work. To learn more about how to customize a child theme, [visit our child theme tutorial](http://woothemes.zendesk.com/entries/22505632-How-to-setup-and-use-a-child-theme), or read more about how child themes at the [WordPress Codex](http://codex.wordpress.org/Child_Themes).

In your child theme, go to the functions.php file and add the following snippet:

|  | add_action( 'woocommerce_single_product_summary', 'wc_ninja_add_brand_to_product_page', 19 ); |
|  | function wc_ninja_add_brand_to_product_page() { |
|  | echo do_shortcode('[product_brand width="64px" height="64px" class="alignright"]'); |
|  | } |

You can also add in this snippet using a plugin like [Code Snippets](https://wordpress.org/plugins/code-snippets/).

This gives us the following logo positioning, which is displayed on all product pages and changes dynamically to fit the brand:

By default, adding a brand’s name to the product page isn’t possible without custom code. The snippet below can be used to display the brand name, but falls outside our scope of support.

First, ensure that you’re making edits in a child theme.

This allows you to customize content without the risk of an update removing your work. To learn more about how to customize a child theme, [visit our child theme tutorial](http://woothemes.zendesk.com/entries/22505632-How-to-setup-and-use-a-child-theme), or read more about how child themes at the [WordPress Codex](http://codex.wordpress.org/Child_Themes).

In your child theme, go to the functions.php file and add the following snippet:

|  | <?php |
|  |  |
|  | /* |
|  | * Increase `1` on line 7 to move position of brand name |
|  | */ |
|  |  |
|  | add_action( 'woocommerce_single_product_summary', 'wc_brands_add_brand_name', 1 ); |
|  |  |
|  | function wc_brands_add_brand_name() { |
|  | global $product; |
|  | $brands =  implode(', ', wp_get_post_terms($product->get_id(), 'product_brand', ['fields' => 'names'])); |
|  | echo "<p>Brand: " . $brands . "</p>"; |
|  | } |

You can also add in this snippet using a plugin like [Code Snippets](https://wordpress.org/plugins/code-snippets/).

To learn more about how to add the Brands Widgets listed below to your site, you can refer [Widgets included with WooCommerce](https://woocommerce.com/document/woocommerce-widgets/).

This widget shows the description for the currently viewed brand archive.

This widget provides **layered navigation** for products based on brand. This widget works together with [other layered-navigation WooCommerce widgets](https://woocommerce.com/document/woocommerce-widgets/#section-2) and can be used accordingly.

This widget lists brands with thumbnails.

Version 1.5+ supports the REST API

The Brands REST API allows you to create, view, update, and delete individual, or a batch, of brands. The endpoint is `/wp-json/wc/v1/products/brands` which basically mimics `/wp-json/wc/v1/products/categories`. You can refer to the same documentation of [product categories REST API](https://woocommerce.github.io/woocommerce-rest-api-docs/#product-categories).

In addition to `/products/brands` endpoints, the `/products` endpoints also updated to display `brands` in the response and check the JSON request for `brands`.

- Retrieve all product brands: `curl https://example.com/wp-json/wc/v2/products/brands -u consumer_key:consumer_secret`
- Create a product brand: `curl -X POST https://example.com/wp-json/wc/v2/products/brands \ -u consumer_key:consumer_secret \ -H "Content-Type: application/json" \ -d '{ "name": "Apple", "image": { "src": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/768px-Apple_logo_black.svg.png" } }'`
- Delete a product brand: `curl -X DELETE https://example.com/wp-json/wc/v2/products/brands/9?force=true -u consumer_key:consumer_secret`
- Set brands to a product: `curl -X PUT https://example.com/wp-json/wc/v2/products/123 \ -u consumer_key:consumer_secret \ -H 'Content-Type: application/json' \ -d '{"brands": [48, 49]}'` Note: When setting a brand to a product the url needs to be `products/123` where `123` is the id of the product you want to update.

To display a product’s brand in the product’s URL, visit **Settings > Permalinks** and add `%product_brand%`, as desired, to your **Product Permalink** setting. Note: `%product_brand%` requires `shop` as a base: `/shop/%product_brand%`

The [product import/export feature](https://woocommerce.com/document/product-csv-importer-exporter/) built into WooCommerce does not yet have feature parity with the [Product CSV Import Suite](https://woocommerce.com/products/product-csv-import-suite/) extension as it currently only handles default fields + meta fields while brands are stored in taxonomies.

As such, the Product CSV Import Suite is the tool for the job. You’ll need to add a column with the heading `tax:product_brand` to the CSV file with the brand names in that column so that the brand information is tied to your products.

Yes. When you have **WooCommerce Brands** installed, a new option will display for the brand attribute under the **Google Listings and Ads** tab on the product edit page. Each product can then be edited and have its brand attribute set to “From WooCommerce Brands”:

In your theme’s `functions.php` file, add:

|  | add_filter( 'woocommerce_sortable_taxonomies','wt_sort_brands' ); |
|  | function wt_sort_brands( $sortable ) { |
|  | $sortable[] = 'product_brand'; |
|  | return $sortable; |
|  | } |

Brand thumbnails will then be organized in the same order that they appear in the backend.

Each brand has its own archive, viewable at http://domain.com/`brand`/brand-slug/. The `brand` section of the above URL structure can be adjusted by adding the following snippet to your theme’s `functions.php` file, or to your custom functionality plugin:

|  | function customise_product_brand_slug ( $tax ) { |
|  | $tax['rewrite']['slug'] = 'custom-slug'; // Replace 'custom-slug' with your desired slug. |
|  | return $tax; |
|  | } |
|  | add_filter( 'register_taxonomy_product_brand', 'customise_product_brand_slug' ); |

Go to **Settings > Permalinks** and re-save after adding the above code snippet. This ensures your permalinks are refreshed and ready to go, using the new brand slug.

With the following code snippet you’ll want to find the page ID of your own Brands parent page and replace it with the appropriate page ID. In our example we used a page with the ID of 14, but change it to your own. Add this to your child theme’s `functions.php` file, or to your custom functionality plugin:

|  | function wc_custom_brands_breadcrumb( $crumbs, $breadcrumb ){ |
|  |  |
|  | // The ID for the page that you want to act as the brands top archive |
|  | $page_url = get_the_permalink(14); |
|  |  |
|  | foreach( $crumbs as $key => $crumb ){ |
|  | if( $crumb[0] === __('Brands') ) { |
|  | // If you have changed the slug with the snippet above |
|  | // The breadcrumb will still say Brand, so you will want to |
|  | // Replace 'Name' below with your desired breadcrumb text |
|  | // Otherwise, you'll want to remove the next line of code entirely |
|  | $crumbs[$key][0] = __( 'Name', 'woocommerce' ); |
|  | $crumbs[$key][1] = $page_url; |
|  | } |
|  | } |
|  |  |
|  | return $crumbs; |
|  | } |
|  | add_filter( 'woocommerce_get_breadcrumb', 'wc_custom_brands_breadcrumb', 20, 2 ); |

|  | <?php |
|  | if ( is_plugin_active( 'woocommerce-brands/woocommerce-brands.php' ) ) { |
|  |  |
|  | add_action( 'woocommerce_shop_loop_item_title', 'add_brands_to_product_loop' ); |
|  |  |
|  | // Add brands to product loop. |
|  | function add_brands_to_product_loop() { |
|  | $terms = get_the_terms( get_the_ID(), 'product_brand' ); |
|  | if ( ! empty( $terms ) && ! is_wp_error( $terms ) ) { |
|  | $term = join( ', ', wp_list_pluck( $terms, 'name' ) ); |
|  | echo esc_html( $term ); |
|  | } |
|  | } |
|  | } |

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

