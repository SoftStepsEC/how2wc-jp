---
title: WooCommerce Pages
url: https://woocommerce.com/document/woocommerce-pages/
---

Upon installation, WooCommerce creates the following new pages via the [Setup Wizard](https://woocommerce.com/document/woocommerce-setup-wizard/):

- Shop – No content required.
- Cart – Contains the [WooCommerce Cart Block](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/cart-block/) and shows the cart contents.
- Checkout – Contains [WooCommerce Checkout Block](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/) and shows information such as shipping and payment options.
- My Account – Contains `[woocommerce_my_account]` shortcode and shows customers information related to their account, orders, etc.
- Refund and Returns Policy (Unpublished draft) – Contains sample text to help you get started writing your store’s [Refund and Returns Policy](https://woocommerce.com/document/refund-policy-page-guidelines/). Not required but strongly recommended.

**How can I add a shortcode if I am using the block editor?**

To add the shortcode to a page with the Block Editor, please use the `Shortcode` Block, enter the [shortcode](https://woocommerce.com/document/woocommerce-shortcodes/) and save the page.

If you skipped the Setup Wizard or want to install missing WooCommerce pages, go to **WooCommerce > Status > Tools** and use the page installer tool. This will create any missing default WooCommerce pages.

By default, WooCommerce will set the Cart, Checkout, My account, Terms and conditions (ToC), and Shop pages to the default pages that were created during onboarding. If you create new pages that differ from the default pages or want to change what pages are used for things like cart and checkout, you need to set those in the **Page setup**settings.

To set pages for Cart, Checkout, My Account, and Terms and Conditions, navigate to **WooCommerce > Settings > Advanced.** Then select the page of your choice in the relevant dropdown.

**Why can’t I set the Cart, Checkout, and My Account pages to the same page?**

It results in incorrect redirects and broken payment gateway functionality. WooCommerce 3.7 and up prevent this from happening.

**What is the Terms and Conditions page?**

The Terms and conditions page is a non-required but highly recommended page. Setting it in your WooCommerce page setup settings will display a link to your shop’s terms and conditions to your customers at checkout. The customer is notified that by continuing at checkout they agree to the terms.

## What is the Shop page?

The Shop page is the main page where the products of a shop will be displayed. It is also the destination of the **Continue Shopping** link shown under certain conditions when adding a product to the cart, or when viewing an empty cart. The Shop page is based on a template that either transforms the assigned page, or displays default content if not page is assigned. As such, it may render differently than other pages on your site.

The `/shop/` URL cannot be deleted. If a page assigned as Shop page has a [slug](https://wordpress.com/support/permalinks-and-slugs/) other than `shop`, then it will load at that URL. E.g. `example.com/my-fancy-store/`. In that case, `example.com/shop/` will return a 404 error (page not found). However, if Shop page is not set, `example.com/shop/` will still work, and load the default content, usually a list of products. A redirection plugin or code snippet can be used if that behavior is undesirable.

To tell WooCommerce what page to use as the Shop page:

1. Navigate to **WooCommerce > Settings > Products.**
2. Select the page you’d like to use as your shop page in the “Shop Page” dropdown.
3. Press the “Save changes” button at the bottom of the screen.

If your site is using a [block theme](https://woocommerce.com/document/woocommerce-store-editing/blocks/#block-themes), your [product catalog templates](https://woocommerce.com/document/woocommerce-store-editing/customizing-shop-page-catalog/#built-in-templates) can be customized in the site editor.

Note that you can also display products on pages other than the shop page using [WooCommerce blocks](https://woocommerce.com/document/woocommerce-store-editing/customizing-shop-page-catalog/product-collection-block/), and [product shortcodes.](https://woocommerce.com/document/woocommerce-shortcodes/products/)

If you’re using SEO plugins, they may include settings specific to custom post type archives, and these settings are what you should be using to control the shop page.

This page should be compatible with all WordPress themes, even ones not made specifically for WooCommerce, as of version 3.3x. Should you be using a custom/child theme or a version of WooCommerce prior to 3.3x, or experiencing a compatibility issue, go to: [Third-party/custom theme compatibility](https://woocommerce.com/document/third-party-custom-theme-compatibility/).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

