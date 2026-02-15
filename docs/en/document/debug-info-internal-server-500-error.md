---
title: HTTP 500 Internal Server Error — getting more information
url: https://woocommerce.com/document/debug-info-internal-server-500-error/
---

An HTTP 500 Internal Server Error is a commonly encountered error. It is often temporary and is a general server error response.

Generally, an HTTP 500 Internal Server Error’s output is not descriptive and does not help narrow down the cause of the issue. It is considered best practice to show a generic error like the one displayed below on live/production sites:

```
Internal Server Error

The server encountered an internal error or misconfiguration and was unable to complete your request.

Please contact the server administrator at [support email] and inform them of the time the error occurred, and anything you might have done that may have caused the error.

More information about this error may be available in the server error log.

[server/port information]
```

If you encounter a persistent internal server error, you will need more information to troubleshoot it.

To enable WordPress debugging mode:

1. Connect to your site using [Secure File Transfer Protocol](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol) (SFTP).
2. Open the file named `wp-config.php`.
3. Look for the following line of code: `define('WP_DEBUG', false);`
4. Change the value from `false` to `true`.
5. Save the file.

**Note:** If the value in the line mentioned above is already set as `true`, another extension, plugin, or server configuration may be suppressing the error output.

Refresh the page you saw the error on; you should now see more descriptive error messages which will help in troubleshooting. [Learn more about debugging in WordPress](https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/).

Since this is a server-level error, you’ll often find further details in server error logs. Your hosting provider can usually help you find these if they are available.

