---
title: Digital/Downloadable Product Guide
url: https://woocommerce.com/document/digital-downloadable-product-handling/
---

While the default downloadable product settings work for most Woo merchants, some merchants may find that they need a different configuration. This page guides you through the different downloadable product configurations to help you find one that fits your needs.

On this page you’ll learn:

- How to choose and set the File Download Method.
- How to protect your uploads from unauthorized access.
- How to choose where to store your downloadable products.
- How customers receive and access downloadable products.

1. Navigate to **WooCommerce > Settings > Products > Downloadable Products.**
2. Select a File Download Method from the dropdown:
  - **Force Downloads**– File downloads are forced, [using PHP](https://woo.com/document/digital-downloadable-product-handling/#force-downloads-require-allow_url_fopen-to-be-on). To ensure files are protected from direct linking, Force Downloads can be used. However, if your files are large, or the server is underpowered, you may experience timeouts during download. In this case, you need to upgrade your server or use one of the redirect methods instead. **Note:** Force Downloads require PHP functionality. The allow_url_fopen function in PHP must be set to On. To check the status of allow_url_fopen on your site you can: create a phpinfo() [page as described here](https://woocommerce.com/document/finding-php-error-logs/#php-error-logs-on-the-server), install one of the [phpinfo plugins from WordPress.org](https://wordpress.org/plugins/search/phpinfo/), or contact your host’s support.
  - **X-Accel-Redirect/X-Sendfile**– Downloads are handled by the server (nginx/apache). This method requires the X-Accel-Redirect/X-Sendfile module to be installed and enabled on the server. Confirm with your web host that one of these modules is installed before using this method.**It’s the most reliable method** because the file is served directly to the customer. This option offers the best performance and security (files are protected by an .htaccess file.) .
  - **Redirect only (insecure)** – Customers access downloads by being redirected directly to the file through the link provided. Using this method means whoever has the upload link will be able to access the file, even when they are not logged in. The risk is customers who purchase the product can share the link with others that have not.
  

**Note**: If you selected either Force Downloads or X-Accel-Redirect/X-Sendfile then you have the option to enable the “Allow using redirect mode (insecure) as a last resort” setting. Enabling this setting allows the “redirect method” to be used if a file cannot be delivered/served to your customer using your selected method (Forced Downloads or X-Accel-Redirect). This comes with the same risks as the “redirect only” method described above, but is helpful in cases where you host assets across different platforms that may not work with your preferred method.

1. Select “access restriction” options:
  - Tick the “**Downloads Require Login”** checkbox if you want users to be logged in to download files. Guest checkout would need to be disabled.
  - Tick the **“Grant access to downloadable products”**after payment checkbox if you wish to grant access to files when orders are Processing, instead of Completed. This can be most helpful if you sell downloadable products and physical products together, customers don’t have to wait for the physical product to arrive to access their downloadable content.
  
2. Determine if you want to keep “**Append a unique string to filename for security**” enabled. This setting is enabled by default (and is recommended) to enhance the security of your files. It is not required if your upload directory is properly configured and secured through other means. Activating or deactivating this setting does not impact any links or files that were previously uploaded; it will only impact files uploaded**after** the change.
3. Click **Save changes**.

**Note:** Additional settings can be found in the **WooCommerce > Settings > Products > Approved Download Directories**(next to “Downloadable Products in the menu at the top of the page). These settings are particularly useful for sites where there are one or more shop managers or users with the ability to edit products. [Click here](https://woocommerce.com/document/approved-download-directories/) to learn more.

By default WooCommerce introduces a `.htaccess` file to protect your `wp-content/uploads/woocommerce_uploads` directory, however, this doesn’t guarantee the protection of this directory, since everything depends on the configuration of the server.

If you are using an NGINX server for your site along with **X-Accel-Redirect/X-Sendfile** or **Force Downloads** download method, it is necessary that you modify the configuration for better security. Head over to the [WooCommerce Developer Documentation](https://developer.woocommerce.com/docs/code-snippets/using_nginx_server_to_protect_your_uploads_directory/) for further details.

As described in Settings and Configuration, WooCommerce appends a unique string to the filename of uploaded files to enhance security and this setting is enabled by default on every install of WooCommerce.

Storing files for downloadable products comes down to preference and the level of security needed for your digital products. Since WooCommerce only needs a valid External URL to work, there are a few different options for storing your uploads.

This section will answer a few questions about storage and and how to manage and protect your uploads directory:

#### Can I use cloud storage to store my files and downloads?

The short answer is: Yes!

WooCommerce only needs an external URL that points to your digital download file to work. They shouldn’t need further validation. However, some cloud storage providers, like Google Drive, only function when you select “Redirect Only (insecure)” as the File Download Method. The [Setup and Configuration](https://woo.com/document/digital-downloadable-product-handling/#setup-and-configuration) section explains the difference between the methods.

#### I have attached a file from the media library to a product. How can I secure the file and make it unreachable?

When you upload a file from the media library instead of using WooCommerce for the upload, anyone with a link can access the file because WordPress’s media library is inherently public, as it stores all images attached to posts and pages. Upload files from WooCommerce instead of selecting them from the media library to prevent your downloadable products from being accessed in this way. You can achieve this by uploading files via the “Edit Product” page. WooCommerce will then upload those files to the `woocommerce_uploads` folder, which remains unreachable to the public.

#### What file extensions can I use?

WooCommerce allows for the same file extensions defined by WordPress. You can see the full list via [WordPress Codex: Uploading Files](https://codex.wordpress.org/Uploading_Files).

#### What is the maximum file size that can be used?

WooCommerce itself has no limitation on the maximum file size. However, your website’s server likely has a maximum limit. Reach out to your hosting company if you need the limit increased.

When a customer orders a downloadable product they receive an email with the download link for the product they purchased. If they have an account on your site, the download link is also available to them by navigating to `My Account > Downloads`. Here are a few things to note about how your downloadable product configuration can impact when your customers have access to downloads:

- If you enable “Grant access to downloadable products after payment”, customers can download the product via the link on the order received page, download it from the order email, or access it from the “My Account > Downloads” page if they have an account with your store.
- If you do not enable “Grant access to downloadable products after payment”, customers gain access to downloads only when the order is marked as Complete. For products marked as both “virtual” and “downloadable,” this process is automatic. If the product is only marked as “downloadable,” you need to manually mark the order as complete for customers to access the downloads.

**Note about PayPal Standard (deprecated):**

If you are using PayPal standard (deprecated), there is a delay when using the IPN to track payments, which may lead to a file link not appearing on the “Order Received” page. To avoid this you can follow the instructions below or switch to [PayPal Payments](https://woocommerce.com/products/woocommerce-paypal-payments/) , our recommended PayPal plugin. Follow these instructions if you choose to continue using PayPal Standard:

1. Enable [Payment Data Transfer](https://developer.paypal.com/api/nvp-soap/payment-data-transfer/) (PDT) by going to gateway settings and selecting it as the PayPal Identity Token.
2. Enable PDT in your PayPal account under **Profile > Profile and Settings > My Selling Tools > Website Preferences.**
3. Enable auto-return, and enter the return URL as https://shipyouridea.com/checkout/order-received/ (replacing shipyouridea.com with your site’s address), then enable PDT.
4. Copy your identity token to your settings under WooCommerce > Settings > Checkout > Paypal. This will allow payments to be verified without the need for PayPal IPN.

Upon processing and payment of the order, the customer receives an invoice/order confirmation containing a clickable link to download.

If your Completed Order emails do not include links for the download files, then there may be an issue with your site’s database, which we have a guide for fixing here: [https://woocommerce.com/document/completed-order-email-doesnt-contain-download-links/](https://woocommerce.com/document/completed-order-email-doesnt-contain-download-links/)

You can edit a customer’s access to a purchased downloadable item by following the instructions below:

1. Go to: **WooCommerce > Orders** and select the order to view or edit.
2. Scroll down to the **Downloadable Product Permissions** meta box, which displays the download and how many times the customer had accessed it.
3. Revoke access, grant access to new downloads, or exit order.

**What happens if I edit a downloadable product’s files after customers have purchased it?**

- *Editing*an existing download file row (changing the name, file URL or both) updates the download links on past purchases, but it leaves the expiry date and downloads remaining intact.
- *Adding* a new download does not affect past orders. Only new purchasers gain permission to download it.

If you have products that grant ‘lifetime access’ or similar to all downloads added to a product, a subscription or membership may be more appropriate. You can also combine files into a single archive (zip). If you want to restore previous functionality, [there is a plugin available here.](https://github.com/woocommerce/grant-download-permissions-for-past-woocommerce-orders)

Reports track and log unique IDs for downloads of digital/downloadable products. For more information click here: [WooCommerce Reports](https://woocommerce.com/document/woocommerce-analytics/#downloads-report).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

