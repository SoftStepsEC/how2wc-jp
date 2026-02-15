---
title: Fixing blurry product images
url: https://woocommerce.com/document/using-the-appropriate-product-image-dimensions/
---

The majority of blurry product image issues are caused by theme styling, where the design of the theme specifies image dimensions that may not play nicely with WooCommerce.

**Note:** Anytime a new theme is activated *or* image dimension settings are changed, previously-created thumbnails will need to be regenerated. To do so via your WP Admin dashboard, navigate to *WooCommerce > Status > Tools > Regenerate store thumbnails*.

As of version 3.3, [theme compatibility](https://woocommerce.wordpress.com/2017/12/09/wc-3-3-will-look-great-on-all-the-themes/) and [improvements to image rendering and cropping](https://woocommerce.wordpress.com/2017/12/11/wc-3-3-image-size-improvements/) are supported in WooCommerce.

This means that:

- Blurry images caused by theme incompatibility or overriding code should no longer occur.
- Store owners can control the width and height of their main images.
- Thumbnail resizing can be done automatically or manually.
- Images shown to customers always look great by default, so your products keep selling themselves!

To learn how to use these new features, see [Adding and managing products](https://woocommerce.com/document/managing-products/) and [Adding product images and galleries](https://woocommerce.com/document/adding-product-images-and-galleries/).

If your blurry image issue persists, it could be because:

- Your image size settings are too small.
- Original images need to be of a higher resolution.

To solve this:

- Your image dimensions should match or be higher than those of your theme.
- Original images you upload should be at least 800×800 pixels or higher to work for most themes.

- **Single product image:** The largest image on the individual product details page. It is sometimes referred to as the main/featured image.
- **Catalog image:** A medium-sized image used in product loops — such as on the shop page, product category pages, related products, and in upsells and cross-sells.
- **Product thumbnail images:** The smallest image required, commonly used in the cart, for widgets, and in gallery images (optional) beneath the single product image.

As of **WooCommerce version 3.3**, product image settings can be found under the **Customizer** in *WooCommerce > Product Images*. The image below is what this looks like by default in a theme like Storefront; other themes may change or add additional options.

The images you upload are **resized to match the values you input**. For example, if your settings are 100×100 pixels and you upload a 300×600 pixel image, it is resized to 100×200 pixels.

You can also choose to hard-crop your images. This forces them to the size specified in the settings (regardless of the raw image you upload), so they are cropped, rather than distorted in scale.

**Note:** If you change settings *after* uploading product imagery, you may need to regenerate thumbnails within WordPress for the changes to apply. Head to *WooCommerce > Status > Tools > Regenerate shop thumbnails*, and click the **Regenerate** button.

The theme you choose determines the maximum size an image will be. You will need to know the dimensions it renders them in to appropriately set those in WooCommerce.

Determines where your theme renders catalog thumbnails the largest. In some cases, this is the shop page.

With the developer tools enabled in your browser of choice, right-click the image and select **Inspect** or **Inspect Element**. This will tell you the image dimensions. Make a note of this as you will need to use them later.

In the example above, the largest catalog images are rendered at 324×324 pixels.

Repeat the process for the single product image — usually the largest image on a product page.

In Storefront, the largest single product image is 800×800 pixels. Although not visibly rendered at that size, this sizing is required for the zoom effect.

The smallest product image required is likely the thumbnail in the product gallery. Repeat the inspection process mentioned above to get the dimensions.

In Storefront, it renders at 46×46 pixels.

Now that we know all thumbnail image sizes for our specific theme, we can add images exceeding the largest dimensions to WooCommerce to ensure that future image sizes will be this size or larger.

Any new product images that are uploaded will now have thumbnails with these settings; they should appear without distortion or blurriness.

**Note:** Saving changes **does not** automatically update all previously uploaded product imagery. To update old images, WordPress needs to regenerate the thumbnails. In your WP Admin dashboard, head to *WooCommerce > Status > Tools > Regenerate shop thumbnails*, and click the **Regenerate** button.

High Dots Per Inch (HiDPI) displays — commonly known as [retina displays](https://en.wikipedia.org/wiki/Retina_display) — contain twice as many pixels (or more) than older displays. For pixel-perfect imagery on retina displays, set your thumbnails to **double the size** rendered by the theme. For example, if a theme renders images at 80×80 pixels, you want them to be 160×160 pixels.

**Note:** This approach can impact performance, as larger images take longer to load. This is a personal preference; we recommend consulting your analytics before making a decision. Your stats should tell you which devices and screen sizes the majority of your customers use.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

