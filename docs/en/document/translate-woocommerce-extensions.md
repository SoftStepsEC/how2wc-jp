---
title: Translating WooCommerce Extensions
url: https://woocommerce.com/document/translate-woocommerce-extensions/
---

Plugins sold on WooCommerce.com are translation ready and can be used with any translation plugin. Some even have bundled translations available and we’re always happy to work with translators to increase translation coverage!

If you’re interested in translating WooCommerce or extensions, please review [this document on localization](https://woocommerce.com/document/woocommerce-localization/) to get started.

If a plugin has a translation bundled, it will be loaded automatically when your site language is switched away from English. We try to bundle complete translations when possible but will bundle partial translations if a complete translation is not available, so some strings may be missing from the translation.

If you build your own translation and would like to submit it for bundling, please [get in touch with our help desk](https://woocommerce.com/my-account/create-a-ticket/) to pass the translation to the plugin developer.

If you want to **translate an extension** into your own language manually, a gettext tool like [PoEdit](https://poedit.net/) will be helpful. Please ensure you know how to properly translate a .pot file, these tutorials will be helpful:

- [Translate a WordPress Plugin](https://wplang.org/translate-theme-plugin/)
- [Translate WordPress Themes or Plugins](https://nicola.blog/2015/09/02/translate-wordpress-theme-plugins-loco-translate/)

You’ll need a couple things to get translating:

- Your gettext tool of choice, ie PoEdit (recommended) or LocoTranslate
- The plugin’s **textdomain**. If you’re not sure of which textdomain to use, it’s usually listed at the top of the main plugin file — download the plugin, unzip it, open the folder, and look in the file with the same name as the plugin (will not be in a sub folder, will always be in the main folder).
- The plugin’s **.pot file** — this is typically in a `/languages/` directory or `/i18n/` directory within the plugin.

Once you have the plugin’s textdomain and its .pot file, you can get translating 🙂

When you’re done, you can add your translations to the same folder in which you found the .pot file. Ensure you’ve named them correctly!

For example, if the plugin .pot file is named `woocommerce-plugin-textdomain.pot`, your translation files should be named `woocommerce-plugin-textdomain-aa_AA.po` and `woocommerce-plugin-textdomain-aa_AA.mo`, where `aa_AA` is the [code for your language](https://wordpress.org/support/article/installing-wordpress-in-your-language/) (e.g., fr_FR).

```
text-domain
```

If you want your translations to be saved in the event of plugin upgrades, you could also move them to a WordPress core directory — translations for a plugin can be saved to:

```
wp-content/languages/plugins/woocommerce-plugin-textdomain-aa_AA.po
```

The `wp-content/languages/plugins/` directory will hold translations for any plugin. You can safely store your custom translation there and it will not be overwritten with plugin updates.

**Note #1:** Loco Translate offers three different locations for where to create the translation. The best choice for your own translation is **Custom**, not just to prevent custom translations from being undone by updates, but also because it’s needed for strings in extensions like WooCommerce Subscriptions to be properly translated. Avoid the *Author* location since it’s inside the plugin and will be overwritten by extension updates, as well as the *System* location, which could be overwritten by translations from *translate.wordpress.org*. **Note #2**: If you encounter any technical issues while using Loco Translate, please [get in touch with the Loco Translate support team](https://wordpress.org/support/plugin/loco-translate/).

SkyVerge extensions use a common skeleton for development, so as a result, the plugin will have a textdomain and translation, as well as a textdomain and translation for the skeleton. As such, some of the strings in your plugin may be part of the skeleton.

You can translate the skeleton just like a plugin, but its translation will need to be saved in a different location (with the benefit being that if you translate it once, it will apply to all SkyVerge extensions using those strings).

```
We recommend translating what you need to from the skeleton / framework by following the steps below, then moving onto the plugin's strings, following the steps in the section above.
```

Here are some steps to translating the SkyVerge plugin framework — ensure you replace `nb_NO` in the below steps with the appropriate text domain for your translation.

If you have already started a translation of the framework .pot file, you can skip steps 1 through 5 and just rename the `.po` and `.mo` files to `woocommerce-plugin-framework-nb_NO.po` and `woocommerce-plugin-framework-nb_NO.mo`.

1. In your plugin, find the `woocommerce-plugin-framework.pot` file in either of the following two locations (your plugin will only have one of these): vendor/skyverge/wc-plugin-framework/woocommerce/i18n/languages/woocommerce-plugin-framework.pot lib/skyverge/woocommerce/i18n/languages/woocommerce-plugin-framework.pot
2. Open the `woocommerce-plugin-framework.pot` file in PoEdit or similar and click on Create New Translation. [](https://woocommerce.com/wp-content/uploads/2015/10/poedit-new-translation.png)
3. Set the language of the translation and click OK [](https://woocommerce.com/wp-content/uploads/2015/10/poedit-save-translation.png)
4. Select **File > Save** then save the file on your computer, ensuring that you name it exactly `woocommerce-plugin-framework-nb_NO.po` (the `.po` extension should be added automatically by the application).
5. Translate some strings and click on **File > Compile to MO…** and ensure you name the file exactly `woocommerce-plugin-framework-nb_NO.mo`
6. Once you have made a few test translations, upload both the .po and .mo files via FTP to the `wp-content/languages/woocommerce-plugin-framework/` folder in your site (you will likely have to create this folder). The two files should have the following paths: wp-content/languages/woocommerce-plugin-framework/woocommerce-plugin-framework-nb_NO.mo wp-content/languages/woocommerce-plugin-framework/woocommerce-plugin-framework-nb_NO.po
7. Visit the frontend or admin of your site to verify if the new translations were picked up. If not, please send us admin and FTP credentials and we would be more than happy to troubleshoot.
8. Assuming the translation test passed, complete the translations on your local computer, recompile the MO file when satisfied, then upload the two files again to the `wp-content/languages/woocommerce-plugin-framework/` directory.

If you would like to submit a translation for the `woocommerce-plugin-framework`, please [open an issue or pull request on GitHub](https://github.com/skyverge/wc-plugin-framework).

If you want to use multiple languages or display a language different than your site language, than a multilingual tool like WPML comes into play. WPML has [document available](https://wpml.org/documentation/getting-started-guide/theme-localization/) on translating plugins.

To use WPML with WooCommerce, you should install the [WooCommerce Multilingual plugin](https://wordpress.org/plugins/woocommerce-multilingual/), which their team can help you with in terms of set up and configuration.

[Loco Translate is a solid approach](https://woocommerce.com/document/woocommerce-localization/#creating-custom-translations-with-Loco-Translate) in managing your languages in WooCommerce.

- [Get PoEdit](https://poedit.net/)
- [WPML documentation](https://wpml.org/documentation/getting-started-guide/theme-localization/)

