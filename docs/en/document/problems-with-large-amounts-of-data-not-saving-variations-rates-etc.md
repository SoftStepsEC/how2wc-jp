---
title: Problems with large amounts of data not saving (variations, rates etc)
url: https://woocommerce.com/document/problems-with-large-amounts-of-data-not-saving-variations-rates-etc/
---

If you notice product variations, tax rates and other large data sets not saving, Suhosin (a security module in PHP) may be preventing the POST data from being saved. This issue can also be caused by servers with version PHP **5.3.9+**and servers running**mod_security**.

If enabled, Suhosin may need to be configured to increase its data submission limits. Changing Suhsoin settings differ from host to host so it’s usually better to consult with the provider than attempt it yourself, however some hosts allow you to change settings via **php.ini, suhosin.ini, or .htaccess.**Commonly, the following vars will need changing:

```
suhosin.post.max_array_index_length = 256
suhosin.post.max_totalname_length = 65535
suhosin.post.max_vars = 1024
suhosin.post.max_name_length = 256
suhosin.request.max_varname_length = 256
suhosin.request.max_array_index_length = 256
suhosin.request.max_totalname_length = 65535
suhosin.request.max_vars = 1024
```

After saving you will need to restart the server for the changes to take effect. See [http://www.hardened-php.net/suhosin/configuration.html](http://www.hardened-php.net/suhosin/configuration.html) for more information on Suhosin settings.

In **shared hosting environments** it may not be possible to edit php.ini, in which case you may be able to set the suhosin settings via .htaccess:

```
php_value suhosin.max_array_index_length 256
php_value suhosin.post.max_array_index_length 256
php_value suhosin.post.max_totalname_length 65535
php_value suhosin.post.max_vars 1024
php_value suhosin.post.max_name_length 256
php_value suhosin.request.max_varname_length 256
php_value suhosin.request.max_array_index_length 256
php_value suhosin.request.max_totalname_length 65535
php_value suhosin.request.max_vars 1024
```

It is still recommended however to consult your hosting providers documentation, or raise a ticket with them for assistance.

**If you use non-latin characters**, you may want to increase the following value from the default 64. This will help with issues with non-latin characters.

```
suhosin.request.max_varname_length = 256
```

Newer versions of PHP implement a php.ini directive called max_input_vars usually set to 1000. This means that posting > 1000 form fields for instance would be truncated preventing data from being saved.

This can be changed in php.ini:

```
max_input_vars = 3000
```

If you need to do this via htaccess (on a shared host for instance) you may use:

```
php_value max_input_vars 3000
```

Mod_security can also prevent data saving; you may experience error 503’s if this is the case. As with the above issues, you may want to contact your host to help resolve this. Workarounds include:

- Configuring mod_security to allow the data through (advanced)
- [Disabling mod security by IP](http://www.askapache.com/htaccess/modsecurity-htaccess-tricks.html#Disabling_mod_security_conditionally_IP)
- (Dreamhost only) Turn the “Extra web security” setting off in the control panel.

References: [http://www.nivas.hr/blog/2012/04/04/beware-of-max_input_vars-php-ini-configuration-option/](http://www.nivas.hr/blog/2012/04/04/beware-of-max_input_vars-php-ini-configuration-option/) [https://shopplugin.net/kb/unable-to-save-products-with-large-amount-of-variations/](https://shopplugin.net/kb/unable-to-save-products-with-large-amount-of-variations/)

To verify that you are **really** experiencing the issue describe in this document, you can temporarily install and activate this free plugin: [WP Max Submit Protect](http://wordpress.org/plugins/wp-max-submit-protect/).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

