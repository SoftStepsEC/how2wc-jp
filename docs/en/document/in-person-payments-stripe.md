---
title: Getting started with In-Person Payments with Stripe
url: https://woocommerce.com/document/in-person-payments-stripe/
---

With the Stripe WooCommerce Extension, your customers can pay for products and services in-person using the [M2](https://stripe.com/gb/terminal/m2) (in the US) and [WisePad3](https://stripe.com/gb/terminal/wisepad3) card reader (in the UK). Alternatively, you can get started with no additional hardware using Tap to Pay on iPhone, or Tap to Pay on Android.

In-Person Payments via Stripe is available to qualified merchants using iPhone, iPad, or Android devices for non-subscription-based products.

You will need to meet the following requirements in order to collect payments in-person using the Stripe WooCommerce Extension:

- Connection to the Internet via WiFi or cellular data.
- The latest version of the Stripe WooCommerce Extension active on your WooCommerce site.
- A U.S. or U.K. Stripe account in good standing.
- The latest version of the Woo Mobile App.
- A device running iOS 14+ or Android 5+.

If you’d like to collect In-Person Payments using **Tap to Pay**, you also need to meet these additional requirements:

- iPhone XS or newer that:
  - Is running iOS 16+
  - Is signed in to an iCloud account
  - Has a passcode set
  - Does not have the [NFC](https://developer.apple.com/design/human-interface-guidelines/nfc) chip disabled
  
- Android device that
  - Contains a functioning NFC antenna and chipset.
  - Is not “rooted.”
  - The device bootloader is locked and unchanged.
  - Runs Android 11 or above.
  - Uses Google Mobile Services.
  - Has a hardware-backed keystore.
  - Has stable connection to the internet
  

Allow your reader to fully charge before the first use. The reader ships partially charged, but we recommend that you charge your reader fully before the first use.

To charge your reader, use the supplied cable to connect the USB-C on the reader to a USB charger. A full charge will take a few hours.

With a full charge, the reader should be able to process600 to 800 contactless transactionsbefore needing a recharge.

Your reader will need to be connected to your device using the Woo Mobile App. You should not pair the card reader in your phone or tablet’s settings.

To connect your card reader:

1. Navigateto **Menu** page.
2. Select**Payments**:

1. Tap **Continue setup** for In-Person Payments:

1. Tap the **Connect card reader**button:

1. Tap **OK** to allow the Woo Mobile App to use your device’s Bluetooth capabilities to scan for your card reader.
2. Turn on your card reader by holding the power button for one second.

**NOTE:**Keep the card reader near the mobile device while the Woo Mobile App completes the scanning process.

1. Tap **Connect to Reader** to begin the connection process.

1. Tap the **Allow While Using App** prompt when asked.

That’s it: your reader is now connected and ready to accept payments!

When collecting a payment, In-Person Payments supports the following payment methods:

- **Cash**
- Card reader
  - You’ll also be given the option to use [Tap to Pay](https://woocommerce.com/document/in-person-payments-stripe/#collecting-payment-ttp) to collect the payment if you are using a supported device.
  
- Shareable payment link
  - This link can be shared with a customer and used to pay for the order online.
  
- Scan to Pay
  - This will generate a QR code that a customer can scan to pay for the order online.
  

After selecting **Tap to Pay on iPhone** for the first time, the Woo Mobile App will:

- Check that your device is ready to use Tap to Pay on iPhone
- Display a prompt to accept the terms and conditions.
- Ask you tocontinue with your device’s Apple ID or another Apple ID.

**NOTE:**The Apple ID you use will be associated with a merchant account for merchant account management and fraud prevention and compliance purposes through Apple. You can unlink your Apple ID from a merchant account by contacting Apple Support

If selecting **Tap to Pay on iPhone** after it is set up:

- The Woo Mobile App will display the payment screen.
- The customer can tap their preferred payment method on the area indicated on your device.
- The app will process the payment.
- You will be prompted to print or email a receipt.

With In-Person Payments, there are two ways of creating orders to collect payments:

1. [Build orders](https://woocommerce.com/document/in-person-payments-stripe/#build-orders)
2. [Collect payments for an order placed online](https://woocommerce.com/document/in-person-payments-stripe/#collect-order-payment)

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
  - Orders placed online with a **Cash on Delivery** payment method will have the `Processing` status.
  
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

If you offer local pickup or curbside pickup options, you’ll need to decide if you want to deliver to your customers, have them pick up their orders, or both.

You can specify [shipping zones](https://woocommerce.com/document/setting-up-shipping-zones/#shipping-zones) to determine what shipping methods customers may be eligible for. Shipping zones allow you to offer specific fulfillment options, like [Local Pickup](https://woocommerce.com/document/local-pickup/), to customers depending on where they are located in the world.

Like any Payment Method, customers using**In-Person Payments**should be aware of what data is shared about them and their transactions with others. Customers using**card-present payments**can expect to have the following personal data shared with [our partners at Stripe](https://woocommerce.com/document/woopayments/account-management/partnership-with-stripe/):

- Their location at the time and date of purchase.
- Their email address.
- Their name.
- AStripe assigned customer ID if they had prior payments for this store.
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
3. Select the **Issue Refund** option.
4. Adjust the quantity of the products you’d like to refund.
5. Select **Next**.
6. Enter a reason for the refund, if desired.
7. Tap the **Refund** button.
8. Select **Refund** again to confirm the refund.

No, In-Person Payments is not compatible with[test mode](https://woocommerce.com/document/stripe/customer-experience/testing/).

Yes, your mobile device needs to be connected to the Internet to collect payments.

If you are using cellular data to connect to the internet, please be sure**Cellular Data**is enabled for the**“Woo**” application in your device’s**Cellular** **Settings**.

In-Person Payments supports *most* credit and debit cards. It also supports payments using the following wallets:

- Apple Wallet
- Google Wallet
- Samsung Pay
- VISA payWave
- MasterCard PayPass
- AMEX ExpressPay
- Interac
- Discover D-PAS

Not at this time. Support for subscription products will be coming in a future release.

If you’re using the Jetpack plugin to connect the app to your site, make sure that the Jetpack connection is active and working correctly. You can verify some[known issues](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)or try[reconnecting your site](https://jetpack.com/support/reconnecting-reinstalling-jetpack/).

If you’re still having difficulty, please fill out our contact form to reach our support team from within the app by going to Menu > Settings > Help & Support > Contact Support.

