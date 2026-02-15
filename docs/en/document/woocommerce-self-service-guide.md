---
title: WooCommerce self-service guide
url: https://woocommerce.com/document/woocommerce-self-service-guide/
---

WooCommerce troubleshooting and conflict testing are useful for finding out why your site is having problems. Have an issue with your WooCommerce store? We aim to help you solve it.

Most issues are caused by:

- Outdated software on your site
- Conflict with your theme
- Conflict with another plugin

Keeping software up to date helps protect your website against hacking. The latest versions of WordPress, WooCommerce, and WooCommerce.com Marketplace extensions, as well as your theme and other plugins, often have bug fixes that resolve the current trouble you’re having. This forms the basis of troubleshooting and conflict testing.

To check if there are updates for your website, go to **WooCommerce > Status > System Status**, where important notifications are highlighted in red.

[How to understand the WooCommerce System Status Report](https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/).

To ensure that the update process runs as smoothly as possible:

1. Make a full backup of your site, data, and files.
  - Ask your hosting company to assist you, or
  - Use [Jetpack Backup](https://jetpack.com/support/restoring-with-jetpack-backup/) (it’s free)
  
2. Go to**Dashboard > Plugins**, and update third-party plugin(s) that are out of date. Do not update WooCommerce yet.
3. Update extensions purchased from WooCommerce.com. You can also download the extension(s) from your [WooCommerce.com account](https://woocommerce.com/my-account/) and overwrite plugin(s) manually via File Transfer Protocol (FTP) in **/wp-content/plugins/**
4. Go to: **WordPress Dashboard > Plugins** and update **WooCommerce** to its [latest stable version](https://wordpress.org/extend/plugins/woocommerce/changelog/).
5. **Update WordPress** to its current version. A notification in your **WordPress dashboard** tells you whether an update is available or not.
6. **Update your theme** to the current version. Check with the author to see if you’re running the latest version.

[Learn how to update WooCommerce](https://woocommerce.com/document/how-to-update-woocommerce/).

Almost half of the interactions we receive are related to issues caused by conflicts with third-party themes and plugins. Troubleshooting and conflict testing are the best ways to identify the conflict.

To troubleshoot theme and plugin conflicts:

1. **Switch to a default WordPress theme** to see if the problem still exists. If it disappears, contact your theme developer about the issue; there may be an update available that solves it. If the problem persists while using a default theme, go to the next step.
2. Temporarily deactivate all plugins (except WooCommerce and the WooCommerce.com extension(s) giving trouble). Does that fix it?
  - If **yes**, it’s likely there is a conflict with one of the disabled plugins. To pinpoint which one, reactivate plugins one at a time, repeat the actions taken when the issue appeared, and see when/if the issue reappears.
  - If **not**, and the issue remains while running a default theme with no extra plugins activated, go to the next step. Please note we cannot provide support for third-party plugins and themes. If a conflict test reveals the issue is a conflict between WooCommerce software and a third-party plugin or theme, please contact the developer of the plugin or theme in question.
  
3. Contact one of our Happiness Engineers to investigate and advise. In your support request, please provide us with as much info as possible . Answering the following questions will help speed up the process:
  - When exactly did you first notice the problem?
  - Have any updates been applied to your website recently?
  - Have you changed themes or made design changes?
  - Have you installed any new plugins?
  - Can the issue be replicated on multiple devices?
  - Is your problem happening in one browser or all of them?
  - Do you see a specific error message? Please take and share a screenshot.
  

[See how to test for theme and plugin conflicts](https://woocommerce.com/document/how-to-test-for-conflicts/).

Fatal error messages typically tell you the path, including the name of the plugin or theme causing it. This helps track down where/what to fix.

The WooCommerce System Status Report provides a wealth of info on versions, template overrides, and memory. To access it, go to **WooCommerce > Status > System Status**.

Items requiring action will be highlighted in red. This may include [updating memory](https://codex.wordpress.org/Editing_wp-config.php#Increasing_memory_allocated_to_PHP), creating pages correctly, or updating outdated plugins. [Learn how to understand the System Status Report](https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/).

[See our guide for troubleshooting a slow site](https://woocommerce.com/document/troubleshooting-a-slow-site/) for tips and tricks.

A zip file can be uploaded directly via your WordPress admin, under **Plugins > Add New**. If uploading a newer version of the plugin, updates will be applied automatically

Alternatively, to update a plugin manually via FTP, unzip the download, upload the files via FTP, and overwrite existing files. There is **no need to deactivate the plugin or delete files**. You cannot automatically update WooCommerce plugins via your WordPress admin unless you activate your subscription — you **must** do it via FTP.

Extensions and theme subscriptions purchased from the official WooCommerce.com Marketplace do not use manually entered keys. To activate a subscription for these products, please [connect your WooCommerce.com account to your store](https://woocommerce.com/document/managing-woocommerce-com-subscriptions/#connect-your-site-woocommercecom-account).

You can also:

- Visit [My Downloads](https://woocommerce.com/my-account/downloads/) to manually download purchased extensions and themes.
- View [My Subscriptions](https://woocommerce.com/my-account/my-subscriptions/) to manage extension and theme renewals.

Requesting a new feature or help with customization is beyond the scope of our [Support Policy](https://woocommerce.com/support-policy/). Customizations or particular features/functionality can be addressed by contacting [Codeable](https://www.codeable.io/partners/woocommerce/?ref=qGefA6).

Ideas or feature requests for official WooCommerce.com Marketplace extensions and WooCommerce core can be posted directly on our [Feature Request Board](https://woocommerce.com/feature-requests/woocommerce/). We act on feedback and ideas with the highest priority.

You’re running an older version of the WooCommerce database compared to the plugin version you have active and need to update to the latest. More info at: [How to Update WooCommerce – Data update notice](https://woocommerce.com/document/how-to-update-woocommerce/#db-update).

If you notice product variations, tax rates, and other large data sets not saving, see solutions at [Problems with large amounts of data not saving (variations, rates, etc)](https://woocommerce.com/document/problems-with-large-amounts-of-data-not-saving-variations-rates-etc/).

If you have found a bug in the core WooCommerce plugin (**not** in an extension or theme) that persists after performing the above troubleshooting steps, report it to our developers at the [WooCommerce GitHub repository](https://github.com/woocommerce/woocommerce/issues/).

[Our documentation](https://woocommerce.com/learn/) covers all of our plugins, extensions, and themes in detail. We put a lot of effort into improving content and making it easier to navigate.

Here are a few resources to assist you:

- [WooCommerce troubleshooting](https://woocommerce.com/documentation/woocommerce/get-help/troubleshooting-get-help/)
- [How to work with variable products](https://woocommerce.com/document/variable-product/)
- [Translation/localization](https://woocommerce.com/document/woocommerce-localization/)
- [Fixing blurry product images](https://woocommerce.com/document/using-the-appropriate-product-image-dimensions/)
- [Fixing outdated WooCommerce templates](https://woocommerce.com/document/fix-outdated-templates-woocommerce/)

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

