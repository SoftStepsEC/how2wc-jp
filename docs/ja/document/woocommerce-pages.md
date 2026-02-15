---
title: WooCommerceページ
url: https://woocommerce.com/document/woocommerce-pages/
---

インストール時に、WooCommerce は [セットアップ ウィザード](https://woocommerce.com/document/woocommerce-setup-wizard/) を通じて次の新しいページを作成します。

- ショップ – コンテンツは不要です。
- カート – [WooCommerce カートブロック](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/cart-block/) が含まれ、カートのコンテンツが表示されます。
- チェックアウト – [WooCommerce チェックアウトブロック](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/) が含まれ、配送や支払いオプションなどの情報が表示されます。
- マイアカウント – `[woocommerce_my_account]` ショートコードが含まれ、顧客のアカウント、注文などに関する情報が表示されます。
- 返金・返品ポリシー（未公開の下書き） – ストアの[返金・返品ポリシー](https://woocommerce.com/document/refund-policy-page-guidelines/) の作成に役立つサンプルテキストが含まれています。必須ではありませんが、強くお勧めします。

**ブロック エディターを使用している場合、ショートコードを追加するにはどうすればよいでしょうか?**

ブロック エディターを使用してページにショートコードを追加するには、`ショートコード` ブロックを使用し、[ショートコード](https://woocommerce.com/document/woocommerce-shortcodes/) を入力してページを保存してください。

セットアップウィザードをスキップした場合、または不足しているWooCommerceページをインストールしたい場合は、**WooCommerce > ステータス > ツール** に移動し、ページインストーラーツールを使用してください。これにより、不足しているデフォルトのWooCommerceページが作成されます。

WooCommerce では、カート、チェックアウト、マイアカウント、利用規約（ToC）、ショップページが、初期設定時に作成されたデフォルトページとして設定されます。デフォルトページとは異なる新しいページを作成したり、カートやチェックアウトなどのページを変更する場合は、**ページ設定** で設定する必要があります。

カート、チェックアウト、マイ アカウント、利用規約のページを設定するには、**WooCommerce > 設定 > 詳細設定** に移動します。次に、関連するドロップダウンで希望のページを選択します。

**カート、チェックアウト、マイアカウントページを同じページに設定できないのはなぜですか?**

その結果、リダイレクトが不正確になり、決済ゲートウェイの機能が損なわれます。WooCommerce 3.7以降では、この問題は発生しません。

**利用規約ページとは何ですか?**

利用規約ページは必須ではありませんが、設定を強くお勧めします。WooCommerceのページ設定で設定すると、チェックアウト時にショップの利用規約へのリンクが表示されます。チェックアウトに進むことで、利用規約に同意したと通知されます。

## ショップページとは何ですか?

ショップページは、ショップの商品が表示されるメインページです。また、商品をカートに追加した際、またはカートが空の場合、特定の状況下で表示される「**買い物を続ける**」リンクのリンク先でもあります。ショップページはテンプレートに基づいて作成されており、割り当てられたページを変換するか、ページが割り当てられていない場合はデフォルトのコンテンツを表示します。そのため、サイト上の他のページとはレンダリング結果が異なる場合があります。

`/shop/` URL は削除できません。ショップページとして割り当てられたページに `shop` 以外の [スラッグ](https://wordpress.com/support/permalinks-and-slugs/) が設定されている場合、その URL で読み込まれます。例: `example.com/my-fancy-store/`。その場合、`example.com/shop/` は 404 エラー（ページが見つかりません）を返します。ただし、ショップページが設定されていない場合は、`example.com/shop/` は引き続き機能し、デフォルトのコンテンツ（通常は商品リスト）を読み込みます。この動作が望ましくない場合は、リダイレクトプラグインまたはコードスニペットを使用できます。

WooCommerce にショップ ページとして使用するページを指示するには:

1. **WooCommerce > 設定 > 商品** に移動します。
2. 「ショップページ」ドロップダウンから、ショップページとして使用したいページを選択します。
3. 画面下部の「変更を保存」ボタンを押します。

サイトで [ブロック テーマ](https://woocommerce.com/document/woocommerce-store-editing/blocks/#block-themes) を使用している場合は、[製品カタログ テンプレート](https://woocommerce.com/document/woocommerce-store-editing/customizing-shop-page-catalog/#built-in-templates) をサイト エディターでカスタマイズできます。

なお、[WooCommerce ブロック](https://woocommerce.com/document/woocommerce-store-editing/customizing-shop-page-catalog/product-collection-block/)や[商品ショートコード](https://woocommerce.com/document/woocommerce-shortcodes/products/)を使用することで、ショップページ以外のページにも商品を表示することができます。

SEO プラグインを使用している場合は、カスタム投稿タイプ アーカイブに固有の設定が含まれている可能性があり、これらの設定を使用してショップ ページを制御する必要があります。

このページは、WooCommerce バージョン 3.3x 以降のすべての WordPress テーマ（WooCommerce 専用でないものも含む）と互換性があります。カスタムテーマ、子テーマ、または 3.3x より前のバージョンの WooCommerce をご利用の場合、あるいは互換性の問題が発生している場合は、[サードパーティ製/カスタムテーマの互換性](https://woocommerce.com/document/third-party-custom-theme-compatibility/) をご覧ください。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

