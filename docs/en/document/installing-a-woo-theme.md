---
title: Installing a theme
url: https://woocommerce.com/document/installing-a-woo-theme/
---

The easiest way to install your theme is via the WordPress Dashboard:

1. **Go to** your WooCommerce.com account [Downloads](https://woocommerce.com/my-account/downloads/) page. Click the download icon to get a compressed [.zip file](http://en.wikipedia.org/wiki/Zip_(file_format)) on your computer.
2. On your website, go to **Appearance > Themes** and click the Add New button.****
3. **Click** **Upload** to upload the .zip file you downloaded in step 1.
4. **Go to** **Appearance > Themes** to **Activate**.

If your theme was purchased from WooCommerce.com, upon successful purchase, you [have the option](https://woocommerce.com/document/managing-woocommerce-com-subscriptions/#automatic-installation) to add the theme to your site automatically, along with other options like downloading the theme file for manual installation or accessing the theme documentation.

Now that you’ve installed your theme it’s time to set it up! We have [documentation for each of our themes](https://woocommerce.com/documentation/themes/) as well as a [Help Desk](https://woocommerce.com/my-account/tickets) if you need further help with your theme configuration.

So go to our [theme docs](https://woocommerce.com/documentation/themes/) and find your theme for help with the configuration.

#### The package could not be installed. The theme is missing the style.css stylesheet.

If you’re seeing this message, its likely that you tried to upload a plugin or PSD file when trying to activate a theme.

#### The package could not be installed. PCLZIP_ERR_BAD_FORMAT (-10) : Unable to find End of Central Dir Record signature

This message normally means that you’ve uploaded a corrupt zip file. Download the theme again from [WooCommerce.com](https://woocommerce.com/my-account/downloads)and upload it to your website.

#### Can I switch from one theme to another without losing my data?

Customers commonly ask us if they will lose content when they switch from one theme to another. You will not lose content. Posts, pages, comments, users and settings are all saved into a database. If you are switching from one theme that has a

If you are switching from one theme that has a [custom post type](http://codex.wordpress.org/Post_Types) built-in to a theme that does not have the same custom post type built-in, then this content will not display in your new theme. You will not ‘lose’ the content as this is still saved in the database.

For example, some of our themes have the ‘Portfolio’ custom post type built-in. If the new theme you are switching to does not have built-in support for the Portfolio custom post type it would not have the ability to display the content (that is saved in the database).

