---
title: WooCommerce Blueprints
url: https://woocommerce.com/document/woocommerce-blueprints/
---

**WooCommerce Blueprints** is a feature introduced in **WooCommerce 9.9** to help you streamline the setup, management, and testing of your store configurations. Whether you’re launching multiple stores, collaborating with a team, or validating a new extension, Blueprints allow you to import and export your store’s settings, plugins, and themes with just a few clicks. With Blueprints, you can:

- Save time by reusing preconfigured store setups.
- Ensure consistency across teams and environments.
- Test new features or configurations safely and efficiently.

A **Blueprint** is a portable configuration file that captures your WooCommerce store’s setup. It can include your WooCommerce settings, active plugins, and theme. This makes it easy to recreate a store environment, share configurations with teammates, or rapidly spin up new stores using your preferred setup.

Blueprints use the [WordPress Playground blueprint format](https://developer.wordpress.org/playground/blueprints/), making them portable and compatible with a wide range of WordPress tooling.

To enable Blueprints in your store:

1. Head to **WooCommerce > Settings > Advanced** **> Features**.
2. Scroll down to the **Blueprint** option.
3. Select the **Blueprint (beta)** checkbox to enable Blueprints.
4. Select **Save changes**.

Once enabled, a new **Blueprints** option will appear under **WooCommerce > Settings > Advanced > Blueprints**

Exporting a blueprint allows you to save your current store configuration into a `.json` file that can be reused and imported into another WooCommerce site. To export your WooCommerce store Blueprint, follow the steps below:

1. Navigate to **WooCommerce > Settings > Advanced > Blueprints**.
2. Scroll down to the **Export** section.
3. Choose what you’d like to include in the export.
4. After selecting your preferences, select the **Export** to generate and download the Blueprint file.

You can select the following WooCommerce settings to export:

- General
- Products
- Tax
- Shipping
- Payments
- Accounts & Privacy
- Integrations
- Site Visibility
- Advanced

The Blueprint export process relies on the WooCommerce Settings API, so only settings registered through this API are included. Custom database tables, such as those used for Approved Download Directories or REST API keys created by legacy code, are not included.

Additionally, payment account configurations are not exported or imported, meaning users will need to connect/configure their payment accounts manually after import.

Currently, we only support plugins and themes available on [WordPress.org](http://wordpress.org/). But with this you can select which plugins and extensions you want to include in the Blueprint export.

Importing a Blueprint file allows you to apply a previously saved store configuration to a new or existing WooCommerce site.

1. Go to **WooCommerce > Settings > Advanced > Blueprints**.
2. Scroll down to the **Import** section.
3. Upload a blueprint file.
4. Click on the **Import** button.

**Import is restricted to the Coming Soon mode**

Blueprint imports are only allowed when the store is in Coming Soon mode to reduce the risk of accidental or unauthorized imports on production sites. This acts as a safeguard to prevent destructive configuration changes on live environments. If you’re developing locally or need to override this restriction (e.g., for staging/testing purposes), you can allow imports in live mode by defining a constant in your wp-config.php file: `define( 'ALLOW_BLUEPRINT_IMPORT_IN_LIVE_MODE', true );`

- You can quickly apply a starter configuration across all new stores, using a shared theme and plugin set.
- Ensure consistency by syncing store settings and plugin configurations across the development or staging environment.
- Test your WooCommerce extensions in different environments and store configurations using a collection of blueprint files.
- Easily replicate your store’s configuration when launching in a new market or testing a new feature/extension.

To ensure Blueprints are safe and reliable, we conducted a thorough security audit and implemented several protections across both the feature and its underlying infrastructure:

- **Strict schema validation**: All Blueprint files are validated against a strict JSON schema before being applied. We’ve made sure this schema will reject unexpected fields and enforce stricter typing where possible.
- **Permission checks****are performed****fo r every step**: Only authorized users can import or export Blueprints. All REST API endpoints and background processes include permission checks to prevent unauthorized access.
- Option restrictions : To mitigate risk, Blueprint imports enforce a blacklist that blocks updates to sensitive or high-risk WordPress options, such as:
  - Site URLs (siteurl, home)
  - User management and system-related settings
  

This allows most site configurations to be portable while protecting critical options from being unintentionally or maliciously overwritten.

- Enhanced SQL execution safety : Blueprints support applying SQL changes as part of the import process. To ensure safety, only specific query types are allowed (INSERT, UPDATE, and REPLACE INTO), and each query is carefully validated before execution. Safeguards include:
  - Blocks unrecognized or unsafe SQL commands
  - Detects SQL injection patterns
  - Prevents writes to protected tables
  

These protections apply when executing imports, reducing the risk of unsafe or unexpected database changes.

- **Audit logging**: Blueprint import and export operations are logged for traceability. You can view logs under **WooCommerce > Status > Logs**. Look for logs in the source column titled`wc-blueprint`.

⚠️ **Security Best Practices:**Even with safeguards in place, we recommend reviewing Blueprint files before importing, especially if they come from a third party. Ensure the content looks as expected and avoid applying changes you don’t fully trust.

