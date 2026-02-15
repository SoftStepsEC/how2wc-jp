---
title: Virtual and downloadable products
url: https://woocommerce.com/document/managing-products/virtual-downloadable/
---

On this page, you’ll learn how to add and configure both virtual and downloadable products.

When a product is virtual and/or downloadable, it means that the item:

- Is not physically shipped
- Can be downloaded digitally, or
- Both

These settings are useful for intangible products (such as services or an album) which might include both delivery and download options.

When adding a [simple product](https://woocommerce.com/document/managing-products/#simple-products), you can tick the **Virtual** checkbox in the product type panel (see the image below).

When it comes to [variable products](https://woocommerce.com/document/managing-products/#variable-products), this checkbox appears for **each variation** (see the image below).

Selecting the **Virtual** option disables all shipping-related fields (such as shipping dimensions). A virtual product will also **not** trigger the shipping calculator in the customer’s cart and checkout.

When adding a simple product, you can select the **Downloadable** checkbox from the product type panel. This adds the following fields to the **General** section of the **Product data** panel:

- **Downloadable files**: Add file(s) for customers to download.
- **Download limit**: Determine how many times a customer can download the file(s). Leave this blank for unlimited downloads.
- **Download expiry**: Specify the number of days before a download expires after purchase.

For maximum flexibility, unless also [marked as virtual](https://woocommerce.com/document/managing-products/virtual-downloadable/#adding-a-virtual-product), downloadable products have fields for shipping information and incur shipping calculations at checkout. This allows you to **offer physical products that include a download** — for example, digitally delivering the user manual for a smart device instead of including a printed one in the box.

You can check the **Virtual** box if the downloadable product is not shippable.

**Note:**Orders containing **only** products that are **both virtual and downloadable** will skip the **Processing** order status and move directly to the **Completed** order status. [Learn more about managing orders](https://woocommerce.com/document/managing-orders/#order-statuses).

To add a simple downloadable product:

1. In your store’s WP Admin dashboard, go to **WooCommerce > Products > Add Product** to add a new simple product.
2. Tick the **Downloadable** checkbox.
3. After ticking this box, additional options will appear:
  - **Downloadable files**: Add file(s) for customers to download.
  - **Download limit**: Determine how many times a customer can download the file(s). Leave this blank for unlimited downloads.
  - **Download expiry**: Specify the number of days before a download expires after purchase.
  
4. Click the **Add File** button and name your file. If hosted elsewhere, enter the file’s full URL. If you need to add a new file or choose one from your Media Library, click **Choose file**. Upload your file and click **Insert** to set up each downloadable file’s URL.
5. Enter **Download limit** *(optional).* Once a customer reaches this limit, they can no longer download the file.
6. Enter **Download expiry** *(optional)*. Download links expire after the number of days specified (leave this field blank for no expiration).
7. Click **Publish** or **Update**.

For more details about downloadable product settings, configurations, and troubleshooting, [review our digital/downloadable product guide](https://woocommerce.com/document/digital-downloadable-product-handling/).

The steps for making a variable product downloadable are very similar to those for making a simple product downloadable. For more details, [see our variable product documentation](https://woocommerce.com/document/variable-product/#downloadable-variations).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

