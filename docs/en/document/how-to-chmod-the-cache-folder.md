---
title: How To CHMOD the cache folder
url: https://woocommerce.com/document/how-to-chmod-the-cache-folder/
---

In order for the image resizer to be able to show resized images, it needs to have permission to store the resized files in a cache folder. This folder is located in your theme folder for example: `wp-content/themes/freshnews/cache/`. To allow the image resizer to write to this folder, you have to CHMOD the cache folder.

CHMOD means simply **setting write permission** so the script is able to write to the cache folder. We need to set the permissions to 775.

You need to connect via FTP and locate the theme folder mentioned above. You then use your FTP-program to set the permissions set permission to 775 (or 777 or full write permissions) on the cache folder.

Here are a few tutorials to help you out with this:

- [About.com: How to CHMOD from FTP](http://php.about.com/od/phpbasics/ht/chmod.htm)
- [Siteground: CHMOD with FTP](http://www.siteground.com/tutorials/ftp/ftp_chmod.htm)

If you already have an FTP program installed, search the help file or try to google it (ex. “cuteftp how to chmod”).

- [SmartFTP](http://www.smartftp.com/) is a free FTP program and it is very easy to [CHMOD](http://www.smartftp.com/support/kb/how-to-chmod-file-folders-f13.html).
- [FireFTP](http://fireftp.mozdev.org/) is a free addon to Firefox.

If you don’t have the required connection details to connect to your host, you need to ask your hosting provider for the host name, username and password.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

