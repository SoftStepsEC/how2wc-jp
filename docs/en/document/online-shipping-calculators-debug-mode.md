---
title: Online Shipping Calculators & Debug Mode
url: https://woocommerce.com/document/online-shipping-calculators-debug-mode/
---

If shipping costs provided by your WooCommerce installation are higher or lower than what you expect, we recommend enabling the debug mode within the shipping plugin settings section that you are using.

Once this option is enabled, add a product to cart and in most cases you will see useful information on the cart page and/or on the checkout page that explains why shipping costs are different from what you expect, or why they are simply not displayed at all.

We also recommend comparing shipping costs displayed on your WooCommerce site to shipping costs from the carrier’s online rate calculators. Nearly all shipping companies provide such a tool, but it is important that you use the exact same values as what is enabled in the shipping method settings (as they can modify the rates) and ensure that the package(s) used and total weight and dimension are correct.

When you experience an issue, make sure that:

- **Weights and dimensions** need to be entered for all products, as they are required for the API to successfully return rates. You can read more about how to add shipping info to products the [Adding Dimensions and Weights to Products for Shipping](https://woocommerce.com/document/adding-dimensions-and-weights-to-products-for-shipping/) document.
- **Packaging being used** is correct. Debug will show the package weight and dimensions, and some plugins will also have a “Packed” line in the Debug output for further clarity. More info about box packing can be found in the [Understanding Box Packing Calculations](https://woocommerce.com/document/understanding-box-packing-calculations/) document.
- **Currency** is correctly set. Some plugins require the shop to use a specific currency. If this is the case, it will be specified in the specific plugin’s documentation and you can confirm or change the shop currency on the **WooCommerce > Settings > General** settings page.
- **Shop base location** is correct. Some plugins require the shop to have a specific base location. Confirm or change shop location at: **WooCommerce > Settings > General**.
- **API keys** are correct. If not, an “Authorization failed” error message will be displayed in the API Response section.
- **wp_remote_get()** function is enabled on your server. You can verify that there is a checkmark next to the “Remote get” section of the site’s System Status Report on the **WooCommerce > System Status > Server Environment** page. If this is not the case, contact your host and ask for assistance.
- **SOAP** is installed and [enabled on your server](https://www.php.net/manual/en/class.soapclient.php). You can verify that there is a checkmark next to the “SoapClient” section of the site’s System Status Report on the **WooCommerce > System Status > Server Environment**page. If this is not the case, contact your host and ask for assistance.

Online calculator: [https://www.fedex.com/ratefinder/home](https://www.fedex.com/ratefinder/home)

Online calculator: [http://postcalc.usps.com/](http://postcalc.usps.com/)

Online calculator: [https://wwwapps.ups.com/ctc/request?loc=en_US&WT.svl=PNRO_L1](https://wwwapps.ups.com/ctc/request?loc=en_US&WT.svl=PNRO_L1)

Online calculator: [http://auspost.com.au/apps/postage-calculator.html](http://auspost.com.au/apps/postage-calculator.html)

Online calculator: [http://www.canadapost.ca/cpotools/apps/far/business/findARate?execution=e1s1](http://www.canadapost.ca/cpotools/apps/far/business/findARate?execution=e1s1)

Online calculator: [https://www.nzpost.co.nz/tools/rate-finder](https://www.nzpost.co.nz/tools/rate-finder)

Online calculator: [https://eshiponline.purolator.com/ShipOnline/Estimates/Estimate.aspx?lang=e](https://eshiponline.purolator.com/ShipOnline/Estimates/Estimate.aspx?lang=e)

Online calculator: [http://www.royalmail.com/price-finder](http://www.royalmail.com/price-finder)

2015 Flat Rates: [http://www.royalmail.com/sites/default/files/Royal-Mail-UK-and-international-parcel-and-letter-prices-30-March-2015.pdf](http://www.royalmail.com/sites/default/files/Royal-Mail-UK-and-international-parcel-and-letter-prices-30-March-2015.pdf)

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

