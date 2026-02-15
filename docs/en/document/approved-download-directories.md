---
title: Approved Download Directories
url: https://woocommerce.com/document/approved-download-directories/
---

**Approved Download Directories** is a feature that helps manage which directories are allowed for the storage of downloadable product files.

Introduced in WooCommerce 6.5, it’s of particular use if you already sell, or plan on selling, downloadable products, and especially if there are multiple users on your site with the ability to create and modify products. You may, for instance, have a small number of administrators, but multiple shop managers or product vendors creating products and adding files.

On this page, you’ll learn the following:

- Where downloadable files are stored.
- Which settings are available with which to manage approved download directories.
- How to enable or disable rules.
- What additional tools are available.
- Learn why some downloadable files might be disabled.

When WooCommerce is installed, it tries to create a new directory named `woocommerce_uploads`, which is located inside WordPress’ own uploads directory. That is why the `woocommerce_uploads` folder is included in the Approved Product Downloads Directory and ticked as Enabled by default and recognized as safe.

However, in many cases, it may be preferable to store files elsewhere, such as using a cloud storage solution for very large files. WooCommerce fully supports this, but it also recognizes the challenges this introduces:

- It may be company policy to store files only in approved locations to which administrators have full read/write privileges. In other words, letting employees link to downloads stored in their personal cloud storage account may not be acceptable.
- Linking to files accessed via domains you do not control can also introduce various types of security risks, and so it may be desirable to limit acceptable locations to those on a pre-approved list.

The Approved Download Directory feature is intended to help with these challenges.

WooCommerce provides a range of settings found at **WooCommerce > Settings > Products > Approved Download Directories** to help site administrators exercise control over the locations used for storing and serving product downloads.

From this location, approved directories can be added, edited or removed, and it is also possible to disable or enable this feature entirely (rules can also be disabled or enabled on an individual basis). Note that all approved directories, including file paths, are expressed as URLs.

Some things to keep in mind:

- The scheme, or protocol, matters. In other words, `http://example.com/` is not the same as `https://example.com/`. You can add both if needed. You can also use the `//example.com` shorthand, which serves as a “wildcard” notation, to cover both the `http` and `https` versions of the same URL.
- You can enter file paths directly which, once saved, automatically converts into URLs using the **file://** scheme. For example, a file path entered as `/directory/path/example/` is saved as `file:///directory/path/example/`.
- Each approved directory implicitly covers all possible subdirectories. For example, if `https://my.site/files/` is added to the list of approved directories, then it is perfect fine to add a file located within `https://my.site/files/nested/sub-directories/` to a product.
- These settings only impact digital downloads. They have zero impact on the WordPress media library or image handling generally.

To emphasize, **only site administrators** have the power to modify this list (or, in the context of multisite networks, network administrators), and nobody else is able to add downloadable files to products **unless** there is a corresponding entry on this page.

- If you are the site administrator, and you are the only person managing your store, then you don’t need to worry about any of this. Any time you add a downloadable file as a site admin that is not covered by an existing rule, a new rule will automatically be added.
- It is also possible to [disable this functionality](https://woocommerce.com/document/approved-download-directories/#enable-and-disable-rules) entirely.
- In cases where another site user, such as an editor or shop manager, tries to supply a URL that is not an approved directory, they see an error like the following one. This encourages them to contact the site admin for further help.:

**Note:**

In the case of the [Product Vendors](https://woocommerce.com/products/product-vendors/) extension, error messages like these are not displayed to vendor-level users.

The **Stop / Start Enforcing Rules** button near the top of the settings screen toggles the enforcement of the rules for cases where management of approved directories proves impractical. For example, if the person adding all the images has a “shop manager” role instead of an “Administrator” role.

- To enable all the rules, an administrator can click on the **Start Enforcing Rules button**. It will then change to say Stop Enforcing Rules.imilarly, it can be disabled by clicking on **Stop Enforcing Rules**.
- Administrators can also use the **Enable All** and **Disable All** buttons to enable and disable all the rules, respectively.
- Rules can also be enabled or disabled in bulk, by select some or all rules and using the **Bulk Edit** menu.
- To enable an individual rule, an administrator can either hover over a rule in the list and select Enable/Disable from the quick links that appear. Or click on the rule’s URL and enable/disable it from the Edit Approved Directory screen.

To reset or delete all rules, see the [Additional Tools section](https://woocommerce.com/document/approved-download-directories/#additional-tools) below.

If the download file can be reachable by customers who haven’t paid for it, it means either:

- The file was added to the media library via a method that wasn’t the WooCommerce upload mechanism. WordPress’s media library is public by default, because it’s where all images attached to posts and pages are placed. When creating a downloadable product, you should upload the file from within the WooCommerce product, instead of picking an existing file from the media library.
- You are using the **Redirect only (insecure)** method for file downloads. Using this method means your files will be unprotected and whoever has the upload link can access the file, even when they are not logged in. Read more about that in [Digital/Downloadable Product Handling](https://woocommerce.com/document/digital-downloadable-product-handling/).

There may be occasions when, as site administrator, you find you need additional control over this functionality. For instance, if you import product data using some method other than our official importer tool, then the creation of new download paths may not initially be noticed by WooCommerce. For this reason, a couple of extra tools can be found in **WooCommerce > Status > Tools**:

- **Synchronize approved download directories**— this tool triggers a fresh scan of the product catalog. When downloadable product paths are discovered that are not already covered by existing Approved Download Directory rules, they are to the list, but is initially disabled.
- **Empty the approved download directories list —** is used to delete the existing Approved Download Directory list entirely.

It is entirely possible, especially in more complex multi-user setups, that a downloadable file may be added to a product and, later on, the corresponding rule in the Approved Download Directory list may be disabled or deleted.

In these cases, the affected downloadable files will also be marked as disabled with a red asterisk that appear to the right of the File URL field.

Customers who had purchased the product will no longer be able to access the disabled downloads, until or unless a site administrator corrects the problem.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

