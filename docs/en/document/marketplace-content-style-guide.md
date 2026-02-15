---
title: Marketplace Content Style Guide
url: https://woocommerce.com/document/marketplace-content-style-guide/
---

This guide provides formatting and writing standards for creating product pages and documentation on the WooCommerce Marketplace. Following these guidelines ensures consistency across the Marketplace and creates a professional experience for merchants browsing and purchasing extensions.

For product page structure, required elements, and asset specifications, refer to [Product Page Content and Assets](https://woocommerce.com/document/product-page-content-and-assets/).

Use the format **“Product Name for WooCommerce”** rather than “WooCommerce Product Name” throughout the product copy.

This format ensures your product name complies to [trademark rules](https://woocommerce.com/trademark-guidelines/) and leads with its unique identifier, improving discoverability and clarity.

Follow the [WooCommerce Grammar, Punctuation, and Capitalization Guide](https://developer.woocommerce.com/docs/best-practices/coding-standards/grammar-punctuation-capitalization) for comprehensive guidance. Key points include:

**Use the Oxford comma** when listing three or more items:

- ✓ “Track orders, manage inventory, and process refunds.”
- ✗ “Track orders, manage inventory and process refunds.”

**Use active voice** instead of passive voice whenever possible:

- ✓ “The extension sends email notifications when orders ship.”
- ✗ “Email notifications are sent by the extension when orders are shipped.”

**Capitalization:**

- Use sentence case for headings (capitalize only the first word and proper nouns)
- Do not use ALL CAPS for emphasis
- Capitalize product names, features, and WooCommerce terminology correctly

**Spelling and terminology:**

- Use American English spelling
- Use “ecommerce” (lowercase, no hyphen)
- Use “WooCommerce” (not “Woocommerce” or “wooCommerce”)

Maintain clean, consistent formatting by following these standards. Custom styling interferes with the Marketplace design system and creates an inconsistent experience.

**Do not:**

- Center headings or body text
- Alter the default text color
- Add custom font sizes or font families
- Use bold or italic formatting excessively

**Do:**

- Use left-aligned text throughout
- Allow headings and paragraphs to inherit default styles
- Use bold sparingly for key terms only

**Do not:**

- Include more than one H1 tag per page (the product title serves as the H1)
- Center-align headings
- Apply custom colors or styles to headings

**Do:**

- Use H2 for main sections
- Use H3 for subsections within an H2 section
- Maintain a logical heading hierarchy (do not skip levels)

**Do not:**

- Create custom-styled sections or containers
- Add borders around sections
- Apply background colors to content areas
- Add custom spacing between sections
- Add additional styles to columns

**Do:**

- Use standard paragraph and heading blocks
- Let the Marketplace template handle section spacing
- Use the default column block without style modifications

**Do not:**

- Customize bullet or number designs with custom CSS
- Add custom spacing between list items
- Create nested lists more than two levels deep

**Do:**

- Use the standard unordered or ordered list blocks
- Apply the approved list classes for styled checkmarks (see Formatting Tools below)

Do not use emojis in product pages or documentation. Emojis can cause accessibility issues, display inconsistently across devices, and create an unprofessional appearance.

- ✗ “🚀 Boost your sales!”
- ✓ “Boost your sales”

Do not include links to external websites. All support and documentation links should point to Marketplace URLs:

- Link to your product documentation hosted on WooCommerce.com
- Link to Marketplace support resources
- Do not link to external support portals, documentation sites, or landing pages

The WooCommerce Marketplace provides several formatting tools to create visually appealing content while maintaining consistency.

Use these CSS classes to create professional checkmark lists:

**Primary checkmark list** (`wccom-tick-list-primary`)

Creates bold checkmarks in green circles. Use for main benefit lists at the top of your product description.

```
<ul class="wccom-tick-list-primary">  <li>Accept payments globally</li>  <li>Automatic tax calculation</li>  <li>Real-time shipping rates</li></ul>
```

**Secondary checkmark list** (`wccom-tick-list-secondary`)

Creates lightweight green checkmarks. Use for feature lists and secondary content throughout the page.

```
<ul class="wccom-tick-list-secondary">  <li>Supports 100+ currencies</li>  <li>PCI compliant</li>  <li>Automatic updates</li></ul>
```

Use the box shortcode to highlight important information.

Available styles:

**Info box** – For general tips and helpful information:

*Can be used with or without* `style="info"`.

**Alert box** `style="alert"` – For warnings or important notices:

**Error box** `style="error"` – For critical warnings or known limitations:

**Success box** `style="success"` – For positive confirmations or best practices:

Use callout boxes sparingly. Overuse reduces their impact and creates visual clutter.

When creating documentation for your product, follow these additional guidelines:

- Begin with a clear introduction explaining what the extension does
- Please use the synced pattern titled “ Docs – Installation ”
  - This explains how our mutual customers should install purchases from WooCommerce.com.
  
- Document all your products features and settings
- Provide troubleshooting guidance for common issues

For detailed documentation frameworks, refer to [Support and Documentation Best Practices](https://developer.woocommerce.com/docs/extensions/best-practices-extensions/support-and-documentation/).

When adding visual content:

- Use the modern WordPress admin color scheme
- Use a recent core WordPress theme unless documenting a different theme
- Ensure screenshots are clear and legible
- Optimize file size
- Do not include sensitive or personal information in screenshots
- Add alt text to all images for accessibility

