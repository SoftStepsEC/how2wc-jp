---
title: Increasing the WordPress memory limit
url: https://woocommerce.com/document/increasing-the-wordpress-memory-limit/
---

There are two ways to address memory limit issues in WordPress:

- Adjust the memory limit yourself.
- Contact your hosting company.

Below, you’ll find several methods for adjusting WordPress memory limits yourself.

**Note:** This section requires advanced knowledge.

Add the following code snippet to the top of your site’s `wp-config.php` file:

```
define('WP_MEMORY_LIMIT', '256M');
```

This code snippet should be added **above** the line that says, `/* That's all, stop editing! Happy publishing. */`.

WordPress memory can differ from server memory; it must be set regardless of server memory settings. [Learn more about editing your wp-config.php file](https://developer.wordpress.org/advanced-administration/wordpress/wp-config/#Increasing_memory_allocated_to_PHP).

If you have access to your site’s `php.ini` file, adjust the line below:

```
memory_limit = 256M ; Maximum amount of memory a script may consume (64M)
```

If the line in your `php.ini` file specifies 64M, try 256M instead.

If you don’t have access to `PHP.ini`, try adding the following snippet to an `.htaccess` file:

```
php_value memory_limit 256M
```

If you do not feel comfortable trying the above methods yourself (or the above did not work for you), contact your hosting provider and ask them to increase your WordPress memory limit.

