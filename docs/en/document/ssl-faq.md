---
title: SSL FAQ
url: https://woocommerce.com/document/ssl-faq/
---

Get answers to frequently asked questions about using secure socket layer (SSL) certificates with WooCommerce and WordPress.

Use Qualys SSL Labs [SSL Server Test](https://www.ssllabs.com/ssltest/index.html) to determine whether your website is configured correctly after installing an SSL certificate. This test also reviews and grades the security of your web server configuration. Your web host needs to handle these changes.

No. Although it’s a step in the right direction, SSL alone does not make your site PCI-compliant. Learn more about [PCI-DSS compliance and WooCommerce](https://woocommerce.com/document/pci-dss-compliance-and-woocommerce/).

SSL certificates vary in features and price — from free to more than $1,000 USD per year. Unless your business has large enough revenues to warrant the extras offered by more expensive SSL certificates, you do not need them.

The three most important factors to consider are:

- Level of encryption (256-bit recommended)
- Browser recognition
- Warranty

As an example, let’s compare two SSL certificates — one costs $10 USD per year and the other $1,000 USD per year. Typically, the only difference between the two regarding the three factors mentioned above is the warranty and (possibly) browser recognition. Both SSL certificates should offer 256-bit encryption and 99%+ browser recognition.

Ultimately, you’ll pay a higher price for brand name and insurance.

Free and paid SSL certificates are available, with affordable options priced at less than $10 USD/year.

- [Let’s Encrypt](https://woocommerce.com/document/ssl-and-https/#free-option-lets-encrypt) (free, and available on some web hosts with a one-click install)
- [Namecheap](http://www.namecheap.com/ssl-certificates.aspx) (paid)

No. A dedicated IP address is not required for HTTPS connections to a web server. There are a few catches, however.

- Users running Windows XP or Internet Explorer 8 or older may see security warnings. Google has also [dropped IE8 support](http://support.google.com/a/bin/answer.py?hl=en&answer=33864).
- Web hosts running cPanel or other control panels that have not yet been updated to support this technology may require your site to have a dedicated IP address.

Typically, this issue occurs when your website loads your logo or other images from URLs containing `http://`.

To solve this, in your logo/image URLs, replace the `http://` with `https://`.

WordPress should automatically update most assets’ URLs to `https://`, but hosting configurations with a **reverse proxy** can break this functionality.

A properly configured web server and reverse proxy pass along the connection type, requiring no changes to WordPress or other PHP files. Some web hosts may require an additional patch to your `wp-config.php` file; others, such as [Network Solutions](https://woocommerce.com/document/ssl-by-proxy-problems-network-solutions/), do not have a proper fix due to their broken setup.

We do not recommend doing this. A constant SSL connection typically breaks any caching you may have configured, which causes problems when scaling a website.

A constant SSL connection may not be an issue for small or average sites. If you have questions about this, please contact your hosting provider.

It is a common misconception that a page where shoppers enter their credit card details must be SSL-secured. While this helps build customer trust, it is not necessarily required.

Instead, the **URL that credit card details are posted to** must be SSL-secured. With DPM gateways, the form is posted directly to the payment gateway’s secure servers, so your web server never sees those details. Because your server does not handle those details, it does not require extra security.

Yes. If you are doing business online, you should [invest in an SSL certificate](https://woocommerce.com/document/ssl-faq/#section-4) to increase customer trust in your site/brand. Ultimately, you must decide whether the cost will be beneficial to your business.

No. If you are using Cloudflare’s free SSL, you may not be able to access your admin area if WooCommerce is active.

No. Because it is built on WordPress (which does not support shared certificates), WooCommerce only supports **dedicated** SSL certificates.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

