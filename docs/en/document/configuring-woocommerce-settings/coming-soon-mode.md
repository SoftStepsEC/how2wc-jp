---
title: WooCommerce Coming soon mode
url: https://woocommerce.com/document/configuring-woocommerce-settings/coming-soon-mode/
---

**Coming soon mode** lets you control the visibility of your site while it is under construction. This feature is managed via the **Site visibility** tab in WooCommerce settings and provides flexibility and control over who can access your store during the setup phase.

As of [WooCommerce 9.1](https://developer.woocommerce.com/2024/07/11/woocommerce-9-1-coming-soon-product-lookup-optimizations-and-checkout-styling-galore/), *Coming soon* mode is **enabled by default** for all stores. In addition from [version 9.4](https://developer.woocommerce.com/2024/11/11/woocommerce-9-4-supercharging-the-product-collection-block-more/) onward, a **Site visibility badge** has been added under **WooCommerce > Settings > Advanced > Features**. This feature allows users to hide/show the site visibility badge on admin interface.

In the **Site visibility** settings located under *WooCommerce > Settings > Site Visibility*, two options are available to manage how your site appears to visitors.

When *Coming soon* mode is enabled, your site is in a development state and not accessible to the public. The site is hidden from visitors behind a *Coming soon* **landing page**. Only authorized users or those with a private link can view the store.

The following additional settings then become available:

1. Apply to store pages only :
  - This setting is ideal for merchants who are installing WooCommerce on an **existing site**. Enabling this option ensures that **only store-related pages** are protected by *Coming soon* mode.
  - Visitors will not be able to access store pages without permission; other parts of the site remain accessible.
  - With this option enabled, the Coming soon landing page is displayed instead of the following WooCommerce store pages:
    - Cart (Assigned via *WooCommerce > Settings > Advanced*).
    - Checkout (Assigned via *WooCommerce > Settings > Advanced*).
    - Terms and conditions (Assigned via *WooCommerce > Settings > Advanced*).
    - Shop (Assigned via *WooCommerce > Settings > Products > General*).
    - Privacy policy (Assigned via *Settings > Accounts & Privacy*).
    
  
2. Share your site with a private link :
  - This feature allows you to share access to your under-construction site with friends, family, and colleagues.
  - A private link is generated for you to provide selective access to your site, facilitating feedback and collaboration during the setup phase.
  

When **live mode** is enabled, your site is fully accessible to all visitors, indicating that it is open for business. Let the orders roll in!

Stores that are already live will **default to live mode** — they will not be affected by *Coming soon* mode unless manually changed.

Stores that install WooCommerce and complete the onboarding process will **default to Coming soon mode**. The mode’s application, whether to the entire site or just store pages, follows specific logic:

1. Apply to entire site
  - This is the default setting for new sites, determined by the `fresh_site` WordPress flag. The `fresh_site` WordPress flag option can be accessed via `https://yoursitename.com/wp-admin/options.php`
  - If the first admin user registration date is less than a month ago.
  - You can share your site privately using the **Share your site with a private link** option.
  
2. Apply to store pages only
  - For sites that do not meet the criteria for whole site protection, the **Apply to store pages only** toggle is enabled by default.
  - This ensures that only the store pages are protected, allowing other parts of the site to remain accessible.
  

The *Coming soon* page template is fully customisable in the [Site Editor](https://woocommerce.com/document/woocommerce-store-editing/the-editor/), allowing you to tailor its appearance to match your brand. You can adjust colors, fonts, and layout to create a unique coming soon page that reflects your store’s style. For more information, please visit [customising coming soon template](https://woocommerce.com/document/configuring-woocommerce-settings/coming-soon-mode/customising-coming-soon-template/).

After you’ve launched your store, your live storefront may not display immediately on your site’s front end. This is likely due to **server caching**, which temporarily stores frequently accessed data to speed up your site for visitors. Your newly-launched store will be ready to view as soon as your server’s cache gets updated. You can wait for this to happen on its own, or contact your web host for instructions on how to do this manually.

Server caching enhances the user experience with faster page loading; it also lightens the load on your server, boosting your store’s efficiency and reliability. However, from time to time, you may need to clear the server cache to ensure visitors see the latest updates to your store.

### Clear your server cache

Below, we’ve listed some common hosts with links to support articles for managing caching on their platforms. Find your host below and follow the instructions provided on their website to clear your server cache. If your host is not listed, please contact their support team for assistance.

- [Bluehost](https://www.bluehost.com/help/article/wordpress-how-to-use-our-page-caching-feature)
- [Nexcess](https://www.nexcess.net/help/how-to-use-the-nexcess-page-cache/)
- [Pressable](https://pressable.com/knowledgebase/edge-cache/#purging-flushing-edge-cache)
- [SiteGround](https://www.siteground.com/kb/clear-site-cache/)
- [WordPress.com](https://wordpress.com/support/clear-your-sites-cache/#clear-your-sites-cache)
- [Cloudflare](https://developers.cloudflare.com/cache/how-to/purge-cache/)
- [Hostinger](https://support.hostinger.com/en/articles/6215624-how-to-use-cache-manager)
- [Ionos](https://www.ionos.com/digitalguide/hosting/blogs/wordpress-cache-clear/)

### Third-party optimization tools

If you use third-party software for site optimization (such as a Content Delivery Network (CDN) or WordPress plugins), please refer to their respective documentation for guidance. For more information, review [WordPress.org’s developer caching documentation](https://developer.wordpress.org/advanced-administration/performance/cache/).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

