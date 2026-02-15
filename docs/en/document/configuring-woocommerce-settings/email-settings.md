---
title: Email Settings
url: https://woocommerce.com/document/configuring-woocommerce-settings/email-settings/
---

WooCommerce has a variety of built-in emails to help communicate your store’s operations. This guide provides a detailed overview of the email settings in WooCommerce, including:

- The [email notifications](https://woocommerce.com/document/configuring-woocommerce-settings/email-settings/#email-notifications) built into the WooCommerce plugin.
- Settings to [set the sender information](https://woocommerce.com/document/configuring-woocommerce-settings/email-settings/#email-sender-options) for your shop’s emails.
- [Email Template settings](https://woocommerce.com/document/configuring-woocommerce-settings/email-settings/#email-templates) to customize the look of your shop’s emails.
- Settings available to [customize or disable individual emails](https://woocommerce.com/document/configuring-woocommerce-settings/email-settings/#editing-individual-emails)
- [Custom Email Templates (Developers)](https://woocommerce.com/document/configuring-woocommerce-settings/email-settings/#custom-email-templates)

Find these settings on your site at: **WooCommerce > Settings > Emails**.

For each WooCommerce email listed, it’s possible to configure your settings (optional). More detailed instructions below in: **Editing Individual Emails**.

- **New order**— The system sends new order emails to your chosen recipient(s) upon receiving a new order.
- **Cancelled order**— The system sends cancelled order emails to your chosen recipient(s) when orders are marked cancelled (if they were previously processing or on-hold).
- Failed order — Two notifications are sent when orders are marked failed (if they were previously pending or on-hold):
  - A notification to your chosen recipient(s) with order details.
  - A notification to the customer explaining that their order was unsuccessful due to a payment issue, with instructions to try again with a different payment method.
  
- **Order on-hold —** The system sends this order notification to customers with their order details when an order is placed on-hold from the Pending, Cancelled or Failed order status.
- **Processing order —** The system sends this order notification to customers containing order details after payment.
- **Completed order**— The system sends order complete emails to customers when their orders are marked completed, this usually indicates that their orders are shipped.
- **Refunded order —** The system sends order refunded emails to customers when their orders are refunded. This email has settings for both partial and full refunds.
- **Order Details**— You send this email manually from the “Edit Order” screen to [share invoice details and a payment link](https://woocommerce.com/document/managing-orders/paying-for-orders/#pay-for-order-email-link) with customers. This email has setting for paid and unpaid orders.
- **Customer note**— The system sends customer note emails when you add a note marked “Note to Customer” to an order. Learn more about: [Order Notes](https://woocommerce.com/document/managing-orders/view-edit-or-add-an-order/#order-notes)
- **Reset password —** The system sends customer “reset password” emails when customers reset their passwords.
- **New account**— The system sends customer “new account” emails when a customer signs up via checkout or account pages.

**Note:** WooCommerce is highly extensible, open source software. Extensions commonly add additional emails to WooCommerce. If you see additional information to what’s pictured and mentioned here, it’s been added by an extension, your theme, or custom code.

Beneath the table of email notifications, there are options you can use to set the **“From” name** and **“From” address** used for emails sent by WooCommerce. We recommend using an email address that uses your site’s domain to help ensure your emails are delivered. See more in our [email authentication documentation](https://woocommerce.com/document/email-authentication/#email-domains-should-match-your-website-domain).

Starting with **WooCommerce version 9.8**, email settings have been updated. These new settings are enabled by default for new stores. You can turn them on or off by going to: **WooCommerce > Settings > Advanced > Features**.

For version 9.8 and later, the Email Template settings let you customize:

- **Logo** – Add your store’s logo or header image
- **Logo width** – Set how wide your logo appears in emails (in pixels)
- **Header alignment** – Position your logo left, center, or right
- **Font family** – Choose the text font for your emails
- **Footer text** – Edit the text that appears at the bottom of your emails

For earlier WooCommerce versions or if you haven’t turned on the new email settings in your store, you can customize the following options in the Email template settings:

- Header image — Enter the URL of an image you want to show in the email header.
  - You can upload an image via **Media > Add New** **Media File** menu option.
  
- **Base color**— C*olor for WooCommerce email templates.*
- **Background color**— *Background color for WooCommerce email templates.*
- **Body** **background color —** *Body background color for WooCommerce email templates.*
- **Body** **text color**— *Body text color for WooCommerce email templates.*
- Footer Text — Enter text to include beneath the main body of your emails. Available Placeholders are:
  - {site_url} — The URL to your site as set in **Settings > General > Site Address (URL)**
  - {site_title} — The title of your site as set in **Settings > General > Site** **Title**
  
- **Footer Text Color —**You can now set the email footer text color. You can either enter the HEX code directly in the text field, or select the text field, which will open up the color picker.

From WooCommerce 9.8 onwards, the Color palette feature is enabled by default for new WooCommerce stores and can be enabled or disabled for all WooCommerce stores by going to: **WooCommerce > Settings > Advanced > Features**.

You can customize the color scheme of your store’s emails from here. Choose to either automatically sync with your store’s theme or manually set each color:

- **Sync with theme** – Match your email template colors with your store’s theme.
- **Accent color** – Used for buttons and links.
- **Email background** – The background color of the entire email.
- **Content background** – The background color of the main content area.
- **Heading & text** – The color of primary text and headings.
- **Secondary text** – Used for additional elements like footer content.

This last setting, the **Enable email insights** checkbox, tells your store to send you helpful emails based on how you are building your store. For example, you may receive an email noting a record sales day. Or that you’ve beat a previous record day. This is not an email list sign up, the emails are sent from the WooCommerce plugin on your store itself.

After you’ve made and saved your changes, you can select the “Click here to preview your email template” link at the top of the section to see how your emails will look.

From WooCommerce 9.8 onwards, the Email preview feature is enabled by default for new WooCommerce stores and can be enabled or disabled for all WooCommerce stores by going to: **WooCommerce > Settings > Advanced > Features**.

You can preview any of your store’s emails in the Email Preview section. Choose a template from the dropdown menu, then select either the desktop or mobile icon to see how it will appear on each device.

To test the email, use the **“Send a test email”** option to send a preview to any email address you choose.

From the **Email Notifications** list above, select **Manage** on the right side of the email you’d like to edit.

With **WooCommerce 9.8** onwards, if you have enabled the new email settings experience from **WooCommerce > Settings > Advanced > Features**, you will have access to view and update the following settings:

- **Enable/Disable** — Enable this email notification. (The Order Details email is sent manually and so can’t be disabled)
- **Recipient(s)** — Enter recipients (comma separated) for this email. Defaults to the site administrator email set in Settings > General. Only emails meant for shop managers and admins have this setting. (i.e., the New order, Cancelled order, and Failed order emails.)
- **Subject** — This controls the email subject line. Leave blank to use the default subject. Accepts placeholders.
- Email heading — This controls the main heading contained within the email notification. Leave blank to use the default heading. Accepts placeholders.
  - The Refunded Order and Order details emails have additional subject and email heading fields to accommodate different possible payment or refund statuses on orders.
  
- Additional content — Add text to appear below the main email content. Accepts Placeholders.
  - Available placeholders are:
    - {site_title} — The title of your site as set in Settings > General > Site Title
    - {site_address}, {site_url} — The web address to your site as set in Settings > General > Site Address (URL)
    - {order_date} — The date the order was placed
    - {order_number} — The order number for the relevant order.
    
  
- Email type — Choose which format of email to send. Options include:
  - Plain Text – A simplified version of the email without HTML formatting. Note: Text fields are limited to 155 characters. If your products have long names or multiple variations/add-ons, the content may be truncated.
  - HTML — A version with rich formatting for images, different fonts, and layouts.
  - Multipart — Sends both HTML and plain text versions of the content. The recipient’s email client will choose which version to display based on its capabilities and settings
  
- **Cc(s)** – Any email address you would like Cc’ed on the email you are editing
- **Bcc(s)** – Any email address you would like Bcc’ed on the email you are editing

From the email editing screen, you can also preview each template on desktop or mobile and send a test email to the address of your choice.

For WooCommerce versions **earlier than 9.8**, or if the updated email settings are not enabled:

On this screen, you can edit the following settings. Some emails have slightly different options.

- **Enable/Disable**— Enable this email notification. (The **Order Details** email is sent manually and so can’t be disabled)
- **Recipient(s) —** Enter recipients (comma separated) for this email. Defaults to the site administrator email set in **Settings > General**. Only emails meant for shop managers and admins have this setting. (i.e., the **New order**, **Cancelled order**, and **Failed order** emails.)
- **Subject**— This controls the email subject line. Leave blank to use the default subject. Accepts placeholders.
- Email heading — This controls the main heading contained within the email notification. Leave blank to use the default heading. Accepts placeholders.
  - The **Refunded Order** and **Order details** emails have additional subject and email heading fields to accommodate different possible payment or refund statuses on orders.
  
- **Additional content —** Add text to appear below the main email content. Accepts Placeholders.
- Available placeholders are:
  - {site_title} — The title of your site as set in **Settings > General > Site** **Title**
  - {site_address}, {site_url} — The web address to your site as set in **Settings > General > Site Address (URL)**
  - {order_date} — The date the order was placed
  - {order_number} — The order number for the relevant order.
  
- Email type — Choose which format of email to send. Options include:
  - *Plain Text*— A stripped-down version of the email without any HTML formatting.
  - HTML — A version with rich formatting for images, different fonts, and layouts.
  - Multipart — Sends both HTML and plain text versions of the content. The recipient’s email client will choose which version to display based on its capabilities and settings.
  

If using Plain Text emails, keep in mind that text fields are limited to 155 characters. If your products have long names and/or numerous variations/add-ons, the field may be truncated.

If you’re a developer or are comfortable editing PHP files, WooCommerce provides everything you need to make changes to email templates. At the bottom of the settings page for each email, there’s a note that tells you which PHP template is associated with that email. There’s also a button you can use to quickly copy the template file to your theme.

Every WooCommerce email is built from of a combination of templates. This allows you more control over customization. To find out more information on the template structure for WooCommerce emails, [see our template structure documentation](https://woocommerce.com/document/template-structure/).

We recommend keeping template customizations in a child theme, so changes don’t get overwritten when performing updates. More at: [How to set up and use a child theme](https://woocommerce.com/document/set-up-and-use-a-child-theme/).

For some more tips on editing customizing WooCommerce emails, see this [post on the WooCommerce blog](https://woocommerce.com/posts/how-to-customize-emails-in-woocommerce/#creating-custom-templates-with-code).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

