---
title: Tap to Pay on iPhone
url: https://woocommerce.com/document/woopayments/in-person-payments/tap-to-pay-iphone/
---

With Tap to Pay and the [Woo Mobile App](https://woocommerce.com/mobile/), merchants based in the United States and the United Kingdom can **accept in-person contactless payments, right on their iPhone** — no extra terminals, hardware, or readers needed.

Tap to Pay on iPhone is supported **for U.S. and UK merchants** whose iPhone meets all of the following requirements:

- iPhone XS or newer.
- iOS 16.7 or later.
- The NFC (near field communication) chip must not be disabled.
- The device must be signed in to an iCloud account.
- The device must have a passcode set.

**NOTE:** UK merchants require version 15.9 or above of the Woo Mobile App.

In the United Kingdom, Tap to Pay is limited to **£100 per transaction**. For payments **over £100**, the ability to complete the transaction depends on the type of card being used and how it verifies PINs:

Most UK-issued cards still rely on **Offline PIN**, which means they cannot be used for transactions above the £100 limit with Tap to Pay, as there is no hardware to insert the card and verify the chip.

Use the [WisePad 3 card reader](https://woocommerce.com/products/wisepad3-card-reader/) for transactions requiring Offline PIN verification.

1. Make sure you have [WooCommerce](https://woocommerce.com/start/#/) and [WooPayments](https://woocommerce.com/payments/) installed and activated on your store.
2. Download the WooCommerce Mobile App for iOS .
  - If you already have the app installed, ensure it has been updated to the latest version.
  
3. Follow the [instructions to register and/or log in](https://woocommerce.com/document/woocommerce-ios/).

1. When viewing the details of an unpaid order, tap on the `Collect Payment` button, then tap on `Card`.
2. You will be given the option to collect the payment using `Tap to Pay on iPhone` or a [Bluetooth Reader](https://woocommerce.com/document/woopayments/in-person-payments/quick-start-guide/).
3. After selecting `Tap to Pay on iPhone` since this is the first time using the feature, the app will check that your device is ready to use Tap to Pay on iPhone and display a prompt to accept the terms and conditions.
4. You will have the option to continue with your device’s Apple ID or another Apple ID.
  - Your Apple ID will be associated with a merchant account through Apple for merchant account management, fraud prevention, and compliance purposes.
  - You can unlink your Apple ID from a merchant account by [contacting Apple Support](https://support.apple.com/contact) or following the instructions sent by email after setup.
  

You can accept payments for existing orders via Tap to Pay on your iPhone, but you can also quickly create new orders.

**NOTE:** Tap to Pay on iPhone can only collect payment in the country’s default currency — for example, UK merchants can only accept payments in GBP. If a customer [uses a different currency](https://woocommerce.com/document/woopayments/currencies/multi-currency-setup/#customer-default-currency), Tap to Pay on iPhone will not be available to collect payment.

Tap to Pay on iPhone can be used with orders created within the app or orders that were placed by customers on your site that have an [order status](https://woocommerce.com/document/managing-orders/order-statuses) of *Pending Payment*.

To collect the payment for an order:

1. Navigate to the **Orders** tab.
2. Tap on the order for which you’d like to collect payment.
3. Tap on the `Collect Payment` button.
4. Select the `Tap to Pay on iPhone` option.
5. The built-in reader will prepare to take the payment and then display the payment screen.
6. The card or phone used as the payment method can be tapped on the area indicated.
7. The app will process the payment.

NOTE: Tap to Pay will adjust your inventory if the payment is associated with a specific product or products.

**Note: this feature has been deprecated in app version 18.2.** Please use order creation for full order features.

Tap to Pay on iPhone can also be used to collect **Simple Payments** for a quick transaction.

1. Navigate to the **Menu** tab.
2. Click on the `Payments` option under the **General** heading.
3. Select `Collect Payment`.
4. Enter the amount to collect.
  - Optional: Add the customer’s email and/or a note about the transaction.
  
5. Toggle the tax collection on or off, as needed.
6. Select the `Take Payment` button.
7. Select the `Tap to Pay on iPhone` option.

**NOTE:** This method of payment collection *will not* adjust your inventory.

If you’re using the Jetpack plugin to connect the app to your site, make sure that the Jetpack connection is active and working correctly. You can verify some[known issues](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)or try[reconnecting your site](https://jetpack.com/support/reconnecting-reinstalling-jetpack/).

If you’re still having difficulty, please fill out our contact form to reach our support team from within the app by going to Menu > Settings > Help & Support > Contact Support.

