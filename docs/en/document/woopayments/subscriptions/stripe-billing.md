---
title: WooPayments: Stripe Billing for subscriptions
url: https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/
---

Besides basic compatibility with [the Subscriptions extension](https://woocommerce.com/products/woocommerce-subscriptions/), WooPayments also offers one more feature to Subscriptions users based in the United States: the ability to utilize a billing engine powered by our payments partner, called Stripe Billing.

**NOTE:** Prior to version 10.2, WooPayments offered an integrated subscriptions feature that did not require the Subscriptions plugin. However, that feature has now been removed for all merchants. The Stripe Billing feature is similar, but you must have the Subscriptions extension installed to use it.

With WooCommerce Subscriptions, automatic recurring payments are initiated by your WooCommerce site and then processed by the payment gateway the customer chose during checkout. This is called an “on-site” billing engine.

An alternative approach is to allow the payment gateway *itself* to initiate the recurring payment. This is called an “off-site” billing engine, and it’s how Stripe Billing works.

The advantages to using an on-site billing engine are:

- **More features.** Many of the advanced features of the Subscriptions plugin are only available for subscriptions that use the on-site billing engine.
- **Less complexity**. Your site is the “source of truth” for what payments should be made and when. There’s no second system that needs to be kept in sync.
- **More supportable.** Because all the recurring billing data is stored on your site, it’s much easier to fix if anything were to go wrong.
- **Widely available.** Stripe Billing is only available for WooPayments merchants in the U.S., but the Subscriptions extension can be used by merchants everywhere.
- **No extra fees.** The Subscriptions plugin is available for a simple yearly price, whereas using Stripe Billing charges you a fee on every subscription transaction.

The sole advantage of the off-site billing engine is:

- **Reliability.** If your site were to go offline for an extended period of time (e.g., multiple days), an off-site billing engine could still take recurring subscription payments.

Note, however, that this “reliability” has several tricky downsides:

- First, letting the payment gateway take renewals while your site is offline means that renewals will be created in the payments system but *not* in WooCommerce itself. The resulting information mismatch can be very difficult and time-consuming to fix.
- Second, should you ever decide to close your business or otherwise shut down the site, it’s very easy to forget that *renewals will still happen* unless you cancel them all beforehand. Many merchants delete their sites and think that it will automatically stop all renewal payments. *This is not the case with an off-site billing engine!*
- Even if your site goes offline while using the on-site engine, the missed subscription renewals will start again from where they left off once the site is back online. In other words, payments may be delayed, but they will not be entirely skipped.

To use the Stripe Billing feature of WooPayments:

- You must have [WooCommerce Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/) installed and active.
- Your WooPayments account must be based in the United States.

If you do not meet these criteria, the Stripe Billing option will not be available.

Enabling the Stripe Billing option will incur an additional fee on subscription products or renewals that use the Stripe Billing engine. This fee applies to *the entire order*, not just the subscription line item. Please see [our fees page](https://woocommerce.com/document/woopayments/fees-and-debits/fees/#united-states) for full details.

Note that, if you have [mixed checkout](https://woocommerce.com/document/subscriptions/store-manager-guide/#mixed-checkout) enabled in the Subscriptions settings, this might result in being charged a larger-than-expected fee for certain orders. As an example, if a customer is purchasing an inexpensive subscription alongside a much more expensive *non*-subscription product, the additional fee will be applied to the entire order amount, not just the inexpensive subscription item(s).

Assuming you meet the criteria above, you can enable the Stripe Billing option like so:

1. Navigate to your site’s administrator dashboard.
2. Locate your WooPayments settings at **Payments > Settings**.
3. Scroll down to the *Advanced settings* section at the bottom.
4. Check the box next to **Enable Stripe Billing for future subscriptions**.

1. Click **Save Changes** at the bottom of the page.

Once the setting is enabled, any new subscriptions paid for with WooPayments will be powered by the off-site Stripe Billing engine.

**NOTE:** The setting is called “Enable Stripe Billing for *future* subscriptions” for a reason. If you have existing subscriptions using the on-site Subscriptions billing engine, there is no way to migrate those over to use Stripe Billing.

To find subscriptions that are using the Stripe Billing engine:

1. Go to **WooCommerce > Subscriptions** in your site’s dashboard.
2. Look for any subscription with a question mark icon after the date in the *Next Payment* column.

1. Hovering over the question mark will show a popup: “This date should be treated as an estimate only. The payment gateway for this subscription controls when payments are processed.” (This message is normal for Stripe Billing subscriptions.)
2. Click the subscription number to open up the subscription details.
3. You’ll see a WooPayments Subscription ID beginning with `sub_` in the details box. This confirms that the subscription you’re viewing is powered by the off-site Stripe Billing engine.

When Stripe Billing is enabled, the settings for the Subscriptions extension remain in their normal location under **WooCommerce > Settings > Subscriptions**.

However, some of the settings and other WooCommerce Subscriptions features will not work for subscriptions that use the Stripe Billing engine. Those are:

- [Customizable payment retry system](https://woocommerce.com/document/subscriptions/develop/failed-payment-retry/)
- [Early renewals](https://woocommerce.com/document/subscriptions/early-renewal/)
- [Free / no cost subscriptions](https://woocommerce.com/document/subscriptions/store-manager-guide/#section-9)1
- [Limited payment coupons](https://woocommerce.com/document/subscriptions/store-manager-guide/#section-12)
- [Manual renewal](https://woocommerce.com/document/subscriptions/renewal-process/#manual-recurring-payments) and the [auto-renewal toggle](https://woocommerce.com/document/subscriptions/renewal-process/#auto-renew-toggle)
- [Manually creating subscriptions](https://woocommerce.com/document/subscriptions/add-or-modify-a-subscription/) with custom [billing schedules](https://woocommerce.com/document/subscriptions/add-or-modify-a-subscription/#section-3)2
- [Manually editing subscriptions](https://woocommerce.com/document/subscriptions/add-or-modify-a-subscription/#section-10)3
- [Subscription switching](https://woocommerce.com/document/subscriptions/switching-guide/)

1 Free subscriptions can be purchased, but will always use the on-site engine. 2 The billing schedule will always be determined by the product configuration. 3 Line items, amounts, and dates cannot be changed.

Additionally, using Stripe Billing for subscriptions is incompatible with the [manual capture setting](https://woocommerce.com/document/woopayments/settings-guide/authorize-and-capture/). You cannot use both at the same time.

You can disable the off-site Stripe Billing engine at any time.

If you do disable it, any existing subscriptions that use the Stripe Billing engine will be automatically moved to use the on-site Subscriptions engine instead. This happens as soon as you click the **Save changes** button at the bottom.

Migration may take some time depending on how many subscriptions you had on Stripe Billing. The process occurs behind the scenes, and your customers shouldn’t notice any difference in behavior. [Migration logs](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/#migration-logs) are also available, should you need them.

When the migration is finished, the notice will change to inform you of that, and your subscribers will continue to renew automatically as before.

**NOTE:** If the migration notice does not appear when you disable the setting, and instead the setting box becomes disabled or “grayed out”, you may not have the full Subscriptions extension installed or active. See [this section](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/#migrating-subscribers).

If you need to view the subscription migration log files (for example, if our support staff asks for them), you can do that by following these steps:

1. Go to **WooCommerce > Status > Logs** in your site’s admin dashboard.
2. Use the dropdown to find a log file beginning with `woopayments-subscription-migration-` followed by date in the `YYYY-MM-DD` format.
3. Once you’ve selected a log, click the **View** button to load it.
4. Select the entire log contents and copy them to the clipboard.
5. Open a new text file on your computer and paste the log contents in.
6. Attach that file to your email response to our support staff.

Prior to version 10.2.0, WooPayments included an integrated subscriptions feature that didn’t require the Subscriptions extension. However, all customer-facing and merchant-facing aspects of that feature have now been fully removed for everyone.

What we did **NOT** do is stop existing subscriptions still using this old feature. This means that you may still have subscribers paying you, and their renewal orders being created, but neither you nor the customer can view, manage, or cancel the subscriptions. If your subscriptions pages in the dashboard have disappeared after updating to 10.2.0 or later, this is almost certainly the reason why! Please read further for instructions on how to resolve this situation.

In order to manage these older subscriptions, you must install the Subscriptions plugin. The emails we sent to you contain instructions for how to obtain a free copy. (If you did not receive such an email, please [contact support](https://woocommerce.com/my-account/contact-support/) for help.)

Once you have the Subscriptions extension installed, your ability to view, manage, and create subscriptions will be restored. Customers will also regain those abilities.

Afterward, you can optionally [disable Stripe Billing](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/#disabling), or simply do nothing to keep using it.

[Disabling the WooPayments gateway](https://woocommerce.com/document/woopayments/settings-guide/#enable-woopayments) only affects the payment options shown in the WooCommerce checkout form. Because existing subscriptions renew *without* going through the checkout form, they will not be affected, and they will continue to renew automatically via WooPayments.

That said, if you do disable the gateway, no *new* Stripe Billing subscriptions will be created. This is because Stripe Billing subscriptions *must* be paid for via WooPayments, but that cannot happen with the gateway disabled. Any subscription purchases made with another gateway will use the on-site WooCommerce Subscriptions billing engine.

If you attempt to deactivate the WooPayments plugin while your site has Stripe Billing subscriptions, a popup warning will be shown:

If you deactivate, any Stripe Billing subscriptions that were not cancelled prior to the plugin being deactivated *will continue to collect payments from customers!*This is due to the the [off-site billing engine](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/#billing-engines) that Stripe Billing uses.

Furthermore, because WooPayments is deactivated, your site will no longer generate the corresponding WooCommerce orders or send associated emails to customers. As you can imagine, **this situation is almost never advisable.**

If you do not want renewal payments to keep being charged, you should [cancel all Stripe Billing subscriptions](https://woocommerce.com/document/subscriptions/store-manager-guide/#cancel-or-suspend-subscription) before deactivating WooPayments!

If you have taken your site offline, or for some other reason you cannot reactivate the WooPayments plugin and cancel existing subscriptions, please [contact us](https://woocommerce.com/my-account/contact-support/) for help.

They will keep renewing until they are cancelled, due to the [off-site billing engine](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/#billing-engines). This also means that renewal orders will still be created in WooCommerce.

Of course, if WooCommerce Subscriptions is deactivated, no new subscriptions can be created, since subscription products will no longer be available.

Most extensions that work with WooCommerce Subscriptions will be compatible with Stripe Billing subscriptions as well. However, keep in mind the [incompatible settings](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/#incompatible-settings).

As an example, AutomateWoo is mostly compatible, but if you try to use it to edit the line items of a Stripe Billing subscription, that will not work.

Yes, subscriptions that use Stripe Billing are compatible with the usual Subscriptions reports under the **WooCommerce > Reports > Subscriptions** tab.

