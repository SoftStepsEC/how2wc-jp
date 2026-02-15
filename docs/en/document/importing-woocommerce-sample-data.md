---
title: Importing WooCommerce Sample Data
url: https://woocommerce.com/document/importing-woocommerce-sample-data/
---

Right after installing WooCommerce, your store may look empty — no products, orders, reviews. This is intentional so you can get started creating your own products and setting up WooCommerce exactly as you need.

But maybe you’d like to see what a store full of sample products looks like. If so, we’ve got some data for you! This document covers how to import the sample WooCommerce product data included in the plugin files.

Sample data for WooCommerce is located in a file called either `sample_products.csv` or `sample_products.xml`, which are located in the WooCommerce plugin folder in `woocommerce/sample-data/`. You can get it in two ways:

- Re-download [WooCommerce.](http://wordpress.org/extend/plugins/woocommerce/) Open the .zip and find the files in the folder.
- Get the file from your site via SFTP, etc.

**This is the recommended approach.**

From the WordPress Dashboard:

1. Go to: **Products > All Products**.
2. Click the **Start Import** button.
3. An **Import Products** screen appears.

1. Select **Choose file** and then select the **sample-products.csv**file you downloaded.
2. **Continue**. A Column Mapping screen appears. WooCommerce maps columns from the sample CSV automatically.

1. Scroll down and click the button to “**Run the Importer**”.

You now have sample product data in WooCommerce!

From the WordPress Dashboard:

1. Go to: **Tools > Import**.
2. Select **WordPress**. (Click to install the importer if it’s not on your site already)

1. **Run Importer**.
2. Select **Choose file** and then select the **sample-products.xml**file you downloaded.
3. Click the button to “**Upload file and import**”.
4. Assign an author for the products: This is your call to make, though we recommend assigning the posts to an existing user.
  - Import our default Shop Manager author,
  - Create a new user,
  - Or, assign the posts to an existing user.
  
5. Check or uncheck the box for **Download and import file attachments**. This imports all sample product images to your site if ticked.

1. **Submit** and your sample data is imported!

See our documentation on [Adding and Managing Products](https://woocommerce.com/document/managing-products/) for more information if you’d like to explore more.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

