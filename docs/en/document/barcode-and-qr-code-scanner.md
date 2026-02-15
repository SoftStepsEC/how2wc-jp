---
title: Barcode and QR code scanner
url: https://woocommerce.com/document/barcode-and-qr-code-scanner/
---

**Looking to use a physical scanner in Point of Sale (POS) mode?** [Check out our documentation here.](https://woocommerce.com/document/point-of-sale-mode-barcode-scanning/)

The WooCommerce Mobile App supports the most widely used barcode formats on both Android and iOS platforms.

This powerful tool streamlines your workflow by allowing you to [create new orders](https://woocommerce.com/document/creating-orders-on-the-mobile-app/#section-3) directly from the **Orders** screen. Add products to orders during the order creation process, and quickly locate products from the products screen.

**Note:**The mobile app’s barcode scanner now works with codes added to either the **SKU** field or the **GTIN, UPC, EAN, and ISBN** field, in a product’s **Inventory** tab. The **GTIN, UPC, EAN, and ISBN** field is newer, and a better choice for all stores, especially if you use standard retail barcodes. If you use the new field, SKU can be used for a human-readable identifier instead.

Barcodes can be set for both products and variations. For barcode format which use a check digit and/or a country code, such as GTIN, UPC, EAN, and ISBN, please include those in the barcode you set.

You can add barcodes for both products and variations by typing them manually or scanning them within the app.

You can set barcodes using the **Products** tab, in the *Inventory* section. For variations, you can open each variation’s *Inventory* section individually.

Android devices use [ML Kit](https://developers.google.com/ml-kit/vision/barcode-scanning/android) to recognize and decode barcodes.

- QR code
- Aztec Code
- Data Matrix
- PDF417
- UPC-A
- UPC-E
- EAN-8
- EAN-13
- Code 39
- Code 93
- Code 128
- Interleaved 2 of 5 (ITF)
- Codabar

- 1D barcodes containing a single character.
- Barcodes in ITF format with fewer than six characters.
- Barcodes encoded with FNC2, FNC3, or FNC4.
- QR codes generated in Extended Channel Interpretation (ECI) mode.

iOS devices use the [Vision framework](https://developer.apple.com/documentation/vision/) to recognize and decode barcodes.

- Aztec
- Codabar
- Code 39
- Code 39 with Checksum
- Code 39 Full ASCII
- Code 39 Full ASCII with Checksum
- Code 93
- Code 93i
- Code 128
- Data Matrix
- EAN-8
- EAN-13
- GS1 DataBar
- GS1 DataBar Expanded
- GS1 DataBar Limited
- Interleaved 2 of 5 (I2of5)
- Interleaved 2 of 5 (I2of5) with Checksum
- ITF-14
- MicroPDF417
- MicroQR
- Modified Plessey (MSI Plessey)
- PDF417
- QR
- UPC-E

Unfortunately, Apple’s official documentation does not provide specific information about unsupported barcode types.

If you’re using the Jetpack plugin to connect the mobile app to your site, ensure that the Jetpack connection is active and functioning correctly. [Review common issues](https://jetpack.com/support/getting-started-with-jetpack/known-issues/) or [reconnect your site](https://jetpack.com/support/reconnecting-reinstalling-jetpack/).

If you’re still having difficulty, contact support from within the app by going to *Menu > Settings > Help & Support > Contact Support*.

