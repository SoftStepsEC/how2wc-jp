---
title: Remove Related Products Output
url: https://woocommerce.com/document/remove-related-posts-output/
---

This is a **Developer level** doc. If you are unfamiliar with code/templates and resolving potential conflicts, select a [WooExpert or Developer](https://woocommerce.com/customizations/) for assistance. We are unable to provide support for customizations under our[Support Policy](https://woocommerce.com/support-policy/).

|  | /** |
|  | * Remove related products output |
|  | */ |
|  | remove_action( 'woocommerce_after_single_product_summary', 'woocommerce_output_related_products', 20 ); |

```
.related.products {
  display: none;
}
```

