---
title: Troubleshooting a slow site
url: https://woocommerce.com/document/troubleshooting-a-slow-site/
---

The first step for troubleshooting a slow WooCommerce site is to determine the root cause.

Using a caching plugin such as [WP Super Cache](http://wordpress.org/plugins/wp-super-cache/) is a good way to optimize site performance[.](http://wordpress.org/plugins/wp-super-cache/) You can also use a Content Delivery Network (CDN) such as [Jetpack’s site accelerator](https://jetpack.com/features/design/content-delivery-network/) or [Cloudflare](https://www.cloudflare.com/) to speed your site up further.

Be careful, though — caching plugins have the potential to cause your site to load incorrectly (or not at all) if incorrectly configured. Make sure to double-check and confirm settings after implementation.

Contact your hosting provider to discuss the impact your hosting plan has on site performance. We recommend high-quality, dedicated hosting over cheap hosting plans on shared servers. [See our recommended WooCommerce hosting solutions](https://woocommerce.com/hosting-solutions/).

A common cause of slow site performance on the front end is image size. The file size of your product/blog images directly impacts the speed at which your site loads.

[Jetpack Boost](https://jetpack.com/boost/) or a third-party tool like [Smush](http://wordpress.org/plugins/wp-smushit/) can help optimize images within WordPress.

[View our guide for fixing blurry images in WooCommerce](https://woocommerce.com/document/using-the-appropriate-product-image-dimensions/).

Minification improves your site’s loading speed by reducing the size of its code files. It removes unnecessary characters like spaces, line breaks, and comments from HTML, CSS, and JavaScript files — without affecting their functionality. This reduced file size results in faster download and execution times, enhancing overall website performance and user experience.

To minify files on your site, you can choose from a variety of [third-party plugins](https://wordpress.org/plugins/search/minify/).

It may also be necessary for you to [increase your site’s WordPress memory limit](https://woocommerce.com/document/increasing-the-wordpress-memory-limit/).

A sluggish site can sometimes be related to extension/plugin load.

To test this, deactivate all extensions and plugins, reactivating them one by one until you find a potential cause. You could also use the third-party [Plugin Organizer](https://wordpress.org/plugins/plugin-organizer/) to control the order of activation, toggling plugins on or off on a per-page/post basis.

To test your theme, temporarily switch to a default WordPress theme (such as [Twenty Twenty-Five](https://wordpress.org/themes/twentytwentyfive/)) and navigate through the site. If you notice a performance improvement, the problem is likely related to your theme.

- [Pingdom Website Speed Test](http://tools.pingdom.com/fpt/)
- [Google PageSpeed tools](https://developers.google.com/speed/pagespeed/)

- Offload all unnecessary functions to another server or third-party service, such as [sending email via a dedicated Simple Mail Transfer Protocol (SMTP) provider](https://woocommerce.com/document/email-smtp-providers/).

- [Ten ways to improve the speed of your WooCommerce store](https://woocommerce.com/posts/ten-ways-to-speed-up-your-woocommerce-store/)
- [WooCommerce performance best practices](https://developer.woocommerce.com/docs/best-practices/performance/performance-best-practices/)
- [WordPress.org performance optimization tips](https://developer.wordpress.org/advanced-administration/performance/optimization/)

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

