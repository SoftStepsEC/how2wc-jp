---
title: Setting up Shipping Zones
url: https://woocommerce.com/document/setting-up-shipping-zones/
---

If you sell physical products on your WooCommerce store, you need to configure shipping zones. Shipping Zones are the foundation for most shipping options/configurations in WooCommerce. How you configure your shipping zones determines the shipping options and rates customers see on the cart and checkout pages.

This page outlines three steps to configure shipping zones in WooCommerce:

1. Create and configure shipping zones.
2. Add shipping methods to shipping zones.
3. Manage shipping zones and shipping methods.

You can add as many shipping zones or shipping methods as you need to your shipping settings; there’s no limit.

A **Shipping Zone** is a geographical area to which you ship items. Shipping zones can be as specific as you need. You can set them to specific postal/zip codes, specific geographical regions, entire countries, etc. There are three important things to keep in mind about how your customers will match with shipping zones and see shipping options:

- Customers only see the methods available for their address and its corresponding shipping zone.
- Shipping zones are assigned based on the first one the customer matches with.
- Each customer matches only **one** shipping zone.

For example, you could create these shipping zones in WooCommerce:

Notice that each shipping zone serves a different geographical region and offers different shipping methods depending on the customer’s location.

Setting up shipping in WooCommerce starts with adding shipping zones. This section will guide you through the following steps:

1. Adding a shipping zone
2. Configuring a shipping zone
3. Adding shipping methods to a shipping zone
4. Sorting shipping zones
5. Editing and deleting shipping zones

**Prerequisite:** Go to **WooCommerce > Settings** and check that your **shipping location** is configured properly on the **general** settings tab.

Visiting **WooCommerce > Settings > Shipping**for the first time, you’ll notice two things:****

- A prompt to add a new shipping zone
- A default shipping zone called **Rest of the world**

The **Rest of the world** zone is used for customers that do not match any of the shipping zones you add. Adding methods to this zone is **optional.**

If you use the **Rest of the world**shipping****zone but want to exclude certain regions, you can do that by adding a shipping zone for the region you want to exclude without any shipping methods assigned to it.

Follow these steps to add a shipping zone:

1. Go to: **WooCommerce > Settings > Shipping > Shipping zones**.
2. Click **Add zone** at the top.
3. Enter a descriptive **Zone name**.
4. Select the **Zone regions** that apply. Regions can consist of: Countries, States/Provinces, Continents.
5. Optional: **Limit to specific zip/postcodes** to further narrow which customers match this zone. Zip/Postcodes must be entered one code per line.

1. **Add Shipping Methods** to this zone.
2. **Save changes**.

A wildcard can be used to capture all postcodes that share the same beginning, so it is the recommended option for postcodes with non-numeric characters. Examples:

– 902* would capture 90210 and also 90288-1234; – CB23* would capture CB23 1EX; – CB2* would capture CB2 3AA and CB23 1EX.

**Using wildcards in numeric ranges (e.g., 902*…990*)is not supported.**

Below is an example of what a completed set of shipping zones looks like:

Sorting shipping zones accurately ensures that your customers see the correct shipping options on the checkout page. Two reminders about shipping zones:

- **Shipping zones** match customers based on their **shipping address** and customers can only match one shipping zone.
- Zones are matched in a **hierarchy**, or from the top of the list to the bottom of the list. WooCommerce will choose the first shipping zone that a customer matches and show those options to the customer on the cart/checkout pages.

**How do I make sure customers see the right shipping zones and shipping options?**

Match customers to the correct shipping zone by ordering the shipping zones from the **smallest** geographical area to the **largest** geographical area. For example, if you have shipping zones for cities, countries, and states/provinces you’ll want to order them as follows:

1. City
2. State/Province
3. Country

If your customers aren’t seeing the correct shipping methods on the cart and checkout pages, the shipping zones are most likely in the wrong order.

To sort shipping zones in the shipping settings:

1. Go to: **WooCommerce > Settings > Shipping > Shipping Zones**.
2. **Click and hold** on the handles on the left side of the shipping zone (next to the name) and **drag** the shipping zone to the correct place in the list.
3. Click **Save changes** to finish.

Editing and deleting shipping zones can be done on the same page as adding them. The **edit** and **delete** options are on the right side of the shipping zone list.

Follow these steps to edit or delete a shipping zone:

1. Go to **WooCommerce > Settings > Shipping > Shipping Zones**.
2. Select Edit or Delete on the right side of the shipping zone.
  - Use **Edit** to revise the name, regions, or shipping methods
  - Use **Delete** to remove the shipping zone.
  
3. **Save changes**.

The next step is to add shipping methods to the shipping zone that you created. Shipping methods are the shipping options that customers will see on the checkout page. WooCommerce has three core shipping methods built-in: [Flat Rate](https://woocommerce.com/document/flat-rate-shipping/), [Free Shipping](https://woocommerce.com/document/free-shipping/), and [Local Pickup](https://woocommerce.com/document/local-pickup/).

1. Go to **WooCommerce > Settings > Shipping > Shipping zones**.
2. Click **Edit** on the shipping zone where you want to add a shipping method.

1. Click **Add shipping method** at the bottom of the screen.

1. Select the shipping method you want to add and click the **Continue** button.

Need help setting up core shipping methods? Refer to the documentation below for specific configuration steps for each:

- [Configuring Local Pickup – Legacy/Classic Checkout](https://docs.woocommerce.com/document/local-pickup/)
- [Configuring Local Pickup – Cart/Checkout Blocks](https://woocommerce.com/document/woocommerce-blocks-local-pickup/)
- [Configuring Flat Rate Shipping](https://woocommerce.com/document/flat-rate-shipping/)
- [Configuring Free Shipping](https://woocommerce.com/document/free-shipping/)

Sorting shipping methods determines their order in the list of available shipping options customers see on the cart and checkout pages. All shipping methods in the shipping zone that matches with a customer will show on the cart/checkout pages.

Follow these steps to sort shipping methods within a shipping zone:

1. Go to **WooCommerce > Settings > Shipping > Shipping Zones** and click **edit** next to the zone with the shipping methods you want to sort.
2. **Click and hold** on the handles on the left side of the shipping method (next to the name) and **drag** the shipping method to the correct place in the list.
3. Click the **save** button to finish making changes.

The **default selected shipping method** is the first, enabled shipping method in the shipping zone that the customer matches with.

To deactivate or completely remove shipping methods from a shipping zone:

1. Go to **WooCommerce > Settings > Shipping > Shipping zones**.
2. Use the Edit link on the shipping zone from which you want to remove a shipping method. Complete one of these two actions:
  - Toggle the switch under the **Enabled** column to deactivate the shipping method.
  - Use the **Delete** link to remove the shipping method.
  
3. **Save Changes**.

Customers see the shipping methods, as options to select, from their matched shipping zone on the cart page after they use the “**Calculate Shipping**” link. Below is an example of the configured shipping zones and shipping methods, as well as how customers will see those options on the cart page:

- In the 90210 zip code in California, we offer Free Shipping.
- In the United States, we offer a Domestic Flat Rate.
- In North America, we offer a second, different Flat Rate.
- For the rest of the world, we offer a third, different Flat Rate.

This is what our customers would see if they use the **Calculate Shipping** option:

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

