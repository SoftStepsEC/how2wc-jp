---
title: Troubleshoot receipt issues
url: https://woocommerce.com/document/mobile-receipts/troubleshoot-receipt-issues/
---

This page is a handy guide for helping to troubleshoot some of the more common issues you may encounter when trying to generate a receipt for customers through the Woo Mobile app.

If a receipt fails to generate, check if your device is offline, as this might prevent access to the receipt. Tap the “See receipt” link on the order details screen to retry printing or resend the receipt to the customer. **Please note** that clearing the app’s cache or reinstalling the app will remove receipts from your device.

You can also reprint the receipt from Stripe’s dashboard.

Ensure the mobile app device is connected to the same WiFi network as the printer, and verify that the printer is powered on. For Bluetooth printers, confirm that the printer is paired with the mobile app device and actively connected.

If you are using a portable printer with WiFi Direct support (e.g., [Brother RJ-4250WB-L](https://brothermobilesolutions.com/products/mobile-printers/ruggedjet-series/ruggedjet-4-series/brother-ruggedjet-rj4250wbl/)), ensure the mobile device has access to cellular data, then connect to the printer’s WiFi through the device’s WiFi settings. More details are available [here](https://woocommerce.com/document/getting-started-with-in-person-payments-woopayments/#portable-wifi-printer).

Additional software may be required to enable mobile device printing for other printers. If you are not using the Brother RJ-4250WB-L, contact your printer vendor for assistance.

If you can select the printer on the receipt preview screen but nothing happens after initiating the print action, try restarting the printer. If an error message appears, take note of it and contact the printer vendor for support.

For Brother RJ-4250WB-L, make sure you have selected the correct paper size (4”x39”) in the receipt preview screen.

### Does the app log show the error if the receipt fails to generate or print?

**Android:** Printing errors are managed by the Android operating system. In most cases, the system logs will contain relevant information, but these logs will not include any prefixes like “WooCommerce” or “StripeTerminal.” The only event the app might log is the RECEIPT_PRINT_FAILED tracking event.

**iOS:** The app will log an error if there is no data to generate a receipt. However, it will not log or display errors if the receipt fails to print, as the printing process is beyond the app’s control.

