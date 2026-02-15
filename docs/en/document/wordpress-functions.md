---
title: WordPress functions
url: https://woocommerce.com/document/wordpress-functions/
---

In WooCommerce and WordPress, functions are blocks of code that perform specific tasks on your website, like displaying posts or adding products to a cart. They streamline complex processes, making your website run more efficiently and consistently. By using functions, you can avoid repeating code, keeping your site’s backend clean and manageable.

Think of functions as tools in a toolbox—each one is designed for a particular job and can be reused as needed. This saves time and helps your website behave predictably when calling a function.

**Note:**This document is meant to serve as a helpful guide for advanced troubleshooting; however, the procedures described are beyond the scope of our [support policy](https://woocommerce.com/support-policy/) and we cannot provide direct assistance with implementing them. If you would like to seek assistance from a qualified WordPress/WooCommerce developer, we highly recommend [Codeable](https://codeable.io/?ref=z4Hnp) or a [Woo Agency Partner](https://woocommerce.com/development-services/).

In WooCommerce and WordPress, there are distinct categories of functions, each serving specific purposes:

- **Core functions**: These are essential for basic operations and WordPress and WooCommerce include these by default. They handle tasks like setting up the environment, managing sessions, and rendering pages.
- **Theme functions**: Specific to themes, these functions help in customizing the appearance and layout of your site. They can modify elements like headers, footers, and sidebars.
- **Plugin functions**: Developed for plugins, these functions extend the capabilities of your WordPress site beyond the core installation. They can add new features, like SEO tools or security enhancements.
- **Hook functions**: Hooks are points in the WordPress code where functions can attach to modify default behavior. Functions attached to hooks can trigger actions (Action Hooks) or filter data before it is used (Filter Hooks).
- **User-defined functions**: These are custom functions that you or developers write to perform specific tasks not covered by existing functions. They allow for customizations that are unique to your site.

Each type of function plays a crucial role in enhancing and personalizing your WordPress website, providing the flexibility to meet various needs and preferences.

An example of a well-known core function in WooCommerce is `wc_get_product()`. This function helps you find and display information about products in your store using their unique ID numbers.

For instance, if you want to show a product’s name somewhere specific on your website, this function can help you grab that name quickly.

To add custom functions to your WooCommerce site, we recommend using a separate plugin such as [Code Snippets](https://wordpress.org/plugins/code-snippets/) or [WPCode](https://wordpress.org/plugins/insert-headers-and-footers/). These plugins allow you to add functions without modifying your site or theme files. This helps ensure that theme or site updates don’t erase custom functions that you have added.

You can also manually add custom functions by editing your theme’s functions.php file. You can access this through an FTP client or the File Manager in your web hosting control panel. Alternatively, some themes allow you to edit this file from within your site’s admin area under **Appearance > Theme File Editor**.

Using a plugin is generally safer for those who are not comfortable editing theme files directly, as it reduces the risk of breaking your site due to a coding error. It also keeps your custom code separate from theme files, which is useful when updating your theme.

Do you still have questions and need assistance?

- [Get in touch](https://woocommerce.com/my-account/create-a-ticket/) with a Happiness Engineer via our Help Desk. We provide support for extensions developed by and/or sold on WooCommerce.com, and Jetpack/WordPress.com customers.
- If you are not a customer, we recommend finding help in the [WooCommerce support forum](https://wordpress.org/support/plugin/woocommerce/) or hiring a Woo Agency Partner. These are trusted agencies with a proven track record of building highly customized, scalable online stores.[Learn more about Woo Agency Partners](https://woocommerce.com/development-services/).

