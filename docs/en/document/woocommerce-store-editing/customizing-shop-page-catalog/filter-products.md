---
title: Product Filters block
url: https://woocommerce.com/document/woocommerce-store-editing/customizing-shop-page-catalog/filter-products/
---

Effective product filtering improves the shopping experience by allowing customers to easily find the products they need and proceed to checkout without unnecessary delays. WooCommerce now offers the **Product Filters block** to streamline this process, enabling shoppers to filter products in your store’s catalog.

The Product Filters block provides a fast, seamless experience, where filters are dynamically applied without requiring a full page reload. This block is available from WooCommerce 9.9 and comes with a new “Chips” display style for the Attribute and Status filter blocks. Additionally, this block is context-aware, meaning it can be added inside the [Product Collections block](https://woocommerce.com/document/woocommerce-store-editing/customizing-shop-page-catalog/product-collection-block/) to show relevant filter results for specific product collections.

The Product Filters block was introduced in WooCommerce 9.9 to provide a faster and more fluid shopping experience. This block is context-aware, allowing for more accurate and dynamic filtering based on the surrounding content. You can apply filters in real-time without needing to reload the page.

The Product Filters block can be used on the [Archive Templates](https://woocommerce.com/document/woocommerce-store-editing/customizing-shop-page-catalog/#built-in-templates) (e.g., Product Catalog, Product Taxonomy templates):

- You can add the Product Filters block anywhere on the templates page.
- It will automatically apply filters to the products shown in the archive.

This allows you to create a streamlined experience for customers where filters dynamically reflect the products in the selected Archive template.

The Product Filters block is built from several inner blocks. All inner blocks support real‑time updates, so customers never wait for a page refresh when refining their search.

The Product Filters block comes with a better mobile experience. On mobile, the filter options are hidden inside a modal, which can be revealed by tapping a new filter button. This improves the user experience by keeping the interface clean and uncluttered until the customer opts to filter the products.

These blocks were deprecated in WooCommerce 9.9 and are no longer available in the block inserter, but may exist on older stores using older versions of WooCommerce.

Shop owners are encouraged to upgrade to the new **Product Filters block** introduced in version 9.9 for improved accessibility conformance.

The Active Filters block shows all the product filters that are currently active, and enables customers to disable active filters.

This block works well in tandem with the **Filter by Price**, **Filter by Attribute**, **Filter by Stock**, and **Filter by Rating** blocks. When users select one or more filters from filter blocks, the Active Filters block will display those filters.

#### Active Filters – Block Structure

The active filters block is made up of 2 inner-blocks:

- A heading – which can be removed
- The Active Filters Controls block – which is locked.

#### Customizing the Active Filters Block

After selecting the “Active Filters Controls” block, in the sidebar block settings there is an option to control how selected filters are displayed.

The Filter by Price block enables customers to filter products by choosing a price range.

#### Filter by Price – Block Structure

The Filter by Price block is made up of 2 inner-blocks:

- A heading – which can be removed
- The Filter by Price Controls block – which is locked.

#### Customizing the Filter by Price Block

The Price Range Selector can have editable text input fields, as well as sliders to adjust the price range, or be limited to the draggable sliders.

When the price range selectors are set to be editable, you can choose whether to make the price input fields inline with the slider, or on their own line.

The Filter by Attribute block enables customers to filter products based on selected attributes.

#### Filter by Attribute – Block Structure

The Filter by Attribute block is made up of 2 inner-blocks:

- A heading – which can be removed
- The Filter by Attribute Controls block – which is locked.

#### Customizing the Filter by Attribute block

Access the block’s settings in the sidebar after selecting the “Filter by Stock Controls” inner-block.

There are settings available to:

- Include or omit the product count.
- Allow selecting a single, or multiple options.
- Select the Filter Conditions – if multiple options are allowed to be selected.
- Set the Display Style to list or dropdown.
- Select the Product attribute to be filtered by.
- Configure the text color.
- Hide or show the Apply filters button.

To use the Filter by Attribute block, you’ll need to have at least 1 product on your store that has an attribute assigned to it.

The Filter by Stock block enables customers to filter the product grid by stock status.

#### Filter by Stock – Block Structure

The Filter by Attribute is made up of 2 inner-blocks:

- A heading – which can be removed
- The Filter by Stock Controls block – which is locked.

#### Customizing the Filter by Stock block

Access the block’s settings in the sidebar after selecting the “Filter by Stock Controls” inner-block.

There are settings available to:

- Display the product count for each stock status.
- Allow selecting a single, or multiple options.
- Set the Display Style to list or dropdown.
- Hide or show the Apply filters button.

The Filter by Rating block lets customers filter the product catalog by rating. If no products in your store have ratings, this filter option will display when a product receives a review.

#### Filter by Rating – Block Structure

The Filter by Rating block is made up of 2 inner-blocks:

- A heading block – which can be removed
- The Filter by Rating Controls sub-block – which is locked.

#### Customizing the Filter by Rating block

Access the block’s settings in the sidebar after selecting the “Filter by Rating Controls” inner-block.

There are settings available to:

- Display product count next to the rating options.
- Allow selecting multiple ratings in the filter.
- Display the filter as a list, or dropdown.
- Show an “Apply filters” button

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

