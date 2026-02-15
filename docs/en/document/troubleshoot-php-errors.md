---
title: Troubleshoot PHP errors
url: https://woocommerce.com/document/troubleshoot-php-errors/
---

PHP is a popular scripting language that powers many websites, including those created with WordPress. It runs on your web hosting server and allows your website to perform complex functions — such as processing form submissions, managing user sessions, and interacting with databases.

**Note:**This document is meant to serve as a helpful guide for advanced troubleshooting; however, the procedures described are beyond the scope of our [support policy](https://woocommerce.com/support-policy/) and we cannot provide direct assistance with implementing them. If you would like to seek assistance from a qualified WordPress/WooCommerce developer, we highly recommend [Codeable](https://codeable.io/?ref=z4Hnp) or a [Woo Agency Partner](https://woocommerce.com/development-services/).

To find PHP errors on your WordPress site, including those affecting WooCommerce, you can check the error logs, enable WordPress debugging, or consult WooCommerce’s built-in status logs. Here’s how to access each method:

- **Check error logs**: Your web hosting account typically includes error logs that capture any PHP issues. Access these logs through your hosting control panel under sections like “logs” or “error logs.”
- **Enable debugging**: Activate [WordPress’s built-in debugging feature](https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/) to display errors directly on your site. This not only turns on debugging but also displays errors on your site, logging them to a `debug.log` file within the `/wp-content/` directory. Remember to **disable this feature on live sites** to protect sensitive information.
- **WooCommerce status logs**: WooCommerce also maintains its own logs, which can be invaluable for troubleshooting specific issues with your online store. You can view these logs by navigating to *WooCommerce > Status > Logs* in your WP Admin dashboard.

Using these tools, you can effectively track down and resolve PHP errors to ensure your site and online store operate efficiently.

In PHP, there are several categories of error types. Understanding these can help you troubleshoot issues more effectively.

Here are the main types of PHP errors you may encounter:

- **Parse errors**: These occur when there is a syntax mistake in the code. The error will stop the script from running. Common causes include missing semicolons, braces, or other syntax rules.
- **Fatal errors**: These errors are critical and will halt the execution of the script. They occur when PHP understands what you’ve asked but can’t perform the task, such as calling a non-existent function or class.
- **Warning errors**: These do not stop the execution of the script; they simply alert you that something is wrong. An example would be including a file that doesn’t exist. Despite the warning, PHP will continue to execute the script.
- **Notice errors**: Notices are mild errors or alerts that suggest improvements to your code, which don’t necessarily affect the script’s execution. Examples include accessing undefined variables or indices of an array.
- **Deprecated errors**: These are issued when you use PHP code that is outdated and may not be supported in future versions of PHP. It’s a heads-up to update your code to newer standards.
- **Recoverable errors**: These occur when a fatal error is caught by a catchable exception. PHP allows you to handle these errors gracefully by using a custom error handler and continuing the script.

For example, a parse error in PHP might occur when editing a theme file or a custom plugin in your WooCommerce store.

Suppose you want to add custom PHP code to modify how your WooCommerce site displays a product’s price. You might add the following function to your theme’s `functions.php` file:

```
function modify_product_price_display() {
    echo 'New price: ' . wc_get_price_to_display( $product;
}
```

In the above code snippet, the closing parenthesis at the end of the function `wc_get_price_to_display` is missing.

The correct code should be:

```
function modify_product_price_display() {
    echo 'New price: ' . wc_get_price_to_display( $product );
}
```

The missing parenthesis in the first snippet would cause a parse error; PHP expects the syntax to be correct before executing the script.

The error would typically halt the script and could prevent your site from loading completely. It may display an error message that points to the problematic line in the `functions.php` file. This helps you identify and correct the syntax mistake.

Any number of factors can cause fatal errors including your theme, plugins and extensions, server configuration, and more.

For example, a fatal error in a WooCommerce context could occur when you attempt to use an undefined function. Imagine you’re trying to add a function that applies a special discount under certain conditions by adding the following code to your theme’s `functions.php` file:

```
function apply_special_discount() {
    if ( is_user_logged_in() ) {
        add_discount_to_cart(10); // Assume this is meant to add a 10% discount
    }
}
add_action('woocommerce_before_cart', 'apply_special_discount');
```

In this code, if the function `add_discount_to_cart()` is not defined anywhere in your theme, an extension or plugin, or WooCommerce core files, PHP will throw a fatal error when trying to execute it. The error message would typically indicate that the function is undefined, causing the script to halt execution.

This prevents the entire page from loading because the error disrupts the normal life cycle of the WordPress execution that WooCommerce relies on.

Here’s an example of what the fatal error might look like in this scenario:

```
Fatal error: Uncaught Error: Call to undefined function add_discount_to_cart() in /path/to/your/site/wp-content/themes/your-theme/functions.php:5
Stack trace:
#0 /path/to/your/site/wp-includes/class-wp-hook.php(307): apply_special_discount('')
#1 /path/to/your/site/wp-includes/class-wp-hook.php(331): WP_Hook->apply_filters(NULL, Array)
#2 /path/to/your/site/wp-includes/plugin.php(474): WP_Hook->do_action(Array)
#3 /path/to/your/site/wp-content/plugins/woocommerce/includes/class-wc-cart.php(138): do_action('woocommerce_bef...')
#4 /path/to/your/site/wp-content/plugins/woocommerce/includes/class-wc-cart.php(112): WC_Cart->calculate_totals()
#5 /path/to/your/site/wp-content/plugins/woocommerce/includes/class-wc-cart-session.php(53): WC_Cart->init()
#6 /path/to/your/site/wp-content/plugins/woocommerce/includes/class-woocommerce.php(597): WC_Cart_Session->get_cart_from_session()
#7 /path/to/your/site/wp-includes/class-wp-hook.php(307): WooCommerce->init('')
#8 {main} thrown in /path/to/your/site/wp-content/themes/your-theme/functions.php on line 5
```

To resolve such errors, you need to ensure that your code uses properly defined functions.

- [WooCommerce functions](https://developer.woocommerce.com/docs/useful-core-functions/)
- [WordPress functions](https://woocommerce.com/document/wordpress-functions/)

An example of a warning error in PHP when working with WooCommerce could involve file inclusion. Suppose you are customizing your WooCommerce site by adding some additional features through a PHP script. You decide to include a configuration file that contains various settings specific to these features in your theme’s `functions.php` file:

```
include 'config/settings.php';
```

If the file `config/settings.php` does not exist in the specified directory or the path is incorrect, PHP will generate a warning error. This error will inform you that the file was not found. Despite this, the script will continue to execute the rest of the code in the `functions.php` file.

The warning would look something like this:

```
Warning: include(config/settings.php): failed to open stream: No such file or directory in /path/to/your/theme/functions.php on line 10

Warning: include(): Failed opening 'config/settings.php' for inclusion (include_path='.:/usr/lib/php:/usr/local/lib/php') in /path/to/your/theme/functions.php on line 10
```

This error doesn’t stop the page from loading entirely, but the missing configuration file might lead to other functionalities not working as intended if the settings it contains are crucial for those features. Addressing this warning by correcting the file path or ensuring the file exists at the specified location would resolve the issue.

An example of a notice error in PHP when working with WooCommerce can occur when you try to use an undefined variable.

Imagine you are writing a function to adjust the price display based on whether a product is on sale in WooCommerce. You add the following code to your theme’s `functions.php` file:

```
function show_discount_notice() {
    global $product;
    if ($product->is_on_sale()) {
        echo 'Sale Price: ' . $sale_price;
    }
}
add_action('woocommerce_after_shop_loop_item_title', 'show_discount_notice');
```

In this snippet, if the variable `$sale_price` has not been defined or initialized before it’s echoed, PHP will trigger a notice error. This notice would typically say something like:

```
Notice: Undefined variable: sale_price in /path/to/your/theme/functions.php on line 4
```

While the notice doesn’t stop the script from executing, it indicates that your code is trying to use a variable that hasn’t been set. This could lead to incorrect or unexpected output on your website. In this case, initializing `$sale_price` or ensuring it’s derived correctly from your product data would correct the issue and eliminate the notice.

A deprecated error in PHP occurs when a site uses outdated functions or features.

For example, using an outdated WooCommerce hook or filter function in your theme’s `functions.php` file (such as `woocommerce_get_product_terms` to list product categories), which was deprecated in favor of newer functions):

```
function list_product_categories() {
    $terms = woocommerce_get_product_terms($product->id, 'product_cat');
    foreach ($terms as $term) {
        echo $term->name . ', ';
    }
}
add_action('woocommerce_after_shop_loop_item', 'list_product_categories');
```

When you use this deprecated function, PHP will not stop executing the script. Instead, it will log a deprecated warning that might look something like this:

```
Deprecated: woocommerce_get_product_terms is deprecated since version 3.0! Use wc_get_product_terms instead.
```

This error serves as a caution to update your code to align with the current best practices or newer functions available in WooCommerce. Using the recommended `wc_get_product_terms` function instead would resolve this deprecated error and ensure better compatibility with future versions of WooCommerce and WordPress.

A recoverable error occurs when custom error-handling mechanisms can potentially catch and handle the error.

Imagine you are customizing a WooCommerce function to process payments. You accidentally type-hint a parameter incorrectly in a payment processing function:

```
function process_payment(int $amount, array $order_details) {
    // Process payment logic here
    echo "Processing payment of $" . $amount . " for order #" . $order_details['order_id'];
}

try {
    // Simulating a call to process_payment with incorrect type for $order_details
    process_payment(100, "This should be an array");
} catch (TypeError $e) {
    echo "Error: " . $e->getMessage();
}
```

In this code snippet, the `process_payment` function expects an integer for `$amount` and an array for `$order_details`. If you pass a string instead of an array for `$order_details`, it will trigger a `TypeError`. Because this error is occurring within a try block and caught by a corresponding catch block handling TypeError, it becomes a recoverable error:

The output of this error handling might be something like:

```
Error: Argument 2 passed to process_payment() must be of the type array, string given
```

This type of error is recoverable because the execution of the script continues even after the error occurs. This allows you to handle the mistake gracefully without breaking the functionality of the entire application.

PHP has different levels of errors that help programmers understand what kind of problem has occurred in their code. Here’s a simpler breakdown of these error levels:

- **Fatal errors (E_ERROR)**: Serious issues that stop the program right away.
- **Warnings (E_WARNING)**: These are issues that don’t stop the program but indicate something went wrong that might need fixing.
- **Parse errors (E_PARSE)**: These happen when PHP can’t understand the code at all due to mistakes in writing it.
- **Notices (E_NOTICE)**: Minor issues that suggest the code might not work as expected, but the program can still run.
- **Core errors (E_CORE_ERROR)**: Similar to fatal errors but occur when PHP itself starts up, not during the program run.
- **Core warnings (E_CORE_WARNING)**: Like warnings, these happen when PHP starts up.
- **Compile errors (E_COMPILE_ERROR)**: Serious issues found when PHP prepares your code before it runs.
- **Compile warnings (E_COMPILE_WARNING)**: Warnings found during the preparation to run your code.
- **User errors (E_USER_ERROR)**: Errors that programmers create on purpose in their code to handle special cases.
- **User warnings (E_USER_WARNING)**: Warnings that programmers create on purpose in their code.
- **User notices (E_USER_NOTICE)**: Notices that programmers add to help identify less serious issues.
- **Strict notices (E_STRICT)**: Suggestions for how to make the code better and more compatible with future versions of PHP.
- **Recoverable errors (E_RECOVERABLE_ERROR)**: Serious issues that can be caught and managed within the program.
- **Deprecated warnings (E_DEPRECATED)**: Alerts about outdated parts of PHP that will be removed and should no longer be used.
- **User deprecated warnings (E_USER_DEPRECATED)**: Warnings about outdated practices that programmers add to their code.
- **All errors (E_ALL)**: Represents all types of errors and warnings.

Each of these levels helps developers decide how to respond — whether they need to fix the code right away, review it for potential issues, or update it to use newer programming practices.

Do you still have questions and need assistance?

- [Get in touch](https://woocommerce.com/my-account/create-a-ticket/) with a Happiness Engineer via our Help Desk. We provide support for extensions developed by and/or sold on WooCommerce.com, and Jetpack/WordPress.com customers.
- If you are not a customer, we recommend finding help in the [WooCommerce support forum](https://wordpress.org/support/plugin/woocommerce/) or hiring a Woo Agency Partner. These are trusted agencies with a proven track record of building highly customized, scalable online stores.[Learn more about Woo Agency Partners](https://woocommerce.com/development-services/).

