---
title: Troubleshooting image upload issues in the Woo Mobile App
url: https://woocommerce.com/document/troubleshooting-image-upload-issues-in-the-woo-mobile-apps/
---

Here are some error messages you may encounter in the Woo Mobile App when attempting to upload product images or downloadable files.

This usually means that the file(s) you want to upload exceeds the limit imposed by the server. The simplest test to check for this problem is modifying the image to make it smaller (i.e., <1MB), saving it in a web-friendly format such as .jpg or .png, and trying the upload again.

There are **two ways** to fix this issue:

A particular image file may not upload because its dimension is too large. To fix this, adjust the size of your image to make it smaller using an image editor or online tool. Learn more about the [ideal image size for WooCommerce](https://woocommerce.com/document/adding-product-images-and-galleries/#what-is-the-ideal-image-size-to-use-with-woocommerce).

There are two ways to increase the maximum (max) file size of your site.

- Contact your host directly and ask them to increase the file size limit for you.
- If you are comfortable making technical updates to your site, access your main WordPress folder via FTP and look for the `php.ini` file. Open it and **add the lines of text below** before saving. (If you cannot locate `php.ini`, you can create a new one, paste the necessary text into it, and upload it to your main WordPress folder.)

```
upload_max_filesize = 128M
post_max_size = 128M
max_execution_time = 300
```

This will increase your site’s maximum upload limit and allow you to upload your images.

**Note**: Some****[WordPress hosts](https://woocommerce.com/hosting-solutions/)****may restrict your ability to increase the upload size limit manually. If your attempt was unsuccessful, you will need to contact your host to request a limit change.

MultipurposeInternetMailExtensions (MIME) types are used by browsers and other internet devices to determine the type of content associated with a page. For instance, if you have a .png file and a .jpeg file on the page, the browser would know by their MIME types to treat both files asimagesrather than videos or other file types.

WooCommerce allows for the same file extensions defined by WordPress. You can see the full list via[WordPress Codex: Uploading Files](https://codex.wordpress.org/Uploading_Files). If you cannot upload a specific file via the app, it could be because the MIME-type is not supported. To work around a problem with a file type that was not allowed, you can try opening the file in the original app used to create it, and then export it into a web-friendly format such as .jpg or .png. If you downloaded it from the web, note that .webp images are not supported, and you should try tapping the image and viewing it in a new browser window before downloading. If those things don’t help, you can report this issue by contacting our support team at mobile-support@woocommerce.com and include the device details, how the image was created, whether the image was edited prior to upload, and, if possible, a copy of a sample file that is failing to upload.

If you upload a file that exceeds the maximum file upload limit, it will fail and produce an error. The maximum file upload limit can vary from 2 MB to 150 MB, and depends on the site’s hosting package.

**How to check the maximum upload file size**

To check the maximum upload file size, click Media > Add New Media File from your WordPress dashboard. The maximum upload file size is shown at the bottom of the upload window, as shown in the screenshot.

To increase the maximum upload file size, please check the section on how to Increase max file size.

The file size you are trying to upload might exceed the maximum memory limit configured for the site. You can either try to upload an image with a smaller size or increase the WordPress memory limit for the store. To increase the WordPress memory limit, please check out [this document](https://woocommerce.com/document/increasing-the-wordpress-memory-limit/).

Your storage capacity is the amount of disk space available when uploading various files and images to your website. It’s similar to the disk space on your desktop computer but is located on WordPress.com’s servers instead of inside your computer.

If you’re using WordPress.com to host your site, navigate to **My Site** (or My Sites if you have more than one) and select **Media** from the left sidebar. This will display your storage limit and the amount you have already used.

Your standard free WordPress.com account comes with 3GB of storage space. If you need additional storage space, [upgrade your account to a paid plan](https://wordpress.com/pricing/). Alternatively, you can delete images or videos to make space, but please know that deleting media files that are linked to either your own site or other sites will cause broken links in any content that previously pointed to those files.

This means the app is unable to find the path of the file that needs to be uploaded. It may help if you try to move or re-save the image to a new location on your device and try again.

The file the app is trying to access cannot be found on the device. It may help if you try to move or re-save the image to a new location on your device and try again.

The app does not have sufficient permission to read the file.

The three issues above issues are caused by using external file managers when selecting an image from the device. If you face any of the above issues, please fill out our contact form to reach our support team from within the app by going to My Store > Settings icon > Help & Support. It may help if you try to move or re-save the image to a new location on your device and try again.

Timeout or connection issues can happen when the internet connection on the device is unstable. Here are some steps you can take to figure out where the issue lies:

- You can try to upload images using a different connection. WiFi is recommended.
- If the internet connection is stable, please head to `https://YOURSITE.com/wp-admin/upload.php` (change `YOURSITE` to your site’s URL) using your mobile device’s browser, and try uploading the image. If the image upload works from the web but not the app, please reach out to our support team.
- Your site may be experiencing site performance issues. We’d suggest checking if you have any security plugins, and contacting your hosting provider, then searching server logs for any blocked requests from our servers. [This document goes into more detail](https://woocommerce.com/document/android-ios-apps-troubleshooting-error-fetching-orders/#section-3).

**Note:** The WooCommerce Mobile App only supports access for shop owners, administrators, and shop managers.

If you’re using the Jetpack plugin to connect the mobile app to your site, ensure that the Jetpack connection is active and functioning correctly. [Review common issues](https://jetpack.com/support/getting-started-with-jetpack/known-issues/) or [reconnect your site](https://jetpack.com/support/reconnecting-reinstalling-jetpack/).

If you’re still having difficulty, contact support from within the app by going to *Menu > Settings > Help & Support > Contact Support*.

