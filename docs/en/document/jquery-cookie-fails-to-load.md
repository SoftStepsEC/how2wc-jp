---
title: jQuery.cookie.js/jQuery.cookie.min.js scripts fail to load
url: https://woocommerce.com/document/jquery-cookie-fails-to-load/
---

This is a problem with the server-setting, meaning that your hosting company will need to solve this on your behalf. The problem is outdated MOD_SECURITY core ruleset.

This is by far the best option as everything will then work as by design. Contact your hosting provider for assistance.

## Option 2: Rename files and update functions.php

Alternatively, you’ll need to change how WooCommerce handles the files. This change will need to be repeated whenever you update the WooCommerce plugin as the changes will be overwritten.

Rename these files:

```
wp-content/plugins/woocommerce/assets/js/jquery-cookie/jquery.cookie.js
wp-content/plugins/woocommerce/assets/js/jquery-cookie/jquery.cookie.min.js

to:

wp-content/plugins/woocommerce/assets/js/jquery-cookie/jquery_cookie.js
wp-content/plugins/woocommerce/assets/js/jquery-cookie/jquery_cookie.min.js
```

And add the following to your theme’s functions.php file:

.gist table { margin-bottom: 0; }

|  | add_action( 'wp_enqueue_scripts', 'custom_frontend_scripts' );function custom_frontend_scripts() {global $post, $woocommerce; |
|  |  |
|  | $suffix = defined( 'SCRIPT_DEBUG' ) && SCRIPT_DEBUG ? : '.min'; |
|  | wp_deregister_script( 'jquery-cookie' ); |
|  | wp_register_script( 'jquery-cookie', $woocommerce->plugin_url() . '/assets/js/jquery-cookie/jquery_cookie' . $suffix . '.js', array( 'jquery' ), '1.3.1', true ); |
|  | } |

If the first two options aren’t possible, then you can use a plugin, which renames the file being loaded:

- If you are using **WooCommerce 2.6.14 or below**: [woocommerce-jquery-cookie-fix. zip](http://cld.wthms.co/1hR5y/2rLEZX6V)
- If you are using WooCommerce 3.0.0 or above: [woocommerce-js-cookie-fix](https://github.com/rynaldos/woocommerce-js-cookie-fix)

Note: Please remove any previous fixes you may have applied.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

