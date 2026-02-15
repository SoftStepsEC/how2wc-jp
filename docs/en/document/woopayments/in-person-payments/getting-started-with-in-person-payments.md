---
title: Getting started with In-Person Payments with WooPayments
url: https://woocommerce.com/document/woopayments/in-person-payments/getting-started-with-in-person-payments/
---

With**WooCommerce In-Person Payments**,your customers can pay for products and services in-person using the [M2 card reader](https://woocommerce.com/products/m2-card-reader/), [WisePad 3 card reader](https://woocommerce.com/products/wisepad3-card-reader/), or [Tap to Pay](https://woocommerce.com/document/woopayments/in-person-payments/getting-started-with-in-person-payments/#collecting-tap-to-pay) on a compatible iPhone or Android device.

Currently, **In-Person Payments** & **Tap to Pay for WooPayments** are available for the following countries and features:

You will need to meet the following requirements in order to collect payments in-person using WooPayments:

- A connection to the Internet via WiFi or cellular data.
- The latest version of **WooPayments**.
- A WooPayments account based in one of the following countries:
  - Canada
  - United Kingdom
  - United States
  
- A WooPayments account in good standing.
- The latest version of the Woo Mobile App.
- A device running iOS 15+ or Android 5+.
- The [Woo Mobile App](https://woocommerce.com/mobile/) is connected to your site.

Using [Tap to Pay on iPhone](https://woocommerce.com/document/woopayments/in-person-payments/tap-to-pay-iphone/) and [Tap to Pay on Android](https://woocommerce.com/document/woopayments/in-person-payments/tap-to-pay-android/) have specific requirements and processes for accepting payments. Please view the relevant page for your particular device.

In addition to the above requirements, the fees for accepting In-Person Payments are different than the fees for accepting online payments.

The fees for In-Person Payments are dependent on the country your business is located in. You can find more information on [our fees page](https://woocommerce.com/document/woopayments/fees-and-debits/fees/).

Allow your reader to fully charge before the first use. Both the [M2](https://woocommerce.com/products/m2-card-reader/) and the [WisePad 3](https://woocommerce.com/products/wisepad3-card-reader/) readers ship partially charged, but we recommend that you charge your reader fully before the first use.

To charge your reader, use the supplied cable to connect the USB-C on the reader to a USB charger. A full charge will take a few hours.

With a full charge, the reader should be able to process600 to 800 contactless transactionsbefore needing a recharge.

Your reader will need to be connected to your device using the WooCommerce Mobile App. You should not pair the card reader in your phone or tablet’s settings.

To connect your reader:

1. Navigateto **Menu** page.
2. Select**Payments**:

1. Tap **Continue setup** for In-Person Payments:

1. Tap the **Connect card reader**button:

1. Tap **OK** to allow the WooCommerce Mobile App to use your device’s Bluetooth capabilities to scan for your card reader.
2. Turn on your card reader by holding the power button for one second.

**NOTE:**Keep the card reader near the mobile device while the WooCommerce Mobile App completes the scanning process.

1. Tap **Connect to Reader** to begin the connection process.

1. Tap the **Allow While Using App** prompt when asked.

**NOTE:**Starting *Oct 13th, 2025* a new firmware update may require an additional pairing step. If applicable, you will see a 6-digit code on both the card reader and in the mobile app. If these numbers match, confirm on both devices that you wish to complete the pairing process.

That’s it: your reader is now connected and ready to accept payments!

When collecting a payment, In-Person Payments supports the following payment methods:

- **Cash**
- Card reader
  - You’ll also be given the option to use [Tap to Pay](https://woocommerce.com/document/woopayments/in-person-payments/getting-started-with-in-person-payments/#requirements-ttp) to collect the payment if you are using a supported device.
  
- Shareable payment link
  - This link can be shared with a customer and used to pay for the order online.
  
- Scan to Pay
  - This will generate a QR code that a customer can scan to pay for the order online.
  

Orders are eligible for In-Person Payments if **all** of the following are true:

- The order status is **pending**, **on hold**, **processing** or **failed**.
- The payment method is **cash on delivery**, **woocommerce_payments** or **none** (the payment assigned when an order is [created manually](https://woocommerce.com/document/getting-started-with-in-person-payments-woopayments/#section-7)).
- The Store’s address is set to an address in the USA, Canada, or UK.
- The currency is USD, CAD, or GBP.
- The order is **not** paid.
- The order is **not** refunded.
- The order does **not** include any subscription products.

With In-Person Payments, there are two ways of creating orders for payments:

1. [Build orders](https://woocommerce.com/document/woopayments/in-person-payments/getting-started-with-in-person-payments/#build-orders)
2. [Collect payments for an order placed online](https://woocommerce.com/document/woopayments/in-person-payments/getting-started-with-in-person-payments/#collect-order-payment)

Please note that when collecting payment for orders through In-Person Payments, it is **only possible to collect the full order amount**. If you would like to be able to charge for a partial order amount, consider splitting that order into separate smaller orders for each separate partial amount you would like to charge.

With In-Person Payments, you can build an order in the Woo Mobile App and collect payment immediately.

To build an order and collect payment:

1. Navigate to the **Orders** section of the Woo Mobile App.
2. Tap on the `+` icon in the top-right corner to create an order.
3. To add products to the order, you can either:
  - Scan product barcodes using your device’s camera.
    - If the barcode matches a SKU for a product available on your store, it will automatically be added to the order.
    
  - Select **Add Products**.
  
4. If you choose **Add Products**, select the product(s) you’d like to add to the order and tap the **# Product(s) Selected** button to add the product(s) to the order.
5. After the order is fully created, select the **Collect Payment** button to take payment.
6. Choose how to collect payment.

**NOTE:****For quick payments without inventory tracking, tap the **Add Custom Amount** button instead of selecting a product. This is perfect when you need to collect payments quickly—such as at trade shows, craft fairs, or for services.

With In-Person Payments, you can allow customers to place an order online using the [cash on delivery](https://woocommerce.com/document/cash-on-delivery/) payment method to then pay for the order in-person using a card or cash.

To collect a payment in-person after it is placed online:

1. Navigate to the **Orders** section of the Woo Mobile App.
2. Tap on the order being paid for.
  - Orders placed online with the **Pay in Person** payment method will have the `Processing` status.
  
3. Review the order details and tap on on the **Collect payment** option.
4. Choose how to collect payment.

An email receipt is sent automatically upon payment collection if a customer email address is set on the order. You can also send the email receipt manually after the payment.

**NOTE:**As an In-Person Payments merchant, you are *obligated* to provide your customers the option of a printed receipt for any payment.

If your mobile device has access to a WiFi Network (e.g. for curbside payments or point-of-sale type payments), you should be able to use any printer accessible via that WiFi network using AirPrint (iOS) or Mopria (Android).

Android users may need to install additional software (e.g., the [Brother Print Service Plugin](https://play.google.com/store/apps/details?id=com.brother.printservice&hl=en&gl=US)) depending on the printer.

WiFi Direct printers, like the[Brother RJ-4250WB-L](https://brothermobilesolutions.com/products/mobile-printers/ruggedjet-series/ruggedjet-4-series/brother-ruggedjet-rj4250wbl/), have their own internal WiFi access hotspot that a mobile device can connect to directly for printing receipts.

To print receipts using a WiFi direct printer:

1. Ensure your mobile device has access to cellular data.
2. Connect to the printer WiFi using your device’s WiFi settings.

You can then accept payments (over cellular data) and print receipts (over WiFi Direct). This can be especially useful for in-person delivery at a customer’s home.

**Note:** Receipts on iOS are generated and stored on the device whereas, on Android, the Woo Mobile app stores the receipt URLs locally in the app. Therefore, when using an iOS device, if a merchant collects payment on device A, the receipt will not be available on device B.

To collect payments from customers:

1. Navigate to the **Menu** tab in your WooCommerce Mobile App.
2. Tap on **Payments**,.
3. Tap on **Collect Payment**.
4. Enter in the amount to collect.
5. Complete optional steps if desired, such as:
  - Add a customer email.
  - Toggle taxation on/off.
  - Add a note to the order.
  
6. Tap on **Take Payment**.
7. Determine how to take the payment:
  - **Cash** allows you to accept cash for the order.
  - **Card Reader** allows the customer to insert, swipe, or tap their preferred payment method using the connected card reader.
  - **Tap to Pay** allows the customer to tap their preferred payment method using your compatible device.
  - **Share Payment Link** allows you to send a web link to the customer for them to pay online.
  - **Scan to Pay** displays a QR code that allows the customer to pay online.
  

Payment can also be made using [Tap to Pay on iPhone](https://woocommerce.com/document/woopayments/in-person-payments/tap-to-pay-iphone/) or [Tap to Pay on Android](https://woocommerce.com/document/woopayments/in-person-payments/tap-to-pay-android/). Please see those respective pages for our full instructions on taking payments via those methods.

If you offer local pickup or curbside pickup options, you’ll need to decide if you want to deliver to your customers, have them pick up their orders, or both.

You can specify [shipping zones](https://woocommerce.com/document/setting-up-shipping-zones/#shipping-zones) to determine what shipping methods customers may be eligible for. Shipping zones allow you to offer specific fulfillment options, like [Local Pickup](https://woocommerce.com/document/local-pickup/), to customers depending on where they are located in the world.

Payments collected using In-Person Payments appear in yourdashboardjustlike other payments processed via WooPayments. As a result, you can find them under**Payments**>**Transactions**.

If you’d like to view *just* In-Person Payments transactions, you can do so by:

1. Showing the **Advanced filters**.
2. Using the `Device type` filter to display payments made with either an `iPhone` or `Android` device.

You can use other filters if you’d like to get more granular reporting about your In-Person Payments transactions.

Like any Payment Method, customers using**In-Person Payments**should be aware of what data is shared about them and their transactions with others. Customers using**card-present payments**can expect to have the following personal data shared with our payments partners:

- Their location at the time and date of purchase.
- Their email address.
- Their name.
- An assigned customer ID if they had prior payments for this store.
- Their address and phone number.
- The quantity, price, and description of items in the order.

All data is used to support fraud detection during payment collection. You can find more details on provacy and our products [here](https://automattic.com/privacy/), and you can manage your store’s privacy policy in the**Settings**>**Privacy** section of your site’s administrator dashboard.

**NOTE**: You can read more about privacy and our products [here](https://automattic.com/privacy/).

If you want to power off the M2 or WisePad 3 to save battery life, hold down the power button for roughly four seconds.

Depending on the device, either the light will go off and stay off, or the LED will display a prompt `Power off?` — which you can confirm with the green enter button on the PIN pad.

You can refund your customers’ In-Person Payment just as you would any other WooPayments payment by following the refund flow on their order in the app or on your site via WP Admin.

If an order was paid with **Interac**, the refund must be initiated from the Woo Mobile App, and the original card used for the purchase must be presented.

To refund through the Woo Mobile App:

1. Navigate to the **Orders** section of your Woo Mobile App.
2. Select the order you’d like to refund.
3. Tap the **Issue Refund** option.
4. Adjust the quantity of the products you’d like to refund.
5. Select **Next**.
6. Enter a reason for the refund, if desired.
7. Tap the **Refund** button.
8. Select **Refund** again to confirm the refund.

No. In-Person Payments is not compatible with [test mode](https://woocommerce.com/document/woopayments/testing-and-troubleshooting/testing/#enabling-test-mode) or [sandbox mode](https://woocommerce.com/document/woopayments/testing-and-troubleshooting/sandbox-mode/).

Yes. Your mobile device needs to be connected to the Internet to collect payments.

If you are using cellular data to connect to the internet, please be sure**Cellular Data**is enabled for the**“Woo**” application in your device’s**Cellular** **Settings**.

In-Person Payments supports *most* credit and debit cards. It also supports payments using the following wallets:

- Apple Pay
- Google Pay
- Samsung Pay
- VISA payWave
- MasterCard PayPass
- AMEX ExpressPay
- Interac
- Discover D-PAS

Not at this time. Support for subscription products will be coming in a future release.

No, In-Person Payments will automatically capture the transaction regardless of whether Manual capture is enabled.

Yes, M2 and WisePad 3 card readers purchased from a different site work as expected with the Woo Mobile App.

Refer to the [WooPayments Card Reader Return Policy](https://woocommerce.com/document/woopayments/in-person-payments/card-reader-return-policy/) for more information.

Orders typically arrive within six business days, but orders placed after 21:00 UTC will ship the following business day.

If you are using [WooCommerce Shipping](https://woocommerce.com/products/shipping/) and an order is eligible for In-Person Payments and for a shipping label to be created, the [“Create Shipping Label” button](https://woocommerce.com/document/woocommerce-shipping/#creating-shipping-labels) will only display after payment has been collected and the order marked as paid.

If you see a message saying “Overdue requirements” in your mobile app under **Settings** (Gear Icon) > **In-Person Payments**, follow these steps.

Open your browser and go to **WP-admin > Payments > Settings**. Scroll down to the **“Transactions and payout”** section, and click the **“Manage in Stripe”** link.

This will take you to a temporary Stripe dashboard where you can review any outstanding requirements, such as updating your phone number or other business details. Stripe will highlight any missing information for you to address.

You can see what countries are presently supported for In-Person Payments [here](https://woocommerce.com/document/getting-started-with-in-person-payments-woopayments/#requirements). If you’re in a country where In-Person Payments is not supported at present, you can [register your interest](https://woocommerce.com/in-person-payments/#register-interest) so we can notify you when it is made available in your country in the future.

If you’re using the Jetpack plugin to connect the app to your site, make sure that the Jetpack connection is active and working correctly. You can verify some[known issues](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)or try[reconnecting your site](https://jetpack.com/support/reconnecting-reinstalling-jetpack/).

If you’re still having difficulty, please fill out our contact form to reach our support team from within the app by going to Menu > Settings > Help & Support > Contact Support.

