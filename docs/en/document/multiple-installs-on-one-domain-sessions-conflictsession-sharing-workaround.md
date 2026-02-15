---
title: Multiple installs on one domain + SESSIONS (conflict/session sharing workaround)
url: https://woocommerce.com/document/multiple-installs-on-one-domain-sessions-conflictsession-sharing-workaround/
---

If you are running multiple installs of WordPress on the same domain, and SESSIONS are being shared between your installs you can add the following to your wp-config.php file to prevent this from occurring:

```
if ( ! session_id() ) {
	session_name( 'PHPSESSID_1' );
}
```

You can change the name to something unique for each install.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

