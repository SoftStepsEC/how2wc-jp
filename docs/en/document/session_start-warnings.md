---
title: session_start warnings
url: https://woocommerce.com/document/session_start-warnings/
---

If you get errors like this in your site header:

```
Warning: session_start() [function.session-start]: open(xxx) failed: Permission denied (13) in xxx/wp-content/plugins/woocommerce/woocommerce.php on line 80
```

your server is to blame.

PHP Sessions may not be set up correctly, or the sessions directory (usually /tmp) is not writable. You need to contact your hosting provider to resolve this.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

