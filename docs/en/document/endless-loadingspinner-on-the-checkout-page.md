---
title: Endless loading/spinner on the checkout page
url: https://woocommerce.com/document/endless-loadingspinner-on-the-checkout-page/
---

The ‘review order’ page loads the payment methods/totals via AJAX – this display a loading spinner briefly. If there are problems, this section may fail to load or the spinner may remain.

First, you should check **WooCommerce > Status** for errors – often errors will be highlighted.

Common causes and resolutions are listed below.

The URLs in **Settings > General** need to match – this is because AJAX requests don’t work across different domains:

Read more on [how to update WordPress and site URLs](https://wordpress.org/support/article/changing-the-site-url/).

## Other JavaScript errors and conflicts

Themes and plugins can create conflicts with JavaScript. To check for errors, use your browser’s error console.

Read more on [how to test for theme and plugin conflicts](https://woocommerce.com/document/how-to-test-for-conflicts/).

View the XHR tab on your browser’s developer console and look at the response. The expected response would be JSON. If the response is HTML this can be caused by a couple of different things. Oftentimes this is caused by an index.html file in the root directory of the WordPress installation.

This can be resolved by either removing the index.html file or by adjusting the indexes directive on the server configuration and prioritizing index.php over index.html. Some caching plugins will also prepend HTML to the JSON response.

You may also see a response of -1, This is a security failure and is caused by a cached [nonce](https://codex.wordpress.org/WordPress_Nonces).

You can also check for conflicts by [turning off other plugins and switching to the default WordPress theme](https://woocommerce.com/document/how-to-test-for-conflicts/) – this will often reveal the problem.

On some servers, the sending of checkout-related emails can cause trouble. You can enable the following filter to defer emails from sending until after the order is sent through, which speeds things up:

`add_filter( 'woocommerce_defer_transactional_emails', '__return_true' );`

**Note**:

This is a **Developer level** doc. If you are unfamiliar working with code and resolving potential conflicts, we recommend you work with a [Woo Agency Partner](https://woocommerce.com/development-services/) for larger projects, or find a WooCommerce developer on [Codeable](https://codeable.io/?ref=z4Hnp) for smaller customizations. We are unable to provide support for customizations under our**Support Policy**.

You need to add this code to your child theme’s `functions.php` file or via a plugin that allows custom functions to be added, such as the [Code snippets](https://wordpress.org/plugins/code-snippets/) plugin. Please don’t add custom code directly to your parent theme’s `functions.php` file as this will be wiped entirely when you update the theme.

We recommend at least 64MB. See: [Increasing the WP Memory Limit](https://woocommerce.com/document/increasing-the-wordpress-memory-limit/)

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

