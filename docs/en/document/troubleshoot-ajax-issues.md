---
title: Troubleshoot AJAX issues
url: https://woocommerce.com/document/troubleshoot-ajax-issues/
---

Asynchronous JavaScript and XML (AJAX) is a web development technique used to create interactive web applications. With AJAX, web applications can send and retrieve data from a server in the background without disrupting the display and behavior of the current page. This means parts of a web page can be updated without needing to reload the entire page.

For example, when you use a search box on an ecommerce site and it suggests products as you type, AJAX is likely operating in the background. This functionality improves the shopping experience by making your website feel faster and more responsive to users.

**Note:**This document is meant to serve as a helpful guide for advanced troubleshooting; however, the procedures described are beyond the scope of our [support policy](https://woocommerce.com/support-policy/) and we cannot provide direct assistance with implementing them. If you would like to seek assistance from a qualified WordPress/WooCommerce developer, we highly recommend [Codeable](https://codeable.io/?ref=z4Hnp) or a [Woo Agency Partner](https://woocommerce.com/development-services/).

Examples in a WooCommerce store:

1. **Product search**: When customers type in the search bar, AJAX helps display product suggestions instantly without reloading the page.
2. **Adding items to cart**: When a customer adds an item to their shopping cart, the cart updates immediately without refreshing the page.

To view and understand AJAX requests in a browser, you can use your browser’s Developer Tools. Here’s a simple way to do it:

1. Right-click the web page and click **Inspect** or press `Ctrl+Shift+I` on Windows (`Cmd+Option+I` on Mac).
2. Click the **Network** tab in Developer Tools. This shows the network activity that happens when the web page loads and while you interact with it.
3. Perform the action that triggers the AJAX request (such as adding an item to your cart).
4. Look for new entries in the **Network** tab. Click one to see the request headers, the response from the server, and the data sent or received.

By examining these details, you can better understand which data the server is sending and receiving. This will help troubleshoot issues or get a clearer picture of how your site communicates in real-time.

AJAX requests can sometimes lead to errors that prevent the expected interaction on your website. Below are some common AJAX errors, what they typically look like, what they mean, and general tips for resolving them.

- **What it looks like**: The server cannot find the requested resource.
- **What it means**: The URL for the AJAX request is incorrect.
- **How to fix it**: Check the URL in your AJAX call to make sure it matches an existing endpoint or path on your server.

- **What it looks like**: The server encountered an unexpected condition.
- **What it means**: There’s a problem on the server side, such as a bug in the script handling the request.
- **How to fix it**: Review the server-side code for errors or check server logs to find what’s breaking the script.

- **What it looks like**: The server refuses to respond to the request.
- **What it means**: The server permissions are preventing the AJAX request.
- **How to fix it**: Ensure the AJAX request has the necessary permissions and is authenticated if needed.

- **What it looks like**: There is no response, and the request times out.
- **What it means**: The AJAX request took too long to receive a response from the server.
- **How to fix it**: Optimize the server-side process to respond quicker or extend the timeout period in the AJAX request.

- **What it looks like**: The response text cannot be parsed.
- **What it means**: The format of the server response is incorrect — usually not properly formatted JSON or XML.
- **How to fix it**: Ensure the server response is in the correct format and content type that the AJAX request expects.

When encountering an AJAX error, using your browser’s Developer Tools to inspect the *Network* tab can provide insights into the request headers, status codes, and server responses which can help identify and resolve the problem more efficiently.

Do you still have questions and need assistance?

- [Get in touch](https://woocommerce.com/my-account/create-a-ticket/) with a Happiness Engineer via our Help Desk. We provide support for extensions developed by and/or sold on WooCommerce.com, and Jetpack/WordPress.com customers.
- If you are not a customer, we recommend finding help in the [WooCommerce support forum](https://wordpress.org/support/plugin/woocommerce/) or hiring a Woo Agency Partner. These are trusted agencies with a proven track record of building highly customized, scalable online stores.[Learn more about Woo Agency Partners](https://woocommerce.com/development-services/).

