---
title: WooCommerceのカートに追加URLを作成する
url: https://woocommerce.com/document/quick-guide-to-woocommerce-add-to-cart-urls/
---

以下では、カスタムURLを使って顧客のカートに商品を追加するための、クリック可能なリンクを作成する方法を説明します。このURLまたはリンクを使用することで、商品をカートに追加したり、数量を指定したり、別のページへリダイレクトしたりすることができます。

カートに追加URLが機能するには、WooCommerceの商品IDが必要です。商品IDは、ストアのWP Adminダッシュボードで「WooCommerce > 商品」を選択し、商品名にマウスオーバーすると確認できます。商品IDは商品名の下に表示されます（下図参照）。

[シンプルな商品](https://woocommerce.com/document/managing-products/add-product/#adding-a-simple-product)をカートに追加するには、以下のURL構造を使用してください。`example.com`をサイトのURLに、`PRODUCT_ID`と`QUANTITY`を具体的な商品の詳細に置き換えてください。

```
https://example.com/?add-to-cart=PRODUCT_ID&quantity=QUANTITY
```

特定の[バリエーション商品](https://woocommerce.com/document/variable-product/)をカートに追加するには、商品編集時に「バリエーション」タブにある「バリエーションID」を使用してください。例えば、ロゴ付きの青いバリエーションを使用する場合は、IDは#39になります（下の画像を参照）。

```
https://example.com/?add-to-cart=VARIATION_ID&quantity=QUANTITY
```

[グループ化された製品](https://woocommerce.com/document/managing-products/add-product/#adding-a-grouped-product)の場合は、各サブ製品の製品 ID と数量を含めます。

1 つのサブ製品の場合:

```
https://example.com/?add-to-cart=GROUPED_PRODUCT_ID&quantity[SUB_PRODUCT_ID]=QUANTITY
```

追加のサブ製品ごとに次の操作を繰り返します。

```
https://example.com/?add-to-cart=GROUPED_PRODUCT_ID&quantity[SUB_PRODUCT_ID]=QUANTITY&quantity[SUB_PRODUCT_ID]=QUANTITY
```

商品がカートに追加された後、**顧客をどこにリダイレクトするか**を選択できます。WooCommerceの設定でカートページまたはチェックアウトページにリダイレクトするように設定されていない限り、デフォルトでは顧客は同じページに留まります。

リダイレクト先をカスタマイズするには、顧客を誘導するURLを追加します。例えば、商品をカートに追加した後に**チェックアウト**ページにリダイレクトするには、次のように記述します。

```
https://example.com/checkout/?add-to-cart=PRODUCT_ID&quantity=QUANTITY
```

別の例として、商品をカートに追加した後に **cart** ページにリダイレクトするには、次を使用します。

```
https://example.com/cart/?add-to-cart=PRODUCT_ID&quantity=QUANTITY
```

アイテムがカートに追加されたときに**ページの再読み込みを防ぐ**には、ストアの WP 管理ダッシュボードの「WooCommerce > 設定 > 製品 > 一般」で AJAX を有効にします。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

