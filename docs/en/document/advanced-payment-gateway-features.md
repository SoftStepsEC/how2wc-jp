---
title: Skyverge Extensions Advanced Payment Gateway Features
url: https://woocommerce.com/document/advanced-payment-gateway-features/
---

```
Note: This documentation only covers payment gateway features for WooCommerce payment extensions developed by Skyverge. Features by other payment gateways such as WooPayments, Stripe, etc., aren't covered.
```

This document covers some advanced features of WooCommerce payment gateway integration plugins (specifically those built by [SkyVerge](http://skyverge.com/)). The following gateways support one or more of the listed features:

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [CyberSource](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

Each payment method may support different features, so please refer to the payment gateway list in each section to determine which gateway supports the feature.

**Supported Gateways**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [CyberSource](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

Each of these payment gateway extensions allows you to authorize charges during checkout, then manually capture them later. You can do this via your Payment gateway control panel / admin, or can easily do so from the WooCommerce *Edit Order* page.

```
Not sure what this means? Check out this tutorial on Authorizing vs. Authorizing and Capturing.
```

When payment is authorized for an order, the order status will be set to “on hold”. You can edit the order by going to **WooCommerce > Orders**, then clicking on the order number to edit the order that needs to have the charge captured.

If your payment gateway requires PHP 5.3, you’ll see a “Capture Charge” button; otherwise, you’ll use the “Capture Charge” action in the **Order Actions** menu:

Once you’ve selected “Capture Charge” and saved the order, payments will be captured via the payment gateway, the order status will update to “processing”, and the Order notes will be updated to reflect these changes (the gateway name will vary in the order notes):

Bulk capturing charges is also possible. Select the orders for which you want to capture charges on the “Orders” page, then use the bulk “Capture Charge” action to update all selected orders:

**Supported Gateways**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [CyberSource](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)

We’re in the process of improving some gateways to allow for automated capture when an order changes to a paid status (typically processing or completed). This will automatically attempt to capture a transaction when the status changes, removing the need to use the “capture charge” action.

This **setting must be enabled** to process auto-captures.

**Supported Gateways**

- [Bambora](https://woocommerce.com/products/bambora/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)

These payment methods allow for partial captures, meaning more than one payment capture can be processed for an order, with a custom amount of your choosing for the capture. This must be enabled in the plugin settings.

To perform a partial capture, edit the order, and click “Capture charge” for the order actions.

You can then enter the desired amount for the capture, and can process the capture. You can repeat this action until the total possible capture amount has been used.

**Supported Gateways**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [CyberSource](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

These payment gateways have **automatic refund support** added. This means that refunds can be processed directly in WooCommerce without the need to log into the payment gateway control panel / admin.

To process an automatic refund, the “Refund via Credit Card” (or “Refund via {Gateway Name}” if you’ve changed the payment method title) option must be used when creating the refund. This will send the refund information to the payment gateway to process the refund.

```
If the transaction has been authorized but not yet been captured, or if the transaction has been captured but is not yet settled in the payment gateway, the order will be voided instead of refunded.
```

For a **partial refund**, selecting “Refund with Credit Card” will process the refund and create an order note to designate the amount that was refunded via the payment gateway.

For **total refunds**, the refund amount will be added to an order note, but the order status will also be updated. If the total amount is completely refunded via this gateway, the order status will be changed to “refunded”, and an additional order note is added for the status change.

This allows merchants to process refund transactions completely inside of WooCommerce, saving time on store management.

You may see an error message that looks something like this when trying to process an automatic refund:

```
Oops, you cannot partially void this order. Please use the full order amount.
```

This means that you’re trying to perform a partial refund, but the charge has not been settled (typically when you try to refund within a day of the purchase). The plugin tries to void this order since the funds have not been transferred (to cancel the order instead of refunding it), but most payment gateways do not permit partial voids.

Please wait until the charge has settled (about one day after the charge was made) to refund this transaction.

**Supported Gateways**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [CyberSource](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

Transactions can be **voided** by using the same workflow as [refunds](https://woocommerce.com/document/advanced-payment-gateway-features/#refunds). A void will occur if the transaction has been *authorized*, but not *captured*. For most payment gateways, voids will also occur for authorized & captured transactions that have not yet been settled in the payment gateway account. As funds haven’t been transferred, a refund can’t truly be processed.

Instead, this will void the authorized charge in the payment gateway and note that the charge is voided via Order Note. **Note that** WooCommerce will still show “Refund via Credit Card” as the text to void a transaction still — this is normal.

When an order is voided, the order status will change to **cancelled**, not refunded.

Most payment gateways **do not allow** partial voids, so you must void an entire order. If you try to partially void an order, you will most likely see this notice:

```
Oops, you cannot partially void this order. Please use the full order amount.
```

If you need to only remit part of the order, either edit the order before capturing the charge, or capture the payment then refund part of it.

**Supported Gateways**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [CyberSource](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

The enhanced checkout form provides an improved checkout experience over the default WooCommerce pay form. This form provides **larger input fields**, **auto-formatted card numbers**, automatic **card-type icon display**, **auto-formatted expiration dates**, and **retina card icons**.

This also includes **mobile-friendly form support**, which means that both credit card and eCheck inputs will use a `tel` type input, bringing up a numeric keyboard instead of a full one on mobile devices:

**Supported Gateways**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [CyberSource](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)

For any payment gateway that supports saved methods, these methods can be managed from the account to set a default or delete saved methods. However, these gateways support **enhanced saved methods**, which have a few extra features. First, the items can use **nicknames** (such as “Personal” or “Business”), making it easy for your customers to identify the item at checkout. The nickname can be added by clicking the “edit” action for the method.

Next, these methods will also use nicknames at checkout so customers can identify their saved cards easily.

**Supported Gateways**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [CyberSource](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

Payment gateways that allow tokenization can let logged-in customers save payment methods during your checkout process by default to use them in future checkouts, with Subscriptions, or for Pre-Orders.

However, these gateways also support adding a saved payment method from the “My account” section using an “Add Payment Method” workflow. Customers can add a saved payment method by going to their My Account page and scrolling to the “My Payment Methods” section. This will list any linked methods, along with the payment method type.

Customers can add new methods by clicking “Add New Payment Method”. This will give them a form to securely save a payment method for future use without going through checkout.

Only the methods that support tokenization will be listed here.

**Supported Gateways**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [CyberSource](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

All of these payment methods fully support WooCommerce Subscriptions, and tokenized or saved payment methods could be used for a subscription. As a result, it could be problematic for a customer to delete this saved payment method, as the next renewal order will fail. You’ll have to ask the customer to add a new method and then manually update the token attached to the subscription.

To avoid this, when Subscriptions is active, the “My Payment Methods” table adapts to it and disables deletion of methods tied to subscriptions.

If a method is tied to more than one subscription, the “Subscription” column will show a comma-separated list of each subscription, and the “View Subscription” button is removed. No method tied to a subscription can be deleted until the subscription is switched to a new payment method.

**Supported Gateways**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [CyberSource](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

These payment gateways support detailed “payment declined” messages on the checkout when available. Typically if a gateway declines a transaction, WooCommerce provides a generic, “Error processing payment, please try another method,” message. This isn’t really helpful to your customers.

If the gateway provides a response code that can display a useful message, such as CVV mismatch or zip code mismatch, the payment gateway will instead display a more intelligent message to the customer to help them successfully complete checkout.

**Supported Gateways**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [CyberSource](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

There are times when saved payment method tokens on your site can get out-of-sync with tokens in your payment gateway account, or you’ll need to manually add tokens. The customer payment token editor allows you to do this for each payment method to save both live and sandbox tokens.

You can access the token editor from the “Edit User” page, right before customer billing details.

This editor lets you change tokens, other method / token information, remove methods, or make new saved methods the default method for the customer. This is also useful for sites running Subscriptions, as you can copy token details from this page to add them to a new subscription.

Note that some gateways may have additional information, depending on what the gateway requires for using tokens. For example, Authorize.Net CIM will show Customer ID (necessary for charging a token). The token editor may also show other information if stored in the gateway (such as the Shipping profile ID in AuthNet CIM).

Have a question before you buy? [Please fill out this pre-sales form.](http://skyverge.com/contact/?form_type=pre-sales)

Already purchased and need some assistance? [Get in touch with support](https://woocommerce.com/my-account/create-a-ticket/) via the help desk.

**Scope of support:**

We are unable to provide support for customizations under our**Support Policy**. If you need to customize a snippet or extend its functionality, we recommend working with a [Woo Agency Partner](https://woocommerce.com/development-services/) or a WooCommerce developer on [Codeable](https://www.codeable.io/partners/woocommerce/?ref=qGefA6#tiers).

