---
title: Order Attribution Tracking
url: https://woocommerce.com/document/order-attribution-tracking/
---

Order attribution tracking is a feature for store owners seeking clarity on the marketing activities, channels, or campaigns driving orders to their online stores. It allows you to attribute orders to traffic sources, providing an understanding of the effectiveness of various marketing efforts.

With this feature, you can discover what prompted a customer’s purchase on your online store. Be it the Google product listing, the trending TikTok video, the shared Facebook post, or perhaps the email campaign from last week.

Knowing the answers to these questions will help you make more informed decisions about where to invest both your time and money.

This new feature makes use of a **last-click attribution model** — widely adopted and the default for most marketing platforms and attribution tools — it gives 100% of the conversion credit to the last interaction before a customer lands on your site. Whether it’s an ad, email, or product listing, the “last thing” clicked takes full credit for the conversion.

As no data is stored in WooCommerce unless an order is placed and all cookies of this feature expire with each session, this feature cannot be used to track your visitors across sessions.

Here are the essential rules governing order attribution tracking:

- **UTM and organic sources take precedence:** [UTM](https://en.wikipedia.org/wiki/UTM_parameters) and organic sources always override any previous source.
- **Type-in (direct) never overrides:** A direct visit (type-in) never overrides a previously identified source.
- **Referral source hierarchy:** The referral source overrides the previous source only if there is no current visitor session active. If it’s within the same session (e.g., within 30 minutes of the first site visit in the same browser), a referral source will never override the previous source.

You can enable (or disable) this feature by going to **WooCommerce > Settings > Advanced > Features > Order Attribution**.

Now that you have order attribution data coming in, let’s discuss how you can analyze and find actionable insights from said data. We have a new order attribution report that you can add to your site via the **WooCommerce Analytics** plugin. This adds five new reports to help you see your top channels, sources, and even devices your customers are using before they buy from your store. See our documentation about each of these reports for further information as well.

Outside these new reports, you can see order attribution data in other places as well. Within the order edit page for each new order, you’ll find two meta boxes — “**Order attribution” and “Customer history.”** These boxes provide more information on the origin of the order and offer a detailed history of the customer’s interactions with your store. These meta boxes show the following information:

- **Order attribution:** Origin, Source type, [UTM](https://en.wikipedia.org/wiki/UTM_parameters) campaign (if source type is UTM), and Medium, Device type, and Session page views. UTM [Source platform, Creative format, and Marketing tactic](https://support.google.com/analytics/answer/10917952#parameters&zippy=%2Cin-this-article) parameters are also supported.
- **Customer history:** Number of orders completed, orders refunded, total spend

The **WooCommerce > Orders** table includes a new column that displays the order origin. This column reveals the origin of each order, providing immediate insight into which channels are driving sales.

**Note:**

Order Attribution Tracking data is available only to orders generated when this feature is enabled. If you deactivate this feature at any point, orders placed during the disabled period will not incorporate this data.

The order attribution tracking feature stores the following information when an order is placed:

- **Referring source:** The URL of the site that referred the visitor to your site.
- **UTM parameters:** If the URL that referred the visitor to your site includes [UTM](https://en.wikipedia.org/wiki/UTM_parameters) parameters, we parse these and store the source, medium, campaign, content, and term parameters.
- **Device type:** The type of device your customer used when placing the order (desktop, tablet, or mobile).
- **Session page views**: The number of page views in the session before placing the order.

The order attribution feature uses these cookies:

When placing orders without any referral or source (i.e., directly from the shop), the origin will always be “Direct.” To conduct tests with various origins, please follow the steps below using an incognito/private window.

#### Referral

- Go to any website and edit a link `href` in developer tools to point to your store. Add items to the cart and complete the checkout.

#### Organic

- Go to https://www.google.com/ and edit a link `href` in developer tools to point to your store. Add items to the cart and complete the checkout.

#### Using UTM Parameters

- Open the store with a URL like `https://yourstorename.com/shop/?utm_source=newsletter&utm_medium=email&utm_campaign=sale&utm_content=utmcontent&utm_term=utm_term`.
- Add items to the cart and complete the checkout.

#### Type-in (Direct)

- Same as above, but without any parameters.

#### Web Admin

- [Manually Add an order from the backend](https://woocommerce.com/document/managing-orders/view-edit-or-add-an-order/#manually-adding-an-order)

#### Unknown

- [Manually Add an order from the backend](https://woocommerce.com/document/managing-orders/view-edit-or-add-an-order/#manually-adding-an-order)
- Then erase the associated metadata from the database:

```
DELETE FROM `wp_wc_orders_meta` WHERE `order_id` = 93 AND `meta_key` LIKE '_wc_order_attribution%';

DELETE FROM `wp_postmeta` WHERE `post_id` = 93 AND `meta_key` LIKE '_wc_order_attribution%';
```

This data is available only to orders generated while the feature is enabled. If you deactivate this feature at any point, orders placed during the disabled period will not incorporate this data.

Yes. The cookies listed above are stored in the visitor’s browser. These cookies will expire with the visitor’s session or if they clear their cookie history.

Only in the event of an order the data stored in these cookies will be accessed.

By default, a customer’s session is considered to last 30 minutes. The cookies set by this feature expire with the session and cannot be used to track your visitors across multiple sessions or for remarketing.

Some Web Application Firewalls use rulesets that incorrectly flag the cookies used to capture visitor information for order attribution, leading to `403 Forbidden` errors for visitors. This issue has been recognized by some of the most common ruleset providers:

- Comodo WAF ruleset – [released an updated ruleset](https://developer.woocommerce.com/2024/01/16/woocommerce-8-5-1-issues-with-web-application-firewalls-modsecurity/#comment-8554) to whitelist the cookies. If your WAF uses this ruleset, any issue should be resolved by updating to the latest version.
- OWASP core ruleset – [recognized the issue](https://github.com/coreruleset/coreruleset/issues/3525#issuecomment-1922034226), but don’t plan to release a fix. If your WAF uses this ruleset, you should add an exclusion rule to resolve the issue. The rule is available in [this Github comment](https://github.com/coreruleset/coreruleset/issues/3525#issuecomment-1922208950).

Updating your ruleset, adding the exclusion rule, or asking your hosting provider to do so should resolve the WAF issues.

**WooCommerce 9.0 introduced another method for avoiding WAF false positives**: the `wc_order_attribution_use_base64_cookies` filter. Setting this filter to `true` will use Base64 encoding for the data captured in the [order attribution cookies](https://woocommerce.com/document/order-attribution-tracking/#section-7), avoiding any substrings that may trip up overzealous WAFs:

```
add_filter( 'wc_order_attribution_use_base64_cookies', '__return_true' );
```

If those options don’t work resolve the WAF issues, you can disable the order attribution feature entirely at **WooCommerce > Settings > Advanced > Features**, or programmatically using:

```
# PHP 
update_option( 'woocommerce_feature_order_attribution_enabled', 'no' );

# WP CLI
wp option update woocommerce_feature_order_attribution_enabled "no"
```

The order attribution information is stored temporarily using cookies in visitors’ browsers. Only in the event of an order, this data will be read and saved as order metadata.

The cookies in visitors’ browsers expire after each session. WooCommerce’s order attribution feature is not suited to tracking visitors across multiple sessions or aggregating behavioral visitor profiles.

Yes, we made WooCommerce’s order attribution compatible with [WP Consent API](https://wordpress.org/plugins/wp-consent-api/) to allow convenient integration with Consent Management Platforms.

If you have previously opted into [sharing data](https://woocommerce.com/usage-tracking/) (with Automattic) in WooCommerce, then statistical order attribution data captured as part of this feature will be shared with Automattic on a per-order basis. Customer data, such as email address, billing, or shipping data, will **not** be transmitted.

