---
title: How timezones work in the Woo Mobile app
url: https://woocommerce.com/document/how-timezones-work-in-the-woo-mobile-app/
---

The Woo Mobile App uses the timezone set in your site’s WP Admin dashboard under **Settings > General > Timezone**.

If this information is not available, the mobile app will default to the timezone of the device being used; this applies to all **statistics** and **order-related** information.

For example, let’s say your store is set to the **New York City** timezone, where it’s August 2. However, if you have traveled to Japan, your phone will be in the **Tokyo** timezone, where it’s already August 3.

If someone places an order on your site, you will receive a push notification on August 3 (Tokyo time). However, if you check your site’s analytics, you won’t see any sales recorded for August 3. This is because, according to your store’s timezone, the sale was made on August 2. This behavior is **expected** and designed to maintain consistency.

If you’re using the Jetpack plugin to connect the mobile app to your site, ensure that the Jetpack connection is active and functioning correctly. [Review common issues](https://jetpack.com/support/getting-started-with-jetpack/known-issues/) or [reconnect your site](https://jetpack.com/support/reconnecting-reinstalling-jetpack/).

If you’re still having difficulty, contact support from within the app by going to *Menu > Settings > Help & Support > Contact Support*.

