---
title: Permalinks
url: https://woocommerce.com/document/permalinks/
---

*Permalink* is short for permanent link. Permalinks are the URL structures used to help organize the content of your website which can be pages, posts, or, in the case of WooCommerce, products. A good URL structure can be efficiently navigated, shared, and referenced by potential customers and search engine crawlers.

On this page you’ll learn:

- How WooCommerce permalinks taxonomy or the structure works.
- How to configure permarlinks for WooCommerce products.

## Taxonomy Permalinks

The permalink settings for WooCommerce are co-located with the usual WordPress settings and can be found at **WordPress > Settings > Permalinks**.

It’s beneficial for permalink structures to be as short as possible and to contain keywords relating to the content they help categorize.

There are 3 settings in **Optional** section that control the base of your WooCommerce product categories, terms, and attributes.

- **Product category base** – the default [product category](https://woocommerce.com/document/managing-product-taxonomies/#section-1) base is **product-category**, e.g. `example.com/product-category/accessories`.
- **Product tag base** – the default [product tag](https://woocommerce.com/document/managing-product-taxonomies/#section-3) base is **product-tag**, e.g. `example.com/product-tag/casual`.
- **Product attribute base** – the default [product attribute](https://woocommerce.com/document/managing-product-taxonomies/#section-6) base is empty and would lead to a URL e.g. `example.com/size/medium`. Adding a custom base, e.g. **attribute**, would change the URL to `yourdomain.com/attribute/size/medium`.

Attributes are only accessible via the **Product attribute base**URL above if **Enable archives** is enabled for it under the settings found at **Products > Attributes > Name of the attribute** as illustrated below.

There are four settings under **WordPress > Settings > Permalinks > Product Permalinks** to select from as your permalink base for products:

- **Default** – *Default* is the only option available when using plain permalinks and relies on ID-based URLs, e.g. `example.com/?product=111`. If you use any of the non-plain permalinks, the product base is `example.com/product/hoodie-with-logo`.
- **Shop base** – the *shop base* uses the shop page name. E.g. `example.com/shop/hoodie-with-logo`.
- **Shop base with category** – the *shop base with category* will use the shop page name first, then add the product category name. An example would be `yourdomain.com/shop/hoodies/hoodie-with-logo`.
- **Custom base** – the *custom base* sets your custom text before the product name, e.g. `example.com/superstore/hoodie-with-logo`.

**Note:** ensure your **Custom base** setting does NOT conflict with the [Taxonomy permalink](https://woocommerce.com/document/permalinks/#section-2) settings. For example, if you set the **product base** to `shop` you should NOT set the **product category base** to `shop` too, as this will not be unique and cause a conflict. WordPress requires these to be unique so it can distinguish *categories* from *products*.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

