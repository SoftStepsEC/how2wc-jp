---
title: Troubleshooting Core Taxes
url: https://woocommerce.com/document/troubleshooting-core-taxes/
---

This document contains troubleshooting suggestions for issues related to taxes in WooCommerce.

The WooCommerce plugin includes support for [basic tax rates](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/). These built-in tax options are referred to as **Core Taxes**. Using Core Taxes, you can set up basic tax options under **WooCommerce > Settings** on the “Tax” tab, and also [use this section](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#configuring-tax-options) to set up manual tax rate tables for different locations and types of products.

To enable automatic tax calculation, you will need to install an additional plugin. The **WooCommerce Tax plugin** is free and provides automated tax calculation for simple situations in many countries. More advanced tax plugins are available for more advanced or specific scenarios and products.

This document will focus mainly on issues related to the core WooCommerce tax rate functionality, providing suggestions on where to find help with other plugins and more complex setups.

This section covers some common issues you may encounter using the core WooCommerce tax tables.

Tax calculation errors most frequently occur due to misconfigured basic tax settings.

#### Tax calculation activation

Ensure the “[Enable tax rates and calculations](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#enabling-taxes)” option is checked in **WooCommerce > Settings > General**.

#### Default customer location

If [set incorrectly](https://woocommerce.com/document/configuring-woocommerce-settings/general/#general-options), first-time visitors may see incorrect tax calculations before providing their address. Remember that using “Geolocate” as your setting requires you to enable [MaxMind](https://docs.google.com/document/d/1GKwihbAWBzhwAjE-fO-5Kyy4RTofLXrw2diSFeFeqAg/edit?tab=t.0).

#### Calculate tax based on

[This setting](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#calculate-tax-based-on) determines whether taxes are calculated based on the customer’s shipping address, billing address, or your store’s address. If this setting is incorrect, WooCommerce may display tax rates based on the wrong location.

**To ensure your basic tax configuration is correct:**

1. Go to **WooCommerce > Settings > Tax**
2. Check that “Calculate tax based on” is set to the appropriate option:
  - **Customer shipping address** – if you want to tax based on where items are shipped
  - **Customer billing address** – for digital products or when shipping address isn’t collected
  - **Shop base address** – only if you charge the same tax rate to everyone
  

[Tax calculations](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/how-taxes-work-in-woocommerce/) in WooCommerce follow a specific logic that determines which rates apply to transactions. When incorrect rates appear, understanding the underlying calculation mechanism can help identify the source of the problem.

WooCommerce processes tax calculations in a hierarchical manner, considering several factors in sequence.

**To verify your tax rates:**

#### Step 1: Identify the tax table

Identify the tax table to use for each product in the cart based on its defined tax class.

#### Step 2: Check location matching

Check the table for each product and for any locations that match the taxable location (store address, customer billing address, or customer shipping address, based on settings). Double-check for any typos in:

**Country and state codes:**

- Country codes and state/province codes should be standard two-letter codes

**Postal codes:**

- Postal/zip codes can include wildcards (`90*`) or a range (`90210-90215`)
- If an issue is suspected, try entering individual codes as a semicolon-separated list or individual rows

**City names:**

- WooCommerce only matches cities based on the exact string entered on the checkout page
- Common mismatches include abbreviations or alternate spellings (for example: “ST CHARLES” vs “SAINT CHARLES”; “New York” vs “NYC”)
- Consider adding multiple rows in the tax table for common city name variations to ensure correct rate application

#### Step 3: Handle priority conflicts

If the taxable location fits into more than one row on the tax table, then choose one rate for each priority.

For example:

- If several rows exist in the tax table at priority 1, choose only the topmost one that matches the current taxable location to apply
- If more rows exist at priority 2, choose only the topmost second-rate that matches the current location to additionally apply, and so on through all priority levels

#### Step 4: Integrate with price display settings

Integrate these calculations with your configured [price display settings.](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#display-prices-during-cart-and-checkout)

**Important:** When troubleshooting, it’s crucial to recognize that WooCommerce stops at the first matching tax location on the appropriate tax table for each priority level, which means the order of your tax rules can significantly impact which rates are applied.

Find additional [advanced core tax table examples here](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/).

If tax isn’t being applied to shipping at checkout, it’s usually due to a misconfiguration. WooCommerce’s core tax system requires several settings to be aligned for shipping tax to work correctly. If you’re not using a plugin like Avalara or TaxJar, follow these steps to troubleshoot the issue.

#### Step 1: Check shipping method tax status

Ensure each [flat rate core shipping method](https://woocommerce.com/document/flat-rate-shipping/) under **WooCommerce > Settings > Shipping > [Your Shipping Zone]** has **Tax Status** explicitly set to **Taxable**. If set to “None,” WooCommerce will not calculate tax on shipping regardless of other settings.

#### Step 2: Configure shipping tax class

Confirm “Shipping Tax Class” is set to the appropriate value under **WooCommerce > Settings > Tax** in the Tax Options section. This value should be:

**Same as cart items** – shipping tax will inherit the highest-priority tax class applied to cart contents. That is:

- If all items in the cart fall into the same tax class, the shipping tax rate will be taken from that tax table
- If more than one tax class is represented among the products in the cart, and any of the products falls into the Standard tax class, it will use Standard rates for shipping
- If more than one tax class is represented among the products in the cart, and none of them are in the Standard tax class, it will use the top-most tax class in the [Additional Tax Rates](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#additional-tax-classes) list that matches at least one product in the cart for shipping rates – [example here](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#shipping-tax-class)

**A specific tax class** (for example: Standard, Reduced Rate) – shipping will be taxed using that class regardless of cart contents.

#### Step 3: Verify tax table configuration

Check that all tax tables that might be used for shipping rates include a row with the “Shipping” checkbox checked. Tax tables can be found on the **WooCommerce > Settings > Tax** tab; check for various rates tables (such as “Standard Rates”) as small links across the top of the tab.

**Confirm the following:**

- The tax rate matches the customer’s location
- The “Shipping” column is checked
- The rate is not overridden by another matching rate with the box unchecked

**Important:** If no applicable rate allows shipping, shipping will not be taxed, even if the shipping method and class are configured correctly.

#### Step 4: Review product-level tax settings

Review product-level tax settings under **Products > Edit Product > Product Data > General**.

WooCommerce will not apply tax to shipping if the cart contains only non-taxable items, and you’re using the “Same as cart items” shipping tax class.

**Confirm for at least one product in the order:**

- Tax Status is set to **Taxable**
- Tax Class is correctly assigned (for example: Standard)

If you’ve enabled Geolocate under **WooCommerce > Settings > General > Default customer location**, WooCommerce attempts to automatically determine a visitor’s location to display location-specific tax rates and shipping options.

However, if customers aren’t seeing taxes until they enter their address, or prices appear incorrect, it’s often due to one of the following:

#### MaxMind Geolocation is not set up correctly

Geolocate in WooCommerce relies on the MaxMind GeoIP database to geolocate customers. To function correctly, this database must be [downloaded and linked using a MaxMind license key](https://woocommerce.com/document/maxmind-geolocation-integration/).

WooCommerce will then automatically download and update the necessary database file. Once this is configured, your store will geolocate customers using MaxMind.

#### Tax-inclusive pricing complications

If your store is configured to display prices inclusive of tax, and you’re selling to multiple countries, this can cause prices to appear differently depending on:

- The customer’s geolocated country
- Whether or not Geolocate has accurately determined their location
- Whether they’ve already entered their full address at checkout

Until a customer confirms their location (for example: by entering a shipping or billing address), tax-inclusive prices may default to your store’s base location tax rates, or may not display tax at all if Geolocate isn’t functioning properly.

#### Best practices for Geolocate

- Always ensure MaxMind Geolocation is set up and active
- Consider enabling **Geolocate (with page caching support)** if you use full-page caching or CDN-level caching
- Be cautious with tax-inclusive pricing when selling internationally, as the displayed tax amount can vary based on detected or confirmed location

If you are using the [WooCommerce Tax](https://woocommerce.com/document/woocommerce-shipping-and-tax/woocommerce-tax/) plugin to calculate taxes automatically, some common issues include:

- **Taxes not calculating for some states in the United States** (usually an issue of where your [tax nexus](https://stripe.com/en-ca/resources/more/nexus-tax-101) is)
- **Show prices inclusive of tax setting is disabled**
- **Taxes not calculating for U.S. Territories**

You can find information on how to debug these issues in our [WooCommerce Tax Troubleshooting Guide](https://woocommerce.com/document/woocommerce-tax/).

A staging site is a clone of your live WooCommerce store used for safe testing and debugging. It allows you to replicate issues – like tax miscalculations or potential conflicts – without disrupting your customers or risking live data.

**Benefits of staging site testing:**

- If you isolate an issue in a staging environment, our Happiness Engineers can more quickly replicate and report the issue to be addressed
- If the issue does not occur on the staging site, it may indicate a conflict on your live site rather than a problem with your WooCommerce settings

**How to create a staging site:** Most hosting providers offer one-click staging environments, or you can create one using plugins like [WP Staging](https://wordpress.org/plugins/wp-staging/). For detailed instructions, refer to the articles:

- [What is a WordPress Staging Site and How Do You Set One Up?](https://wordpress.org/support/article/wordpress-staging-site/)
- [How to Test for Conflicts](https://woocommerce.com/document/how-to-test-for-conflicts/)

#### Using Blueprints for testing

**Starting with WooCommerce 9.9:** [Blueprints](https://woocommerce.com/document/woocommerce-blueprints/) is a tool for importing and exporting store settings that can also help set up a test site quickly. You can find Blueprints under **WooCommerce > Settings > Advanced > Blueprint**.

With Blueprints, you can export your store settings – including Tax settings – for troubleshooting, then import them into a newly created WordPress/WooCommerce site to test; then run a similar conflict test to verify that the basic tax settings are correct.

Caching can serve outdated content, affecting tax calculations. To address this:

1. **Clear all caches** – including browser, plugin, and server-level caches
2. **Exclude dynamic pages** – exclude Cart, Checkout, and My Account from caching
3. **Ensure WooCommerce sessions and cookies are not cached**

You can learn more about configuring caching plugins for WooCommerce on our [How to configure caching plugins for WooCommerce developer documentation](https://woocommerce.com/document/configuring-caching-plugins/).

Charging taxes can quickly become complicated when:

- You need to charge taxes in more than one geographical area or country
- You need to charge taxes that are heavily address-dependent, such as county and city taxes
- You need to charge taxes at different rates for special classes of products
- You need to be able to grant tax exemptions to specific customers, such as non-profits
- You need advanced reporting that can compile data from different platforms and integrations

Maintaining manual tax tables in these cases can be labor-intensive. If your store has complex tax requirements, you may need a more advanced tax plugin.

**Important disclaimer:** We are not tax professionals; our advice only applies to how to use our software. For advice on what — or when — to charge tax/VAT/GST etc., we recommend consulting a tax professional or accountant. Every business is unique, and we are unable to cover all possibilities here.

All three of these options require an external account that charges for their services. Charges are based on the number of API calls per month and the number of annual filings required. These external services may have varying accessibility support; check their documentation or contact their support teams for confirmation.

#### Comparison of advanced automatic tax calculation plugins

You may also need to provide tax exemptions to some shoppers based on their role, country, or quantity of purchases.

#### EU VAT exemptions

A common use case is exempting EU businesses from VAT (Value-added tax) when they provide a valid VAT number and are located outside your store’s home country.

**Available plugins:**

- **EU VAT Number** – note that this plugin does not support EU VAT Number checking for businesses in the UK
- **EU/UK VAT Validation Manager** – note that this is a third party plugin that is not developed or supported by WooCommerce; please use the public forum for that plugin for questions and support

#### Other common tax exemption scenarios

- **Tax Exempt for WooCommerce** – mark certain user roles or specific customers as tax exempt
- **Role Based Tax** – show taxes as inclusive or exclusive based on user role
- **Disability VAT Exemption** – set up VAT exemptions for charities or disabled customers
- **Ultimate Tax Exemption** – exempt customers from tax based on country, and allow other customers to apply for tax-exempt status via a form

More tax-related plugins for complex exemption scenarios can be found in our [marketplace](https://woocommerce.com/product-category/woocommerce-extensions/).

If you’re trying to sync WooCommerce taxes with an external system (such as an accounting or reporting tool), the setup and compatibility depend on that specific integration.

#### Xero integration

For more information about syncing tax information with Xero:

- [Ensure that you have configured the settings correctly here](https://woocommerce.com/document/xero/)
- Enable debug and check the logs
- [Check solutions to common issues here](https://woocommerce.com/document/xero/#troubleshooting)
- [Check common Xero log error messages here](https://woocommerce.com/document/xero/#common-error-messages)

#### QuickBooks integrations

**QuickBooks Integration for WooCommerce by WPSwings:**

- Contact [WPSwings support](https://wpswings.com/contact-us/)

**QuickBooks Sync for WooCommerce by MyWorks Software:**

- Contact [MyWorks support](https://myworks.software/support)

If you’re trying to sync WooCommerce taxes with an external system (such as an accounting or reporting tool), the setup and compatibility depend on that specific integration.

For more information about syncing tax information with:

**Important disclaimer:** This is intended for advanced use cases and may not be suitable for all stores. Custom code may impact accessibility or compliance. Test with assistive technology before using on a live site.

**Safety guidelines:**

- Never add custom code directly to your parent theme’s `functions.php` file, as it will be overwritten when the theme is updated
- Instead, add code to your child theme’s `functions.php` file, or use a plugin that supports custom snippets—such as the [Code Snippets plugin](https://wordpress.org/plugins/code-snippets/)
- Always test any custom code on a staging site before applying it to your live store

**Note:**This document is meant to serve as a helpful guide for advanced troubleshooting; however, the procedures described are beyond the scope of our [support policy](https://woocommerce.com/support-policy/) and we cannot provide direct assistance with implementing them. If you would like to seek assistance from a qualified WordPress/WooCommerce developer, we highly recommend [Codeable](https://codeable.io/?ref=z4Hnp) or a [Woo Agency Partner](https://woocommerce.com/development-services/).

If a store enters product prices including taxes, but levies various location-based tax rates, the prices will appear to change depending on which tax rate is applied. In reality, the base price remains the same, but the taxes influence the total. [Follow this link for a detailed explanation](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#prices-entered-with-tax).

Some merchants prefer to dynamically change product base prices to account for the changes in taxes and so keep the total price consistent regardless of tax rate. This snippet will enable that functionality:

```
add_filter( 'woocommerce_adjust_non_base_location_prices', '__return_false' );
```

The following snippet is useful in cases where a store only adds taxes when the subtotal reaches a specified minimum. In the code snippet below, that minimum is 110 of the store’s currency. Adjust the snippet according to your requirements:

```
add_filter( 'woocommerce_product_get_tax_class', 'big_apple_get_tax_class', 1, 2 );

function big_apple_get_tax_class( $tax_class, $product ) {
    if ( WC()->cart->subtotal <= 110 ) {
        $tax_class = 'Zero Rate';
    }

    return $tax_class;
}
```

Some merchants may require different tax rates to be applied based on a customer role to accommodate for wholesale status or tax exemption.

In this snippet, users with “administrator” capabilities will be assigned the Zero rate tax class. Adjust it according to your requirements:

```
/**
 * Apply a different tax rate based on the user role.
 */
function wc_diff_rate_for_user( $tax_class, $product ) {
    if ( is_user_logged_in() && current_user_can( 'administrator' ) ) {
        $tax_class = 'Zero Rate';
    }

    return $tax_class;
}

add_filter( 'woocommerce_product_get_tax_class', 'wc_diff_rate_for_user', 1, 2 );
add_filter( 'woocommerce_product_variation_get_tax_class', 'wc_diff_rate_for_user', 1, 2 );
```

Taxes that have 0-value are hidden by default. Adding the following snippet will show them regardless:

```
add_filter( 'woocommerce_order_hide_zero_taxes', '__return_false' );
```

One of the tax settings for WooCommerce enables the use of suffixes to add additional information to product prices. It’s available for use with the variations of a variable product, but is disabled at the main variation level as it can impact website performance when there are many variations.

The method responsible for the related price output can be customized via filter hooks if needed for variable products. This will require customization that can be implemented via this filter:

```
add_filter( 'woocommerce_show_variation_price', '__return_true' );
```

Use this snippet to display custom tax rows without affecting totals on the cart and checkout pages:

```
// Show shipping and product taxes separately
function custom_display_tax_rows() {
    // Get the cart instance
    $cart = WC()->cart;

    // Get the shipping tax total
    $shipping_tax_total = $cart->get_shipping_tax();

    // Get the product tax total
    $product_tax_total = $cart->get_cart_contents_tax();

    // Calculate the total tax (excluding shipping tax)
    $total_tax = $product_tax_total;

    // Display custom rows for Shipping Tax, Product Tax, and Total Tax
    if ( $shipping_tax_total > 0 ) {
        echo '<tr class="shipping-tax-row">';
        echo '<th>' . __( 'Shipping Tax', 'your-text-domain' ) . '</th>';
        echo '<td>' . wc_price( $shipping_tax_total ) . '</td>';
        echo '</tr>';
    }

    if ( $product_tax_total > 0 ) {
        echo '<tr class="product-tax-row">';
        echo '<th>' . __( 'Product Tax', 'your-text-domain' ) . '</th>';
        echo '<td>' . wc_price( $product_tax_total ) . '</td>';
        echo '</tr>';
    }

    // Display the total tax only if it's greater than zero
    if ( $total_tax > 0 ) {
        echo '<tr class="order-tax-row">';
        // You might want to show something here; this row is currently empty.
        echo '</tr>';
    }
}

// Hook the function to run when the cart is displayed
add_action( 'woocommerce_cart_totals_after_shipping', 'custom_display_tax_rows', 5 );

// Hook the function to run when the checkout is displayed
add_action( 'woocommerce_review_order_before_order_total', 'custom_display_tax_rows', 5 );
```

WooCommerce calculates tax based on store configuration, tax classes, and rounding settings. In some cases, particularly when using tax-inclusive pricing, small rounding discrepancies may occur, especially when multiple quantities are added to the cart. These are typically the result of how tax is calculated and rounded, and are common across eCommerce platforms.

#### Rounding configuration

You can control how tax is rounded in **WooCommerce > Settings > Tax** under the “Rounding” option:

**Per-line rounding (default):** Tax is calculated and rounded for each line item before totals are added.

**Subtotal-level rounding:** Tax is calculated from the subtotal of all items and rounded once.

Which option to use depends on your tax jurisdiction and how your product pricing is structured. Subtotal-level rounding can reduce minor discrepancies in total tax amounts, but may cause differences when comparing per-item tax breakdowns.

#### Off-by-one rounding

Rounding errors (for example: totals off by 0.01) can occur when prices include tax and customers purchase multiple quantities. This happens when tax is calculated per unit and rounding is applied to each item individually.

#### Display setting mismatches

WooCommerce relies on consistent configuration across these settings:

- Prices entered with tax
- Display prices in the shop
- Display prices during cart and checkout

If these settings are inconsistent (for example: entered with tax, but displayed excluding tax), WooCommerce will reverse-calculate prices using extended precision, which can result in rounding differences. A warning banner appears in the admin when settings are mismatched. You can resolve this using the “Use recommended settings” prompt.

#### Customizing rounding behavior

For stores with strict rounding requirements, WooCommerce provides filters that allow developers to override price and tax behavior. As every site is unique, this code would vary based on the products, prices, and tax rules for your shop. Experimentation would be required to get the exact rounding required.

As an example, this code forces rounding per unit before multiplying by quantity, which worked for one specific shop and its products:

```
add_filter( 'woocommerce_get_price_excluding_tax', 'custom_rounding_per_unit', 10, 3 );
function custom_rounding_per_unit( $price, $qty, $product ) {
    return round( $price / $qty, 2 ) * $qty;
}
```

If you’ve tried the [Common Tax Troubleshooting Scenarios](https://woocommerce.com/document/troubleshooting-core-taxes/#common-issues-with-core-tax-tables) without success, reach out to [WooCommerce support](https://woocommerce.com/my-account/create-a-ticket/) with the following information:

**Required information for support requests:**

- A summary of your goal, comparing your expected results to the actual behaviour you’re experiencing
- A list of steps to help us reproduce the problem
- The link to your staging site and to the product affected by the issue (alternately, you can send us your site’s [Blueprint](https://woocommerce.com/document/woocommerce-blueprints/) so we can recreate your settings for testing)
- A copy of your system status report [which can be accessed by](https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/#system-status) navigating to **WooCommerce > Status > System Status > Get System Report**
- Your most recent error log: For issues with WooCommerce Tax, make sure you have [logging enabled](https://woocommerce.com/document/woocommerce-shipping-and-tax/woocommerce-tax/#troubleshooting) and include the most recent error log from **WooCommerce > Status > WooCommerce Shipping & Tax**

#### WooCommerce Marketplace plugins

If you’re using a tax extension listed on the [WooCommerce Marketplace](https://woocommerce.com/product-category/woocommerce-extensions/) – such as WooCommerce Tax, TaxJar, Avalara for WooCommerce, or Stripe Tax – you can contact [WooCommerce Support](https://woocommerce.com/my-account/create-a-ticket/) for help. These plugins are actively supported and maintained in collaboration with their developers.

#### Third-party plugins

If you’re using a tax plugin not available on the WooCommerce Marketplace, such as one downloaded from another source or custom-developed, support should be obtained directly from the plugin’s developer. Since these plugins are maintained independently, their developers are the most qualified to assist with installation, configuration, and troubleshooting.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

If you experience accessibility issues with this page, please [contact WooCommerce Support](https://woocommerce.com/accessibility/).

