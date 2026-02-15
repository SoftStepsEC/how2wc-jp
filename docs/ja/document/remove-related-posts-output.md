---
title: 関連製品の出力を削除
url: https://woocommerce.com/document/remove-related-posts-output/
---

これは**開発者向け**ドキュメントです。コードやテンプレート、および潜在的な競合の解決方法にご不明な点がある場合は、[WooExpert または開発者](https://woocommerce.com/customizations/)にご相談ください。[サポートポリシー](https://woocommerce.com/support-policy/)に基づき、カスタマイズに関するサポートは提供しておりません。

| | /** |
| | * 関連商品の出力を削除 |
| | */ |
| | remove_action( 'woocommerce_after_single_product_summary', 'woocommerce_output_related_products', 20 ); |

```
.related.products {
  display: none;
}
```

