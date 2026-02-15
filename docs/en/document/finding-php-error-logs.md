---
title: Finding PHP error logs
url: https://woocommerce.com/document/finding-php-error-logs/
---

PHP error logs can be useful when investigating an issue with a WordPress and WooCommercesite. This guide will provide steps and information about how to access PHP error logs within WooCommerce or on a hosting server.

WooCommerce features a logging system accessible in WP Admin via **WooCommerce > Status > Logs**, which records PHP fatal errors among other information.

This log serves as a valuable initial resource, mirroring details that would typically be found in PHP error logs on the server. We recommend you **consult this log first** before proceeding to locate the PHP logs on the server for further troubleshooting.

To access the log files:

1. In your store’s WP Admin dashboard, navigate to**WooCommerce > Status > Logs***.*
2. Under **Browse log files**, you will see a list of available log files.

This interface allows you to **filter**, **sort**, and **manage** log files efficiently. Additionally, you can perform bulk actions, such as downloading or deleting multiple log files simultaneously, by selecting the desired files and utilizing the bulk action dropdown menu.

Choose a group of files for targeted searches by employing filtering and sorting methods. You can then link directly to specific lines within those files containing the relevant results.

This view presents the content of an individual log file, highlighting the start of new entries and their severity levels. It enables users to highlight and create permalinks for specific lines within a file, as well as display extra contextual information for each log entry in a clear and readable format.

From this screen, you can either **download** or **permanently delete** the log file using the buttons located at the top-right of the file viewing interface.

Settings for managing log files can be adjusted via WP Admin at **WooCommerce > Status > Logs > Settings**. The configurable options include:

1. **Logger** allows you to activate or deactivate logging.
2. **Log storage** determines the location where log entries are stored; **File system (default)** is automatically selected. An alternative option is **Database**, which is not recommended for live sites. It’s important to note that changing this setting will not move existing log entries; they will remain in their original location.
3. **Retention period** defines the duration (in days) that log entries will be retained before automatic deletion. The default setting is 30 days.
4. Level threshold specifies the minimum severity level for recording logs, with lower severity levels being omitted. The default setting is None , indicating that all logs are stored. Options include:
  - Alert
  - Emergency
  - Debug
  - Critical
  - Error
  - Warning
  - Notice
  - None
  - Info
  
5. **File system settings**: This specifies the server location where log files are stored (e.g., `/srv/htdocs/wp-content/uploads/wc-logs/`). You have the option to modify this location by setting the `WC_LOG_DIR` constant in your `wp-config.php` file to a new path.

To view fatal errors:

1. In WP Admin, navigate to**WooCommerce > Status > Logs**.
2. On the **Browse log files** screen, select a **fatal-errors** file to open and view its contents.

The types of errors caught in the fatal-error log are PHP fatal errors, runtime errors, and errors purposely triggered in the code by a PHP function. For example, runtime errors can occur due to a typo in the code.

Fatal errors occur when the action in the code cannot be completed. Examples of a fatal error include:

- Calling an undefined function.
- Using an undefined variable.
- Calling a function on a null or otherwise unusable variable.

This does not include web server errors, such as timeouts.

The log will include:

- A timestamp of when the error occurred.
- The error that occurred.
- The file and line in the code for the origination of the error.
- A stack trace, which is a snapshot of the history of the function calls and files leading up to the error.

You can find PHP error logs in several places on your hosting server:

- In your server’s root folder, called `error.log`.
- In `public_html` (or a similar folder) called `error.log`.
- In `var/logs` or similar, called `error.log`.
- Additionally, if you have [debugging enabled](https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/) in WordPress and you have the log saved to a file, it will be in the `wp-content` folder, named `debug.log`

If you’re having trouble finding the file, you can have PHP tell you where it is:

1. Create a file named `phpinfo.php` in the root of your WordPress directory.
2. Open the `phpinfo.php` file in a text editor.
3. Insert the following code into the file: `<?php phpinfo(); ?>`.
4. Open the file on your site. For example, if your site’s URL is `example.com`, you can open the file by visiting `https://example.com/phpinfo.php`.
5. Search the page for the `error_log` value. The file path listed here is the absolute file path of the PHP error log — visit that address on your server and you should see the PHP error log. If the value is empty, you’ll need to set a value to log errors on your site.
6. See the picture below for how this should appear:

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

