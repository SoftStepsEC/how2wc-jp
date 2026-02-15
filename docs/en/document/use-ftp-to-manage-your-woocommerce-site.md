---
title: Use FTP to manage your WooCommerce site
url: https://woocommerce.com/document/use-ftp-to-manage-your-woocommerce-site/
---

FTP (File Transfer Protocol) is a method to transfer files between a client and a server over the internet or a local network. In the context of managing a WordPress site, such as those running WooCommerce, FTP allows you to upload, download, or modify files directly on your web server.

This can be particularly useful for installing themes or plugins, making backups of your site, or troubleshooting issues by editing files directly.

To use FTP, you’ll need an FTP client, which is a software application that facilitates the file transfer process, and your server’s FTP credentials, which typically include a server address, username, and password.

**Note:**This document is meant to serve as a helpful guide for advanced troubleshooting; however, the procedures described are beyond the scope of our [support policy](https://woocommerce.com/support-policy/) and we cannot provide direct assistance with implementing them. If you would like to seek assistance from a qualified WordPress/WooCommerce developer, we highly recommend [Codeable](https://codeable.io/?ref=z4Hnp) or a [Woo Agency Partner](https://woocommerce.com/development-services/).

To access your site’s files via FTP, you’ll need to use an FTP client.

Different web hosting providers offer various tools and resources to facilitate this. Commonly, hosts will provide you with FTP credentials that include a server address, username, and password.

One widely used FTP client is [FileZilla](https://filezilla-project.org/), which is free and compatible with most operating systems. By entering your FTP credentials into FileZilla or a similar client, you can connect to your server and begin transferring files directly to and from your site.

Please reach out to your hosts if you need help with these steps.

When you connect to your WordPress site using an FTP client like FileZilla, here’s how to locate your site’s files:

1. **Connect to your server**: Open your FTP client, enter your FTP credentials, and connect to your server.
2. **Navigate to the root directory**: The root directory might vary depending on your hosting service. Common names for this directory are `public_html`, `www`, `htdocs`, or your domain name.
3. Locate the WordPress files : Inside the root directory, look for the WordPress installation folder. If WordPress is installed in the root directory, you’ll see folders like wp-admin , wp-content , and wp-includes directly within.
  - **wp-admin**: Contains the WordPress admin files.
  - **wp-content**: Houses your themes, plugins, and uploads.
  - **wp-includes**: Includes essential WordPress files.
  

For most tasks, such as theme or plugin installation, modifications, or backups, you’ll primarily be interacting with the `wp-content` folder. This directory contains your active theme’s files, plugins, and any media you’ve uploaded through your WordPress dashboard.

Each file and folder on your WordPress site has permissions that specify what the owner, a group, and everyone else can do with the file. For instance, you might see permissions written numerically as `755` or `644`, which control how files and directories can be accessed and modified. Setting the right permissions will help maintain your site’s integrity and security.

To see and understand file and folder permissions in your WordPress site, you’ll typically use an FTP client, such as FileZilla. Here’s how you can view and interpret these permissions:

1. **Connect to your FTP server**: Open your FTP client and log in with your credentials.
2. **Navigate to your WordPress files**: Go to your root directory or the folder of your WordPress installation.
3. **Check permissions**: In FileZilla, the file list displays permissions for each file. Look at the columns; one will have the label “Permissions” or something similar. You’ll see entries like `drwxr-xr-x` or `-rw-r--r--`.

Permissions are displayed as a series of letters (`drwxr-xr-x`) or as a **three-digit number**. Each character or digit has a specific meaning:

- **First character**: Indicates if it is a directory (d) or a file (-).
- Next three characters (owner permissions) : Shows what the owner of the file can do.
  - r: Read permission (can view the file’s contents).
  - w: Write permission (can modify the file).
  - x: Execute permission (can run the file as a program).
  
- **Next three characters (group permissions)**: Shows what the user group can do, using the same r, w, x notation.
- **Last three characters (others’ permissions)**: Indicates what all other users can do.

Permissions are typically three digits:

- **7** (`rwx`): Read, write, and execute
- **6** (`rw-`): Read and write
- **5** (`r-x`): Read and execute
- **4** (`r--`): Read only

- **Directories**: 755 (`drwxr-xr-x`) — The owner can read, write, and execute. Others can only read and execute.
- **Files**: 644 (`-rw-r--r--`) — The owner can read and write. Others can only read.

These permissions help protect sensitive files from unauthorized changes without preventing necessary operations from being performed by scripts and other site functionalities. Adjusting these settings improperly can expose your site to security risks, so it’s crucial to handle them carefully.

Do you still have questions and need assistance?

- [Get in touch](https://woocommerce.com/my-account/create-a-ticket/) with a Happiness Engineer via our Help Desk. We provide support for extensions developed by and/or sold on WooCommerce.com, and Jetpack/WordPress.com customers.
- If you are not a customer, we recommend finding help in the [WooCommerce support forum](https://wordpress.org/support/plugin/woocommerce/) or hiring a Woo Agency Partner. These are trusted agencies with a proven track record of building highly customized, scalable online stores.[Learn more about Woo Agency Partners](https://woocommerce.com/development-services/).

