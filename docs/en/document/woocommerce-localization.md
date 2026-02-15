---
title: Translating WooCommerce
url: https://woocommerce.com/document/woocommerce-localization/
---

WooCommerce is already translated into a few languages and is translation-ready out of the box. All that is needed is a translation file for your language, which is automatically [installed for the languages on this list](https://translate.wordpress.org/projects/wp-plugins/woocommerce/) by changing the site’s language.

On this page you’ll learn:

- How to set up WordPress in your language.
- How to contribute translations to your WooCommerce language.
- How to manually download translations from translate.wordpress.org
- How to create custom translations for WooCommerce
- How to translate text without localization

The first step to translating WooCommerce is to ensure your site is set to the language you want it translated into. WordPress needs to be told what the default language is and can be done by following these steps:

1. From the WordPress Admin dashboard go to**Settings > General**.
2. Change the **Site Language** setting to the preferred language.
3. Scroll down to click **Save changes** (this immediately changes the navigation menu language as well).
4. Go to to **Dashboard > Updates**.
5. Scroll to the bottom and click **Update Translations**.

The shop now displays in your locale if the language file exists. If it does not, you need to create the language files as per the process explained below.

## Contributing your Localization to Core

We maintain translations at [our project on GlotPress](https://translate.wordpress.org/). If you want to contribute translated strings to your language or wish to start a new translation, register an account at WordPress.org and start translating.

WooCommerce Translation is managed by teams in the [WooCommerce Translation Project](https://translate.wordpress.org/projects/wp-plugins/woocommerce). **Stable** versions and development versions of WooCommerce are translated there and anyone can contribute.

WordPress looks for an at least **90% complete Stable translation** in your language when installing or updating WooCommerce, and then automatically downloads it. If there is a **Stable**translation, but it’s not at least 90% complete, you can download it manually. We encourage you to contribute to the particular language to get it to above 90% so that all users can benefit.

If you’re new to translating, [check out the translators handbook to get started.](https://make.wordpress.org/polyglots/handbook/tools/glotpress-translate-wordpress-org/)

Follow the steps below to manually download translations from the :

1. Go to the **WooCommerce Translations Project** and find your language in the list.
2. Click the title to enter the language’s sub-section.

1. Click the heading in the **Set/Sub Project** column to view and download a **Stable (latest release)** version.

1. Scroll to the bottom of that page for export options. Export as a **Machine Object Message Catalog (.mo)** file for use on your site.

1. Rename this file to **woocommerce-YOURLANG.mo**(e.g., Great Britain English should be *en_GB*, or Afrikaans would be *af*).
2. Upload the file to your site’s **wp-content/languages/plugins/** folder.
3. Once uploaded, this translation can be used.

A number of WooCommerce.com extensions also offer translated versions and you can find out more about this and how to add custom translations under [Translating WooCommerce Extensions](https://woocommerce.com/document/translate-woocommerce-extensions/).

WooCommerce includes a **language file** (.pot file) that contains all of the English text. You can find this language file inside the plugin folder in **woocommerce/i18n/languages/**.

### Creating custom translations with Loco Translate

1. Install and activate the [Loco Translate](https://wordpress.org/plugins/loco-translate/) plugin.
2. Go to **Loco Translate >** **Plugins** and select **WooCommerce**:

1. Click **+ New Language** to add new languages.
2. **Choose the language** to add from the dropdown.
3. Select the folder to add the translation files to, we recommend **Custom**.
4. Click **Start translating**.

**Note #1:** Loco Translate offers three different locations for where to create the translation. The best choice for your own translation is **Custom**, not just to prevent custom translations from being undone by updates, but also because it’s needed for strings in extensions like WooCommerce Subscriptions to be properly translated. Avoid the *Author* location since it’s inside the plugin and will be overwritten by extension updates, as well as the *System* location, which could be overwritten by translations from *translate.wordpress.org*. **Note #2**: If you encounter any technical issues while using Loco Translate, please [get in touch with the Loco Translate support team](https://wordpress.org/support/plugin/loco-translate/).

1. **Save** when finished.

When a new version of WooCommerce is released and updated on your site, you may need to refresh the .po file to look for new strings. Use the “Sync” button to find any new string to start translating.

### Creating custom translations with PoEdit

PoEdit is a more advanced alternative to **Loco Translate**. This method for translating WooCommerce s recommended for only advanced users or translators.

WooCommerce comes with a POT file that can be imported into PoEdit to translate. To get started:

1. Open PoEdit and go to **File > New catalog from POT file**.
2. Choose **woocommerce.pot** and PoEdit will show the catalog properties window:

1. **Enter** **your name and details**, so other translators know who you are, and click ‘**OK**‘.
2. **Save your .po file**. Name it based on what you are translating to, i.e., a GB translation is saved as *woocommerce-en_GB.po*. Now the strings are listed.

1. **Save** after translating strings. The .mo file is generated automatically.
2. **Update** your .po file by opening it and then go to **Catalog > Update from POT file**.
3. **Choose the file** and it will be updated accordingly.

[Webis Multilingual for WooCommerce](https://woocommerce.com/products/webis-multilingual-for-woocommerce/) is available in our Marketplace with a monthly subscription.

1. **Download** the .zip file from your[WooCommerce account](https://woocommerce.com/my-account/downloads/).
2. **Go to**: **WordPress Admin > Plugins > Add New** and **Upload Plugin**. With the file you downloaded, select **Choose File**.
3. **Install Now**and**Activate** the extension.

More information at:[Install and Activate Plugins/Extensions](https://woocommerce.com/document/installing-and-activating-woocommerce-extensions/).

#### Setup and Configuration

#### Global Settings Configuration

Go to: **WooCommerce > Webis Multilingual**and navigate to the **Settings** tab.

1. Languages
  - To add languages, click**“Edit languages”**, select languages you would like to add and save.
  
2. Language Codes
  - Use this section to customize the language code shown in the URL. For example, the default language code for Chinese (simplified) is “zh_CN” and we have modified it to “cn” as shown in the above screenshot.
  
3. Language Switcher
  - Use the “Show flags” checkbox to show/hide flags in the language switcher.
  
4. Cookie Name
  - We use cookies to remember the language selected by the customer. If the site language keeps changing back to the default language, it’s likely that you have your browser cookies disabled or you’re getting the cached page. If the latter, please consult with your developers and add the cookie name to the Cache-Busting Cookies List. In some cases, you may be required to change the cookie name and that is why we have an option to change the name.
  

Go to: **WooCommerce > Webis Multilingual** and navigate to the **String Translation** tab.

Use this section to translate the strings in your storefront.

1. Enable the “Scan Strings” option on the bottom of the page and press “Save Changes”.
2. Visit pages where strings you want to translate get rendered or appear.
3. Search for the strings in “String Translation” menu and add translation by clicking “+” button.

**IMPORTANT**: Please note that you may need to refresh the page a couple of times if the page contains too many strings. And it is very important that you disable the “Scan Strings” option once you are done with scanning as it will have a significant impact on performance and slow the site down.

Translating content is simple with our plugin. Simply, you will find the fields to add translations below where you’d normally input original contents. For example, to add translations for a product, open up the product edit page and find the Webis Multilingual screen element and add translations. Likewise, to add translations for posts, go to the post edit page and find the Webis Multilingual menu.

Here are a couple of examples:

To add translations for products, simply edit the product you wish to translate and add translations to the “Webis Multilingual” section.

To add translations for menu items, go to:**Appearance > Menus**. **Example**: In the above screenshot, we’re adding translations for “Shop” menu item and have three dropdown lists: “All languages”, “Chinese (Simplified)” and “Japanese”. By selecting “All languages”, you are able to add translations for both Chinese and Japanese, and “Shop” menu will show on the storefront for both languages. Please select “Chinese (Simplified)” or “Japanese” if you only want to show the menu item on the storefront for that particular language.

Adding translations is simple with our plugin. Simply go to where you’d normally write your content and you’ll find “Webis Multilingual” section to add translations. We currently support Product, Category, Attribute, Post, Page and Menu translation.

### Making your translation upgrade safe

WooCommerce keeps translations in **wp-content/languages/plugins**, like all other plugins. But if you wish to include a custom translation, you can use the directory **wp-content/languages/woocommerce**, or you can use the snippet. See the [WooCommerce Developer Documenation](https://developer.woocommerce.com/docs/making-your-translation-upgrade-safe/) for more on that.

Using the [Say What? plugin](https://wordpress.org/plugins/say-what/) can assist if you only wish to translate or change a few words without editing a WordPress theme’s .PO file. Requires no custom code.

When activated, it asks for:

1. **Original string** – text you are translating. View the plugin source code to see the exact string.
2. **Text domain** – woocommerce
3. **Text you want to display**

You may see on the Checkout page that some of the strings are not translated. For example, in the screenshot below, `Local pickup` shipping method, `Cash on delivery` payment method, and a message related to Privacy Policy are not translated to while the rest of the form is indeed translated.

This usually happens when you first install WooCommerce and select default site language (English) and later change the site language to another one. In WooCommerce, the strings that have not been translated in the screenshot, are stored in the database after the initial WooCommerce installation. Therefore, if the site language is changed to another one, there is no way for WooCommerce to detect a translatable string since these are database entries.

To fix it, navigate to WooCommerce settings corresponding to the string you need to change and update the translation there directly. For example, to fix the strings in our case above, you would need to do the following, first for the **Local Pickup** shipping method:

1. Navigate to **WooCommerce > Settings > Shipping > Shipping Zones**.
2. Select the shipping zone where the **Local Pickup** shipping method is added.
3. Open the **Local Pickup** shipping method’s settings
4. Rename the method with the proper translation.
5. Click **Save** the save the setting.

Then, in the case of the **Cash on delivery** payment method:

1. Navigate to **WooCommerce > Settings > Payments**.
2. Select the **Cash on delivery** payment method.
3. Rename the method title, description, and instructions with the actual translation.
4. Click **Save** to save the setting.

And for the message relating to the **Privacy Policy**:

1. Navigate to **WooCommerce > Settings > Accounts & Privacy**.
2. Scroll down to the**Privacy Policy** section.
3. Edit the **Registration privacy policy** and **Checkout privacy policy** field with the correct translation.
4. Scroll down and click **Save settings**.

Navigate back to the Checkout page to see the new translations reflected there.

If some of your translated strings don’t show up as expected on your WooCommerce site, the first thing to check is if these strings have both a **Single** and **Plural** form in the *Source text* section.

If this is the case, then it is necessary to translate both these forms for your translation to work as expected. To do this, please **use Loco Translate’s Single and Plural tabs** that show up in the translation section towards the bottom of screen, as pictured below.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

