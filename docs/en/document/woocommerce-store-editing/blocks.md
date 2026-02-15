---
title: Using Blocks in WooCommerce
url: https://woocommerce.com/document/woocommerce-store-editing/blocks/
---

WooCommerce includes a number of blocks that you can insert in posts, pages and Site Editor patterns and templates to customize your catalog, promote your products, and deliver a great checkout experience to your shoppers.

In this guide, we cover the basics of how blocks work, where to find their settings, and how to revert to the classic templates if you run into any issues.

To get the most out of the site editing features built into WooCommerce, you’ll need to use a [Block Theme](https://wordpress.org/documentation/article/block-themes/). It is still possible to utilize blocks without a block theme — however, you’ll only be able to use blocks on posts and pages, and will not have access to the site editor for customizing your shop’s templates.

As always, to make the most of the latest WooCommerce features, including blocks, we highly recommend updating WordPress and WooCommerce to the latest stable version.

A [block theme](https://wordpress.org/support/article/block-themes/) is a theme that consists of templates that can be customized in the Site Editor. This means that not only the post or page content is made of blocks but all areas of the site are made from blocks, including headers, footers, sidebars, and other elements. To take advantage of all of the store editing features in WooCommerce, your site needs to be using a block theme.

To explore available block themes:

1. From your WP Admin Dashboard Navigate to **Appearance > Themes**.
2. Click on “Add New Theme.”
3. Click the “Block Themes” option.

All the shown themes will be editable via the site editor, so you can take advantage of the Store Editing features in WooCommerce.

To **customize** a block-based theme, you need to activate it first. If you’re concerned about doing so, we recommend that you set up a test site first to explore the theme.

Blocks are content elements that make up your site and store. Each item you add to a post or page is a block. You can add blocks for each paragraph, images, videos, galleries, audio, lists, and so much more.

You can add blocks to your pages and templates via [the Editor](https://woocommerce.com/document/woocommerce-store-editing/the-editor/).

Each block has options in the [Block Toolbar](https://woocommerce.com/document/woocommerce-store-editing/blocks/#block-toolbar) and [Block Settings Sidebar](https://woocommerce.com/document/woocommerce-store-editing/blocks/#block-settings). The Block’s Content displays in the center of the editor. Depending on the block’s purpose, the options on the Block Toolbar and Block settings sidebar will change. Many WooCommerce blocks use dynamic content to match the current context (e.g. showing what each customer currently has in their cart;) in the editor these dynamic blocks will show sample content.

There are multiple ways to insert blocks throughout pages.

- At the top left of the page, you’ll notice a toolbar with a square + icon. Clicking this icon opens the Block Inserter. It will allow you to search for blocks and insert them. It also shows additional information per block and a small preview.
- In the editor field, you will see a block inserter option, also with a + icon when you click above, in between, or below blocks that you already have in the editor.

**Pro tip:** A shorthand trick for adding a new block is to type “/” and the block name that you want to insert. This is called the [Slash command.](https://woocommerce.com/document/woocommerce-store-editing/blocks/#searching-for-blocks)

You can search for blocks using:

- The block inserter – type the beginning of a block name or keyword, for example, “image” or “heading”, in the inserter’s search field.
- The Slash Command – start typing the beginning of a block name or keyword and auto-suggested search results will appear.

**Not finding a block when you search for it?** Blocks can be limited to only be available or inserted in certain contexts (templates, areas, inner blocks), and developers can limit which blocks are available in some areas. Here are some examples:

- Some blocks can only be added in certain contexts (e.g. the “Cart Cross Sells” block can only be added inside of the “[Cart items](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/cart-block/#cart-items)” section of the Cart Block)
- Some contexts will limit what blocks can be added in them (e.g. inside the “Cart Totals” section of the cart block, only *paragraph*, *image*, *separator*, and the “*Accepted Payment Methods*” blocks are available to be added)
- Some blocks can only be added once per template or area (e.g. the “*Accepted Payment Methods*” block can only be added to the “*Cart Totals*” section of the cart block once)

These restrictions allow developers who build blocks for specific implementations to ensure that their blocks won’t be inserted in a context that will break the functionality of the block and your store.

If you’d like to remove a block from a page or template, you have several options. To remove a block:

1. Select the block.
2. Click on the three-dot icon in the block’s toolbar or the list view.
3. Click the “Delete” option.

Another way to delete a block is to select the block and press the [keyboard shortcut](https://wordpress.org/documentation/article/keyboard-shortcuts-block-editor/). (*Control + Option + Z* on Mac, or *Shift + Alt + Z* on Windows.) Some blocks can be deleted by pressing the “delete” or “backspace” button on your keyboard after selecting them.

Some templates include placeholder blocks that indicate where the actual content of your store will appear once you publish your changes. We recommend that you do not delete placeholder blocks from your templates without testing to be sure you understand the effects, to avoid unintended errors or missing information on your store.

To customize a block, first select the block you want to customize. Select a block by clicking on the block in the content area, or using the **List View**to find a specific block and selecting it in the list.

You can then access the block’s customization options in two places: the [block toolbar](https://woocommerce.com/document/woocommerce-store-editing/blocks/#block-toolbar) and the [block settings](https://woocommerce.com/document/woocommerce-store-editing/blocks/#block-settings)

When you click on a block, the block’s toolbar will appear above or below it. The toolbar contains essential options for working with that block.

Hover over the icons in your Block Toolbar to display a tool-tip explaining what each icon does:

#### Global Block Toolbar Options

Some options will show in most blocks’ toolbars. These are explained below:

- **Transform**: Change a block to a similar block type. For example, if you want to change your Cart block to the classic version of the cart, clicking this icon will give you the option.
- **Drag**: Click and hold the icon that looks like six dots to drag the block to another section of the page.
- **Move up/down**: Click the up or down arrow to move the block up/down one position on the page.
- **Alignment**: Change the positioning of the block. If available, you will usually find left, right, and center, as well as wide and full width if supported by your theme.
- More Options: The three vertical dots at the end of the toolbar opens a menu with additional actions:
  - **Copy**: Make a copy of the block to your clipboard, which you can then paste elsewhere.
  - **Duplicate**: Create a copy of the block directly below the original.
  - **Add before**: Create a space above the current block to add a new block.
  - **Add after**: Create a space under the current block to add a new block.
  - **Copy styles**: Copy the Styles used on the block.
  - **Paste styles:** After copying a block’s Styles, paste those Styles onto the selected block.
  - **Group/Ungroup:** Using this option, you can group multiple blocks together – useful for applying colors and padding to a set of blocks.
  - **Lock**: Disable the option to move and/or delete the block. Read more about [locked Blocks](https://woocommerce.com/document/woocommerce-store-editing/blocks/#locked-blocks)
  - **Create Pattern**: Save the block with your customizations so you can add it to other areas throughout your site. Read more about [block patterns](https://woocommerce.com/document/woocommerce-store-editing/patterns-template-parts/)
  - **Rename:** Assign a new name to a block as it appears in List View.
  - **Move to:** Click this option, and then click on another section of your page to move the block to that section of the page.
  - **Edit as HTML**: Edit the block content in HTML.
  - **Delete**: Removes the current block from your page.
  

Not all of these settings will be available for every block. For example, if a [block is locked](https://woocommerce.com/document/woocommerce-store-editing/blocks/#locked-blocks), you won’t see the option to delete it, and may not see the option to move it.

#### Block-Specific Toolbar Options

Each block will also have its own toolbar options specific to that block. For example, the Image block toolbar contains settings to add a link, crop the image, and more:

#### Selecting Parent Blocks

When you’ve selected a block that is nested inside of another block, the block toolbar will have an extra, separate button floating to the left of it. Clicking this button will move your selection to the current block’s immediate parent.

The Block Settings sidebar contains more customization options for the block you’re working on. Each block has its own settings that you can find in the settings sidebar:

If you don’t see the sidebar, click the settings icon next to the **Save** button in the top right corner of the editor. This icon looks like a square with two uneven columns:

Note that at the top of the sidebar which expands, there are two tabs. To see the settings for your currently selected block, ensure you’re viewing the “Block” tab. Available options will vary from block to block, some blocks have no settings to alter in the sidebar.

Locked blocks are a feature of the block editor that allows developers or site administrators to restrict certain actions on specific blocks. Locked blocks are particularly useful in Full Site Editing (FSE) and when creating custom block patterns or templates.

When creating your own layouts, you can lock blocks in the editor to prevent them from being moved or deleted. When you lock a block, you also have the ability to unlock it via the “More Options” three dot menu in the block toolbar.

Blocks can also be locked by developers to protect layouts, content, and functionality of templates. Several WooCommerce templates use locked blocks to prevent content from being broken by getting moved out of necessary context, as well as to ensure that certain elements remain ordered or positioned as intended. Often when a block is locked by default like this, it cannot be unlocked.

For example, most checkout fields in the checkout block are locked, to maintain the high converting layout that is the result of our research and testing. These locked blocks show with a lock icon in the list view, as well as a lock icon in the block toolbar when selected.

When you look in the list view, you may notice that some blocks are nested inside of others. We call these nested blocks **inner blocks.**Moving or removing a block that has inner blocks also moves or removes all its inner blocks.

WooCommerces introduces a number of blocks that you can use to showcase your catalog, promote your products in different ways, and deliver a great checkout experience to your shoppers.

Use the following guides to understand how you can use WooCommerce blocks to customize your store:

- [Catalog pages, including your Shop page](https://woocommerce.com/document/woocommerce-store-editing/customizing-shop-page-catalog/)
- [Product pages](https://woocommerce.com/document/woocommerce-store-editing/customizing-product-pages/)
- [Cart and Checkout pages](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/)
- [Order Confirmation page](https://woocommerce.com/document/woocommerce-store-editing/customizing-order-confirmation-page/)

## Using Classic Templates: Placeholder Blocks and Shortcodes

The WooCommerce blocks are fully functional and most extensions fully support the block-based experience at this time. However, it’s possible that while using the WooCommerce blocks an extension running on your store may not work as expected. For backwards compatibility, the classic WooCommerce templates, and cart + checkout shortcodes continue to be available in WooCommerce for existing stores that have customized checkout flows requiring them, and for any new stores that have specific needs not yet possible with the block templates.

If you’re using a block theme, but your shop has customizations in place on the classic templates, or uses extensions that are not yet compatible with store editing and the new block templates, in those cases you can revert to the classic templates in the block editor by swapping the modern blocks for classic blocks.

These classic blocks act as placeholders to display the legacy templates, and so can’t be customized in the block editor, but enable the classic templates to be displayed on block themes.

We’ve included quick-swap options in the site editor for these templates so that you can revert quickly if you need to.

### Reverting to the classic Cart and Checkout

Both the cart and checkout can have their block transformed back to the classic version using the transform button in the block toolbar. Here’s how to do it:

1. **Using a block theme**: Go to **Appearance -> Editor -> Pages ->** Select Cart or Checkout -> click the *Edit icon*****Using a non-block theme**: Go to **Pages -> All Pages**, and then locate and edit the Cart/Checkout page.
2. Open the List View and select the Cart or Checkout block. If you have an incompatible extension installed, a notice will be displayed and you can revert in 1 click.
3. Click the **Transform** button, which is leftmost in the block toolbar
4. Choose “Classic Shortcode”.
5. The block will be transformed into a Classic Shortcode placeholder block.
6. Save your changes by clicking the Update button in the top bar.

To swap the new block templates for their classic versions, you have two options:

- Recommended: When viewing the template you’d like to revert, in the “Template” tab of the settings sidebar, click the “Revert to Classic Template” button. This option is available on the following templates:
  - Product Catalog templates
  - Single Product template
  - Order Confirmation template
  - Product Search Results template
  

- Or, you can manually delete the new blocks from your template, and add their classic counterpart listed in the table below to the template.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

