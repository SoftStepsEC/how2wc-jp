---
title: Creating Shipping Labels in the Mobile Apps
url: https://woocommerce.com/document/creating-shipping-labels-in-the-mobile-apps/
---

The WooCommerce mobile apps support purchasing and printing shipping labels for stores with [WooCommerce Shipping & Tax](https://woocommerce.com/document/woocommerce-shipping-and-tax) or [WooCommerce Shipping](https://woocommerce.com/products/shipping/) extension installed. This guide provides step-by-step instructions to purchase and print shipping labels directly from mobile devices.

For help with installing the WooCommerce Shipping & Tax extension for your store, please visit the [installation guide](https://woocommerce.com/document/woocommerce-shipping-and-tax/#section-2).

1. To get started, go to the **Orders** tab > select an order to fulfill > select **Create Shipping Label**. If you cannot find the button, visit the [Troubleshooting section](https://woocommerce.com/document/creating-shipping-labels-in-the-mobile-apps/#troubleshooting) for more information.

2. Confirm **Ship from** with the address of your store. If your shipping is international, a phone number will be required.

3. Update **Ship to** with the destination address for the shipment. Tap **Done** to verify the address.

If the address cannot be verified, double-check that the entered address is correct, or contact the customer to verify. You can proceed with the address by tapping **Use Address as Entered** at the bottom of the screen.

4. Select **Package Details** to update packaging and weights for your packages. Move items to different packages if needed, and select packaging for each of them:

You can also add new custom packaging or select from a list of boxes and envelopes provided by carriers by selecting **Package Selected** > **Create new package**.

5. If your shipping is international, confirm or update information for **Customs**:

6. Select **Carriers and Rates** for your packages, and whether a signature is required:

7. Confirm **Payment Method** or add a new credit card. You can also choose whether to receive emails for the label purchase receipts by toggling the switch at the bottom.

8. Review information for your purchase and choose whether you want to mark the order as complete and notify the customer by toggling the switch at the bottom. Proceed by tapping the **Purchase Label** button.

When the purchase is complete, you’ll be navigated to the **Print Shipping Labels** screen. You can either choose to print the label or save it for later.

On iOS, the print feature is handled with AirPrint. For more information on how to print from iPhone and iPad, please visit [Apple’s user guide](https://support.apple.com/en-sg/guide/iphone/iph92628b8f/ios).

For more information on how to print from your Android device, please check [Google’s support page](https://support.google.com/android/answer/10177839).

If your label comes with a separate customs form, after printing the label, you’ll be navigated to another screen to print the form:

You can also find the purchased label in the details of your order. Here you can review details for each label, reprint it, or request a refund if needed. If your label comes with a separate customs form, you can also select to print it here.

The “Create shipping label” button will show if the following is true:

- Your store is in the United States (including Puerto Rico, Virgin Islands, and other U.S. territories)
- Your store currency is US Dollars
- At least one product in the order “needs shipping” according to WooCommerce (typically means a non-virtual product)

You may encounter this error when editing origin and destination addresses for shipping labels. This means that we were unable to verify the address with USPS – it may have been entered incorrectly, or isn’t considered “deliverable” by the post office.

Use the [USPS zip code lookup tool](https://tools.usps.com/go/ZipLookupAction) to verify the address. If it’s not recognized, we recommend reaching out to your customer.

If the tool recognizes the address there may be an issue with WooCommerce Shipping. Please [open a ticket](https://woocommerce.com/my-account/create-a-ticket/?ticket-area%3Dwoocommerce-extensions%26ticket-product%3Dwoocommerce-services-extension) with the relevant address information so we can look into it.

Several things can prevent shipping rates from being calculated, the most common reason is the size and weight of your package. So please make sure that the selected package and input weight of the package is correct.

There can also be problems with the USPS API service. Most issues can be diagnosed by looking at the Debug Log at WooCommerce > Status > WooCommerce Shipping & Tax.

For other issues, visit [WooCommerce Shipping Troubleshooting](https://woocommerce.com/document/woocommerce-shipping-and-tax/woocommerce-shipping/#section-11) and [Frequently Asked Questions](https://woocommerce.com/document/woocommerce-shipping-and-tax/woocommerce-shipping/#section-20).

If you’re using the Jetpack plugin to connect the app to your site, make sure that the Jetpack connection is active and working correctly. You can verify some[known issues](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)or try[reconnecting your site](https://jetpack.com/support/reconnecting-reinstalling-jetpack/).

If you’re still having difficulty, please fill out our contact form to reach our support team from within the app by going to Menu > Settings > Help & Support > Contact Support.

