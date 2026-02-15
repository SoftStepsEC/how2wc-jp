---
title: Product Collection Block
url: https://woocommerce.com/document/woocommerce-store-editing/customizing-shop-page-catalog/product-collection-block/
---

The Product Collection block is designed to help you display and customize archives of products; and offer product recommendations.

Upon inserting the block, and depending on the template or page that you are currently editing, you will be prompted to create your own custom product collection; or choose from a list of variations/recipes that enable you to quickly offer some of the most common types of recommendations.

The Product Collection block is used by default in all the WooCommerce templates for displaying your products:

- Product Catalog
- Products by Category
- Products by Tag
- Products by Attribute
- Products by Brand
- Product Search Results

Beyond the templates where it is included, you can add the Product Collection block to any page or template on your site where you’d like to showcase your products.

The Product Collection block has a selection of predefined recipes that you can choose from, and then further customize. The premade collection recipes are great for banners and by default only show a single row of products with no pagination, but can be edited to fit any design or layout. You can also choose to create a custom collection.

By default, the product collection displays your shop’s entire catalog, and adapts to the context of the page that it’s on. For example, if you add a product collection to the “Products by Tag” template and select “create your own”, when a shopper visits the page for a specific tag, they’ll only see the products in your catalog that have that tag. You can disable a product collection from dynamically matching the context of a page by toggling the **Sync with current query** setting in the Collection’s sidebar block settings.

Use this collection to showcase your featured products. See how to [mark products as featured](https://woocommerce.com/document/managing-products/feature-filter-and-sort-products/#mark-a-product-as-featured).

Use this product collection to recommend the products in your shop with the [best reviews](https://woocommerce.com/document/product-reviews/).

Just like the name says, this product collection will showcase the products in your shop that are on sale.

The best sellers product collection showcases the products that have been purchased the most on your site. When products have been sold the same number of times, the product published most recently will be shown first.

The new arrivals product collection highlights products most recently added to your catalog. By default, only products created within the last 7 days will be displayed. This setting can be adjusted in the block sidebar.

Use the Hand-Picked Products collection to showcase a custom selection of products you’ve chosen yourself. Perfect for highlighting exclusive products, or any set of products you want to feature manually.

Use the Related Products collection to automatically recommend items that complement or are similar to what shoppers are already viewing. WooCommerce determines [related products](https://woocommerce.com/document/related-products-up-sells-and-cross-sells/#related-products) automatically based on categories and/or tags.

Use the Upsells product collection to promote higher-end or premium versions of the product a customer is interested in. Add [linked products](https://woocommerce.com/document/related-products-up-sells-and-cross-sells/) on the Edit Product screen.

Use the Cross-sells product collection to highlight products that pair well with items in a customer’s cart. Cross-sells often appear on the cart page or checkout, [suggesting additional items](https://woocommerce.com/document/related-products-up-sells-and-cross-sells/#cross-sells) that enhance or complement the main purchase.

Collections are, essentially, preset filters on the collection block. You can change the selected collection at any time with the “Choose Collection” button in the Block toolbar, then tweak the filters in the [block settings sidebar](https://woocommerce.com/document/woocommerce-store-editing/blocks/#block-settings) as desired.

After selecting which product collection to use, in the list view you’ll see a parent block added that matches the collection you chose, with blocks inside for:

- **Product Template** – These blocks show the product’s image, title, price, and add to cart button.
- **Pagination –**These blocks control how your shoppers navigate through your collection. If you set your collection to show only 1 page of products, these controls will not be displayed.
- **No results**– These blocks show the “Empty state” of the collection. i.e. What your shoppers will see if they navigate to the page and no products match your set collection filters.

Each of these block elements is composed of several nested inner blocks, each of which has its own settings and can be removed if needed. Explore the settings of the parent block and each inner block by selecting it, then checking the block and style settings in the settings sidebar, as well as any settings in the block toolbar. See our guide on exploring block settings here.

In addition to altering the settings of the existing blocks, you can also add additional blocks of your choosing to further customize the product templates, add additional content to the collection area, or change its layout. Feel free to explore and see where your creativity takes you!

The **Product Collection** block offers various layout options and query settings to control how your products are displayed.

#### Default

The **Default** query displays products based on the current template and allows shoppers to filter. The **Default sort by** options are:

- Manual (menu order + name)
- Price, high to low / Price, low to high
- Sales, high to low
- Rating, high to low

All Product Collection blocks using the **Default Query** will sync to this sort order.

#### Custom

The Custom query allows you to display a curated list of products based on specific criteria, rather than relying on the context of the page (as with the Default query type).

This query type allows you to create a custom collection with the help of **Order By**, **Products Per Page**settings**,** and **Sale** and **Stock Status** filters.

**Order By:**With the “Custom” query type, this setting allows you to choose how products should be sorted in the custom collection. The available sorting options are:

- Alphabetical order by product name (A → Z or Z → A)
- Newest to oldest / Oldest to newest
- Price, high to low / Price, low to high
- Sales, high to low / Sales, low to high
- Rating, high to low / Rating, low to high
- Manual (menu order + name)
- Random: Shuffles the product order each time the page loads, providing a fresh experience on each visit.

**Products per Page**: Controls how many products appear within the block at one time. If pagination is not included in the block, only this number of products will display.

**Show Only Products on Sale:** Toggle this option on to display only products that are currently on sale.

**Stock Status**: Select which stock statuses should be included in the product collection.

The Layout settings allow you to control how your products are arranged within the Product collection block.

- **Stack**: Displays products in a single vertical list.
- **Grid**: Displays products in a grid with multiple columns.
- **Carousel**: Displays products in a horizontal slider format. Ideal for use in more visual layouts like landing pages or featured sections.

Customizing your shop page with the Product Collection block gives you lots of options for how to display your products. Here we cover some important basics. You can take things further to create very interesting and compelling designs by utilizing layout blocks to alter the structure, and the style options to match your brand.

To set a product collection to only display a single row of products:

1. In the collection’s **sidebar block settings** choose the “Grid” layout option, then enter how many columns you’d like in your row of products. Leave the “Responsive” toggle **unchecked**.
2. In the collection’s **block toolbar**, click the “Display Settings” icon and set the “Items per page” to the same number of columns you’ve chosen, and the “Max pages to show” to **1**.

Now, your product collection will display as a single row with the number of columns you’ve selected.

If you have a specific design in mind, sometimes you’ll want to display a specific filtered set of products, instead of having the product collection match the query and filters of the current page or template.

To make a Product Collection display a custom filtered set of products:

1. In the collection’s [sidebar block settings](https://woocommerce.com/document/woocommerce-store-editing/blocks/#block-settings) leave the “Sync with current query” toggle disabled. The “Filters” section will appear.
2. Under the “Filters” section in the sidebar block settings, click the three dots menu, then click to toggle the different filtering options.
  - After clicking a filter in the list to toggle it on, that filter and its options will display in the block settings sidebar under the “Filters” section.
  
3. Using your chosen filters filters, select the categories, tags, attributes or combinations that you want to show in this collection.

This can be a great use of a second product collection on a page, that acts as a banner to recommend specific products to your shoppers. The possibilities are nearly endless!

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

