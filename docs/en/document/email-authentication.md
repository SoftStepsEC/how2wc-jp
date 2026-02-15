---
title: Email authentication and sender requirements
url: https://woocommerce.com/document/email-authentication/
---

This document explains what email authentication is, its requirements, and how you can implement it to ensure your store’s emails are successfully delivered.

In this digital age, where online transactions and communications are central to our lives, the integrity of email correspondence is more important than ever. Authenticating outbound emails from your WooCommerce store verifies to your customers that a message actually came from you, or was sent on your behalf from an authorized third-party

Ensuring the authenticity and trustworthiness of your email communications is not just a best practice — it’s a **necessity**. As cyber threats evolve and phishing attempts become more sophisticated, the importance of verifying your identity as an email sender helps protect the email ecosystem and is crucial for maintaining customer trust — a key part of safeguarding your business operations.

Related documents for additional reference:

- [Email troubleshooting](https://woocommerce.com/document/email-faq/)
- [How email works, SMTP providers](https://woocommerce.com/document/email-smtp-providers/)

Email authentication confirms that you, the sender, are who you say you are. Receiving mailboxes check this authentication to ensure emails are genuine and trustworthy. Some public domain email providers (e.g. Gmail, Yahoo) have implemented [authentication requirements](https://woocommerce.com/document/email-authentication/#email-authentication-and-delivery-requirements), and will not deliver your emails to their addresses if those requirements are not met.

Senders can implement strong email authentication by using industry standards such as SPF, DKIM, and DMARC.

SPF records allow a sender to specify the IP addresses (or authorized mail servers) that are allowed to send mail from a specific domain. Service providers can then reject emails sent from an IP address that doesn’t match the SPF records for the email’s domain — like scamming and phishing emails.

A DKIM record adds a digital signature to emails that your organization sends. Recipient email servers then perform a check to see if the signature from the email matches the DKIM record in your domain name system (DNS) settings. A matching signature indicates that the email content hasn’t been modified and is from a legitimate sender.

DMARC allows a sender to indicate that their messages are protected by DKIM and/or SPF. It tells a receiver what to do if neither of those authentication methods passes.

Emails sent by your site that are marked as “from” public domain providers, like `@gmail.com` or `@yahoo.com` will (very) likely be marked as spam. This includes both marketing and order notification emails. Every email marketing platform will have a slightly different process.

We recommend starting with the following actions:

1. Review your WooCommerce email settings at **WooCommerce > Settings > Email** and settings of any plugins that you use to ensure that they send as your branded domain (e.g., me@mybrand.com) and not as your `@gmail.com` or `@yahoo.com` address.
2. If your host delivers your store’s emails (most common), review your host’s documentation about authentication or confirm with customer support that your store’s emails are authenticated with SPF, DKIM, and DMARC. Each host will have a specific process, and they will help you ensure compliance.
3. If you use plugins like WP Mail SMTP or MailPoet to deliver your store’s emails, you will need to follow their recommendations on how to authenticate your branded domain.
4. Check authentication by sending a test email from your store to a service like [mail-tester.com](https://www.mail-tester.com/) to ensure that the authentication is valid. Placing a test order in your store is a good way to do this. Your test results should look like the image below.

Effective February 1, 2024, Google and Yahoo introduced new email sender requirements. This change may prevent your emails from reaching customers, so compliance with the new requirements should be considered mandatory — and all types of emails, whether transactional or marketing, must comply.

This is meant to protect recipients from spam by making it easier for Google and Yahoo to identify fraudulent emails.

Even if you send only transactional emails, it’s important to authenticate your domain to ensure that your email campaigns still reach your audience. As the email industry trends toward requiring authentication for all senders, providers other than Google and Yahoo are likely to follow.

Those who send 5,000 or more messages a day to Gmail accounts will have additional requirements, which are detailed in the next section.

[According to Google](https://support.google.com/a/answer/81126), all senders who send emails to Gmail accounts, and all domains and consumer email brands hosted by Yahoo Mail, **must** meet the following requirements:

- Remove Gmail from your store’s “From:” address.
- Set up SPF or DKIM email authentication for your domain.
- Maintain spam rates below 0.10%.
- Avoid reaching a spam rate of 0.30% or higher.
- Make sure that sending domains or IP addresses have valid forward and reverse DNS records (also known as PTR records).
- Use a Transport Layer Security (TLS) connection for transmitting email.
- Format messages according to the Internet Message Format standard.

Senders of 5,000 or more messages per day to Gmail accounts have the following requirements:

- Both SPF and DKIM are required for larger senders. DMARC email authentication confirms both protocols for your sending domain.
- Marketing messages and subscribed messages must support a one-click unsubscribe and include a visible unsubscribe link in the message body.

Senders of 5,000 or more messages a day to Gmail accounts must implement one-click unsubscribe for marketing emails. If you have been or are planning to send emails to residents of the European Union, this builds on the [GDPR’s unsubscribe requirement](https://gdpr.eu/email-encryption/#:~:text=Essentially%20this%20means%20that%20an,to%20unsubscribe%20in%20every%20communication.), which states that unsubscribe options must be provided in every marketing communication.

The one-click mechanism is intended for machines, rather than humans, to trigger. For instance, Gmail allows users to unsubscribe from marketing emails directly from their inboxes. This functionality became a requirement on February 1st, 2024

Merchants should:

- **Use email addresses associated with their store’s domain**, rather than public domain addresses like `@gmail.com` or `@yahoo.com`.
- Additionally, you must ensure your email setups are configured with proper authentication protocols (the SPF, DKIM, and DMARC protocols described above) to improve email deliverability and comply with the new requirements. This will **help prevent your store emails from being marked as spam** and ensure vital communication with customers remains uninterrupted.

