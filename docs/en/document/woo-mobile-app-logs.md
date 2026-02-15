---
title: Woo Mobile App logs
url: https://woocommerce.com/document/woo-mobile-app-logs/
---

The Woo Mobile App logs record various errors and events and can help you troubleshoot common issues. Here’s a breakdown of what the messages mean and what actions you can take.

#### “[StripeTerminal] …”

These errors come from the Stripe Terminal SDK. They can help diagnose problems with connecting to card readers or processing payments.

#### “[CardPresentPaymentsOnboarding] …”

The app couldn’t fetch site settings, plugins, payment accounts, or the store’s base location. Check your Internet and Jetpack connections to fix this.

#### “Failed to submit email receipt for order: (ORDERNUMBER). Email is not configured”

The Mail app on your device isn’t set up. Configure the Mail app to send receipts.

#### “Failed to collect payment: (REASON)”

This happens when a card is declined. Ask the buyer to use another card. Learn more about [Stripe’s decline codes](https://stripe.com/docs/declines).

#### “Unexpected error when checking for reader update”

The app couldn’t connect to Stripe’s update servers. Retry updating the reader with a stable Internet connection.

#### “Error synchronizing known reader”

The app couldn’t fetch the last connected reader ID. You can still proceed, but you’ll need to confirm the reader manually.

#### “Unexpected error when disconnecting reader”

If this happens in **Settings > In-Person Payments > Manage Card Reader**, try force-quitting the app. Reset the reader by holding its power button for 5 seconds, then reconnect.

#### “Unexpectedly unable to downcast to CardReaderSettingsConnectedViewModel” or “Unexpectedly unable to downcast to CardReaderSettingsSearchingViewModel”

This is rare and you may still be able to process payments. Please report it to our support team if you encounter this error.

Logs related to In-Person Payments on Android have these prefixes:

- “StripeTerminal”: Stripe Terminal SDK errors about reader communication or Stripe backend issues.
- “WooCommerce-CARD_READER”: Logs about UI flows or setup wizards.
- “WordPress-API” and “Volley”: Logs about backend communication.

#### “E/StripeTerminal: Update failed due to low battery on the reader”

Charge the card reader, then retry the update.

#### “E/WooCommerce-CARD_READER: Connecting to reader failed”

The app found the reader but couldn’t connect. Ensure your Internet and Jetpack connections are working.

#### “Scanning failed: [Reason]”

Restart the reader and retry scanning. Ensure the reader is powered on and not connected to another device.

#### “Location settings activity not found”

Location services are disabled in your device settings. Enable location services manually.

#### “Failed to collect payment: (REASON)”

This usually happens if the card is declined and the customer needs to try a different card. [Learn more](https://stripe.com/docs/declines).

#### “Disconnection from reader has failed”

Turn off Bluetooth in your device settings. If the issue persists, force quit the app, reset the reader by holding its power button for 5 seconds, and then reconnect.

#### “WordPress-API …”

The app couldn’t fetch site settings, plugins, payment accounts, or connection tokens. Ensure your Internet and Jetpack connections are active.

Use this guide to identify and resolve issues quickly. If problems persist, contact our support team for help.

**Something missing from this documentation? Still have questions and need assistance?**

- If you have a question about a specific extension or theme you’d like to purchase, [contact us](https://woocommerce.com/contact-us/#sales-form) to get answers.
- If you already purchased this product and need some assistance, get in touch with a Happiness Engineer via our [support page](https://woocommerce.com/my-account/create-a-ticket/) and select this product’s name from the Product dropdown.

