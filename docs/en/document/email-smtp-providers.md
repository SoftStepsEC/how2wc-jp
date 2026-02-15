---
title: Email and SMTP providers
url: https://woocommerce.com/document/email-smtp-providers/
---

This document aims to explain how email works, and also explains the role **Simple Mail Transfer Protocol** (SMTP) providers play in ensuring your WooCommerce store’s emails are delivered to your customers. Understanding how email works is a big part of keeping these emails running smoothly.

Related documents for additional reference:

- [Email troubleshooting](https://woocommerce.com/document/email-faq/)
- [Email authentication and sender requirements](https://woocommerce.com/document/email-authentication/)

Imagine sending an email as sending a letter through the network of a fast-moving postal service. It requires multiple steps:

- Something has to inspire you to write a letter.
- You write the letter.
- You choose how to mail it.
- You apply postage.
- You provide the letter to your preferred postal service.
- The postal service takes over from there.

Instead of going straight from your mailbox to your friend’s, the letter travels through various postal centers. Each center checks the details and delivery address before sending it on to the next facility. This process repeats until it finally reaches your friend.

Much like a letter, your email needs to be:

- Triggered
- Created
- Authenticated
- Passed to a mail server
- Sent

From there, like hopping from one post office to another, your email moves across different computers on the internet until it is received and verified by the receiving server. Once the receiving mail server ensures your email isn’t spam, your message gets delivered swiftly and accurately to the right inbox.

WordPress has a built-in [wp_mail()](http://codex.wordpress.org/Function_Reference/wp_mail) function to initiate email-sending processes. This core function of WordPress acts as a bridge and is **not** the actual email sender. WooCommerce and many other plugins utilize `wp_mail()` to send emails from your site.

No, neither WordPress nor WooCommerce *directly* sends your emails. Here’s what happens:

- After generating the email content, WooCommerce triggers the `wp_mail()` function.
- This function signals WordPress to process the email.
- However, since WordPress isn’t an email server, it delegates this task to PHP.
- PHP then locates a local email server on your web server to dispatch the email.

This means your email takes a three-step journey before it even leaves your web server.

To employ a dedicated SMTP service, you can use a specific plugin provided or a universal SMTP plugin that can connect to any provider. These tools adjust the `wp_mail()` function’s pathway, directing emails from PHP to your chosen SMTP provider. The SMTP service then queues and sends out your emails through its infrastructure.

Integrating a dedicated SMTP provider offers significant advantages for your store’s email communications. Here are three key benefits:

1. **Enhanced deliverability:** SMTP providers specialize in email delivery, helping to ensure your emails consistently reach your customers’ inboxes, bypassing common issues like being marked as spam.
2. **Scalability:** As your store grows, an SMTP provider can handle the increasing volume of emails without compromising speed or reliability. A local email server might struggle under heavy loads.
3. **Detailed analytics:** Many SMTP services provide valuable insights into your email performance, including delivery rates, open rates, and click-through rates. This data can help you refine your email strategies.

Adopting a dedicated SMTP service not only streamlines your email delivery process but also contributes to a more robust and efficient communication channel with your customers.

These are dedicated SMTP providers that work for most websites. Each has a plugin on WordPress.org, can be installed from your WordPress dashboard, and has support available to help you get started.

- MailPoet
  - [Send up to 5000 emails free per month](https://account.mailpoet.com/) (500 unique recipients limit).
  
- Mailjet
  - [Send 6,000 emails free per month](https://www.mailjet.com/pricing/).
  
- Brevo (formerly Sendinblue)
  - [Send 300 emails free per day (about 9,000 per month)](https://www.brevo.com/pricing/).
  
- ActiveCampaign Postmark
  - [Priced plans start at 10,000 emails a month](https://postmarkapp.com/pricing).
  
- WP Offload SES Lite
  - Send 62,000 emails free per month if your website is hosted on AWS or [pricing starts at $0.10 for every 1,000 emails](https://aws.amazon.com/ses/pricing/).
  

The team at MailPoet [wrote an article about SMTP and WordPress](https://www.mailpoet.com/blog/top-three-smtp-plugins-for-wordpress/), which you may find useful.

#### Can I use Gmail as my SMTP provider?

Yes, but the setup process is a bit complex, and you may run into sending limits.

Gmail will disable your account if you send emails to more than 500 unique recipients in 24 hours. This includes emails you send through the Gmail web interface and all emails your website is sending. [Learn more](https://support.google.com/mail/answer/22839?hl=en).

If you’re certain you’ll fall under these usage limits, there are free plugins available on WordPress.org that can help you get Gmail set up as your SMTP provider. There are also guides from other members of the WordPress community illustrating the process.

Understanding why some emails get lost and don’t reach your inbox or spam folder can be confusing. Learning how spam filters work can help you make sense of why they may stop some emails but not others.

#### Why do emails get blocked?

It’s challenging to pinpoint the exact reason for emails getting blocked without looking into server logs and email routes. However, here’s a simplified explanation:

- Spam filters don’t just look for obvious spam content; they evaluate several factors such as:
  - The IP address sending the email,
  - The sender’s details (including the domain and whether the email is authenticated)
  - The volume of emails sent from that IP or sender,
  - How often emails from that sender are marked as spam,
  - The specific wording and formatting of the emails.
  
- A key issue often lies in the email’s point of origin. This affects your “reputation” with spam filters.

Even small differences in how WooCommerce emails are composed or formatted can tip the scales, leading to them being flagged as spam and blocked. Not authenticating your site’s emails can also cause deliverability issues. [Learn more about email authentication](https://woocommerce.com/document/email-authentication/).

#### If emails are being blocked by spam filters, why is it not in my spam folder?

When emails bypass your inbox and don’t appear in your spam folder, it’s often because an external spam filter intercepts them before they reach your email client. The *final* spam filter your emails encounter is the one associated with the email client, which operates based on your settings and how you’ve previously interacted with similar emails. If an email is blocked by an earlier filter, it simply won’t be delivered, which bypasses your spam folder entirely.

Check and monitor the reputation of your website’s IP address for sending emails, if you have a dedicated server for sending emails. For both shared and virtual hosting environments, using a dedicated SMTP provider is advisable, as these environments are typically not optimal for sending emails. [Visit Sender Score to learn more](https://www.senderscore.org/).

