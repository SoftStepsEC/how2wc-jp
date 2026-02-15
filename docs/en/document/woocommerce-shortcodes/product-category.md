---
title: Product Category Shortcodes
url: https://woocommerce.com/document/woocommerce-shortcodes/product-category/
---

These two shortcodes will display your product categories on any page.

- `[product_category]` — Will display products in a specified product category.
- `[product_categories]` — Will display all your product categories.

- `ids` — Specify product [category IDs](https://woocommerce.com/document/find-product-category-ids/) listed. Used with [product_categories]
- `category` — Can be either the category ID, name or slug. Used with [product_category]
- `limit` — The number of categories to display. Entering “0” or leaving undeclared shows all categories. (Interchangeable with `number` as shown in example)
- `columns` — The number of columns to display. Defaults to 4
- `hide_empty` —The default is “1” which will hide empty categories. Set to “0” to show empty categories.
- `parent` — Set to a specific category ID if you would like to display all the child categories. Alternatively, set to “0” (like in the example below) to show only the top level categories.
- `orderby` — The default is order by “name”, “id”, “slug”, or “menu_order” are additional options. If you want to order by the IDs you specified, then you can use `orderby="include"`
- `order` **—** States whether the category ordering is ascending (`ASC`) or descending (`DESC`), using the method set in `orderby`. Defaults to `ASC`.

Imagine you only wanted to show top level categories on a page and exclude the sub categories, well it’s possible with the following shortcode.

```
[product_categories number="0" parent="0"]
```

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

