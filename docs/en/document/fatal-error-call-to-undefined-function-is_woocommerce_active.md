---
title: Fatal error: Call to undefined function is_woocommerce_active()
url: https://woocommerce.com/document/fatal-error-call-to-undefined-function-is_woocommerce_active/
---

Currently, we are aware of two possible causes for receiving the following error:

```
Fatal error: Call to undefined function is_woocommerce_active()
```

First, check the *Subscriptions* page in your [WooCommerce.com account dashboard](https://woocommerce.com/my-account/my-subscriptions/) to see whether all of your extensions are up to date (including [WooSlider](https://woocommerce.com/document/wooslider-woocommerce-product-slideshow/) if you have it installed). If you have activated your keys, then you will receive automatic update notifications.

If you have not activated your keys and are using **WooCommerce 2.0.5 or later**, see whether an extension update is available via your WP Admin dashboard at *WooCommerce > Status*.

If you are on a version of WooCommerce **earlier than 2.0.5**, you will need to check the *Downloads* page in your [WooCommerce.com account dashboard](https://woocommerce.com/my-account/downloads/) and update to the latest version of your extension manually.

To update an extension manually:

1. Unzip the downloaded file and upload its contents to your site via [File Transfer Protocol](https://developer.wordpress.org/advanced-administration/upgrade/ftp/) (FTP).
2. Overwrite the existing files — there is no need to deactivate the extension or delete any files.

**Note**: You cannot manually update WooCommerce.com Marketplace extensions via WP Admin unless you have activated your keys — you must update them via FTP.

Some third-party themes have been known to trigger this error. If all of your extensions from our Marketplace are up to date, switch to a default theme (such as [Twenty Twenty-Five](https://wordpress.org/documentation/article/twenty-twenty-five/)) and attempt to activate the extension again. Once successfully activated, you can switch back to your chosen theme.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

