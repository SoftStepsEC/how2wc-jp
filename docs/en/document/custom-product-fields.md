---
title: Custom Fields on Products
url: https://woocommerce.com/document/custom-product-fields/
---

WooCommerce offers the capability to enhance your product listings with custom fields, a feature that allows you to display additional product details to customers.

Custom fields are additional [metadata](https://developer.wordpress.org/plugins/metadata/) of your products, which can be utilized in various ways within your theme or site to display extra information, tailor the shopping experience, or provide specific product details that aren’t covered by the default product fields.

This flexibility allows you to extend the functionality of your online store per your goals. This guide will walk you through the process of adding custom fields to WooCommerce products directly through the WordPress admin and displaying them on your site.

Before we learn more about custom fields, it’s important to understand the difference between custom fields and product attributes. The difference lies primarily in their application and functionality:

- **Product Attributes** serve as foundational elements for categorizing a broad range of products. They function similarly to [taxonomies](https://developer.wordpress.org/themes/basics/categories-tags-custom-taxonomies/), enabling customers to filter and group products based on these attributes. This feature is crucial for creating meaningful relations among products, helping customers navigate and discover products through attributes like color, size, or material.
- **Custom Fields**, in contrast, are tailored to individual products, providing specific information or options for that single item. Unlike attributes that categorize products into broader groups, custom fields offer unique details or personalization choices for each product.

In essence, while attributes work to organize products into categories or groups based on shared characteristics, custom fields add depth to a product’s individual listing by offering additional information that is specific to that particular item.

To enable Custom Fields for products, please follow the below steps:

1. Go to **WP-admin > Products**
2. Choose to add a new product using the “Add New” button or “Edit” an existing product
3. On the product edit page, click the **“Screen Options”** at the top right corner of the screen.
4. In the dropdown, find and check the **“Custom Fields” option to enable** it for the products

After enabling the custom fields for your products, you can now add custom data to your products:

1. On the same product edit page, **scroll down until you find the “Custom Fields” section**at the bottom
2. To add a new custom field, click on the**“Add Custom Field” button** to create a new field
3. Name your custom field in the **“Name”** input box. This name will be used to reference the field programmatically in your theme or site
4. Enter the value for the custom field in the **“Value”** input box. This could be any piece of information relevant to the product, such as additional specifications, unique identifiers, or custom notes
5. Once you’ve added your custom fields and filled out their corresponding values, make sure to save or update the product

To display the Custom Fields for each product, you have to edit your theme’s files. Learn more about how to do that in the [WooCommerce Developer Documentation](https://developer.woocommerce.com/docs/displaying-custom-fields-in-your-theme-or-site/).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

