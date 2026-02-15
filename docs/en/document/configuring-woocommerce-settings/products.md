---
title: Products Settings
url: https://woocommerce.com/document/configuring-woocommerce-settings/products/
---

The Products Settings on **WooCommerce > Settings > Products** control how products are displayed, measured, inventoried, and downloaded from your shop.

Below you’ll find a general overview and explanation of the settings. If you need more information about adding and managing products, see our [Adding and Managing Products documentation](https://woocommerce.com/document/managing-products/).

The products settings are split between several sections which can be accessed in the sub-menu beneath the “Products” link, these include:

- [General](https://woocommerce.com/document/configuring-woocommerce-settings/products/#general)
- [Inventory](https://woocommerce.com/document/configuring-woocommerce-settings/products/#inventory)
- [Downloadable products](https://woocommerce.com/document/configuring-woocommerce-settings/products/#downloadable-products)
- [Approved download directories](https://woocommerce.com/document/configuring-woocommerce-settings/products/#approved-download-directories)
- [Advanced](https://woocommerce.com/document/configuring-woocommerce-settings/products/#Advanced)

Below you’ll find the options for each.

In the **General** products settings section (**WooCommerce > Settings > Products > General**) are settings for your Shop Page, Measurements units, and Reviews.

These are each of the settings you’ll find in this menu:

- **Shop Page** – select what page you want to be the default shop page. It doesn’t need to be the page named “Shop” that WooCommerce installed, and can be left un-set if you use another method to display products. If no shop page is set, and a page named “Shop” exists, that page will be used as a product archive.
- Add to cart behavior – determines what happens after a customer clicks the Add to Cart button.
  - **Redirect to cart page after successful addition** – automatically takes the customer to the cart page upon adding a product.
  - **Enable Ajax add to cart buttons on archives** – using *AJAX adds the item to the cart without reloading the page.*
  
- **Placeholder Image** – enter the attachment ID or URL of an image to set as the default placeholder image to appear on the front end when no other image is available. This could be your brand logo or an image of a signature product or service. WooCommerce comes installed with a default placeholder image added to your site’s media library.

- **Weight unit**– Select a unit of measurement for products from the drop-down for **weight.**
- **Dimensions unit –**Select a unit of measurement for products from the drop-down for **dimensions.**

- **Enable Product Reviews** – Tick this box to activate [product reviews](https://woocommerce.com/document/product-reviews/).

- **Show “verified owner” label on customer reviews** – Tick this box to display when a customer review is from a customer who has purchased the product.
- **Reviews can only be left by “verified owners”** – Tick this box if you want to restrict everyone except for product buyers from leaving reviews.

- **Enable star rating on reviews:**Tick this box to enable star ratings on reviews.
- **Star ratings should be required, not optional:**Tick this box to make star ratings required to leave a review.

[Read more about how to manage and moderate Product Reviews](https://woocommerce.com/document/product-reviews/).

Clicking on the “Inventory” link (**WooCommerce > Settings > Products > Inventory)** in the submenu at the top of the screen takes you to the store’s inventory settings. These are each of the settings you’ll find in this menu:

**Manage stock** – Choose whether to enable stock management. If enabled, you have the following options:

- **Enable** stock management – Tick this box to enable managed inventory counts for physical products. You enter quantities, and WooCommerce subtracts items as sales are made or orders are returned.
- **Disabled** (box left unticked) – With stock management disabled, stock status for physical products can only be set to “in stock” “Out of Stock” or “On backorder”. Inventory counts will not be kept by the system. More info at:[Managing Products](https://woocommerce.com/document/managing-products/).

**Hold Stock (minutes)** – Hold products (for unpaid orders) for X minutes. When your entered limit is reached, the pending order will be canceled and held stock released back to available inventory. Leave blank to disable. Please note that this only applies to orders in the “Pending payment” status, and not orders that are “On hold”.

**Enable low stock notifications –**tick this box to enable low stock notifications (emails) to be alerted when stock of a product falls to the low-stock threshold.

**Enable out of stock notifications –**tick this box to enable out of stock notifications (emails) to be alerted when a product is out of stock.

**Notification Recipient** – Enter**the email address to receive stock notifications.

**Low Stock Threshold** – Enter the inventory count that will trigger a low stock notification. When product stock reaches this amount you will be notified via email if enabled.

**Out Of Stock Threshold** – Enter the inventory count that will trigger the out of stock status, and an out of stock notification, if enabled.

The two options below are available even if stock management is disabled:

- **Out Of Stock Visibility** – Tick this box to hide out of stock items from the store catalog/customer view.
- Stock Display Format – Select one of the following options for how the number of products in stock is displayed or choose to not display it:
  - Always show stock – “12 in stock”
  - Only show stock when low – “Only 2 left in stock” vs. “In stock”
  - Never show amount
  

**Note:** by default, “In Stock” and your selected stock display format will only be displayed on the product page if a product’s **Track stock quantity** option is **enabled** under the **Inventory tab** of the Edit Product page. The snippet below can be used to force the display of “In Stock” for products that are in stock, even if the quantity is not tracked. The snippet is provided as is. We are unable to provide support for customizations under our [Support Policy](https://woocommerce.com/support-policy/). If you need to customize a snippet, or extend its functionality, seek assistance from a qualified WordPress/WooCommerce Developer. We highly recommend [Codeable](https://codeable.io/?ref=z4Hnp), or a [Certified WooExpert](https://woocommerce.com/experts/).

|  | <?php |
|  |  |
|  | add_filter( 'woocommerce_get_availability', 'custom_override_woocommerce_show_in_stock', 10, 2 ); |
|  |  |
|  | function custom_override_woocommerce_show_in_stock( $availability, $product ) { |
|  |  |
|  | if ( ! $product->managing_stock() && $product->is_in_stock() ) { |
|  | $availability['availability'] = __( 'In Stock', 'woocommerce' ); |
|  | } |
|  |  |
|  | return $availability; |
|  | } |

In the “Downloadable Products” settings (**WooCommerce > Settings > Products > Downloadable products**) you’ll find the settings for how your store handles downloadable products.

Below are brief descriptions of the settings on this page, if you want a more in depth overview of downloadable product handling, please see the [Digital/Downloadable Product Guide](https://woocommerce.com/document/digital-downloadable-product-handling/).

**File Download Method –**Controls how your store provides downloadable files to purchasers. Available options are:

- **Force Downloads** – Files are ‘forced’ to download via a PHP script. Files are not accessible to anyone but purchasers, and direct links are hidden.
- **X-Accel-Redirect/X-Sendfile** – Similar to ‘forced’ above, but it has better performance and can support larger files. It requires that your hosting provider supports either X-Sendfile or X-Accel-Redirect, so you need to check with them first.
- **Redirect only** – A download URL links the user to the file. Files are not protected from outside access.

**Most stores should use one of the first two methods**to keep files safe from outside access. Redirect should only be used if you encounter problems or don’t mind downloads being unsecured.

**Access Restriction** options include:

- **Downloads require login** – Tick this box to require customers to login in to download their purchases. *Does not apply to guest purchases.*
- **Grant access to downloadable products after payment** – Tick this box to grant access to downloads when orders are*Processing*, rather than *Completed*.

**Filename** – **Append a unique string to filename for security** – Tick this box to add additional randomness (security) to the filename to prevent link sharing.

Since WooCommerce 6.5 it is possible to set Approved Download Directories for storing and serving downloadable files. Use the settings at **WooCommerce > Settings > Products > Approved download directories** to help manage the storage of downloadable product files.[Find a detailed overview of this feature here](https://woocommerce.com/document/approved-download-directories/).

These settings are related to how your store utilizes the product attributes lookup table feature. For most users, the default settings are fine and will not need to be changed. [Developers: Learn the technical details about this feature on our developer blog](https://developer.woocommerce.com/2024/06/20/an-optimization-for-the-product-attributes-lookup-table-is-coming/).

You’ll find the settings at: **WooCommerce > Settings > Products > Advanced.**

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

