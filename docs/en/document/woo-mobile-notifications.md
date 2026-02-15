---
title: Woo Mobile App notifications
url: https://woocommerce.com/document/woo-mobile-notifications/
---

With push notifications in the Woo Mobile App, you can manage your online store more efficiently and make timely decisions that keep your business running smoothly and your customers happy.

These notifications are sent directly to your mobile device, enabling you to promptly process and fulfill orders, respond to customer feedback, reduce delays, and prevent potential errors. They also serve as a record of sales, helping you manage inventory and accurately track revenue.

Follow these steps to set up notifications for the Woo Mobile App. If you’re having trouble receiving mobile app notifications, follow these same steps to troubleshoot.

1. [Enable store notifications](https://woocommerce.com/document/woo-mobile-notifications/#enable-store-notifications)
2. [Connect your store to Jetpack](https://woocommerce.com/document/woo-mobile-notifications/#connect-to-jetpack)
3. [Enable notifications on your mobile device](https://woocommerce.com/document/woo-mobile-notifications/#enable-notifications-on-your-mobile-device)
4. [Check the app logs](https://woocommerce.com/document/woo-mobile-notifications/#check-the-app-logs)
5. [Check Android Settings](https://woocommerce.com/document/woo-mobile-notifications/#section-6)

First, ensure [store notifications via email](https://woocommerce.com/document/configuring-woocommerce-settings/emails/#email-notifications) are set up correctly in your site’s WP Admin dashboard. If you encounter issues, review our [email troubleshooting guide](https://woocommerce.com/document/email-faq/).

Next, ensure your site is [connected to Jetpack](https://jetpack.com/support/getting-started-with-jetpack/). Although a Jetpack connection is [required to use the mobile app](https://woocommercehalo.wordpress.com/faq/), you do not need to subscribe to a Jetpack paid plan.

If you encounter issues, try [reconnecting your site](https://jetpack.com/support/reconnecting-reinstalling-jetpack/) or reviewing [known issues](https://jetpack.com/support/getting-started-with-jetpack/known-issues/) with conflicting plugins and extensions.

#### On Android

In the Settings app, navigate to *Notifications > App Notifications > WooCommerce*. (This location may change depending on the Android device you are using.) Ensure that the **All WooCommerce notifications** option is toggled on.

#### On iOS

In the Settings app, navigate to *Notifications > WooCommerce* and toggle the **Allow Notifications** option.

Look for the following information:

#### On Android

```
> Refreshing FCM token
> FCM token retrieved
> Sending FCM token to our remote services
```

#### On iOS

```
2021/10/26 11:57:48:617 am  📱 Registering for Remote Notifications...
2021/10/26 11:57:48:706 am  📱 Device Token Received: [32762876ghgwsyt87613g3169287648723y44784]
2021/10/26 11:57:49:190 am  📱 Successfully registered Device ID 43793459 for Push Notifications
```

If you’re still having issues with push notifications, you can run a [plugin and theme conflict test](https://woocommerce.com/document/how-to-test-for-conflicts/) to find the cause of the problem.

Android devices use additional battery and power-saving features to help extend the battery performance on your device. These features may limit the devices ability to receive notifications, including those from the Woo Mobile app. You can disable these settings following the instructions below. You can also [learn more about notification troubleshooting from Android Police here](https://www.androidpolice.com/android-notification-problems-fixes/).

#### Battery Saver or Power Saving mode

1. Open your phone’s **Settings**menu.
2. Scroll down and select **Battery**.
3. Select **Battery Saver**.
4. Turn off the **Use** **Battery Saver**toggle switch.

#### Adaptive Battery mode

1. Open your phone’s **Settings**menu.
2. Scroll down and select **Battery**.
3. Select **Adaptive preferences**.
4. Turn off the **Adaptive Battery**toggle switch.

If you’re using the Jetpack plugin to connect the mobile app to your site, ensure that the Jetpack connection is active and functioning correctly. [Review common issues](https://jetpack.com/support/getting-started-with-jetpack/known-issues/) or [reconnect your site](https://jetpack.com/support/reconnecting-reinstalling-jetpack/).

If you’re still having difficulty, contact support from within the app by going to *Menu > Settings > Help & Support > Contact Support*.

