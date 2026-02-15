---
title: Import and export a site database
url: https://woocommerce.com/document/import-and-export-a-site-database/
---

WordPress uses a database to store all the content and settings for your WooCommerce store in a structured format.

It organizes data into tables, each dedicated to different types of information such as products, customers, and orders. This organization allows for efficient data management, which can help you to easily store, retrieve, and update your store’s details.

You can [learn more about the WordPress database here](https://learn.wordpress.org/tutorial/the-wordpress-database/).

**Please note that making changes to your site’s database can have major effects on the entire site. Always back up your site before making any database changes, and contact your hosting service for help if you’re unsure.**

**Note:**This document is meant to serve as a helpful guide for advanced troubleshooting; however, the procedures described are beyond the scope of our [support policy](https://woocommerce.com/support-policy/) and we cannot provide direct assistance with implementing them. If you would like to seek assistance from a qualified WordPress/WooCommerce developer, we highly recommend [Codeable](https://codeable.io/?ref=z4Hnp) or a [Woo Agency Partner](https://woocommerce.com/development-services/).

This guide uses a tool called **phpMyAdmin**. Your hosting service may use the same tool or an alternative. Please reach out to them for help on this.

1. Log in to phpMyAdmin:
  - Start by accessing phpMyAdmin through your hosting control panel. This is usually found in sections like “Databases” within your web host’s dashboard.
  
2. Select your database:
  - Once you’re in phpMyAdmin, you’ll see a list of databases on the left side. Click on the database that you want to back up. This database contains all the data for your WordPress site, including WooCommerce information.
  
3. Export the database:
  - After choosing the database, click on the “Export” tab at the top of the screen.
  - You will be presented with two options for exporting your database: “Quick” and “Custom”.
    - **Quick export**: This option is straightforward and exports the entire database using the default settings.
    - **Custom export**: This option allows for more control over the export process, such as choosing specific tables to back up, the output format, and setting other preferences.
    - For most users, the “Quick” method is sufficient and simpler.
    
  
4. Choose the format :
  - Select the format you wish to save your database in. SQL is the most common format and is recommended because it’s easily imported back into any MySQL database.
  
5. Download the backup:
  - Click on the “Go” button. phpMyAdmin will generate a download of your database backup in the format you have selected. Save this file to a secure location.
  - It’s important to download and keep this file offsite or in cloud storage, so that it’s not only on your hosting server.
  
6. Verify the backup:
  - It’s a good practice to ensure your backup file is not corrupt. You can do this by opening the SQL file with a text editor to verify that it has a complete set of data and ends with the line `-- Dump completed on....`
  

Here’s how to import a WordPress site database using phpMyAdmin

1. Access phpMyAdmin:
  - Log in to your hosting account and go to phpMyAdmin.
  
2. Select the existing database:
  - In phpMyAdmin, find and click on the existing database that you want to use from the list on the left side. Ensure that this is the correct database associated with your WordPress site.
  
3. Prepare the database (optional):
  - If necessary, you can clear out the current database before importing new data to avoid conflicts. To do this, select all the tables and choose ‘Drop’ to delete them. **Be very careful with this step as it will delete your current data. Always ensure you have a backup before doing this.**
  
4. Import the database:
  - With the database selected, click on the “Import” tab at the top of the page.
  - In the “File to import” section, click “Choose File” and select the SQL file you want to import. This should be the backup file or another SQL file that contains the data you wish to import.
  - Leave the other options to their default settings, which are usually adequate for most WordPress database imports.
  
5. Start the import process:
  - Click on the “Go” button at the bottom of the page. phpMyAdmin will begin uploading and then importing the file into your selected database. This might take some time for larger file sizes.
  
6. Check for errors:
  - After the import is complete, phpMyAdmin will display a message showing the status of the import. If there are errors, it will provide details about what went wrong. Common issues could involve file size limits or SQL syntax errors.
  
7. Update WordPress configuration (if needed):
  - If the database details (name, user, password) have changed, update your WordPress configuration file (wp-config.php) to reflect these changes. Verify the DB_NAME, DB_USER, and DB_PASSWORD fields are correct.
  
8. Verify your site is working:
  - Go to your WordPress site to make sure it is operating as expected. Check that all pages load properly and the content appears as expected.
  

Keeping your site database secure is crucial for protecting your website from unauthorized access and data breaches. Here’s some general guidance on how to bolster your database security:

- **Use strong passwords:** Always use strong, unique passwords for your database access, and update them regularly.
- **Update regularly:** Keep your database software, WordPress, and any plugins or themes updated to close security vulnerabilities.
- **Limit database access:** Restrict access to your database to only necessary IP addresses to reduce the risk of attacks. Use database settings to block unknown IPs.
- **Regular backups:** Implement a schedule for regular backups and store them in a secure location to aid in quick recovery from data loss or breaches.
- **Data encryption:** Encrypt sensitive data in your database and ensure secure connections (like SSL/TLS) when accessing the database.
- **Apply the least privilege principle:** Only grant necessary permissions for users and applications to perform their required tasks.
- **Monitor and audit:** Keep an eye on access logs and set up alerts for unusual activities or unauthorized access attempts.
- **Change the default table prefix:** Switch from the default `wp_` prefix to a more obscure prefix to help protect against SQL injection attacks. Update this setting during the initial installation or change it for an existing website by modifying the `wp-config.php` file and adjusting the database tables and any associated references. Consider using a plugin for this change or consult with your hosting service for more support.

By following these tips, you can enhance the security of your WordPress database. If you’re unsure about how to action any of these changes, especially when changing the database prefix, reach out to your hosting service for assistance.

Do you still have questions and need assistance?

- [Get in touch](https://woocommerce.com/my-account/create-a-ticket/) with a Happiness Engineer via our Help Desk. We provide support for extensions developed by and/or sold on WooCommerce.com, and Jetpack/WordPress.com customers.
- If you are not a customer, we recommend finding help in the [WooCommerce support forum](https://wordpress.org/support/plugin/woocommerce/) or hiring a Woo Agency Partner. These are trusted agencies with a proven track record of building highly customized, scalable online stores.[Learn more about Woo Agency Partners](https://woocommerce.com/development-services/).

