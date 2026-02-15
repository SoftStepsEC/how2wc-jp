---
title: How to Login into the App
url: https://woocommerce.com/document/android-ios-apps-login-help-faq/
---

After [downloading](https://woocommerce.com/mobile/) and installing the app from your preferred app store and opening the app, click on the Log In button:

If you can visit your site on a browser, you already have the site address. You can get it from the address bar (the place where you enter your store name in your browser app).

This is the same address your customers will access to view your store on the web.

Type or copy that address and enter it in the app.

You can follow the following steps if you are facing an error after entering your WooCommerce store address and tapping the “Continue” button.

- Make sure that you have a working internet connection. You can try opening the WooCommerce store address from your mobile device’s web **browser** to verify that you have a working internet connection.
- Your site needs to be up and running for the app to be able to access it. Sites under maintenance mode, or not yet launched, and sites exhibiting errors won’t work in the app.
- If you can open your store address in the web browser and you are still facing an error message on this screen, you can contact our support team by going to “Help > Contact support” in the app.

The WooCommerce app needs to be able to communicate with your website in order to establish a connection and sign in. To do so, when you enter your site URL in the Woo app, it makes a request to this endpoint: [https://public-api.wordpress.com/rest/v1.1/connect/site-info/?url=https://example.com](https://public-api.wordpress.com/rest/v1.1/connect/site-info/?url=https://example.com)

The detection works by trying each of the following tests:

- **XML-RPC Test** – The WordPress servers try to call the `demo.sayHello` method on **/xmlrpc.php** and expects a “Hello!” response.
- **Fallback Check** – If XML-RPC fails, it checks **/wp-admin/index.php** to see if “[wordpress.org](http://wordpress.org/)” appears in the page source.

If both of these tests fail, the app will assume that the site is not a WordPress site and cannot be connected.

To resolve this issue, please ensure that the [Jetpack IP addresses](https://jetpack.com/support/how-to-add-jetpack-ips-allowlist/) are whitelisted in order to communicate with your site. They may be blocked through your hosting provider, or a CDN service such as Cloudflare.

[Find different options for starting your new store](https://woocommerce.com/hosting-solutions/).

There are two ways to log into the Woo Mobile app to manage your store:

- Using your WordPress.com account to connected via Jetpack.
- Using the site credentials flow and your WP-Admin username and password.

Let’s talk about each option separately below.

**Note:**Logging into the app via the Jetpack flow will give you more features like the ability to access multiple stores without logging out of the app, push notifications for new orders and reviews, Site visitor statistics and access to create Blaze campaigns.

The WooCommerce Mobile App needs to create a connection to your website. This is important for WooCommerce stores as orders, and sales data are sent to your mobile devices. If you’re using the [Jetpack plugin](https://jetpack.com/support/getting-started-with-jetpack/) on your site or if you are using a WooCommerce Extension that uses the **Jetpack Connection Package**, the WooCommerce app will ask you to log in using the WordPress.com account that’s associated with Jetpack. You can also optionally [sign in with store credentials](https://woocommerce.com/document/android-ios-apps-login-help-faq/#enter-store-credentials).

You can find more details in our [What is a WordPress.com Account?](https://woocommerce.com/document/what-is-a-wordpress-com-account/) guide.

#### Extensions Using Jetpack Connection

The following extensions include the Jetpack Connection Package:

- [Google for WooCommerce](https://woocommerce.com/products/google-listings-and-ads/)
- [Jetpack Backup](https://wordpress.org/plugins/jetpack-backup/)
- [Jetpack Boost](https://wordpress.org/plugins/jetpack-boost/)
- [Jetpack Protect](https://wordpress.org/plugins/jetpack-protect/)
- [Jetpack Search](https://wordpress.org/plugins/jetpack-search/)
- [Jetpack Social](https://wordpress.org/plugins/jetpack-social/)
- [Jetpack VideoPress](https://wordpress.org/plugins/jetpack-videopress/)
- [WooPayments](https://woocommerce.com/products/woopayments/)
- [WooCommerce Shipping](https://woocommerce.com/products/shipping/)

There are two ways to find your WordPress.com email:

**For self-hosted sites**: You can find the account in the **Jetpack section -> Dashboard -> Account connection**.

**For WordPress.com sites:** Please check the **https://wordpress.com/me** page for your account email details.

If you have a WooCommerce.com account and are already logged into WordPress.com, please follow the steps mentioned [here](https://woocommerce.com/document/log-into-woocommerce-com-with-wordpress-com/#section-2) to connect your WordPress.com account to WooCommerce.com.

#### I don’t remember my WordPress.com password

If you don’t remember your WordPress.com password, we recommend you log in using the magic link login option by tapping on the “Or log in with magic link” (iOS) / ”Log in with magic link” (Android) button at the bottom of the screen.

You will receive an email to your WordPress.com registered email address. You can tap on the link from the email to log in to the WooCommerce app.

Alternatively, you can tap on the “Reset your password” button to begin the password reset process. You can find more information about our password reset process in our [Account Recovery](https://wordpress.com/support/account-recovery/#password-reset-process) support guide.

#### I requested a login link by email, but I can’t find the email. Why?

Please make sure you are checking the correct email address, as shown in the app. An email might also take a few minutes before it arrives. If you are using a Gmail address, please look for the magic link email in the **Updates** folder as well as in the **Spam** folder.

#### To which email address is the login link sent?

The login link is emailed to the address that is used for your WordPress.com account.

If you prefer to use the WooCommerce app without installing the Jetpack plugin, or if you prefer to sign in using this method, you can use the same credentials you use to sign in to **WP-Admin** to sign in to the mobile app as well.

**Please Note:** If you are using the Jetpack plugin, or any of the plugins that use the Jetpack Connection, you will be prompted to sign in with your WordPress.com account. You can sign in by selecting S*ign in with store credentials* when prompted to log in, and then follow the instructions as outlined below.

To connect using your store credentials:

1. Launch the app and tap “Login”
2. Enter your store address and tap “Continue”
3. If the app does not detect an active Jetpack connection, you’ll be asked to log in using your store credentials.

Store credentials are the **username** and **password** you use to log into your WooCommerce store on the Web. If you forget your credentials, the guide below has various suggestions on how to regain your access:

[https://wordpress.org/support/article/resetting-your-password/](https://wordpress.org/support/article/resetting-your-password/)

The WooCommerce app needs access to your site’s WordPress login page—which it normally expects `/wp-login.php`— in order to authenticate using your site’s WP Admin username and password.

First, please make sure you can log in with the same username and password at the default WordPress login page by appending `/wp-login.php` to your site address. Some hosting companies provide their customers with credentials to access their stores through their control panel but not through the default WordPress login page.

If you can’t log in via `wp-login.php`, please contact your host for assistance.

An application password is a token (a series of characters) generated by a WordPress site that allows a third-party system or app to communicate with it securely via WordPress API without exposing your site credentials. For a WooCommerce store without Jetpack connected, the Woo Mobile app requests an application password from your site to stay connected and sync your data.

If you see this error, a security plugin or a configuration on your site may be blocking the application password feature. You can deactivate the security plugin on your site and try logging in to the app again. If you still need help, please contact your host for assistance.

Once the app authenticates your account, it has a process to verify your user role since it only allows an **Administrator** or **Shop Manager** to manage the store in the app.

If you see this error, here are some troubleshooting steps:

1. Make sure your user role is either Administrator or Shop Manager on WP Admin -> Users -> Profile.
2. If you use any security plugin that may block access to WordPress API, please deactivate it and try again.
3. Try creating another account with the default Administrator or Shop Manager role if you use a plugin to edit your user role or capabilities.

If you fail to log in to the app due to a custom configuration of the WP Admin or login page, the app will prompt you with an alternative to retry with the web browser in the app. Examples of non-standard WP Admin or login pages would be the following:

- Captcha or verification added to the login page.
- Customized or edited login page.
- Customized or edited WP Admin page.

This login flow may also be shown if the password entered is incorrect.

To successfully sign in, you will need to go through two other steps to log into your WP-Admin page and authorize the app to access it:

If you are still unable to log in on the web view, please consider reverting to the default WP Admin or login page temporarily and try again. While the app does its best to account for customized sites, some plugins and configurations are incompatible with the Woo Mobile app. Some users will get a 404 error after trying to authorize access. In these cases, you would need to contact your host for assistance.

This issue can happen when an application password is generated for the WooCommerce Mobile App, but the process is disrupted due to an unexpected error. When you log in to the app again, your site returns this error to the app because the application name must be unique.

To resolve this issue, please go to WP Admin -> Users -> Profile, scroll down to the Application Password section, and click the “Revoke” button on the application name that looks like one of these:

- `com.woocommerce.android.app`
- `com.automattic.woocommerce.ios`

In general, these are the common causes of login issues with store credentials:

1. Custom WP Admin or WP Login page
2. The application password feature is disabled
3. WordPress API is disabled
4. Security plugins or settings that blocked the app from authenticating your account programmatically

If you use any security plugin that does any of those mentioned above, it is worth deactivating it temporarily then checking if you can log in via the app. You may also want to contact your host to confirm if the restrictions do not come from any server settings.

Alternatively, you may want to try connecting to the app using the Jetpack plugin. If you connect to the app with Jetpack, you can see visitor stats in the app, receive push notifications for orders, and manage multiple sites with only one login using your WordPress.com account. If you choose to go that route, you can follow the instructions in the guide below to set up Jetpack:

[https://woocommerce.com/document/jetpack-setup-instructions-for-the-woocommerce-mobile-app](https://woocommerce.com/document/jetpack-setup-instructions-for-the-woocommerce-mobile-app)

Once the Jetpack plugin is installed and connected to a WordPress.com account, after entering your site address to connect to the WooCommerce Mobile App, you’ll be asked to log in using the same WordPress.com account that was used to connect Jetpack.

Make sure that you can access the store from the desktop using the WordPress.com account email that you used to log in to the WooCommerce Mobile App.

#### For a self-hosted site

If your site already has the WooCommerce and Jetpack plugin installed, please ensure that you have connected your WordPress.com account with the Jetpack plugin.

Please follow the following steps to check and connect Jetpack to your WordPress.com account:

1. Access your store’s wp-admin page from a desktop. If you have the right “Role”, you can access the “wp-admin” page by entering the following URL in your desktop browser. [yourstore.com]/wp-admin/
2. Navigate to the Jetpack’s Dashboard page. You can find the Jetpack menu by checking the top left corner.
3. Scroll down to the “Connections” section and check the “Account Connection”. It will look like the following if you haven’t connected your WordPress.com account.
4. Tap on the “*Connect your WordPress.com account*” link and follow the instructions.

Once you have your WordPress.com account connected and authorized, you can log in to the app again, and you should be able to select your store.

It could be one of two reasons.

- Only WordPress.com stores and self-hosted sites with WooCommerce and Jetpack plugins installed are displayed in the list of available options.
- WooCommerce 3.5 or higher is required to be installed and activated on the site you’re trying to connect to. If a store does not meet this requirement, an “**Update to WooCommerce Required**” message will display. We always recommend running the latest version of WooCommerce.

Jetpack is a WordPress plugin that enables a connection from your self-hosted site to a WordPress.com account and provides a common authentication interface across disparate server configurations and architectures. In the WooCommerce Mobile app, the Jetpack plugin is required to access the following features:

- Push notifications for new orders, reviews, etc.
- Site visitor statistics.
- The ability to manage multiple stores from within the app.
- The ability to create Blaze Campaigns

You can still connect your WooCommerce store to the WooCommerce Mobile app without Jetpack. Please refer to the [Enter Store Credentials](https://woocommerce.com/document/android-ios-apps-login-help-faq/#section-8) section for more details.

If you’re having trouble with your site’s jetpack connection, check the Jetpack documentation for how to [fix Jetpack connection issues](https://jetpack.com/support/getting-started-with-jetpack/fixing-jetpack-connection-issues/), including [specific error messages](https://jetpack.com/support/getting-started-with-jetpack/troubleshoot-jetpack-connection-error-messages/) that may occur when connecting your site to your WordPress.com account.

You can also get in touch with [Jetpack support](https://jetpackme.wordpress.com/contact-support/?rel=support) for assistance.

**For self-hosted sites**

Please make sure that you can access the store using your WordPress.com account. You can do this by accessing your site’s `wp-admin` from your desktop browser.

To connect your WordPress.com account with your site’s Jetpack, you can follow the steps [here](https://jetpack.com/support/getting-started-with-jetpack/).

**For WordPress.com site**

For WordPress.com-hosted sites, the Jetpack connection will be done automatically. Please make sure that you can access the store using your WordPress.com account. You can do this by accessing your site’s `wp-admin` from your desktop browser. If you still face an error message on this screen, you can contact our support team by going to “Help > Contact support” in the app.

You can check the Jetpack connection status of the invited users from the `Users` page of `wp-admin`.

If the invited user has a Jetpack connection established, you will see the green Jetpack logo at the end of the row. Please refer to the part highlighted using a red circle in the following screenshot.

If they do not already have their account connected to a WordPress.com account through Jetpack, you can refer to Jetpack’s [Additional Users guide](https://jetpack.com/support/transfer-your-jetpack-connection-or-plan-to-another-user/additional-users/).

You need to have the WooCommerce plugin installed on your WordPress site to turn it into a WooCommerce store.

#### From mobile app

The following instructions will help you to install the WooCommerce plugin on your site from the mobile app.

##### iOS

1. Start by tapping on the “Install WooCommerce” button from the error screen.
2. You will be taken to the “WooCommerce Setup” screen. If asked to do so, kindly login using your WordPress.com account.
3. Once you reach the WooCommerce plugin page, tap the “Install and Activate” button to start the installation process.
4. Wait for the installation and activation to finish. After the mobile app verifies the WooCommerce installation, you will be automatically navigated inside the mobile app.
5. If you face issues during the installation process, you can contact our support team by going to “Help > Contact support” in the app.

#### From desktop browser

Please follow the following steps to install WooCommerce plugin on your site.

1. Access your store’s wp-admin page from a desktop. If you have the right “Role”, you can access the “wp-admin” page by entering the following URL in your desktop browser. [yourstore.com]/wp-admin/
2. From the menu on the left side, select “Plugins -> Add New”.
3. Search for “WooCommerce” and click on “Install Now” to start the installation.
4. Once installation finishes tap “Activate” and follow the instructions to set up your store.

If you’re using the Jetpack plugin to connect the app to your site, make sure that the Jetpack connection is active and working correctly. You can verify some[known issues](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)or try[reconnecting your site](https://jetpack.com/support/reconnecting-reinstalling-jetpack/).

If you’re still having difficulty, please fill out our contact form to reach our support team from within the app by going to Menu > Settings > Help & Support > Contact Support.

