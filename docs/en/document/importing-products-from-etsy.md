---
title: Importing products from Etsy
url: https://woocommerce.com/document/importing-products-from-etsy/
---

If you’re looking to move your store from Etsy to WooCommerce, or just want to set up your personal store outside of Etsy. You can use the few steps below to guide you. You’ll quickly get your Etsy product listings into your WooCommerce-powered store.

**Note:**

This is a one-time import. Any further updates in your Etsy shop won’t automatically sync to WooCommerce after the import.

For this, you’ll want to get your Etsy listing data as a CSV file. Etsy themselves provide their own instructions for this, which you can follow via the button below. Once you have your listing data from Etsy, and have followed our notes, then see **Step 2**. This will point you to our documentation on importing the CSV file into WooCommerce and mapping your columns to the columns WooCommerce can use.

A few things to keep in mind:

- **Etsy does not export the prices or quantities of variants.** If you have variants, their prices will match after importing, and the quantities will be set to 0. You can follow [this guide on how to set up Product Variations](https://woocommerce.com/document/variable-product/) once you have imported all your products.
- **Digital products imported from Etsy will be listed as physical products.** That is not a big problem, though — WooCommerce is built to handle digital products as easily as it handles physical products. To list these items as digital products, [follow our guide here](https://woocommerce.com/document/managing-products/#section-6) on setting up digital products and this [more in-depth look](https://woocommerce.com/document/digital-downloadable-product-handling/) at digital file handling.
- **Manually created .csv files won’t import correctly.** To successfully import products from Etsy, you must follow the steps below using a CSV file exported from Etsy.
- **When an Etsy product has multiple images, none of the images are imported.**When an Etsy product has multiple images, these images have their own separate column headers in the CSV (e.g., IMAGE1, IMAGE2, etc.). However, WooCommerce requires a CSV to have a single column for images. Products with multiple images can have the image URLs contained within that single column, and the URLs are separated by commas. To fix the multiple product images issue, modify the CSV slightly so that all the images in the IMAGE1, IMAGE2, IMAGE3, and IMAGE4 columns are combined into one.

Just in case you haven’t created your store yet, see our guide on [installing WooCommerce](https://woocommerce.com/document/installing-uninstalling-woocommerce/). Once ready and armed with your CSV that’s been adjusted to work with WooCommerce, reference our documentation for using our Product CSV Importer that’s built into WooCommerce.

Need support with migrating your store to WooCommerce? WooExpert agencies are here to help. They are trusted agencies with a proven track record of building highly customized, scalable online stores. [Learn more.](https://woocommerce.com/customizations/)

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

