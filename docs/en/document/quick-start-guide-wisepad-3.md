---
title: WooCommerce In-Person Payments: WisePad 3 Quick Start Guide
url: https://woocommerce.com/document/quick-start-guide-wisepad-3/
---

The WisePad 3 is supported for merchants in the UK and Canada.

- 1x WisePad 3 card reader
- 1x USB-C charging cable
- Quick start guide

This device supports iOS & Android.

1. Make sure you have [WooCommerce](https://woocommerce.com/start/?nuxentrysource=docs_text_cta) and [WooPayments](https://woocommerce.com/products/woocommerce-payments/) installed and activated on your WooCommerce store.
2. Download the [WooCommerce Mobile App](https://woocommerce.com/mobile/) for [iOS](https://apps.apple.com/us/app/id1389130815) or [Android](https://play.google.com/store/apps/details?id=com.woocommerce.android). If you already have the app installed, be sure it has been updated to the latest version.
3. Follow the [iOS](https://woocommerce.com/document/woocommerce-ios/) or [Android](https://woocommerce.com/document/android/) app instructions to register and/or login.

Charge the card reader using the supplied charging cable for approximately 2-3 hours. Charging before the first use helps to prevent potential damage to it. A battery-level indicator icon will appear at the top-left of the device screen to help track the level of the charge.

**Note:** With typical usage, you should charge the reader once a day. A fully charged reader can run ~600-800 transactions on a single charge.

After charging, turn on the device by briefly pressing the power button located at the top right of the PIN pad on the reader. The display powers on and shows the device’s splash screen. The display dims after a few seconds of inactivity. If inactive and disconnected from your application for more than 5 minutes, it will beep and power off. You can turn off the WisePad 3 manually by pressing and holding the power button until the LED display shows a “Power off?” prompt, then press the green enter button to confirm.

**Before you start:**Do not pair the card reader in your device’s Bluetooth settings. The WooCommerce Mobile App will manage the connection automatically.

Make sure Bluetooth is enabled on your device. Open the WooCommerce Mobile App. Navigate to **Settings (Gear Icon) > In-Person Payments > Manage Card Reader.**

Click on Connect Card Reader. If prompted, allow the app to see your location while using the app.

Select the card reader when prompted (it will show the card reader’s serial number) on your smartphone/tablet. Then, pair your device with the WisePad 3 with Pairing PIN. And now your WisePad 3 card reader is connected. In order to accept payments, ensure that “test mode” is disabled for your WooPayments account. The reader will stay connected to your iOS or Android device while in standby and automatically exits standby mode when you resume activity. You can turn off the WisePad 3 manually by pressing and holding the power button until the LED display shows a “Power off?” prompt, then press the green enter button to confirm.

**NOTE:**Starting *Oct 13th, 2025* a new firmware update may require an additional pairing step. If applicable, you will see a 6-digit code on both the card reader and in the mobile app. If these numbers match, confirm on both devices that you wish to complete the pairing process.

**Note:**If you would like to use the card reader for collecting payment in person for orders placed online, such as for curbside or local pickup, you will need to make some changes in your store WP Admin settings by following the instructions in [our documentation](https://woocommerce.com/document/getting-started-with-in-person-payments-with-woocommerce-payments/#section-2). This includes setting up a local pickup zone, enabling cash on delivery, and making sure your products are set to this zone.

To collect a payment for an order placed online by your customer(s) for local pickup, navigate to that order in your WooCommerce Mobile App and click on Collect Payment to finish the transaction. Then tap or insert the credit card to accept the payment. For PIN-based payments, insert the card and complete using the WisePad 3 PIN pad.

If you need to take a quick payment on the go, use the Order Creation feature. Navigate to the Orders tab in the mobile app, click on the ‘+’ sign, and create the order. Then use the card reader to collect payment.

NFC (Near Field Communication) is a feature that enables short-range communication between compatible devices. In the case of In-Person Payments, it’s the communication between a customer’s NFC-enabled bank card and the card reader.

When payment is made via this method, success or failure is signaled via audible beep(s). All 4 LED lights will show as green on the reader when reading the card information. When the card read is successful, they will be accompanied by 1 beep. If there are 2 beeps, there has been an error and you should retry.

Be sure your WooCommerce Mobile App has been updated to the latest version, WooCommerce and WooPayments are up-to-date, and that you are logged in to the mobile app.

**Note:**The “Manage Your Card Reader” options are visible only when:

- The order status is pending, on hold, or processing.
- The payment method is cash on delivery, woocommerce_payments, or none.
- The Store’s address is set to an address in the Canada, or UK.
- The currency is CAD or GBP.
- The order is not paid.
- The order is not refunded.
- Order does not have any subscription products.

- Reboot the reader by pressing the power button once to turn off and again to turn on.
- If the problem persists, force quit the WooCommerce Mobile App and open it again, or reboot your device and reader.
- Confirm the reader is charged and not connected to another device.
- Ensure that the reader was not previously paired directly via the device’s Bluetooth settings. Go to the Bluetooth settings in any previously paired devices and select “Forget device”.
- Confirm the reader is in-range of the WooCommerce Mobile App (usually 10-20 ft).

- Turn the card reader off and then switch it back on again. The card reader should automatically reconnect with your smartphone or tablet if you have completed the initial setup.
- The battery level may be too low. Use the USB cable to recharge the reader then retry.
- Check that the device or smartphone/tablet is within WiFi reception range.
- Check that your WooPayments account is set up and connected in your WooPayments extension settings under WooCommerce > Settings > Payments.
- (Insert Card) Check that the chip of the card is facing the right direction when inserting into the reader.
- (Tap Card) Check if the card supports the right payment method (ex. tap function should have the right symbol on the card).The card should be placed within a 1.5inch/4cm range on top of the tap marking and not inside a wallet.

- Press the power on button to turn on the reader again. The reader will automatically connect with your smartphone or tablet again.
- The battery level may be too low. Use the USB cable to recharge it, then retry.
- Check that the smartphone/tablet is within a few feet of the card reader.

For additional troubleshooting support, refer to the [Getting started with In-Person Payments with WooPayments](https://woocommerce.com/document/getting-started-with-in-person-payments-with-woocommerce-payments/) or [Accepting In-Person Payments with the Stripe WooCommerce Extension](https://woocommerce.com/document/stripe/admin-experience/in-person-payments/) guides.

If you’re using the Jetpack plugin to connect the app to your site, make sure that the Jetpack connection is active and working correctly. You can verify some[known issues](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)or try[reconnecting your site](https://jetpack.com/support/reconnecting-reinstalling-jetpack/).

If you’re still having difficulty, please fill out our contact form to reach our support team from within the app by going to Menu > Settings > Help & Support > Contact Support.

