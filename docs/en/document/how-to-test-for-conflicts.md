---
title: How to test for plugin and theme conflicts
url: https://woocommerce.com/document/how-to-test-for-conflicts/
---

A conflict is an error or malfunction caused by two parts of code giving conflicting signals. For example, plugin A gives the signal to put the order in “Completed” status and plugin B prevents this from happening.

Themes and plugins provide additional functionality and features — it also means more code is running on your website and the risk of incompatibility is higher. We strive to ensure compatibility with our own extensions, but third-party products made for WooCommerce are not guaranteed to work with our software. In this documentation page, we will explain how to test for plugin and theme conflicts.

Testing is the only way to determine what is causing a conflict.

We highly recommend making a backup of your site. Deactivating and reactivating plugins typically does not cause issues, but having a good backup will save you a lot of time and energy on the rare occasion it does.

Most hosting providers offer a backup plan. If not, there are two options:

- Consider [Jetpack Backup](https://jetpack.com/support/restoring-with-jetpack-backup/).
- Use a **staging site**. This is a clone of your production site — one that is processing orders and has visitors — where you can safely test conflicts without your live site being affected and potentially losing revenue. Most hosting providers can help with this or, on most hosting platforms, you can use the [WP Staging](https://wordpress.org/plugins/wp-staging/) plugin to create a clone in your dashboard.

To troubleshoot theme and plugin conflicts:

1. [Update all of your plugins and themes](https://woocommerce.com/document/how-to-update-woocommerce/). In some cases, conflicts can be resolved by using the latest versions of your site software. New releases not only include new features, but security and bug fixes too.
2. Switch to a default WordPress theme, such as Twenty Twenty-Five, or install and switch to Woo’s Storefront Theme , to see if the issue persists.
  - If not , your theme is causing the issue. You can:
    - change your theme.
    - contact the author of the theme and ask them to fix it.
    
  - If the issue **does** persist, go to the next step.
  
3. **Temporarily deactivate** all plugins except WooCommerce and the WooCommerce extensions you’re experiencing issues with.
4. Test if the conflict still exists . How to test it, depends on what type of conflict you were experiencing.
  - If the conflict occurred while browsing your site or the Dashboard, go to the same location. Examples of this would be:
    - A feature not working on the product edit screen
    - A button not showing on the cart page
    
  - If the conflict only happens after a certain process, recreate and follow those identical steps. Examples of this would be:
    - An order is marked “On Hold” instead of “Completed” after product A is added and paid for.
    - An error displays while adding two products to the cart.
    
  - If the conflict no longer exists, it means that the theme or plugins/extensions you deactivated were causing the conflict. If the conflict still exists, see ‘Drop-Ins and Must-Use’ and ‘Unsuccessful Conflict Tests’ below.
  
5. Determine which plugin is causing the conflict by:
  - reactivating them one by one
  - **testing again after each reactivation**. For process-related conflicts, this means recreating the same process over and over again.
  

- [Meks Quick Plugin Disabler](https://wordpress.org/plugins/meks-quick-plugin-disabler/) remembers what plugins you had active when you’re done testing.
- [Theme Switcha](https://wordpress.org/plugins/theme-switcha/) allows you to test switching between themes on your site without affecting the front-end.
- [WP Rollback](https://wordpress.org/plugins/wp-rollback/) allows you to go back to previous versions of themes or plugins, without needing to manually re-install previous versions. This can be helpful for troubleshooting if specific updates have caused issues.
- [Query Monitor](https://wordpress.org/plugins/query-monitor/) helps identify performance issues with your site. It provides detailed insights into database queries, PHP errors, and HTTP API calls. This information is helpful for reviewing the efficiency and speed of the site.

On some sites is a “Must-Use” and/or “Drop-ins” section in the plugins list. These cannot be deactivated by you directly, but they can be the cause of the conflict.

- Some of these plugins are installed by **another plugin** which functions as a “helper plugin”. While doing a conflict test, deactivating those other “parent” plugins will also deactivate these ones.
- Also, many hosting companies use drop-in and/or must-use plugins that they pre-install on your site because it helps with their server setup.

If the conflict persists in the latter case while doing the above tests, it might be caused by a drop-in installed by your host. For example, we’ve seen conflicts caused by drop-in caching plugins. In this case, you need to contact your hosting company for help with deactivation.

Bypassing browser caching during a conflict test ensures that you are working with the most current version of your website. Caching can display outdated information which may interfere with identifying the root cause of the issue.

To do this in Chrome, click on **View > Developer > Developer Tools > Network**and tick the box to select “Disable cache”:

You can then re-enable caching by deselecting this box.

Should nothing change/resolve with issues and/or errors you’re experiencing after testing for conflicts, it likely means there is another cause. There are more suggestions in [our self-service guide](https://woocommerce.com/document/woocommerce-self-service-guide), or you can contact our Happiness Engineers via our [support help desk](https://woocommerce.com/my-account/contact-support/). When contacting Support, please include a detailed description of:

- Steps that can be taken to replicate the issue.
- Conflict tests you performed to exclude conflicts.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

