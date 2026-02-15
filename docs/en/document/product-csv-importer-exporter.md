---
title: Product CSV Importer and Exporter
url: https://woocommerce.com/document/product-csv-importer-exporter/
---

The CSV import and export tool in WooCommerce is a powerful feature designed to streamline the management of your online store’s product and customer data. This tool allows store owners to easily import large volumes of products in bulk, including their attributes, categories, and images, directly into WooCommerce using a CSV file. Additionally, it supports the export of product and customer data, enabling seamless data migration, backup, and analysis. With its user-friendly interface and flexibility, the CSV import and export tool simplifies the process of updating and maintaining your store’s inventory, ensuring efficient data handling and improved store operations.

To get started importing or exporting products, head to **Products > All Products**. There you’ll see **Import** and **Export** buttons next to the “Add New” Product button.

- First-time store owners get started more quickly by exporting and importing products during setup.
- Existing store owners can update tens or hundreds of products with new info or place them on sale, or sync multiple storefronts.

**Note:**

If you are using our premium extension `Product CSV Import Suite`, refer to documentation at: [Product CSV Import Suite](https://woocommerce.com/documentation/plugins/woocommerce/woocommerce-extensions/product-csv-import-suite/).

We recommend using:

- Online spreadsheet editor [Google Drive / Docs](https://drive.google.com/)
- Free spreadsheet app in [OpenOffice](http://www.openoffice.org/)
- Free Calc app in [LibreOffice](http://www.libreoffice.org/)
- [Numbers for macOS](https://www.apple.com/numbers/)

If possible, we recommend avoiding Microsoft Excel, as we’ve seen it have formatting and character encoding issues. But regardless of what tool you use, always ensure you *export* as a CSV file, following the [guidelines](https://woocommerce.com/document/product-csv-importer-exporter/#general-guidelines) below.

To import new products or update existing products, you need a CSV containing your product information. You can:

- [Export](https://woocommerce.com/document/product-csv-importer-exporter/#expoort) a CSV of products from an existing store.
- Download a [CSV file with sample data from GitHub](https://github.com/woocommerce/woocommerce/tree/trunk/plugins/woocommerce/sample-data)and replace the sample data with information for your products.
- Create or bring your CSV. Any information you wish to import must follow the formatting and columns of the [Product CSV Import Schema](https://woocommerce.com/document/product-csv-importer-exporter/#product-csv-import-schema).

**Note:**

If using the built-in WooCommerce Product CSV Importer and Exporter tool to export a CSV, it already follows the schema and is ready to use. If using the blank and formatted CSV file, it also follows the schema; just be sure to enter the info as instructed at [Product CSV Import Schema.](https://woocommerce.com/document/product-csv-importer-exporter/#product-csv-import-schema)

- CSVs should be in UTF-8 format.
- Dates should be defined for the store’s local timezone.
- Use 1 or 0 in your CSV, if importing a Boolean value (true or false).
- Multiple values in a field get separated with commas.
  - See [Comma handling](https://woocommerce.com/document/product-csv-importer-exporter/#comma-handling) section below if importing category names with commas in them.
  
- Wrapping values in quotes allows you to insert a comma.
- Prefix the ID with `id:` if referencing an existing product ID. No prefix is needed if referencing a SKU. For example: `id:100`, `SKU101`.
- Taxonomy term hierarchy is denoted with `>`, terms are separated with commas.
- Draft products are not exported, only published and privately published products.
- It is not possible to assign a specific post ID to a product on import. Products will always use the next available ID, regardless of the ID included in the imported CSV.

When importing products, fields that contain commas can cause issues, as commas are treated as field separators. To prevent this, be sure to escape your needed commas to ensure they are correctly imported.

For example, this would import the categories `Places, People, Cities`

```
Places\, People\, Cities
```

By escaping these commas, you can ensure that the entire category name is treated as a single entity during the import process.

- Images need to be pre-uploaded or available online to import to your store.
- External URLs are supported and imported into the Media Library if used, provided the images are directly accessible and not behind a redirect script (as happens on some cloud storage services).
- You can define the filename if the image already exists in the Media Library.
- The core CSV importer does not currently have the ability to add, edit or update alt text for product images.

First-time and existing store owners using WooCommerce can use the CSV to add new products with one upload.

1. Go to**All Products > Products**.
2. Select **Import** at the top. The **Upload CSV File** screen displays.

1. Select**Choose File** and the CSV you wish you use.
2. Click on the **Continue** button
3. The **Column Mapping** screen displays, WooCommerce automatically attempts to match or map the **Column Name** from your CSV to **Fields**.

1. **Use dropdown menus** on the right side to adjust fields or indicate ‘**Do not import**.’
2. Any unrecognized columns will not be imported by default.

1. Once you are ready, click on the **Run the Importer** button.

1. **Wait until the Importer is finished**. Do not refresh or navigate away from this page while the import is in progress.

Store owners can use the CSV importer tool to bulk update existing products with new info, e.g., adding a brand, changing a tax class, bulk updates for a special sale or event, etc.

1. Make a CSV file as outlined in the [Create Your CSV](https://woocommerce.com/document/product-csv-importer-exporter/#create-your-csv) section, using the IDs and SKUs of products you wish to update. The importer uses the ID and SKU from the CSV to match and update products in your shop.

1. Navigate to **All Products > Products**.
2. Click on the **Import** button at the top. The **Upload CSV File** screen displays.

1. Select**Choose File** and the CSV you wish you use.
2. Tick the checkbox to **Update Existing Products**.

1. Click on the **Continue** button.
2. The **Column Mapping screen**displays and WooCommerce automatically attempts to match or “map” the **Column Name** from your CSV to **Fields**.

1. Use dropdown menus on the right side to adjust fields or indicate ‘**Do not import.**‘
2. Any unrecognized columns will not be imported by default.

1. Click on the **Run the Importer** button.

1. **Wait until the Importer is finished**. Do not refresh or navigate away from this page while the import is in progress.

Your product import is complete!

Store owners can use the CSV Importer tool to convert an existing simple product to a variable product. To do so, follow the below steps:

1. Create a simple product that has a price and SKU.
2. Export product via built-in CSV Exporter on the `All Products` page.
3. Open the CSV file and convert the simple product to a variable by following the below steps:

In this example, we will convert a simple product into a variable product with 1 attribute (size) and 2 variations:

1. Add 2 new rows, one for each product variation. Leave the initial product’s row in place.
2. Add 4 new columns after the last column. Give the columns the following headings :
  - `Attribute 1 name`
  - `Attribute 1 value(s)`
  - `Attribute 1 visible`
  - `Attribute 1 global`
  
3. Add `Size` for the three rows in the `Attribute 1 name` column.
4. Add the attribute values in the Attribute 1 value(s) column
  - In the row for the simple product, add all available attribute values. In this example, we’ve added `S, M` as attribute values for the product.
  - In the first new variation’s row, add `S` as the attribute value.
  - In the second new variation’s row, add `M` as the attribute value.
  
5. Enter `1` for each row in the `Attribute 1 visible` column. This is marking the attribute as visible.
6. Enter `0` for each row in the `Attribute 1 global` column. This is marking the `Is attribute global?` field `false` and means the attribute will only be added to this variable product, and won’t be created globally for reuse on other products.

So far, our new 4 columns look as follows:

1. In the `Type` column, change the type of the product from `simple` to `variable` and add type `variation` to variation rows (2 new rows that you created).
2. Add a SKU to variation rows.
3. Give the new variations a name as well. It looks like this in our example:

1. Update the other columns as well (and any other columns if needed):

1. **Important**: Add a SKU to all variation rows in the `Parent` column — this is to map the parent product with its variations:

1. Save a new CSV file.
2. Import the updated CSV file back to the site using the built-in CSV Importer
3. Select to update existing products option before running the import since we want to update the existing product on the site:

1. Click on the “Continue” button to proceed with import (nothing to be mapped).
2. You will see the following which is expected:

1. Navigate to the product. You will see that it is now variable and has 1 attribute added, but no variations were created. **Note that Used for variations checkbox is not selected.**This is also expected:

1. Open the CSV file again (the one where you already created rows for variations) and delete the parent product row. Leave variations rows without changes:

1. Save the updated CSV file.
2. Next, import the updated CSV file to the site, but this time **don’t** select the box next to `Update existing products`:

1. Proceed with import (no fields need to be mapped). You should see that variations have been imported:

1. After the import is completed, navigate to the product. It will now be a variable product with variations:

Store owners wishing to export their current catalog of products for any reason can generate a CSV export using the built-in product importer/exporter tool.

1. Navigate to **All Products > Products**.
2. Click on the **Export** button at the top. The **Export Products** screen will be displayed.

1. Select to **Export All Columns**. Or select which columns to export by using the dropdown menu.

1. Select to **Export All Products**. Or select which product types to export by using the dropdown menu.

1. Select to **Export All Categories**. Or select which categories to export by using the dropdown menu.

1. Tick the box to **Export Custom Meta**, if you need this info. Metadata on your products is typically from other plugins. Metadata columns are exported with `meta:`-prefixed to the metadata. For example, if you have metadata under the “product_depth” key, a column named `meta:product_depth` will be exported with those values. By default, no additional metadata is exported.
2. Click on the **Generate CSV** button and wait for the export to finish.

Your products are exported and the CSV will be downloaded by your browser

From WooCommerce 9.9, you can export selected products from the product list screen.

1. Go to **Products > All Products**
2. Select the products you want to export
3. Click on the **“Export X Selected”**button at the top

This is the schema used for the built-in **CSV importer and exporter** in WooCommerce (you can review the schema in [full-page on our GitHub repository](https://github.com/woocommerce/woocommerce/wiki/Product-CSV-Import-Schema#csv-columns-and-formatting)).

Yes. Feel free to visit the WooCommerce repo at GitHub to see the custom code at [Adding Custom Import Columns](https://github.com/woocommerce/woocommerce/wiki/Product-CSV-Importer-&-Exporter#adding-custom-import-columns-developers). Be aware that is Developer level info for which we provide no assistance under our [Support Policy](https://woocommerce.com/support-policy/).

Yes. Feel free to visit the WooCommerce repo at GitHub to see the custom code at [Adding Custom Export Columns](https://github.com/woocommerce/woocommerce/wiki/Product-CSV-Importer-&-Exporter#adding-custom-export-columns-developers). Be aware that this is Developer level info for which we provide no assistance under our [Support Policy](https://woocommerce.com/support-policy/).

Previous to WooCommerce 3.6.5, only products with a status of ‘publish’ or ‘private’ were exported, not those in ‘draft.’ If you want to change that, there’s a [filter](https://github.com/woocommerce/woocommerce/blob/master/includes/export/class-wc-product-csv-exporter.php#L128) you can use, but this would require custom coding, which we can’t provide assistance with.

If you’re using the current version of WooCommerce and all your products aren’t exporting, check your [WooCommerce logs](https://woocommerce.com/document/finding-php-error-logs/) for error messages. It may be that a [plugin conflict](https://woocommerce.com/document/how-to-test-for-conflicts/) is causing an error.

Previous to WooCommerce 3.6.5, only products with a status of ‘publish’ or ‘private’ were imported, not those in ‘draft.’ As of WooCommerce 3.7, CSV product import now allows true/false values for the published field, as well as the original 0 (private), -1 (draft), 1 (publish) values.

If you’re using the current version of WooCommerce and all your products aren’t importing, check the import log for error messages. It may be that a product already exists with the SKU you’re trying to use, a [plugin conflict](https://woocommerce.com/document/how-to-test-for-conflicts/) could be causing an error, or you may need to split your csv into smaller files for your server to handle the import successfully.

Are you seeing the following permission error when importing your CSV file? `Sorry, this file type is not permitted for security reasons.`

When an import file contains HTML the file type can be mis-detected by WordPress on some servers. One workaround is to add the following line to your wp-config.php file: `define( 'ALLOW_UNFILTERED_UPLOADS', true );`

For security reasons, you should only enable this temporarily for the duration of the import, and then remove it again from the configuration file.

Alternatively, instead of `Choose a CSV file from your computer`, you can first upload the CSV file to your website’s `upload` directory via FTP or your host’s admin panel file manager. Then, via `Advanced Options`, specify the location of that file for upload:

The *Maximum size* value is set at the server level. To increase the maximum file size, please contact your hosting company. As a workaround, you can split the CSV into multiple parts to upload separately.

When stores need to import a large number of products, the performance of your server becomes crucial. To ensure a smooth import process when using a CSV file, consider breaking it into smaller batches. This reduces the chances of errors and allows for easier troubleshooting if issues occur.

For handling extensive imports, we recommend using the [Product CSV Import Suite](https://woocommerce.com/products/product-csv-import-suite/). This extension supports the import of thousands of products, including complex ones and custom data from extensions like Product Vendors, Brands, Google Product Feed, and more.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

