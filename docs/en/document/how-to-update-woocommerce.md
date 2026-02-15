---
title: How to update WooCommerce
url: https://woocommerce.com/document/how-to-update-woocommerce/
---

Updates to WooCommerce, WordPress, extensions, themes, and payment gateways are a fact of life. Our team is hard at work, releasing updates that add new features, improve security, fix issues, and, in general, make your store **better than ever**.

But how do you update WooCommerce without causing issues? We’ll cover a few of the common ways below.

Any store powered by WordPress and WooCommerce has two places where data and content are stored. One is your `wp-content` folder, where themes, plugins, and uploaded content are located. Another is the database that organizes and stores your product, order, post, page, data (and more).

So, how do you safeguard all of this data and content and keep it backed up?

The most efficient and reliable approach is to use an **automated site backup service**; we recommend [Jetpack](https://jetpack.com/pricing/woocommerce-backup/).

Besides saving you time by not having to do anything manually, you benefit from:

- **Unlimited** storage space.
- Automated regular backups of your **entire site**, including your database, all content, plugins, themes, settings, and more.
- Instant restores so you can **revert to a previous version** with one click.
- Direct access to **24/7 expert support**.

There are two steps for manually backing up your store:

- First, back up your **database**. There are multiple ways to do this; see the [WordPress Codex](https://wordpress.org/support/article/backing-up-your-database/) for options. There are manual and plugin-based options available.
- Using Secure File Transfer Protocol (SFTP), head to your `wp-content` folder to back up your **theme and extension/plugin files**. We **strongly recommend** making a backup of your theme files if you’ve made any customizations.

At first, this may appear technical and complex, but don’t be alarmed! If you’d prefer not to handle this yourself, working with a developer who is familiar with these tasks is also an option — we **highly recommend** hiring a [Woo Agency Partner](https://woocommerce.com/development-services/).

First, let’s review a few terms we’ll be using. Some resources may use other terms like “dev environment”, “testing environment”, and “live environment”, but we’ll stick to the basic three:

- **Local**: On a personal computer, generally not accessible to the public via the web.
- **Staging**: Where you test updates. It should replicate the same server setup as the live site.
- **Production**: Your live site, where people visit and purchase from you.

Keep in mind this is a simplistic overview, and there are many tools and ways to do this. There aren’t absolutes in how you test updates, just as long as you generally **do not test them on a live site**. If you have a developer working on your site, ask them about their process for testing updates.

Most developers will start with a local install. This means that WordPress is set up on their computer and it acts as a server. Using a code editor, one can then build, update, and test updates on their own computer.

When working on a local install, we **highly recommend** you use version control, such as [Git](https://en.wikipedia.org/wiki/Git) or [Subversion](https://en.wikipedia.org/wiki/Apache_Subversion) (SVN). This comes in handy in case you need to revert to a previous working version, and can also make it simpler to deploy a local site to staging and production.

To test an update beyond a local site, it’s best to create a second WordPress install via your host and restore a backup of your live site to it. WordPress hosts often offer tools to set up a staging environment ([Jetpack VaultPress Backup](https://jetpack.com/upgrade/backup/) can also do this for you).

This is a replica of your production site and a safe place to test updates. A staging site can also be shared with others for help with testing. Make sure to test on different devices, check page load time, and so on.

Should all go well during staging tests, you’re ready to update your live production site. You can do this however you prefer, or arrange it with your developer(s).

**Pro tip**: Set your site to [Coming soon](https://woocommerce.com/document/configuring-woocommerce-settings/coming-soon-mode/) mode to prevent people from checking out or making payments. If a transaction occurs during the update, orders may be lost.

To update a production site, some store owners have Git set up to deploy from a master branch. You could also click the **Update** button if you’ve tested these updates and know for certain that they’re safe for your site. Of course, your backups are on standby, ready to restore in an instant if anything unexpected occurs. That way there’s no downtime or revenue lost.

From here, **figure out which tools and strategies work best for you** and your team or developer(s), and **put a good testing process in place**. If you put the time upfront into testing updates, you’re guaranteed to save yourself time, headaches, and money in the end.

To get updates on anything purchased from the WooCommerce.com Marketplace, go to *WooCommerce > Extensions > WooCommerce.com Subscriptions* in your store’s WP Admin dashboard and ensure your store is connected to your WooCommerce.com account. [Learn more about managing WooCommerce.com subscriptions](https://woocommerce.com/document/managing-woocommerce-com-subscriptions/).

Connecting your WooCommerce.com account to your store allows you to:

- View the status of WooCommerce (plus your extensions, themes, and payment gateways).
- Filter these items using *Installed*, *Activated*, *Download*, and *Update Available* options.
- Determine which extensions, themes, and payment gateways are compatible with your version of WooCommerce.

For example: In the **Plugin** and **Tested up to WooCommerce version** columns, it might show that WooCommerce Stripe is known to be compatible up until WooCommerce 5.0 If you have WooCommerce 5.1+ installed.

**Note**: Always take caution when updating; don’t forget to**first test on a staging site** as instructed above in [Testing updates](https://woocommerce.com/document/how-to-update-woocommerce/#testing-updates).

Extensions, payment gateways, and themes **not** developed and maintained in-house by the WooCommerce team are from **third-party developers**. Store owners **must** contact the third-party developer directly for support on updates and compatibility.

Third-party developers should also [add version-check support to their extensions](https://woocommerce.wordpress.com/2017/08/28/new-version-check-in-woocommerce-3-2/).

A WooCommerce **database update notice** displays when you update to a new version of WooCommerce and a database update is needed.

This notice contains two options:

- **Update WooCommerce Database update**: Clicking this button begins the process of updating your database to match the plugin version you installed or updated to. The database organizes, contains, and stores your products, orders, posts, and pages — an essential process.
- **Learn more about updates**: This button directs you to best practices for updating WooCommerce, extensions, and payment gateways, including info on what is updated and in which order.

**Note**: Ensure you have a backup in place *before* clicking **Update WooCommerce Database**.

Once the update process begins, a **WooCommerce database update** notice will be displayed. Clicking the **View progress** link will take you to the **Scheduled Actions** section and show the update’s pending actions.

Once the update process is complete, you will see a dismissible**WooCommerce database update complete** message.

- [WordPress Backups](https://developer.wordpress.org/advanced-administration/security/backup/#Backing_Up_Your_WordPress_Site) (WordPress Codex).
- [Backups](https://jetpack.com/upgrade/backup/) and [security](https://jetpack.com/features/security/) (Jetpack)
- [Managing plugins](https://wordpress.org/documentation/article/manage-plugins/) (WordPress Codex).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

