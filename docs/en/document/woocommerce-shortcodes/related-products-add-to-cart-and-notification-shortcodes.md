---
title: Related Products, Add-to-Cart, and Notification Shortcodes
url: https://woocommerce.com/document/woocommerce-shortcodes/related-products-add-to-cart-and-notification-shortcodes/
---

On this page are shortcodes for adding a **related product section**, an **add-to-cart button with price**, and showing **shop messages/notifications** on non-WooCommerce pages. Listed below are each shortcode and their attributes.

If you want to show the **related products** (products with similar tags or categories) on a single product page to encourage cross-sells/up-sells you can use the **[related_products] shortcode**. Below is the short code and the `attributes` available to format it:

Here are the attributes you can use to format this shortcode:

- **Limit :**Limits the amount of related products shown to users using this shortcode. For example, [related_products limit =’12”] will limit the amount of products shown to 12 products.

- **Columns:**Determines the amount of columns used to display the related products. For example, [related_products columns=”4″] would place products in 4 distinct columns (1 product per row of the column). That means, if we combined it with our limit of 12, we’d have 3 rows of 4 products each.

- **Orderby :**Determines the order of products in the related product section. You can order by price or title.

Here’s an example of how to use this shortcode with a few `attributes` set and the shortcode placed in the “Product description” section of a single product:

`[related_products limit="4" columns ="3" orderby="price"]`

You can use shortcodes to display an “add-to-cart” button on any page. This is helpful if you want to highlight a product somewhere outside your shop page. Below is the short code and its available `attributes` and an example of how it can be used on a post.

These are the attributes that are available:

- **id :** This is the product ID. You can find the product ID by hovering over a product under **Products > All Products**. Adding the product ID to the Add-to-Cart short will display the price and the add-to-cart button for a specific product.
- **style**: This is the general styling for the add-to-cart button; you can set border, border type/color, and padding.
- **sku**: This is the product SKU. If you don’t set the product id, the shortcode will use the SKU to display the correct add to cart button.
- **show_price :**Mark this as “TRUE” or “FALSE” to show the price alongside the add-to-cart button.
- **class :**Add additional CSS.
- **quantity**: Determines the quantity added to the cart. (**note:** this attribute will only work if you are adding the shortcode via a theme templates).

```
[add_to_cart id="99"]
```

Here’s an example of what this looks like with the code: `[add_to_cart id="xx" style="border:none; padding 10px"]` added to a post (**please note:**[add_to_cart] only adds the button and the pricing for the product, it does not add any images or additional product information). :

**Note:** Replace “*xx*” with product id of the product you want to display the add-to cart button for.

Display the URL on the add to cart button of a single product by ID.

Two attributes are available for this shortcode: **id**or **sku**. The same attributes are used with the [add_to_cart] shortcode in the previous example.

```
[add_to_cart_url id="99"]
```

Use `[shop_messages]` to show WooCommerce notifications (like, ‘The product has been added to cart’) on non-WooCommerce pages. This is helpful when you use other shortcodes, like `[add_to_cart]` or `[product_page]`, and would like the users to get some feedback on their actions. Here’s an example of what it looks like with the [add_to_cart id=”xx”] shortcode:

**Note**: If you are using this to display [add_to_cart] messaging you need to deactivate `Enable AJAX add to cart buttons on archives` under **WooCommerce > Settings > Products** general settings for messages to be displayed:

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

