---
title: WooCommerceで共有可能なチェックアウトURLを作成する
url: https://woocommerce.com/document/creating-sharable-checkout-urls-in-woocommerce/
---

共有可能なチェックアウト URL を使用すると、メール キャンペーン、ソーシャル メディア、ランディング ページを通じて、クーポン コード付きのすぐに購入できるバンドルを簡単に共有できます。

以下では、特定の商品とクーポンを自動的にカートに追加し、顧客をチェックアウトページにリダイレクトするカスタムリンクの作成方法を説明します。追加オプションのないシンプルな商品、個別のバリエーション、クーポンなどを含めることができます。

**共有可能なチェックアウト URL の例:**

https://example.com/checkout-link/?products=123:2,456:1&coupon=SPRING10

共有可能なチェックアウト URL では、正しい製品をカートに追加するために WooCommerce 製品 ID が必要です。

特定の[シンプル商品](https://woocommerce.com/document/simple-product/)をカートに追加するには、ストアのWP Adminダッシュボードで**WooCommerce > 商品**から商品IDを見つけてください。商品名にマウスを合わせると、商品IDが商品名の下に表示されます。

特定の[バリエーション商品](https://woocommerce.com/document/variable-product/)をカートに追加するには、商品編集時に商品データの「バリエーション」セクションにあるバリエーションIDを使用します。例えば、次のスクリーンショットにある緑色の小さなバリエーションを追加する場合、IDは83になります。

単一の製品をカートに追加するには、次の URL 構造を使用します。

```
https://example.com/checkout-link/?products=PRODUCT_ID:QUANTITY
```

`example.com` をストアの URL に、`PRODUCT_ID` と `QUANTITY` をカートに追加する商品 ID と数量に置き換えてください。商品 ID と数量はコロンで区切ってください。

追加製品を区切るにはコンマを使用します。

```
https://example.com/checkout-link/?products=
PRODUCT_ID_1:QUANTITY_1,PRODUCT_ID_2:QUANTITY_2,PRODUCT_ID_3:QUANTITY_3
```

**注記：**

1 回の注文につき 1 つの製品に制限されている製品の場合、共有可能な URL に追加された数量に関係なく、カートに追加される製品は 1 つだけです。

[クーポン](https://woocommerce.com/document/coupon-management/) コードを含めると、クーポンが顧客のカートに自動的に適用されます。

```
https://example.com/checkout-link/?products=PRODUCT_ID:QUANTITY&coupon=COUPONCODE
```

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

