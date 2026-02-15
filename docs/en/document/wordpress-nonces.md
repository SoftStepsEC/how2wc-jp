---
title: WordPress nonces
url: https://woocommerce.com/document/wordpress-nonces/
---

The term “nonce” stands for “**number used once**.” It is a security measure used to ensure that a specific request or submission cannot be reused maliciously.

This one-time number helps protect websites from various types of attacks, such as forgery, by making sure each transaction or session is unique and temporarily valid.

**Note:**This document is meant to serve as a helpful guide for advanced troubleshooting; however, the procedures described are beyond the scope of our [support policy](https://woocommerce.com/support-policy/) and we cannot provide direct assistance with implementing them. If you would like to seek assistance from a qualified WordPress/WooCommerce developer, we highly recommend [Codeable](https://codeable.io/?ref=z4Hnp) or a [Woo Agency Partner](https://woocommerce.com/development-services/).

Nonces help keep your WooCommerce site safe. These special security codes verify that actions on your site are performed by the intended person. They prevent anyone from pretending to be that person. This is especially important for preventing unauthorized actions (like Cross-Site Request Forgery or CSRF attacks), where an attacker might try to trick the system into doing something harmful.

By using nonces, you can protect forms and links on your site. This means your site only processes genuine submissions or clicks. This helps prevent anyone from misusing your site’s features or accessing it in harmful ways. This simple step adds a strong layer of security to help keep both your site and its users safe.

Nonces are a built-in feature of WordPress. WooCommerce uses them extensively to enhance security. As part of the WordPress core, nonce functionality provides plugins and themes with methods to generate and verify these security tokens.

This helps securely validate actions such as form submissions, data modifications, and other sensitive operations. By using nonces, WooCommerce confirms that these actions are genuine. This helps prevent unauthorized access and secures e-commerce transactions on your site.

To identify if your WooCommerce site has a nonce issue, you can look for specific symptoms and test certain actions. Here’s a straightforward way to check:

- **Form Submission Errors**: If you receive error messages when trying to submit forms, especially messages related to security or invalid requests, it might indicate a nonce problem.
- **Unexpected Behavior During User Actions**: If actions that require a security check (like log in or changing user details) behave unexpectedly.
- **Look for Consistency**: Nonce issues often show consistent patterns. For instance, if the error only occurs after a page has been open for a long time, it’s likely an expired nonce.
- **Testing with Different Browsers**: Try accessing your site with different browsers or after clearing your browser’s cache. If problems disappear when using a freshly cleared browser, nonce handling could be the issue.
- **Console Errors**: Use your browser’s developer tools to check the console for errors while performing actions that trigger nonce checks. Messages about failed requests or security warnings can point to nonce issues.
- **Plugin Interactions**: Temporarily deactivate other plugins and test again. If the problem resolves, it’s likely a [conflict](https://woocommerce.com/document/how-to-test-for-conflicts/) with how another plugin handles nonces.

Do you still have questions and need assistance?

- [Get in touch](https://woocommerce.com/my-account/create-a-ticket/) with a Happiness Engineer via our Help Desk. We provide support for extensions developed by and/or sold on WooCommerce.com, and Jetpack/WordPress.com customers.
- If you are not a customer, we recommend finding help in the [WooCommerce support forum](https://wordpress.org/support/plugin/woocommerce/) or hiring a Woo Agency Partner. These are trusted agencies with a proven track record of building highly customized, scalable online stores.[Learn more about Woo Agency Partners](https://woocommerce.com/development-services/).

