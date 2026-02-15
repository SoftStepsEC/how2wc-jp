---
title: Mini-Cart block
url: https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/mini-cart/
---

The Mini-Cart block is added to the site header of many block themes by default. It gives customers a way to quickly view and edit their cart contents from any page on your store.

This guide explains the functionality of the Mini-Cart block and provides instructions for customizing its appearance and behavior to ensure a smooth and convenient shopping experience.

The Mini-Cart block displays a button for shoppers to quickly view their cart. It has settings so you can select a different cart icon, show the current total cart price, and choose whether to hide or completely remove the Mini-Cart when a shopper is on the cart or checkout page. There is also a setting to choose whether or not the Mini-Cart drawer gets opened when a shopper adds a product to their cart.

The Mini-Cart block also has block style settings that control the colors of its components, as well as typography and dimension options.

In many cases the Mini-Cart will need no customization at all, as your theme’s styles will be applied.

When the Mini-Cart button is clicked, a cart drawer slides out and gives shoppers easy access to view their selected products, and head to checkout. WooCommerce uses a [template part](https://woocommerce.com/document/woocommerce-store-editing/patterns-template-parts/) to display the Mini-Cart’s contents when your shoppers open the Mini-Cart. To edit the appearance of the expanded Mini-Cart, you’ll need to edit the Mini-Cart template part.

### Accessing the Mini-Cart Template Part

You can access the Mini-Cart Drawer template part to edit it in a few different ways:

- In the block settings sidebar for the Mini-Cart block, choose “Edit Mini-Cart Drawer Template” from the “Cart Drawer” section of settings.

- Access the template part directly using the editor command palette:

1. Navigate to **WP Admin Dashboard > Appearance > Editor**.
2. On your keyboard, press Cmd+k on Mac or Ctrl+k on Windows.
3. Search for the “Mini-Cart” template part

- Access the template part in the editor navigation:

1. Navigate to **WP Admin Dashboard > Appearance > Editor**.
2. Click “Patterns”.
3. Select the “Mini-Cart” template part under “Template Parts” in the patterns menu.

Many of the blocks in the Mini-Cart are locked, which means they can’t be removed or rearranged, however, you can edit the content and settings for the existing blocks. You can also add blocks of your own choice to customize both the filled and empty states of the Mini-Cart.

#### Mini-Cart States

Once you’ve accessed the template part, if you open the list view you’ll see that it contains a block called “Mini-Cart Contents”, which has two *states* nested inside of it:

- Filled Mini-Cart view
- Empty Mini-Cart view

WIth any block selected, In the block toolbar you’ll see the option to adjust which state you’re viewing. Or you can select a block from either the **Filled**or **Empty** Mini-Cart from the list view and the appropriate state will be displayed.

To add a block to a state of the Mini-Cart:

1. Select the state you’d like to edit.
2. Click the “Add Block” button in the template.
3. Search for the block of your choice and select it.

#### Mini-Cart Block Settings

In the **Filled** Mini-Cart view there are block settings to:

- Adjust the color, typography and dimensions of the heading elements.
- Control the button style and color of the “View my Cart” and “Go to Checkout” buttons in the Mini-Cart footer.
- You can edit the text of the headings or buttons by clicking on the text.

In the **Empty** Mini-Cart view there are block settings to:

- Adjust the color, typography and dimensions of the paragraph element.
- Control the button style and color of the “Start Shopping” button.
- You can edit the “Your cart is currently empty!” message or the button text by clicking on the text.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

