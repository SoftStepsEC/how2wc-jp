---
title: Accessibility Features in the WooCommerce Plugin
url: https://woocommerce.com/document/accessibility-features-in-woocommerce/
---

WooCommerce is built on top of WordPress, which adheres to strict accessibility coding standards.

The WooCommerce plugin inherits these practices and introduces its own accessibility features to ensure compatibility with assistive technologies such as screen readers and keyboard-only navigation. This page outlines the built-in accessibility features within the plugin.

**Note:** Many regions legally require ecommerce sites to be accessible. Ensuring your store is accessible supports legal compliance in countries with accessibility laws like the [Americans with Disabilities Act (ADA)](https://ada.gov/) in the United States and the [European Accessibility Act (EAA)](https://employment-social-affairs.ec.europa.eu/policies-and-activities/social-protection-social-inclusion/persons-disabilities/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en), a directive that applies to all EU member countries. There are also laws around accessibility in other countries, and we recommend reviewing [web accessibility laws worldwide](https://www.w3.org/WAI/policies/) to ensure you comply with your local requirements.

For guidance on this, you can refer to our guide on [accessibility tips for WooCommerce stores](https://woocommerce.com/document/accessibility-tips-for-store-owners/).

When using a WordPress with an [accessibility-ready theme](https://wordpress.org/themes/tags/accessibility-ready/), WooCommerce supports full keyboard navigation, allowing users to move through the interface using only the keyboard:

- Logical tab ordering throughout checkout, cart, and forms.
- Clear focus indicators to show the currently selected element.
- All interactive components (buttons, dropdowns, toggles) are accessible without a mouse.
- Buttons are operable via both Spacebar and Enter keys, and links are activated with the Enter key. Dialogs and modals retain keyboard focus properly while open.

Please note that theme styles can override what is set by WooCommerce, so you will also need to confirm that the theme you are using on your site supports accessibility.

WooCommerce uses semantic HTML and ARIA roles to ensure that screen reader users can navigate and understand site content:

- Forms, buttons, and interactive elements are clearly labeled.
- Dynamic updates (e.g., cart totals, validation messages) use ARIA live regions for announcements.
- Page structures make use of headings, lists, and landmarks to convey content hierarchy.
- Elements have the correct role—buttons are announced as buttons, links as links, and form fields include proper labels and states such as “pressed” or “expanded.”

Forms, especially during checkout, are designed with accessibility in mind:

- Every input is associated with a descriptive <label>.
- Required fields are clearly marked, and errors are communicated both visually and programmatically. You may need to confirm that your theme also supports this.
- Instructions and field groups are screen reader-friendly.

Please note that themes and third-party plugins that modify the WooCommerce checkout experience can break accessibility. If your checkout page is modified, check to ensure that visible labels, required indicators, and error messages are still present.

The WooCommerce plugin handles form errors with accessibility in mind:

- Errors appear close to the relevant field.
- ARIA attributes link error messages with their inputs.
- Real-time validation helps users fix issues without resubmitting the form.
- Success and error messages are also announced via screen readers using ARIA live regions.

ARIA roles enhance the experience for screen reader users:

- Layout areas controlled by the plugin are marked with roles such as main, navigation, and region and have unique names.
- Interactive elements like collapsible menus and modals use ARIA states (e.g., aria-expanded).
- Live regions update users when content changes dynamically.

WooCommerce blocks used in product listings, cart, and checkout are built with accessibility in mind:

- Use of HTML5 semantic elements.
- Full keyboard and screen reader compatibility.
- Built to align with WordPress accessibility guidelines.

*Note: Some older, deprecated blocks may have limited accessibility support and may require testing or extra configuration. We encourage you**to update to new blocks as they become available and avoid the use of deprecated blocks for improved accessibility and features.*

- **Zoom Support**: WooCommerce is compatible with browser zoom settings up to 400%. Content remains readable and interactive without overlap or loss of functionality.
- **Motion Sensitivity**: Animations respect the prefers-reduced-motion setting in users’ operating systems where applicable.
- **Accessible Defaults**: Out-of-the-box configurations are designed to meet WCAG Level AA color contrast and usability requirements.
- **Screen Reader Testing**: WooCommerce is tested using screen readers such as VoiceOver (macOS) JAWS(Windows) and NVDA (Windows).

We welcome feedback about accessibility in WooCommerce. If you encounter issues or have suggestions, please [contact support](https://woocommerce.com/contact-us/) or email us at [accessibility@woocommerce.com](mailto:accessibility@woocommerce.com). Accessibility is an ongoing priority, and your input helps us build better experiences for everyone.

