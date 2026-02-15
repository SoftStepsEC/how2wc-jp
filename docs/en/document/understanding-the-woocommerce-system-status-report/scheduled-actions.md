---
title: Scheduled actions
url: https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/scheduled-actions/
---

Scheduled actions manage background tasks related to WooCommerce order notifications and payment processing. Gaining a clear understanding of these actions can help your store run more efficiently, and prevent issues — such as missed order updates or delayed customer emails.

You can find all scheduled actions in your store’s WP Admin dashboard under **WooCommerce > Status > Scheduled Actions**.

Before explaining how scheduled actions work, it is helpful to understand both cron and WP-Cron.

Cron is a time-based task scheduling tool commonly used to automate maintenance tasks on servers. [WP-Cron](https://developer.wordpress.org/plugins/cron/#what-is-wp-cron) is WordPress’s way of handling scheduled tasks.

WP-Cron runs whenever someone visits your website, initiating when a page is requested. It allows WordPress to execute scheduled tasks in the background, minimizing the impact on page load times or site performance. WP-Cron also checks for theme or plugin updates, sends emails, and schedules sale prices in WooCommerce.

Because WP-Cron relies on site traffic, scheduled tasks may be delayed if there is low traffic to your store. Conversely, excessively high traffic could cause performance issues.

[WP Crontrol](https://wordpress.org/plugins/wp-crontrol/) is a free, helpful tool for viewing, triggering, and troubleshooting cron events.

Further reading on WP-Cron:

- [Debugging WP-Cron](https://woocommerce.com/document/subscriptions/develop/complete-guide-to-scheduled-events-with-subscriptions/#debugging-wp-cron)
- [Replace WP-Cron with a real cron job](https://woocommerce.com/document/automatewoo/replace-wordpress-cron-real-cron-job/)

[Action Scheduler](https://actionscheduler.org/) is a scalable, traceable job queue for handling large sets of tasks within WordPress. It’s widely used to manage millions of WooCommerce Subscriptions payments, WooCommerce webhooks, and events or emails for other extensions/plugins.

Action Scheduler sends tasks in batches of 20, preventing PHP memory exhaustion. It can handle multiple batches simultaneously, processing up to five queues at once.

Action Scheduler uses a custom WordPress post type — `scheduled-action` — to store details such as the **hook name**, **arguments**, and the **scheduled time**for future tasks. It runs by attaching itself as a callback to the `action_scheduler_run_schedule` hook, which is triggered using WordPress’s built-in WP-Cron.

Essentially, WP-Cron activates Action Scheduler.

Once triggered, Action Scheduler looks for `scheduled-action` posts that are ready to run. By default, it relies on WP-Cron, which means it is also dependent on site traffic. You can also [set up custom server-side cron jobs](https://woocommerce.com/document/automatewoo/replace-wordpress-cron-real-cron-job/) to run WP-Cron independently and bypass traffic dependency, making it more reliable.

As mentioned above, you can find scheduled actions in your store’s WP Admin dashboard under **WooCommerce > Status > Scheduled Actions**.

From here, you can:

- Run a pending action.
- View scheduled actions with a specific status (such as all in-progress actions).
- View log entries for failed actions.
- Search scheduled actions by hook name, scheduled date, or group name.

For additional information on WP-Cron, scheduled actions, and troubleshooting tips for common issues:

- [Action Scheduler](https://actionscheduler.org/)
- [Replace WP-Cron with a real cron job](https://woocommerce.com/document/automatewoo/replace-wordpress-cron-real-cron-job/)
- [Debugging WP-Cron](https://woocommerce.com/document/subscriptions/develop/complete-guide-to-scheduled-events-with-subscriptions/#debugging-wp-cron)
- [AutomateWoo: Performance](https://woocommerce.com/document/automatewoo/performance/)
- [Complete guide to Scheduler events with Subscriptions](https://woocommerce.com/document/subscriptions/develop/complete-guide-to-scheduled-events-with-subscriptions/)
- [WordPress Developer Handbook: Cron](https://developer.wordpress.org/plugins/cron/)

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/) for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

