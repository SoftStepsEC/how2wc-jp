---
title: チェックアウトブロック
url: https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/
---

チェックアウトブロックは、簡素化されコンバージョンを最適化したチェックアウトフローの一部です。顧客はここでショッピング情報と支払い情報を入力して購入を完了します。

このページでは、チェックアウト ブロックの構造、設定、カスタマイズ オプションの概要を説明し、ストアのブランド アイデンティティを管理し、顧客にとって視覚的に魅力的なチェックアウト ジャーニーを作成します。

- [チェックアウトブロックの構造](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#checkout-block-structure)
- [チェックアウトブロックの設定](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#checkout-block-settings)
- [チェックアウトフィールド](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#checkout-fields-block)
- [チェックアウト合計](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#checkout-totals-block)
- [店舗受取配送]オプション](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#blocks-local-pickup)

**注:**チェックアウト ブロックはどのページにも追加できますが、すべてが適切に機能するには、まず **WooCommerce > 設定 > 詳細設定** からストアの [詳細設定](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/) で **選択したチェックアウト ページを指定** する必要があります。

チェックアウトブロックには、[チェックアウトフィールド](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#checkout-fields-block)と[チェックアウト合計](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#checkout-totals)という2つの主要な内部ブロックが含まれています。これらはチェックアウトエクスペリエンスの重要な要素です。[リストビュー](https://woocommerce.com/document/woocommerce-store-editing/the-editor/#list-view)を使用して、これらのブロックがどのように組み合わされているかを確認してください。

チェックアウトブロックを構成する内部ブロックの多くは完全に動的であり、WooCommerceの他の設定に基づいて動作します。例えば、支払いオプションブロックには、以下の条件を満たすすべての支払い方法が表示されます。

- ストアで利用可能であること、および
- [決済ゲートウェイの設定](https://woocommerce.com/document/configuring-woocommerce-settings/#payments)に従って、[チェックアウトブロック](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/#compatible-extensions)と互換性があること。

これらの内部ブロックは、ブロックエディターで設定する必要がないため、このドキュメントには記載されていません。[リストビュー](https://woocommerce.com/document/woocommerce-store-editing/the-editor/#list-view)を使用してこれらのブロックをクリックすると、[設定サイドバー](https://woocommerce.com/document/woocommerce-store-editing/blocks/#block-settings)で各内部ブロックの説明を確認できます。

可能な場合は、設定サイドバーでこれらのブロックをクリックすると、WooCommerce の関連設定に移動し、設定できるようになります。

チェックアウトブロックには、ブロック設定サイドバーから設定できる設定が1つだけあります。**ダークモード入力**です。この設定を切り替えることで、チェックアウトフォームのフィールドやその他の入力欄のスタイルを、暗い背景のページやセクションに合わせて適切に設定できます。

**チェックアウトフィールド** ブロックには、顧客が購入を完了するために情報を入力するフィールドが含まれています。各フィールドに対応する内部ブロックが含まれており、これらの内部ブロックのほとんどは動的です。その動作は以下に基づいています。

- 現在の顧客の注文、および
- [WooCommerce 設定](https://woocommerce.com/document/configuring-woocommerce-settings/) の設定方法。

チェックアウトフィールドブロックは、メインのチェックアウトブロック内にネストされた**最初のブロック**です。このブロックには、配送先住所ブロックと請求先住所ブロックと共有される以下の設定が含まれています。1つのブロックでこれらの設定を変更すると、他のブロックの設定も変更されます。

- **フォームステップオプション**：この設定を切り替えることで、セクション見出しに番号を追加し、ガイド付きのチェックアウトフローを作成できます。
- **住所フィールド**：この設定を使用して、「会社名」、「住所2行目」、「電話番号」フィールドの表示/非表示を切り替えます。また、チェックアウトを完了するために「住所」と「電話番号」フィールドを必須にするかどうかも設定できます。

チェックアウトフィールドブロック内には追加のブロックがネストされており、これらはすべて[リストビュー](https://woocommerce.com/document/woocommerce-store-editing/the-editor/#list-view)から位置や名前を変更できます。一部のブロックには追加の設定が含まれており、以下に概要を示します。

エクスプレスチェックアウトブロックは、エクスプレスチェックアウトをサポートする決済ゲートウェイ（[WooPay](https://woocommerce.com/woopay/)、ApplePay、Google Payなど）がアクティブな場合にのみコンテンツを表示します。このブロックには追加設定はありません。エクスプレスチェックアウトを有効にするには、[WooPayments](https://woocommerce.com/payments/)（お住まいの地域で利用可能な場合）のご利用をお勧めします。

配送ブロックでは、お客様が注文商品を配送するか、現地で受け取るかを選択できます。設定サイドバーには、外観をカスタマイズするためのオプションが含まれています。

このブロックと**ピックアップ方法**ブロックは次の場合にのみ表示されます。

- **WooCommerce > 設定 > 配送 > ローカルピックアップ** で [ローカルピックアップのブロックバージョン](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#blocks-local-pickup) が有効になっています。
- 編集中のチェックアウトページは、**WooCommerce > 設定 > 詳細設定** でチェックアウトページに指定されています。

＃＃＃＃ 外観

- **アイコンを表示**: 配送オプションの横にアイコンを表示し、視覚的に区別できるようにします。
- **料金を表示**: 各オプションの横に配送料金を表示し、顧客に明確な価格情報を提供します。

このブロックの設定は、[チェックアウトフィールドブロック](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#checkout-fields-block)の設定と同じです。これらの設定は**リンク**されているため、一方の設定を変更すると、もう一方の設定も変更されます。

利用規約ブロックは、購入が完了する前に顧客がストアのポリシーを確認するのに役立ちます。

- **チェックボックスを必須**: この設定を切り替えると、顧客は注文を進める前に利用規約に同意することを確認するボックスにチェックを入れることが必須になります。

利用規約**とプライバシーポリシーのページを指定することで、ブロックのコンテンツ内のストアのポリシーに自動的にリンクします。

[ページ設定の詳細](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#page-setup)と[プライバシーポリシーのオプション](https://woocommerce.com/document/configuring-woocommerce-settings/accounts-and-privacy/#privacy-policy)をご覧ください。

アクション ブロックは、チェックアウト時に顧客に追加のナビゲーション オプションを提供します。

- **ナビゲーション オプション**: **カートに戻るリンクを表示** 設定を切り替えて、顧客がカートに戻って変更できるようにするリンクの表示/非表示を切り替えます。
- **カートに戻るボタン**: カートに戻るリンクを有効にすると、ドロップダウン メニューが表示され、リンクをクリックすると買い物客が戻るページを選択できます。

チェックアウト合計ブロックには、注文概要、クーポン入力フォーム、注文合計を構成する費用のリストを表示する内部ブロックが含まれています。これらの内部ブロックは、1つを除いてすべて[ロック](https://woocommerce.com/document/woocommerce-store-editing/blocks/#locked-blocks)されています。これらの内部ブロックはデフォルトの位置から上下に移動できますが、削除することはできません。

**クーポン フォーム** は、チェックアウト合計セクション内でロックが解除されており、**削除できる** 唯一のブロックです。

サイトの[指定されたチェックアウトページ](https://woocommerce.com/document/woocommerce-pages/#tell-woocommerce-what-pages-to-use)にチェックアウト ブロックを配置すると、ローカルピックアップ設定が利用できるようになります。

[WooCommerce ブロックのローカルピックアップ](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/woocommerce-blocks-local-pickup/)を使用すると、顧客に1つ以上のピックアップ場所を提供できます。このオプションを有効にすると（**WooCommerce > 設定 > 配送 > ローカルピックアップ**でピックアップ場所を設定すると）、サイトのチェックアウトブロックに[配送方法とピックアップ方法のブロック](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/#delivery-block)が表示され、買い物客が注文のピックアップ場所をより効率的に選択できるようになります。

これは、配送ゾーンを設定するときに以前に設定可能だった[従来のローカルピックアップ オプション](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/woocommerce-blocks-local-pickup/#difference-from-legacy-local-pickup)とは異なります。

[WooCommerce ブロックのローカルピックアップのオプションを確認する](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/woocommerce-blocks-local-pickup/)。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

