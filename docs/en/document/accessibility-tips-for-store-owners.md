---
title: Accessibility Tips for WooCommerce Store Owners
url: https://woocommerce.com/document/accessibility-tips-for-store-owners/
---

While WooCommerce provides accessible foundations, store owners play a key role in creating an inclusive experience. This page offers tips and best practices for improving the accessibility of your store’s content, design, and customizations.

In many parts of the world, ecommerce stores are legally required to meet accessibility standards. Making your store accessible not only supports a better customer experience – it can also help you comply with laws such as the [Americans with Disabilities Act (ADA)](https://ada.gov/) and the [European Accessibility Act (EAA)](https://employment-social-affairs.ec.europa.eu/policies-and-activities/social-protection-social-inclusion/persons-disabilities/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en). Most regulations reference the [WCAG 2.2 Level AA standard](https://www.w3.org/TR/WCAG22), which defines measurable accessibility requirements.

Add descriptive alt text to product images and other visuals. This helps screen reader users understand the purpose and context of the image.

Avoid leaving alt text blank unless the image is decorative. If it is [decorative](https://www.w3.org/WAI/tutorials/images/decorative/), leave the alternative text field blank so screen readers can skip it. Product images and linked images are never decorative.

If you’re adding custom forms (e.g., using an extension), ensure that:

- Each field includes a visible and programmatic label.
- You don’t rely solely on placeholder text, which disappears as users type.

Labels should describe the purpose of the field clearly, and related instructions should be close to the input field. Error messages should be linked programmatically to the relevant inputs using ARIA attributes and announced by screen readers.

Themes significantly impact accessibility. Choose a theme marked as [accessibility-ready in the WordPress repository](https://wordpress.org/themes/tags/accessibility-ready/), as these meet established accessibility standards.

Themes with this designation have passed WordPress’s accessibility review, which checks for keyboard navigation, color contrast, and other WCAG criteria.

If choosing a theme outside WordPress.org, ask the developer for an Accessibility Conformance Report or other accessibility documentation before selecting it.

Avoid autoplaying sliders, videos, or animations unless users can pause or disable them. These effects can be problematic for users with vestibular or cognitive conditions.

Animations should respect the “Reduce motion” setting in the user’s operating system. You can test this by enabling the “Reduce motion” option in macOS or Windows and checking that non-essential motion is suppressed on your site. Here’s how to turn on reduced motion on your computer for testing:

- **On Windows 11**: Go to *Settings > Accessibility > Visual Effects > Animation Effects*.
- **On macOS**: Navigate to *System Preferences > Accessibility > Display > Reduce motion*.

Use accessibility evaluation tools or perform manual tests:

- Navigate your site using only a keyboard: use the tab key to tab through all buttons, links, and form fields, and return key to trigger buttons and links. Ensure that you can search for products, add products to the cart, and complete a checkout without using a mouse.
- Use screen readers or browser extensions like [WAVE](https://wave.webaim.org/) or [axe DevTools](https://chromewebstore.google.com/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd) or WordPress accessibility plugins like [Equalize Digital Accessibility Checker](https://equalizedigital.com/accessibility-checker/?ref=woocommerce) to identify issues.
- Try zooming in to 200% or 400% to ensure that all content is still readable and no elements overlap or disappear.
- Test your site with free screen readers like [NVDA](https://www.nvaccess.org/) (Windows) or [VoiceOver](https://support.apple.com/guide/voiceover/welcome/mac) (Mac) to better understand how users with visual impairments experience your store.

Be aware of the following common limitations and how to mitigate them:

- **Third-Party Extensions**: Not all extensions are equally accessible. Check documentation or test before implementing.
- **Custom Blocks**: If you use or build custom blocks, follow semantic HTML and [accessibility best practices](https://developer.woocommerce.com/docs/extensions/best-practices-extensions/accessibility/).
- **Site-Specific Customizations**: Custom code (JS/CSS) may unintentionally affect accessibility. Always re-test relevant flows after making changes.
- If your customizations include color options, test them for contrast using online contrast checkers. For example, make sure button text is readable against its background color. Consider warning users (via admin UI) when settings create inaccessible combinations.

Helpful tools and references for store owners:

- [WordPress Accessibility Handbook](https://make.wordpress.org/accessibility/handbook/)
- [WAVE Accessibility Tool](https://wave.webaim.org/)
- [axe DevTools Extension](https://chromewebstore.google.com/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd)
- [NVDA Screen Reader](https://www.nvaccess.org/)
- [VoiceOver (macOS/iOS)](https://support.apple.com/guide/voiceover/welcome/mac)
- [Accessibility Checker plugin for WordPress](https://wordpress.org/plugins/accessibility-checker/)

We welcome suggestions and feedback from store owners. If you discover accessibility issues or have ideas for improvements, please [contact support](https://woocommerce.com/contact-us/) or email us at [accessibility@woocommerce.com](mailto:accessibility@woocommerce.com). Your input helps us support a more inclusive web.

