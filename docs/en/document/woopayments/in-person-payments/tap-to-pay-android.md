---
title: Tap to Pay on Android
url: https://woocommerce.com/document/woopayments/in-person-payments/tap-to-pay-android/
---

With Tap to Pay and the [Woo Mobile App](https://woocommerce.com/mobile/), merchants based in the United States, the United Kingdom, and Canada can **accept in-person contactless payments, right on their Android phone** — no extra terminals, hardware, or readers needed.

Tap to Pay on Android is supported **for U.S., UK, and Canadian merchants** whose Android device meets all of the following requirements:

- Contains a functioning NFC antenna and chipset.
- Device is not “rooted.”
- Device bootloader is locked and unchanged.
- Runs Android 11 or above.
- Uses Google Mobile Services.
- Has a hardware-backed keystore.
- Has stable connection to the internet.

As of now, **Interac cards are not supported** with the Tap to Pay on Android feature for transactions within **Canada**. Interac is a widely used payment processor specific to the Canadian market, and we understand the importance of this payment method for both merchants and customers alike. While this limitation is present, we’re committed to providing seamless and efficient payment solutions for all our merchants. As an alternative, we strongly encourage the use of the [WisePad 3 card reader](https://woocommerce.com/products/wisepad3-card-reader/) for accepting Interac card payments. The WisePad 3 offers a versatile solution for in-person transactions, ensuring you can cater to all your customers’ preferred payment methods without interruption.

Tap to Pay functionality in Canada and the UK includes region-specific limitations on contactless transactions:

1. Make sure you have [WooCommerce](https://woocommerce.com/start/#/) and [WooPayments](https://woocommerce.com/payments/) installed and activated on your store.
2. Download the WooCommerce Mobile App for Android .
  - If you already have the app installed, ensure that it has been updated to the latest version.
  
3. Follow the [instructions to register and/or log in](https://woocommerce.com/document/android/#connect-to-your-store).

1. When viewing the details of an unpaid order, tap on the `Collect Payment` button, then tap on `Card`.
2. You will be given the option to collect the payment using `Tap to Pay on Android` or a [Bluetooth Reader](https://woocommerce.com/document/woopayments/in-person-payments/quick-start-guide/).
3. After selecting `Tap to Pay on Android`, since this is the first time using the feature, the app will check that your device is ready to use Tap to Pay.

You can accept payments for existing orders via Tap to Pay on your Android phone, but you can also quickly create new orders.

**NOTE:** Tap to Pay on Android can only collect payment the country’s default currency — for example, UK merchants can only accept payments in GBP. If a customer [uses a different currency](https://woocommerce.com/document/woopayments/currencies/multi-currency-setup/#customer-default-currency), Tap to Pay on Android will not be available to collect payment.

Tap to Pay on Android can be used with orders created within the app or orders that were placed by customers on your site that have an [order status](https://woocommerce.com/document/managing-orders/order-statuses/) of *Pending Payment*.

To collect the payment for an order:

1. Navigate to the **Orders** tab.
2. Tap on the order you’d like to collect payment for.
3. Tap on the `Collect Payment` button.
4. Tap on `Card`.
5. Select the `Tap to Pay on Android` option.
6. The built-in reader will prepare to take the payment and then display the payment screen.
7. The card or phone used as the payment method can be tapped on the area indicated.
8. The app will process the payment.

**Note: this feature has been deprecated in app version 18.2.** Please use order creation for full order features.

Tap to Pay on Android can also be used to collect **Simple Payments** for a quick transaction.

1. Navigate to the **Menu** tab.
2. Click on the `Payments` option under the **General** heading.
3. Select `Collect Payment`.
4. Enter the amount to collect.
  - Optional: Add the customer’s email and/or a note about the transaction.
  
5. Toggle the tax collection on or off, as needed.
6. Select the `Take Payment` button.
7. Select the `Tap to Pay on Android` option.

