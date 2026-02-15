---
title: 製品カテゴリのショートコード
url: https://woocommerce.com/document/woocommerce-shortcodes/product-category/
---

これら 2 つのショートコードを使用すると、どのページにも製品カテゴリが表示されます。

- `[product_category]` — 指定した商品カテゴリーの商品を表示します。
- `[product_categories]` — すべての商品カテゴリーを表示します。

- `ids` — 商品の[カテゴリID](https://woocommerce.com/document/find-product-category-ids/)を指定します。[product_categories] と共に使用します。
- `category` — カテゴリID、名前、またはスラッグのいずれかを指定できます。[product_category] ​​と共に使用します。
- `limit` — 表示するカテゴリの数です。「0」を入力するか、何も指定しないと、すべてのカテゴリが表示されます。(例のように `number` と置き換え可能です)
- `columns` — 表示する列の数です。デフォルトは4です。
- `hide_empty` — デフォルトは「1」で、空のカテゴリは非表示になります。「0」に設定すると、空のカテゴリが表示されます。
- `parent` — すべての子カテゴリを表示する場合は、特定のカテゴリIDを設定します。または、「0」（以下の例のように）に設定すると、最上位カテゴリのみが表示されます。
- `orderby` — デフォルトは「name」、「id」、「slug」、または「menu_order」による並べ替えです。追加オプションとして、指定したIDで並べ替えたい場合は、`orderby="include"` を使用できます。
- `order` **—** `orderby` で設定された方法を使用して、カテゴリーの並べ替えを昇順 (`ASC`) にするか降順 (`DESC`) にするかを指定します。デフォルトは `ASC` です。

ページにトップレベルのカテゴリのみを表示し、サブカテゴリを除外したいとします。次のショートコードを使用するとそれが可能です。

```
[product_categories number="0" parent="0"]
```

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

