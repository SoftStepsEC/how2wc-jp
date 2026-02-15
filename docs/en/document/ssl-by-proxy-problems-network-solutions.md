---
title: SSL by proxy problems (Network Solutions)
url: https://woocommerce.com/document/ssl-by-proxy-problems-network-solutions/
---

Hosts that insist on SSL by proxy, such as Network Solutions), will cause problems with WordPress and WooCommerce because they prevent PHP and the WordPress [is_ssl()](http://codex.wordpress.org/Function_Reference/is_ssl) function from detecting if the page is being served over **HTTPS**. This causes a **redirect loop**.

In [Network Solutions’ own words](http://www.networksolutions.com/support/ssl-redirects/):

> Network Solutions® uses a proxy SSL; this does not allow the use of server-side variables to detect HTTPS (secure). All server-side coding will always detect HTTP (non-secure), and for programs that attempt to redirect non-secure connections (http://) to a secure connection (https://) will result in an infinite loop and server error after 30 seconds.

Network Solutions have been aware of this limitation since 2007, so don’t expect a change in policy anytime soon.

There is no workaround within PHP (http://stackoverflow.com/questions/4686668/https-redirect-for-network-solutions). The only workaround is:

1. **Turn off the Force SSL settings within WooCommerce**
2. **Use Javascript to redirect to SSL**

```
<script language="javascript">
if (document.location.protocol != "https:")
{
document.location.href = "https://subdomain.yourdomain.com" + document.location.pathname;
};
</script>
```

Please note that we cannot officially support this non-standard setup.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

