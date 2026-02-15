---
title: ページショートコード
url: https://woocommerce.com/document/woocommerce-shortcodes/page-shortcodes/
---

WooCommerceは、サイトのどこかにカート、チェックアウト、アカウントエリアが設定されていないと正常に機能しません。これらのショートコードを使用すると、サイトのページにこれらのエリアを追加できます。

WooCommerce バージョン 8.3 以降、新規インストールではカートブロックとチェックアウトブロックがデフォルトになりました。現在、マイアカウントエリアを表示するためのブロックベースの代替手段はありません。

**注:** WooCommerceブロックとして利用可能な、コンバージョンに最適化された新しい[カートブロックとチェックアウトブロック](https://woocommerce.com/document/cart-checkout-blocks-status/)のご利用を推奨いたします。ただし、場合によってはショートコード版の方が拡張機能との互換性が高い場合があります。

**woocommerce_cart** – カートページを表示します **woocommerce_checkout** – チェックアウトページを表示します **woocommerce_my_account** – ユーザーアカウントページを表示します **woocommerce_order_tracking** – 注文追跡フォームを表示します

ほとんどの場合、必要なショートコードは [セットアップ ウィザード](https://woocommerce.com/document/woocommerce-onboarding-wizard/) によって自動的にページに追加されるため、手動で追加する必要はありません。

カート ページで使用されるカート ショートコードは、カートの内容、クーポン コードのインターフェイス、その他の基本的な注文情報を表示します。

```
[woocommerce_cart]
```

チェックアウト ページで使用されるチェックアウト ショートコードは、チェックアウト プロセスを表示します。

```
[woocommerce_checkout]
```

「マイアカウント」エリアを表示します。現在ログインしているお客様は、過去の注文履歴の確認や情報の更新が可能です。ログインしていないお客様には、サインインフォームが表示されます。また、[アカウントとプライバシー設定](https://woocommerce.com/document/configuring-woocommerce-settings/#accounts-and-privacy-settings)で登録フォームを有効にしている場合は、登録フォームも表示されます。現在、マイアカウントエリアを表示するためのブロックベースの代替手段はありません。

```
[woocommerce_my_account]
```

ユーザーが注文番号と請求先メールアドレスを入力することで、注文のステータスと詳細を確認できます。これはストアにアカウントを持っていないゲストユーザーにとって便利ですが、「cart」「checkout」「my account」ショートコード（またはブロック）とは異なり、必須ではありません。以下は、ゲストの「My Account」ページでの使用例です。

```
[woocommerce_order_tracking]
```

IDまたはSKUで、単一の商品ページ全体を表示します。これは、ショップページ以外のページ（例えば、新商品に関する投稿など）に商品を追加したい場合に便利です。*（xxとxxxは実際の商品番号またはSKUに置き換えてください）*

```
[product_page id="xx"]
```

```
[product_page sku="xxx"]
```

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

