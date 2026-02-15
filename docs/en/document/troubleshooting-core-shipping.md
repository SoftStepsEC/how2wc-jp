---
title: Troubleshooting Core Shipping
url: https://woocommerce.com/document/troubleshooting-core-shipping/
---

*Last updated July 18, 2025.*

This guide helps store owners resolve problems with built-in shipping features in WooCommerce. Use the steps below to troubleshoot incorrect rates, missing methods, or unexpected checkout behavior.

This guide focuses on issues with shipping options included in WooCommerce core:

- [Flat Rate Shipping](https://woocommerce.com/document/flat-rate-shipping/) – Standard shipping rates per item, class, or order
- [Free Shipping](https://woocommerce.com/document/free-shipping/) – No-cost shipping with optional conditions
- [Local Pickup](https://woocommerce.com/document/local-pickup/) – Customer collection from your store

The guide also provides guidance on where to find support for other shipping plugins and more advanced configurations beyond the core functionality.

**Note:** The built-in WooCommerce shipping features do not include live rates or label printing.

- **WooCommerce Shipping** is a free extension that can be added to allow you to print USPS, UPS, and DHL labels right from your WooCommerce dashboard and save on shipping
- **Live rates** require advanced extensions such as USPS, UPS, or FedEx to display real-time rates at checkout

More advanced shipping extensions exist for complex scenarios and products. See the [core shipping limitations section](https://woocommerce.com/document/troubleshooting-core-shipping/#core-shipping-limitations-and-alternatives) below.

Shipping problems typically fall into one of these categories:

- Missing or incorrect shipping rates
- Shipping methods not appearing at checkout
- Unexpected shipping costs
- Shipping zone not matching customer addresses
- Shipping tax not applied or incorrect

Follow these steps to confirm if any known and fixed bugs are addressed already, and your settings are correct. These are the same steps our Happiness Engineers follow when investigating issues.

Make sure WordPress, WooCommerce, your current theme, and all extensions are using the latest versions. Updates often contain fixes for known issues.

**How to check for updates:**

1. Navigate to **Dashboard > Updates** in your WordPress admin
2. Check for available updates to WordPress core, themes, and plugins
3. Update all components before proceeding with troubleshooting

#### Shipping zones

1. Go to **WooCommerce > Settings > Shipping > Shipping zones**
2. Confirm the customer’s address matches one of the [configured zones](https://woocommerce.com/document/setting-up-shipping-zones/)
3. Make sure each relevant zone has at least one active shipping method

#### Shipping methods

1. Within each zone, verify that the [correct methods](https://woocommerce.com/document/setting-up-shipping-zones/#adding-shipping-methods-to-zones) are enabled (for example: Flat Rate, Free Shipping, Local Pickup)
2. Double-check any conditions applied to the method
3. For Free Shipping, check if minimum order amounts or coupons are set correctly

#### Product shipping settings

1. From the Product Editor, in the Product data panel, select the option to [manage shipping settings](https://woocommerce.com/document/product-shipping-classes/#section-3)
2. Confirm that the product has a shipping class (if required by your setup)
3. Verify the [product type](https://woocommerce.com/document/managing-products/#virtual-and-downloadable-products) is not set to Virtual, as shipping would not apply to non-physical products

WooCommerce includes a built-in debug mode for core shipping methods like Flat Rate, Free Shipping, and Local Pickup. When enabled, this mode logs information directly in the cart page to help reveal which shipping zone is being matched to the customer’s address.

**To enable shipping debug mode:**

1. Go to **WooCommerce > Settings > Shipping > Shipping settings**
2. Under debug mode, check the **Enable debug mode** box
3. Save changes
4. Reload the cart or checkout page to see debug messages under the available shipping options

**Important:** Remember to disable debug mode after testing, as it displays on the front-end to customers.

Sometimes, custom cart and checkout pages built with plugins, theme builders, or custom modules can cause unexpected behavior or prevent certain features from working.

A quick test to make sure this isn’t a conflict with your configuration is to try with the default Cart and Checkout pages, using the default WordPress editor, and the Cart and Checkout shortcodes or blocks:

**Available options:**

- [Cart shortcode](https://woocommerce.com/document/woocommerce-shortcodes/page-shortcodes/#cart): `[woocommerce_cart]`
- [Cart block](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/#using-the-cart-and-checkout-blocks) (available in block editor)
- [Checkout shortcode](https://woocommerce.com/document/woocommerce-shortcodes/page-shortcodes/#checkout): `[woocommerce_checkout]`
- [Checkout block](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/#using-the-cart-and-checkout-blocks) (available in block editor)

For more information, see [WooCommerce page setup documentation](https://woocommerce.com/document/woocommerce-pages/).

## Advanced troubleshooting steps

Below are tools and techniques to help troubleshoot more complex shipping problems. Use these methods to inspect shipping logic, identify theme or plugin conflicts, and catch hidden errors.

Browser developer tools (such as Chrome DevTools or Firefox Developer Tools) help you inspect dynamic behavior on the cart and checkout pages.

**How to access developer tools in common browsers:**

- **Chrome:** Press F12 or right-click and select “Inspect”
- **Firefox:** Press F12 or right-click and select “Inspect Element”
- **Safari:** Enable Developer menu in Safari preferences, then press Option+Command+I
- **Edge:** Press F12 or right-click and select “Inspect”

**Key tabs to check:**

#### Console tab

Look for JavaScript errors or warnings that could be interfering with shipping method display or updates.

#### Network tab

Monitor AJAX requests such as `?wc-ajax=update_shipping_method` and `?wc-ajax=update_order_review`. This can help confirm whether rate recalculations and shipping method updates are occurring when cart items or addresses change and confirm if something is blocking the AJAX request.

#### Elements tab

Check the HTML structure to ensure shipping options are rendering and not being hidden by theme CSS or JavaScript.

**Use these tools to diagnose issues such as:**

- Shipping not updating after a quantity change
- Custom checkout modifications blocking or hiding shipping fields
- JavaScript errors preventing form submission or rate display

WooCommerce features a logging system accessible in WP Admin via **WooCommerce > Status > Logs**, which records PHP fatal errors among other information.

This log serves as a valuable initial resource, mirroring details that would typically be found in PHP error logs on the server. We recommend you consult this log first before proceeding to locate the PHP logs on the server for further troubleshooting.

Learn more about [finding PHP error logs](https://woocommerce.com/document/finding-php-error-logs/).

Template overrides are a common cause of issues with how shipping options are displayed in WooCommerce. When a theme customizes core WooCommerce templates, outdated or faulty overrides can lead to missing methods, incorrect shipping information, or errors during checkout.

#### Common issues and troubleshooting actions

If you suspect a conflict on your site, follow our [conflict testing guide](https://woocommerce.com/document/how-to-test-for-conflicts/). This guide walks you through the safest way to identify whether a plugin, theme, or custom code is causing the issue, and best practices to consider before making any changes.

If the issue persists in a conflict test, [open a support request](https://woocommerce.com/my-account/create-a-ticket/) so we can identify any issue to be fixed.

**New in WooCommerce version 9.9:** [Blueprints](https://woocommerce.com/document/woocommerce-blueprints/) is a tool for importing and exporting store settings. It helps developers, agencies, and merchants save time by reusing and sharing store configurations—making setup faster and troubleshooting easier.

**Where to find Blueprints:** You can find Blueprints under **WooCommerce > Settings > Advanced > Blueprint**. It currently supports core WooCommerce settings and can be used through the admin interface or WP-CLI.

**How to use Blueprints for troubleshooting:**

With Blueprints, you can export your store settings – including Shipping settings – for troubleshooting.

If you’re still experiencing shipping issues after following the steps above:

1. [Export your settings](https://woocommerce.com/document/woocommerce-blueprints/#section-3) using Blueprints
2. Set up a staging site using a default theme like [Storefront](https://wordpress.org/themes/storefront/) or [Twenty Twenty-Five](https://wordpress.org/themes/twentytwentyfive/) with WooCommerce active (and Blueprints enabled)
3. [Import the settings](https://woocommerce.com/document/woocommerce-blueprints/#section-7) into the staging site using Blueprints

If the issue does not occur on the staging site, it may indicate a conflict on your live site rather than a problem with your WooCommerce settings

This process helps recreate your store’s environment for more accurate testing and troubleshooting.

**Important:** For any of the issues below, if the specified instructions do not help, then please make sure to go through the [Basic Troubleshooting Steps](https://woocommerce.com/document/troubleshooting-core-shipping/#basic-troubleshooting-steps) and [Advanced Troubleshooting Steps](https://woocommerce.com/document/troubleshooting-core-shipping/#advanced-troubleshooting-steps) first.

This is a common issue typically related to a misconfiguration in shipping zone settings, but [theme or plugin conflicts](https://woocommerce.com/document/how-to-test-for-conflicts/) can also cause this error (for example: a third-party plugin restricting shipping to some countries or regions).

**Error message customers see:** `Error: "No shipping options are available for this address. Please verify the address is correct or try a different address."`

**To troubleshoot this issue:**

1. **Check shipping zones :** Ensure the customer’s shipping address matches a shipping zone. You can check your set shipping zones at **WooCommerce > Settings > Shipping > Shipping zones**
2. **Verify shipping methods:** Once you have located your shipping zones and confirmed the customer’s address matches one of your zones, confirm that the matched shipping zone has at least one [shipping method](https://woocommerce.com/document/setting-up-shipping-zones/#adding-shipping-methods-to-zones) enabled
3. **Review zip code ranges:** Check for overlapping or incomplete zip code ranges (especially with [wildcards or spacing](https://woocommerce.com/document/setting-up-shipping-zones/#adding-a-new-zone)) on your shipping zones settings page
4. **Check product settings:** In the product edit page, confirm the product is not marked as Virtual, and that weight, dimensions, and shipping class are added as these must match your shipping method condition (depends on shipping method used on your site)
5. **Enable debug mode:** Enable [Shipping debug mode](https://woocommerce.com/?post_type=documentation&p=18734005250648&preview=true#enable-shipping-debug-mode) to surface helpful error messages

If you see taxes charged on shipping, but should not be, follow these steps to disable taxes on shipping:

1. Go to **WooCommerce > Settings > Shipping > Shipping zones > Edit the shipping method**
2. Confirm the method’s **Tax status** is set to **None** (if you don’t need taxes being collected for shipping rates)

### Taxes not being charged on shipping

If taxes are not applying to shipping costs at checkout, it’s often due to a misconfiguration in your tax settings. Review this [troubleshooting guide on shipping tax settings](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/).

Unexpected flat rate shipping behavior is often caused by one or more configuration issues:

**Check rate calculation settings:**

- Verify if the rate should apply per item, per class, or per order
- Use `[qty]` to multiply cost per item
- Use `[fee]` for percentage-based fees
- See [examples on how to use the formulas for advanced flat rate shipping costs](https://woocommerce.com/document/flat-rate-shipping/)

**Review shipping class configuration:**

- Make sure the Shipping class cost is defined in the shipping method settings
- Confirm the product is assigned to the correct shipping class
- If using class costs plus base cost, ensure [calculation type is set appropriately](https://woocommerce.com/document/flat-rate-shipping/#shipping-classes)
- If behavior is inconsistent, try testing with just one product in the cart to narrow down the cause

By default, WooCommerce will show all shipping methods that match the customer and the cart contents. This means Free Shipping will also show along with Flat Rate and other Shipping Methods.

**Since WooCommerce 9.9:** There’s a built-in setting to hide all other shipping methods when Free Shipping is available:

1. **Check your WooCommerce version:** You can verify your version under **WooCommerce > Status**
2. **If you’re using WooCommerce 9.9 or higher:** Go to **WooCommerce > Settings > Shipping > Shipping options** and enable **Hide shipping rates when free shipping is available**
3. If you’re on an older version of WooCommerce: Free Shipping will not automatically hide other methods unless:
  - A [custom code snippet](https://woocommerce.com/document/hide-other-shipping-methods-when-free-shipping-is-available/#php-snippets) is added correctly and is active on your site
  - Or a [third-party plugin](https://woocommerce.com/document/hide-other-shipping-methods-when-free-shipping-is-available/#use-a-plugin) that provides this functionality is installed and active
  

By default, WooCommerce will show all shipping methods that match the customer and the cart contents. This means Free Shipping will also show along with [Flat Rate](https://woocommerce.com/document/flat-rate-shipping/) and other [Shipping Methods](https://woocommerce.com/product-category/woocommerce-extensions/shipping-methods).

Make sure to review the following if [Free shipping](https://woocommerce.com/document/free-shipping/) is missing at checkout or isn’t showing up when the cart meets configured conditions:

- **Verify Shipping zones :** Ensure the customer’s shipping address matches a configured zone and confirm that the relevant shipping zone includes the correct regions
- **Confirm Free shipping method configuration:** Confirm Free shipping method is added and check the intended “[Free Shipping Requires](https://woocommerce.com/document/free-shipping/#section-2)” dropdown option is selected
- **Check product shipping classes:** Ensure products aren’t assigned to a class that excludes free shipping or applies a different shipping cost

Review the following settings if the shipping rate shown at checkout doesn’t match the rate you configured for the customer’s location:

1. **Verify customer address:** Verify that the customer’s full shipping address is entered on the checkout page, including country/state/city/postcode
2. **Check store address:** Ensure that the store address is entered at **WooCommerce > Settings > General**
3. **Use Shipping Debug Mode:** You can enable this option in **WooCommerce > Settings > Shipping > Shipping settings**. Once this option is enabled, please double check the checkout page (using the checkout shortcode) to confirm which shipping zone is being matched
4. **Review zone configuration:** Check for overlapping zip code ranges or zone ordering issues by going to **WooCommerce > Settings > Shipping > Shipping zone**
5. **Verify location codes:** Confirm that country and state abbreviations are using 2-letter ISO codes in zones
6. **Test plugin conflicts:** If a plugin adjusts shipping dynamically (for example: [Conditional Shipping & Payments](https://woocommerce.com/products/conditional-shipping-and-payments/)), test logic rules by deactivating the plugin and then checking if the behavior persists

### Shipping costs aren’t updating in cart or checkout

If shipping rates don’t reflect changes to products, addresses, or quantities, check the following:

#### Check shipping zone configuration

Go to **WooCommerce > Settings > Shipping >**[Shipping zones](https://woocommerce.com/document/setting-up-shipping-zones/) and confirm that the customer’s address matches a defined zone with at least one active shipping method.

#### Clear browser and site cache

Caching plugins or server-side caching can block live rate updates from appearing correctly. To fix this:

1. Clear your browser cache
2. Clear your site cache
3. If you’re using a caching plugin or your hosting provider offers caching, make sure the following pages are excluded from caching :
  - Cart
  - Checkout
  - My Account
  

After you clear your site and browser caches and update any shipping method exclusions, reload your site and complete a test checkout to confirm that the correct shipping rates appear.

#### Force cart refresh with AJAX

Ensure your theme supports AJAX updates, or direct users to select “Update Cart” if rates don’t automatically recalculate.

This section outlines common misconfigurations related to shipping classes and provides steps to resolve them.

#### Shipping class cost not applied to shipping cost

This can happen when shipping class and their rates are left empty or not configured correctly. Check the following:

1. **Product class assignment:** In the Product data panel, select the option to manage shipping settings. Ensure each product is assigned to the correct class
2. **Method class rates:** Confirm that class-specific rates are defined in the Flat Rate method settings, under the relevant “Shipping class costs” options

#### Shipping cost always shows $0

If your Flat Rate shipping method is enabled but the cost is returning $0, please review the following:

1. **Set base costs:** Make sure to set at least a base cost or a Shipping class costs
2. **Configure calculation type:** Set the Calculation Type for the shipping class to either “Per class” or “Per order,” depending on how you want shipping costs calculated. This setting directly affects how rates are applied at checkout

If the shipping costs are not calculated until the customer enters their shipping address, you can review the following:

1. **Check calculation settings:** In **WooCommerce > Settings > Shipping > Shipping settings > Calculations**, ensure the “Hide shipping costs until an address is entered” box is unchecked
2. **Verify geolocation setup:** If you’re using Geolocate, please ensure a proper [license key](https://woocommerce.com/document/maxmind-geolocation-integration/#create-a-maxmind-license-key) for MaxMind Geolocation is entered in the [integration tab](https://woocommerce.com/document/maxmind-geolocation-integration/#add-maxmind-geolocation-license-key-to-woocommerce-settings) under **WooCommerce > Settings > Integration > MaxMind Geolocation**

[Shipping classes](https://woocommerce.com/document/product-shipping-classes/) define cost rules for methods like [Flat Rate](https://woocommerce.com/document/flat-rate-shipping/#shipping-classes) shipping. If items with specific classes aren’t showing the correct charges at checkout, review the following settings for possible misconfigurations:

**Confirm the product has the correct class assigned:** In the Product data panel, select the option to manage shipping settings. Make sure the correct Shipping Class is selected and saved. For variable products, check each variation’s settings individually.

**Check the shipping method settings in the correct zone:** Go to **WooCommerce > Settings > Shipping > Shipping zones**. Select the zone your customer falls into and open the Flat Rate (or other applicable) method. Ensure you’ve entered a cost for the relevant shipping class under “Shipping Class Costs.”

**Understand how Flat Rate prioritizes costs:** By default, Flat Rate shipping uses the highest class cost from items in the cart. If you want to [combine flat rate shipping classes](https://woocommerce.com/document/flat-rate-shipping/#shipping-classes) to charge per class, you’ll need to enable “Per class: Charge shipping for each class individually” under Calculation type.

Shipping methods may display differently between using shortcode vs the Checkout block. Test thoroughly with both types of checkout interfaces.

- **Shortcode-based checkout:** Use the `[woocommerce_checkout]` shortcode to create a shortcode-based checkout
- **Block-based checkout:** Add the Checkout Block for a block-based checkout

If you’re seeing duplicate pickup options at checkout, it’s likely because the legacy local pickup method was added to a shipping zone before you enabled the block-based Local Pickup option in **WooCommerce > Settings > Shipping > Local pickup** (you will not see this option if you are not using the Checkout block). This means you have both local pickup options enabled at once.

**Important:** Do not use both pickup options at the same time, as it may confuse customers. A notice will appear on the Local Pickup settings page if both options are active.

**Solution:** If you’re using a block-based checkout, remove the legacy Local Pickup method from your shipping zones in **WooCommerce > Settings > Shipping**. The new Local Pickup option for block-based checkout doesn’t need to be added to a shipping zone—it’s managed separately in the Local Pickup settings page at **WooCommerce > Settings > Shipping > Local Pickup**.

WooCommerce matches customers to the first zone that fits their shipping address. If your customers aren’t seeing the correct shipping methods on the cart and checkout pages, the shipping zones are most likely in the wrong order.

**Best practice:** To show the right options at checkout, list zones from most specific to broadest—like City, then State, then Country. Learn more about [sorting shipping zones](https://woocommerce.com/document/setting-up-shipping-zones/).

The title set on a shipping method added to a shipping zone is what is displayed to customers during the checkout process. You can change the shipping method title easily by editing the shipping method added to the shipping zone.

To ensure compatibility with WooCommerce core features, use the default page editor and the core WooCommerce cart and checkout [shortcodes](https://woocommerce.com/document/woocommerce-shortcodes/) or [blocks](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/).

If you’re using a third-party theme, builder, or plugin for your cart or checkout pages and you’re troubleshooting shipping issues, switch to the default WooCommerce setup to isolate the cause. Use the default page editor along with the core WooCommerce cart and checkout shortcodes or blocks.

This helps determine whether the issue is related to your custom setup or WooCommerce itself.

Marking a product as “Virtual” disables all shipping options for that item, so virtual products do not trigger shipping calculations or display shipping fields at checkout.

**To set a product as virtual:** Edit the product, then check the Virtual checkbox.

The shipping tax is based on cart items or the Standard tax rate. If taxes are not applied to shipping costs at checkout, it’s often due to a misconfiguration in your tax settings. Review this [troubleshooting guide on shipping tax settings](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/).

Flat rate, free and local pick up core shipping methods work with shipping classes, shipping zones, and shipping methods, and the products shipping weight or dimensions don’t impact on this. However, this is helpful to properly display product metadata to your customers, and especially helpful when working with live rates.

WooCommerce applies the “Rest of the World” zone when a customer’s address doesn’t match any other defined shipping zone. You cannot move, rename, or delete this zone.

**For specific cases:** Like Northern Ireland, you can separate Northern Ireland from the UK using an extension like [Shipping Locations Pro](https://woocommerce.com/products/shipping-locations-pro/).

**Setting up postal code zones:** You can also set up a [new shipping zone](https://woocommerce.com/document/setting-up-shipping-zones/#adding-a-new-zone) based on postal codes with wildcards (*).

**How to use zip/postcodes to limit a shipping zone:** A local shipping zone can include one or multiple (one per line) of the following: specific postcodes, numeric ranges (for example: 90210…99000), and postcodes with wildcards(*).

**Using wildcards:** A wildcard can be used to capture all postcodes that share the same beginning, so it is the recommended option for postcodes with non-numeric characters.

**Examples:**

- `902*` would capture 90210 and also 90288-1234
- `CB23*` would capture CB23 1EX
- `CB2*` would capture CB2 3AA and CB23 1EX

**Note:** Using wildcards in numeric ranges (for example: 902*…990*) is not supported.

The following options are built into WooCommerce and cover the most common shipping needs for many stores:

#### Flat Rate Shipping

Allows you to define a [standard shipping rate](https://woocommerce.com/document/flat-rate-shipping/) per item, per shipping class, or per order.

#### Free Shipping

Allows you to add a “[free shipping](https://woocommerce.com/document/free-shipping/)” option for customer orders if they either meet certain criteria (for example: a minimum order spend amount) or if you want to offer free shipping to all customers within a certain geographical area.

#### Local Pickup (legacy)

Allows you to offer customers the [option to collect their purchases directly](https://woocommerce.com/document/local-pickup/) from your store. Customers must enter an address and must be matched to a shipping zone with this shipping method added to see this shipping option, and taxes are calculated based on the store location.

#### WooCommerce Blocks: Local Pickup

Allows you to offer one or more pickup locations during checkout using the [WooCommerce Checkout block](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/woocommerce-blocks-local-pickup/). Customers can select a pickup location without entering a shipping address, and taxes are calculated based on the selected pickup location.

**Important limitation:** WooCommerce core shipping does not offer the option to display live shipping rates at checkout and also does not offer a way to print labels for order fulfillment. Recommendations for these can be found below.

The below solutions enable you to generate and print shipping labels directly from your WooCommerce dashboard or through integrated platforms:

#### WooCommerce Shipping

Allows you to [print discounted USPS, UPS, and DHL labels](https://woocommerce.com/products/shipping/) directly from your WooCommerce dashboard.

#### ShipStation

Allows you to connect your WooCommerce store to [ShipStation](https://woocommerce.com/products/shipstation-integration/) for streamlined order fulfillment, including batch label printing, shipping automation, and discounted rates.

#### Stamps.com

Allows you to generate and print USPS shipping labels directly from your WooCommerce dashboard using your [Stamps.com](https://woocommerce.com/products/woocommerce-shipping-stamps/) account.

**When to use ShipStation over WooCommerce Shipping:** WooCommerce Shipping works well for most small to medium-sized stores with moderate shipping needs. Choose ShipStation if you manage high order volumes, wish to print labels in bulk, sell on multiple channels, or require shipping automation.

The below extensions allow you to display real-time shipping rates from major carriers at checkout, helping you provide accurate shipping costs to your customers. This is not an exhaustive list. Please check our [marketplace](https://woocommerce.com/product-category/woocommerce-extensions/shipping-methods/) for more shipping extensions available on WooCommerce.com

#### Available live rate extensions:

- **UPS® Shipping Method** – offers UPS live rates at checkout
- **USPS Shipping Method** – offers USPS live rates at checkout
- **FedEx Shipping Method** – offers real-time FedEx shipping rates at checkout by integrating your WooCommerce store with the FedEx API (United States or Canada only)
- **Royal Mail Shipping Method** – offers Royal Mail shipping rates at checkout without requiring an API connection (UK only)

#### General tips for troubleshooting API shipping rates

Follow these troubleshooting steps to identify and fix common issues that prevent live shipping rates from appearing at checkout:

1. **Enable plugin-specific debug/logging tools** – Instructions on enabling debug mode can be found [here](https://woocommerce.com/document/shipping-method-debug-mode/)
2. **Ensure products have complete weight and dimension data**
3. **Validate API credentials** – Incorrect credentials are a common cause of issues when using live rate shipping extensions that rely on an API. These problems often relate to authorization or authentication errors. One example of this can be found in the [UPS troubleshooting guide](https://woocommerce.com/document/ups-shipping-method/#troubleshooting)
4. **Verify shipping origin ZIP code** in the plugin’s settings

These advanced plugins let you customize shipping rules and rates to accommodate unique business requirements or specialized shipping scenarios:

#### Conditional Shipping & Payments

Allows you to [conditionally](https://woocommerce.com/products/conditional-shipping-and-payments/) enable or disable the shipping methods (and payment methods) based on factors like cart contents, customer roles, or shipping destinations.

#### Table Rate Shipping

A highly flexible shipping solution that allows you to [set up multiple table rates per shipping zone](https://woocommerce.com/products/table-rate-shipping/). It allows you to define multiple shipping rates based on factors like destination, weight, item count, price, or shipping class.

#### Per Product Shipping

Allows you to define [individual shipping costs for specific products](https://woocommerce.com/products/per-product-shipping/), which can be combined with other shipping methods or used as a standalone option.

#### Distance Rate Shipping

Allows you to [calculate shipping rates based on the distance or travel time](https://woocommerce.com/products/woocommerce-distance-rate-shipping/) between your store and the customer’s address, using Google Maps Distance Matrix API.

This section highlights additional plugins that can enhance your shipping workflow:

#### Shipment Tracking

Allows you to [add shipment tracking information](https://woocommerce.com/products/shipment-tracking/) to WooCommerce orders, enabling customers to track their packages via emails, the order tracking page, and their account dashboard.

If you’re still having trouble, please reach out to [WooCommerce support](https://woocommerce.com/my-account/create-a-ticket/) with the following information:

**Required information for support requests:**

- Details of the issue you’re facing
- Clear reproduction steps (including the shipping address you are testing with)
- Troubleshooting steps you’ve taken already
- Any error messages from your [browser console](https://woocommerce.com/document/troubleshoot-javascript-errors/) or [PHP error Logs](https://woocommerce.com/document/finding-php-error-logs/)
- A copy of your [WooCommerce System Status Report](https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/#system-status)
- [Blueprint of your WooCommerce settings](https://woocommerce.com/document/woocommerce-blueprints/#section-3) or a [Staging](https://woocommerce.com/posts/what-is-staging-site-wordpress-how-to-set-one-up/) site

**Screenshots to include:**

- Cart and checkout pages to display the issue
- Shipping settings, including your shipping zones and shipping methods
- Affected product edit page displaying the shipping configuration

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

If you experience accessibility issues with this page, please [contact WooCommerce Support](https://woocommerce.com/accessibility/).

