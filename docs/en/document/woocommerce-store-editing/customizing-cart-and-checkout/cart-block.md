---
title: Cart block
url: https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/cart-block/
---

The Cart block in WooCommerce allows customers to review and manage the items they intend to purchase. It offers options for updating quantities and removing products, as well as reviewing shipping options and adding coupons to the order.

This page explains the components of the Cart block and how to customize both its filled and empty states.

**Note:**

You can add the Cart block to any page, but, for everything to function properly, you’ll need to first **designate your chosen checkout page** in your store’s [advanced settings](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/) via **WooCommerce > Settings > Advanced.** You can only have **one** designated cart page at a time.

The Cart block has two customizable states:

- [Filled Cart](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/cart-block/#filled-cart-state)
- [Empty Cart](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/cart-block/#empty-cart-state)

If you open the [List View](https://woocommerce.com/document/woocommerce-store-editing/the-editor/#list-view), you’ll see that the cart template contains a block named Cart. This Cart block has these two states nested inside of it. Each state contains distinct elements and customization options.

When any block inside the main Cart block is selected, you’ll see an option in the block toolbar to adjust which state you’re viewing. You can also select Filled Cart or Empty Cart blocks via the List View to display the appropriate state.

Most blocks in the filled cart state contain dynamic content, depending on what your customers have in their cart. As such, most are [locked](https://woocommerce.com/document/woocommerce-store-editing/blocks/#locked-blocks); they **cannot** be removed or rearranged.

#### Cart Items

The Cart Items section includes a block displaying the line items in the cart, as well as a subsection displaying [cross-sells](https://woocommerce.com/document/managing-products/product-editor-settings/#cross-sells).

#### Cross-Sells

Cross-sells are product recommendations displayed in the Cart to encourage customers to add related items before checkout, thus increasing the average order value.

**Note:**

Earlier, this functionality was provided by the **Cross-Sells block**. Beginning with WooCommerce 10.2, this block has been [soft-deprecated](https://developer.woocommerce.com/2025/08/28/developer-advisory-product-collection-blocks-cross-sells-replaces-the-cart-cross-sells/) and replaced with the more flexible **Product Collection block**, which now powers cross-sells.

When a new Cart block is added, the Cross-Sells section is now automatically powered by the [Product Collection block](https://woocommerce.com/document/woocommerce-store-editing/customizing-shop-page-catalog/product-collection-block/). By suggesting complementary products in the cart using cross-sells, you can significantly increase the average order value.

The **Product Collection block** powering Cross-Sells includes several [block settings](https://woocommerce.com/document/woocommerce-store-editing/blocks/#block-settings) to control how products are displayed:

- Linked Product : Show products based on items in the Cart or select a specific product.
  - From products in the cart: Displays cross-sells linked to the items currently in the customer’s cart.
  - From a specific product: Allows you to select a single product, and its linked cross-sells will be shown regardless of what is in the cart.
  
- **Order By**: Define the order of products (e.g., alphabetically).
- **Layout Style**: Display products in a *Stack*, *Grid*, or *Carousel*.
- **Width**: Set the block to either stretch and fill available space (*Fill*) or remain at a fixed width.
- **Products per Page**: Adjust how many products appear on each page.
- **Columns**: Control the number of columns in the layout, with a responsive option to adapt for smaller screens.
- **Max Pages to Show**: Limit the number of cross-sell product pages (set 0 to show all).
- **Filters**: Refine results by showing only products on sale or by stock status (*In stock*, *Out of stock*, *On backorder*).

Because the Product Collection block is shared across WooCommerce, you can use the same customization patterns in other parts of your store, creating a more unified merchandising experience.

**Note for existing stores:**

If your Cart page already contains a Cross-Sells block, it will continue to work as expected. You will also see an option to transform it into a Product Collection block.

The Cross-Sells section is [unlocked](https://woocommerce.com/document/woocommerce-store-editing/blocks/#locked-blocks) and can be removed or rearranged if desired.

#### Cart Totals

In the **Cart Totals** section, both the Order Summary heading and coupon form are unlocked and can be removed. Additionally, the **Proceed to Checkout**block contains a setting to change the destination link for the Proceed to Checkout button, allowing you to direct customers to a specific checkout page.

By default, the **Empty Cart** state displays a *Your cart is currently empty!* message, with a **Newest Products block** that recommends your shop’s newest products below it. Each of these elements can be removed or rearranged to suit your needs. You can edit the text by clicking on it in the Editor.

The Newest Products block allows you to control the number of products displayed, and choose whether or not to show additional details (such as product image, title, price, rating, add to cart button, etc.).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

