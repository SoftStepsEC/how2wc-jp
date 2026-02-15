---
title: Single Product Block
url: https://woocommerce.com/document/single-product-block/
---

The Single Product block in WooCommerce lets you showcase an individual product anywhere on your site, whether it’s a landing page, blog post, or homepage.

This block brings the full product experience into the WordPress Block Editor, allowing you to display key product details, such as product image, price, description, reviews, and an Add to Cart button, all in one visually engaging element. It’s a powerful way to highlight specific products and drive conversions without directing customers away from their current page.

The Single Product block is built from several inner blocks. All inner blocks support real‑time updates, so customers never wait for a page refresh when refining their search.

Now that we’ve explored the purpose of each inner block, let’s dive into their individual settings to better understand how to customize and control their appearance and behavior within the Single Product block.

The Product Image block displays the main image of the product and serves as a key visual element in the Single Product block. This block helps customers get a quick visual understanding of the product and can optionally link to the full product page.

#### Block Settings

- **Image Size**: Define the image dimensions manually in pixels. Leave these fields blank to use the default image size from your theme or WooCommerce settings.
- **Link to Product Page**: When enabled, clicking on the product image will take the customer to the original product page.
- **Show On-Sale Badge**: When enabled, a “Sale” badge appears on the product image if the item is currently discounted.
- **Sale Badge Alignment: Left, Center, Right**: Choose where the “Sale” badge is positioned over the image – Left, Center, or Right. Align it based on your layout or visual design preference.
- Image Sizing  Options: Choose whether you want to display the Product Image to its Full Size or you prefer to display a cropped version.
  - **Full Size:** Displays the complete image as uploaded.
  - **Cropped:** Trims the image to fit a uniform display size, based on your theme’s image cropping settings.
  

The Product Title block displays the name of the product and plays a key role in product identification, accessibility, and SEO. It helps guide shoppers to the product page when configured as a clickable link.

#### Block Settings

- **Make Title a Link**: When enabled, the product title becomes a clickable link that directs visitors to the original product page.
- **Open in New Tab**: Determines whether the link opens in a new browser tab. This is useful when you want users to stay on the current page while still giving them access to more product details.
- **Link Rel**: Allows you to define the rel attribute for the link (e.g., nofollow, noopener, sponsored).

The Product Rating block displays the product’s average customer rating in a star format. This block is a quick trust builder, giving potential customers insight into product popularity and satisfaction.

#### Block Settings

- **Text Color**: Customize the color of the stars and the text shown next to the star rating (e.g., the number of reviews).
- **Typography and Dimensions**: You can further the typography and dimensions of the block.

The Product Price block displays the product’s current price, including sale pricing when applicable.

#### Block Settings

- **Text Color**: Change the color of the price text to better match your site’s design.
- **Background Color**: Adjust the background color behind the price label for added visual emphasis.
- **Typography and Dimensions**: You can further the typography and dimensions of the block.

The Product Summary block displays a short description of the product, pulled from the product’s short description field.

#### Block Settings

- **Max Word Count**: Limit how many words to display. If set to a specific number, only the first paragraph up to that limit is shown. Set to **0** to show the full summary.
- **Show Description if Empty:** When enabled, and if the product’s short description is empty, the block falls back to the full product description.
- **Link to Description:** Adds a button that takes shoppers directly to the Product Description section on the Product page.
- **Typography and Dimensions**: You can further the typography and dimensions of the block.

Prior to WooCommerce 10.0, the Single product block and Single Product Template block comes with the Classic version of the **Add to Cart with Options Block**. It provides a simplified experience with key options – Quantity selector and Add to Cart button

#### Block Settings

- Quantity Selector: Choose how shoppers select quantity:
  - **Input:** A numeric input field where customers can type a number
  - **Stepper:** Plus/minus buttons to increase or decrease the quantity.
  

Introduced in WooCommerce 10.0, the [Add to Cart + Options (Beta) block](https://woocommerce.com/document/add-to-cart-options-block/) offers a fully blockified, customizable add-to-cart form. You can switch to this new block to customize more

The Product Meta Block displays the product’s SKU, categories, tags, and other meta. By default, it displays the SKU, categories, and tags.

#### Product SKU

The Product SKU block displays the SKU of the product.

#### Product Categories Block

The Product Categories block displays a list of categories the product belongs to.

#### Block Settings

- **Transform to Variation**: Change the taxonomy from *Product Categories* to *Product Tags, Brands, etc.,* using the dropdown.

- **Styles:** Choose between Default and Pill-shaped****tag styles.
- **Color**: Customize Text, Background, and Link colors for improved visual integration.

#### Product Tags Block

The Product Tags block displays product tags for further classification and filtering.

#### Block Settings

- **Transform to Variation**: Change the taxonomy from *Product Tags* to *Product Categories, Brands, etc.,* using the dropdown.
- **Styles:** Choose between Default and Pill-shaped****tag styles.
- **Color**: Customize Text, Background, and Link colors for improved visual integration.

#### Typography Settings

All of the inner blocks within the Single Product block come with a set of design controls that allow for consistent styling across your content. These include:

- **Font**: Choose a specific font (based on your theme’s available fonts) or leave it as *Default*.
- **Size**: Select a preset size (S, M, L, XL, XXL) or fine-tune it using custom controls for precise scaling.
- **Appearance**: Adjust text weight and style if your theme supports multiple font appearances (e.g., bold, italic, light).
- **Line Height**: Modify the vertical spacing between lines for better readability.
- **Letter Spacing**: Control the space between individual characters. Useful for subtle design refinement.
- **Text Decoration**: Add styling such as underline, strikethrough, or none for headings or prices.
- **Letter Case**: Transform text to **uppercase**, **lowercase**, or **title case** depending on your design preference.
- **Dimensions**: Fine-tune the padding and margin for spacing inside and around each block element.

- Width Settings :
  - **Fit**: Automatically adjusts to content width.
  - **Grow**: Expands to fill the available space.
  - **Fixed**: Lets you set a specific width.
  
- Border Controls :
  - Add borders with customizable thickness.
  - Use the **Radius** option to round the block’s corners for a softer, more modern appearance.
  

These layout and typography options are especially useful when customizing product presentations to match your brand’s style or align with different page sections.

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

