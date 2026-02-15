---
title: Bulk Editing Products
url: https://woocommerce.com/document/bulk-editing-products/
---

Much like WordPress’ other post types that let you assign categories, tags or post statuses en masse, WooCommerce products also have a bulk editing feature.

This document covers the bulk editing options for WooCommerce products accessible from the Products list screen. Refer to [built-in product CSV importer and exporter](https://woocommerce.com/document/product-csv-importer-exporter/) for an alternative bulk edit approach that can leverage spreadsheets, or refer to [Adding and Managing Products](https://woocommerce.com/document/managing-products/) for individual product management.

To access bulk editing features:

1. Navigate to **Products > All Products**.
2. Tick the checkbox on the left hand side for two or more products in the list.
3. Select **Edit** from the **Bulk Actions** menu at the top or bottom of the list.
4. Click **Apply** to enter the world of bulk editing.

An edit screen with the bulk editing fields appears, changes made here will be applied to all the selected products when you hit the **Update** button, visible to the bottom-right of the edit window.

Below are the default WooCommerce fields one might encounter. Extensions that have been added to your store may add additional options of their own.

- **Bulk Edit** – shows the currently selected products that will be affected. Click the *x*to remove a particular product from the active bulk edit session.
- **Product Categories** – a list of your product categories that can be ticked or unticked to assign or remove them from the selected products.
- **Comments** – can be set to either **Allow** and **Do not allow**
- **Status –** reflecting the product’s published status, options include **Published, Private, Pending Review,**or**Draft**
- **Product Tags**– once you start typing, existing product tags are offered as options to click. Otherwise, add one or more new tags, separated by commas.
- **Price** – options include **Change to, Increase existing price by (fixed amount or %),**or **Decrease existing price by (fixed amount or %)***.*After an option is selected, an additional **Enter Price ($)** field is added to which you can add the number reflecting your choice.
- **Sale***–*options are
- **Change to** – this will change the **Sale Price(s)** to the amount specified
- **Increase existing sale price by (fixed amount or %)** – if a Sales Price already exists, it can be increased via this option by typing just a number for a fixed amount, or a number followed by % for a percentage of the existing Sales Price.
- **Decrease existing sale price by (fixed amount or %)** – if a Sales Price already exists, it can be decreased via this option by typing just a number for a fixed amount, or a number followed by % for a percentage of the existing Sales Price.
- **Set to regular price decreased by (fixed amount or %)** – override the existing Sales Price with a new price based on the Regular Price decreased by either a fixed amount (if specifying a number only) or a percentage (a fixed number followed by %). **Selecting this option and either leaving the value blank or specifying 0, will remove the Sales Price from the product(s).**
- Selecting any of the options reveal an additional **Enter sale price ($)** field.
- **Tax status**– can be **Taxable, Shipping only** or **None**.
- **Tax class** – options will show the default **Standard rates**, plus whatever else you have configured under WooCommerce > Settings > Tax > Tax Options > Additional tax classes, which normally includes**Reduced rate rates**, and **Zero rate rates**.
- **Weight** – only has one option; **Change to**. When selected, an additional field is added with which to adjust the weight.
- **L/W/H** – Should the **Change to** option be selected, 3 additional fields for *Lenght, Width*and *Height* respectively, are added.
- **Shipping class** – options will include **No Shipping**, plus whichever classes have been configured under WooCommerce > Settings > Shipping > Shipping Classes.
- **Visibility** – in reference to the product visibility in store, the option are **Catalog & search, Catalog, Search**, and**Hidden**.
- **Featured**– simply **Yes**or****No**.
- **In stock**– options are **In stock, Out of Stock** or **On backorder**.
- **Manage Stock***–***Yes**or**No***.*
- **Stock Qty** – option are **Change to, Increase existing stock by**, or **Decrease existing stock by**.
- **Backorders?** – can be set to **Do not allow, Allow but notify the customer**, or **Allow**.
- **Sold individually?** – options are either **Yes** or **No**.

Bulk editing from the **All Products** page works best with Simple products, and cannot edit the complexities of variable, grouped, or other complicated products.

To bulk edit all the variations of a single variable product check our [variable products documentation](https://woocommerce.com/document/variable-product/#bulk-editing)

Bulk editing can only be applied to products that are visible and can be ticked for inclusion in a bulk editing session.

**Increase the number of products** visible on any one page by going to **Screen Options > Number of items per page**. Be aware that loading and editing excessively high numbers of products on one page might strain your server, and take a long time to update. If you encounter issues with larger numbers of products, try working in smaller batches.

**Filter by category, product type, or stock status** by selecting the relevant attributes from the dropdowns at above the product lists, and clicking the **Filter** button.

**Sort products by column ascending or descending** by clicking on hyperlinked column headings. By default Name, SKU, Price and Date (published) columns can be used for this type of sorting.

Quick editing is similar to Bulk editing, but applies to one product only. To access Quick editing, hover over a particular product to reveal its links, and then select **Quick editing**.

It’s exactly the same as Bulk editing, except that because only one product is involved, the product’s current values are shown in the fields instead of **– No Change –** as is the case when bulk editing.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

