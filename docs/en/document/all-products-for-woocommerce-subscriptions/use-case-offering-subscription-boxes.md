---
title: Use Case: Coffee Beans Subscription Box
url: https://woocommerce.com/document/all-products-for-woocommerce-subscriptions/use-case-offering-subscription-boxes/
---

You’ve always wanted to roast your own beans. You love the smell of coffee in the morning so much that you’ve started a store selling your coffee creations. You now want to offer your roasts on subscription, but need a bit of flexibility as your business is growing quickly:

- You have learned that you can acquire more customers if you make your beans available both as a one-time purchase and on subscription.
- You need to start managing your inventory of coffee beans more accurately: One-time purchases and subscription deliveries of a coffee bean variety should pull stock from the same SKU.
- In addition to selling coffee beans individually, you would love to offer them in a pick-and-mix bundle. Customers will be able to personalize its contents according to their taste and, optionally, purchase it on subscription.
- Finally, you would like to give your bundle subscribers the freedom to change the contents of their bundle.

In short, you want to build a state-of-the-art subscription box store with WooCommerce. Here’s how to do it!

WooCommerce Subscriptions is the perfect tool for selling recurring products or services, as it can reliably manage thousands of active subscriptions for you. However, there are a couple things it can’t do out-of-the-box:

**1. It does not allow the same product to be offered both as a one-time purchase and on subscription.**

Depending on the kind of Subscription Box you want to sell, some customers may not be willing to commit to a subscription before they’ve had a chance to try what you offer. To work around this limitation, you could create another WooCommerce product and offer that as a one-time purchase. However, doing so will unnecessarily complicate inventory management for you.

**2. It works only with dedicated Subscription product types.**

WooCommerce Subscriptions introduces a new Subscription product type that lets you define a billing schedule for your recurring product/service. It also allows you to create Variable Subscription products with multiple subscription options and/or configurable attributes. However, a Subscription Box usually consists of multiple products that need to be inventory-managed individually. This is a complex problem that can’t be solved with WooCommerce Subscriptions alone.

While these limitations won’t necessarily prevent you from building a Subscription Box store with WooCommerce Subscriptions, they can complicate things as your business grows. That’s where All Products for WooCommerce Subscriptions and WooCommerce Product Bundles come in handy:

**All Products for WooCommerce Subscriptions** is a WooCommerce Subscriptions add-on that allows you to add subscription plans to existing products. To purchase a product on subscription, customers may choose a plan before clicking the Add to Cart button. You can also use it to:

- Purchase entire carts on subscription.
- Add products to existing subscriptions.

**WooCommerce Product Bundles** allows you to create assembled products and customizable, pick-and-mix boxes. The extension has been around since the early days of WooCommerce and has been battle-tested on many high-traffic sites.

**Tip**: If the box you want to offer consists of configurable parts, and you want to offer multiple product options for each part, check out [Composite Products](https://woocommerce.com/products/composite-products/) instead of Product Bundles. Here’s an example to understand the difference between the two extensions: Product Bundles would be the right choice if you need to offer a complete skateboard that customers can’t personalize in any way. Composite Products would be a better option if you want to build a skateboard configurator that customers will use to pick a custom deck, wheels, etc for their personalized skateboard.

Here’s a complete list of plugins/extensions you’ll need to set up a Subscription Box store with WooCommerce:

- [WooCommerce](https://woocommerce.com) (free)
- [WooCommerce Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/)
- [All Products for WooCommerce Subscriptions](https://woocommerce.com/products/all-products-for-woocommerce-subscriptions/)
- [WooCommerce Product Bundles](https://woocommerce.com/products/product-bundles/)
- [Storefront](https://woocommerce.com/storefront/) (free)

To get started:

1. Purchase [WooCommerce Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/), [All Products for WooCommerce Subscriptions](https://woocommerce.com/products/all-products-for-woocommerce-subscriptions/) and [WooCommerce Product Bundles](https://woocommerce.com/products/product-bundles/).
2. Download the 3 .zip files from your WooCommerce account.
3. Starting with **WooCommerce Subscriptions**, go to **Plugins > Add New > Upload** and select its .zip file.
4. Click **Install Now**, and then **Activate**.
5. Repeat for **All Products for WooCommerce Subscriptions** and **WooCommerce Product Bundles**.

If you are only interested in creating a pick-and-mix subscription box, you can skip this step.

Assuming you have already created the **Spicy**, **Nutty**, **Fruity** and **Woody** **Beans** products, here’s how you can offer them on subscription:

1. Go to **WooCommerce > Products** and locate the **Spicy Beans**product.
2. **Edit** the product.
3. Go to **Product Data > Subscriptions**.
4. Click **Add Plan** to add a subscription plan. Every plan you add here will create an option that customers can choose before adding the product to their cart.
5. Repeat the previous step to add more plans.
6. **Optional**: To provide an incentive for subscribing, consider [offering a discount](https://woocommerce.com/document/all-products-for-woocommerce-subscriptions/store-owners-guide/#subscription-discounts) with each plan.
7. **Update** the product to save your changes.

To **create a new Product Bundle**:

1. Go to **WooCommerce > Products** and click **Add Product**.
2. Enter a **Title**, **Description** and **Short Description**.
3. Locate the **Product Data** panel and select the **Product bundle** type.

Then, **add bundled products** to it:

1. Go to the **Bundled Products** tab in the left menu.
2. Use the search field to find the **Spicy Beans** product.
3. Click on its title to add it.
4. Repeat to add the remaining Coffee Bean products to your Box.
5. To require customers to choose exactly 4 items, enter **4** in the **Min Bundle Size** and **Max Bundle Size** fields.

Next, **configure pricing options**. Customers should be free to choose any combination of 4 coffee bean packs, and pay for each pack individually:

1. Go to the **General** tab in the left menu and make sure that the **Regular Price** and **Sale Price** fields are blank.
2. Go to the **Bundled Products** tab. In the **Basic Settings** section of each bundled item, check the **Priced Individually** option.

Then, **configure shipping options**. The next steps assume that you are going to **assemble** the selected coffee bean packs in a special box you’ve built for this purpose:

1. Ensure that the **Virtual** option is unchecked.
2. Go to the **Shipping** tab on the left menu.
3. Enter the weight and dimensions of your box, and/or optionally assign a **Shipping Class** to it.
4. Go to the **Bundled Products** tab on the left menu.
5. Open/expand all bundled products and ensure that **Shipped Individually** is **unchecked**.

1. Go to **WooCommerce > Products** and locate the****bundle you just created.
2. **Edit** the product.
3. Go to **Product Data > Subscriptions**.
4. Click **Add Plan** to add a subscription plan. Every plan you add here will create an option that customers can choose before adding the product to their cart.
5. Repeat the previous step to add more plans.
6. **Optional**: To provide an incentive for subscribing, consider [offering a discount](https://woocommerce.com/document/all-products-for-woocommerce-subscriptions/store-owners-guide/#subscription-discounts) with each plan.
7. **Update** the product to save your changes.

1. Go to **WooCommerce > Settings > Subscriptions**.
2. Locate the **Switching** section.
3. Enable **Allow Switching > Between Subscription Plans** and **Allow Switching > Between Bundle Configurations**.

When this option is enabled, customers who view an active subscription from **My Account > Subscriptions** will see an **Upgrade or Downgrade** button next to every product with configurable content or multiple subscription plans.

You can change the text of this button from **WooCommerce > Settings > Subscriptions > Switching > Switch Button Text**.

When clicking this button, customers will be taken to the Subscription Box page, where they can choose a new configuration. Currently, it is only possible to modify the contents of a subscribed bundle — plan changes are not supported just yet.

Now customers can:

**1. Purchase your individual coffee bean packs one-time, or on subscription.**

**2. Purchase a personalized box with 4 coffee bean packs, one-time or on subscription.**

**3. Modify the contents of their personalized subscription box mid-term.**

