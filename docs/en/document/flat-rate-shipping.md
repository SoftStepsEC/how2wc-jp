---
title: Flat Rate Shipping
url: https://woocommerce.com/document/flat-rate-shipping/
---

Flat Rate Shipping is a shipping method included in WooCommerce that allows you to define a standard shipping rate per item, per shipping class, or per order. On this page you’ll learn how to:

- Create and Configure standard flat rates
- Combine Flat Rates with [Shipping Classes](https://woocommerce.com/document/product-shipping-classes/)
- Configure advanced Flat Rates

**Note:**

This shipping method has to be added to a **Shipping zone**. If you haven’t configured your Shipping zones yet, please check our [Setting up Shipping Zones guide](https://woocommerce.com/document/setting-up-shipping-zones/) before proceeding.

1. Go to **WooCommerce > Settings > Shipping > Shipping zones**.

2. Click the **Edit** button on the shipping zone where you want to offer this method.

3. Inside the shipping zone, click the **Add shipping method** button.

4. Then, select the shipping method and click the **Continue** button.

5. Enter a **Name** that displays to customers in the cart and checkout pages.

6. Select the **Tax Status** to determine whether tax is applied to the **Cost**.

7. Enter the**Cost** for this option, to be applied to the entire cart.

- You can add additional costs per item to this field. See [Advanced Costs](https://woocommerce.com/document/flat-rate-shipping/#advanced-costs) below.
- You can keep the cost at $0.00 to disable Flat Rate, which can be useful if you configured Shipping Classes ([see below](https://woocommerce.com/document/flat-rate-shipping/#shipping-classes)).

8. Click the **Create** button to finish.

Flat Rates can combine with [Shipping Classes](https://woocommerce.com/document/product-shipping-classes/) to offer customers more dynamic shipping rates. If Shipping Classes are configured, additional fields for “shipping class costs” will appear in the flat rate configuration form:

Each shipping class has a cost field associated with it. For products that aren’t assigned to any category, there’s a cost field called “no shipping class cost”. The costs entered into these fields are an **additional cost**added to the **cost** field at the top of the Flat Rate shipping configuration form. To charge shipping costs based only on shipping classes, deactivate the **cost** field at the top of the form by setting it to $0.00.

The **Calculation Type** in the last dropdown of the form determines the shipping costs when products from multiple shipping classes are in a customer’s cart. You can calculate them in two different ways:

- **Per Class:** Charge shipping for each shipping class individually.
- **Per Order:**Charge shipping for the most expensive shipping class.

Here are two examples to show how these two calculations differ from each other:

**Example:**Flat Rate calculated**per shipping class:**

The customer pays $11.00 for shipping in this example because shipping is calculated **per shipping class** (*Cost Field $0.00 + Heavy Shipping Class $10.00+ Small Shipping Class $1.00 = $11.00)*

**Example**: Flat Rate calculated **per order**:

The customer pays $10.00 for shipping in this example because shipping is calculated **per order**and only the heavy shipping class is added to the cart flat rate *(Cost Field $0.00 + Heavy Shipping Class (most expensive) $10.00= $10.00)* .

You can configure Flat Rates based on the quantity of items in a cart or a percentage of the total order costs. Additionally, when you use percentage-based shipping fees, you can set minimum and maximum shipping costs to ensure that you never charge too little or too much for shipping.Configuring advanced flat rates requires writing a shipping formula. Here are the components/placeholders available for these formulas:

- **[qty]**— This is the number of products in the cart
- [fee percent=”numeric value”] – This calculates a shipping fee as a percentage of the total cost of products to be shipped. If all items in the order require shipping, the percentage is applied to the order total. To ensure accurate shipping costs, you can set a minimum or maximum fee for the percentage-based calculation using the following:
  - min_fee=”numeric value”
  - max_fee=”numeric value”
  

**Below are a few examples of how to set up advanced flat rates:**

- **Example: Quantity Based Flat Rate**– You want to charge your customers a $10 standard flat rate + $2 for each item in their cart. In the cost field write this formula:

**10 + ( 2 * [qty] )**

- **Example: Percentage-Based Flat Rate –**You want to charge your customers a $10 flat rate + a 10% shipping fee on their order total. In the cost field write the following formula:

**10 + [fee percent="10"]**

- **Example: Percentage-Based Flat Rate with Min Fee Applied:**You want to charge your customers a $10 flat rate + 10% shipping fee on their total order. Additionally, you want to make sure that your customers are never charged less than $4.00 for shipping. In the cost field write this formula:

**10 + [fee percent="10" min_fee="4"]**

Setting up a combination of free shipping for some products and a flat rate for others requires the use of [Shipping Classes](https://woocommerce.com/document/product-shipping-classes/).

In this use case, we set up three shipping classes: **Free Shipping**, **Regular Shipping**, and **Expedited Shipping**. We then [assigned them to the appropriate products](https://woocommerce.com/document/product-shipping-classes/#section-3). Now, we’ll use the following settings to offer free shipping for the products in the “free shipping” class and flat rates based on quantity for the products in the “regular” and “expedited” shipping classes (**Note:** *customers will only see the general name of the flat rate that is entered at the top of the settings, not the shipping class names*):

1. **Set** the base cost (top of the page) to `$0.00` or leave it `blank`.
2. **Add** the cost of the Expedited Shipping Class Cost field. For our example, we use `20 * [qty]` or $20.00 per product of that class in the cart.
3. **Add** the cost of the Regular Shipping Class Cost field. For our example, we use `10 * [qty]` or $10.00 per product of that class in the cart.
4. **Add** the cost of the Free Shipping Class to $0.00.
5. **Select**`Per Class: Charge shipping for each shipping class individually` from the **Calculation Type** dropdown menu at the bottom of the page.

Here is an example of a customer cart and total shipping costs based on the configuration above. **Notice** that shipping fees are only charged to products in the **regular** and **expedited**shipping classes, while the four products from the **free shipping** class have no shipping fee charged to them:

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

