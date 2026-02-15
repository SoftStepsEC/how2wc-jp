---
title: 詳細設定
url: https://woocommerce.com/document/configuring-woocommerce-settings/advanced/
---

「詳細」設定エリアでは、カートやチェックアウトなどのWooCommerceページの設定、REST APIを使用して外部アプリケーションを連携するためのアクセストークンの作成、ストアへのカスタムWebhookの追加、高パフォーマンス注文ストレージや新しい商品エディターなどの新機能や実験的な機能の有効化などを行うことができます。これらの設定は、**WooCommerce > 設定 > 詳細** から行えます。

詳細設定のさまざまなセクションには、サブメニューからアクセスできます。

- [ページ設定](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#page-setup)
- [REST API](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#rest-api)
- [Webhooks](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#webhooks)
- [レガシーAPI](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#legacy-api)
- [WooCommerce.com](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#woocommerce-com)
- [機能](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#features)

WooCommerce が特定のアクションを実行するためにユーザーをどこに送信すればよいかがわかるように、ページを設定する必要があります。

- **カートページ** – このページには、お客様のカートに入っている商品が表示されます。
- **チェックアウトページ** – このページでは、お客様がお支払い情報を入力し、注文を送信します。
- **マイアカウントページ** – このページでは、登録済みのお客様が注文内容を確認したり、アカウント情報を更新したりできます。
- **利用規約** – このページには、利用規約が表示されます。

HTTPS経由で配信されていないサイトでは、ページ設定エリアに**Force Secure Checkout**設定も表示されます。この設定の詳細については、[SSLとHTTPSに関するドキュメント](https://woocommerce.com/document/ssl-and-https/#woocommerce-force-ssl-setting)をご覧ください。

WooCommerce のインストール時に作成されたページをそのまま使用する必要はありませんが、カートページとチェックアウトページのページは必ず設定しておく必要があります。設定されていない場合、顧客は商品を購入して支払いを行うことができません。これらのページは通常、WooCommerce のインストール/設定時に作成され、設定されます。詳しくは、[WooCommerce ページ](https://woocommerce.com/document/woocommerce-pages/) をご覧ください。

＃＃＃＃ 利用規約

**利用規約** ページを使用するには、**[ページ] > [新規追加]** で新しいページを作成し、ドロップダウンでページを選択します。

`[woocommerce_checkout]` [ショートコード](https://woocommerce.com/document/woocommerce-shortcodes/page-shortcodes/#checkout) を使用すると、チェックアウト時に利用規約がインラインで表示されます。顧客が「利用規約」リンクをクリックすると、利用規約が展開されて表示されます。その後、顧客は内容をスクロールし、同意するチェックボックスにチェックを入れることができます。

[ブロック版チェックアウト](https://woocommerce.com/checkout-blocks/)では、購入者に「ご購入手続きに進むことで、**利用規約**および**プライバシーポリシー**に同意したものとみなされます」というメッセージと、設定されている場合それぞれのページへのリンクが表示されます。このメッセージは、ブロックエディターでニーズに合わせて編集できます。

#### チェックアウトエンドポイント

エンドポイントは、WooCommerce が検出したときにさまざまなコンテンツを表示するために使用する、Web サイト URL 内の追加部分です。

チェックアウトエンドポイントは、チェックアウトおよび注文の支払いプロセスにおける特定のアクションを処理するために、ページURLに追加されます。これらは一意である必要があり、特別な理由がない限り、通常は変更する必要はありません。チェックアウトエンドポイントは次のとおりです。

- お支払い
- 注文受付
- お支払い方法の追加
- お支払い方法の削除
- デフォルトのお支払い方法の設定

開発者向けドキュメントで [WooCommerce エンドポイント](https://developer.woocommerce.com/docs/woocommerce-endpoints/) の詳細をご覧ください。

#### マイアカウントエンドポイント

これらのエンドポイントは、アカウントページにおける特定のアクションを処理します。これらは一意である必要があり、特別な理由がない限り、通常は変更する必要はありません。「マイアカウント」エンドポイントは次のとおりです。

- 注文
- 注文の表示
- ダウンロード
- アカウントの編集
- 住所
- お支払い方法
- パスワードを忘れた場合
- ログアウト

開発者向けドキュメントで [WooCommerce エンドポイント](https://developer.woocommerce.com/docs/woocommerce-endpoints/) の詳細をご覧ください。

これらの設定は、**WooCommerce > 設定 > 詳細 > REST API** にあります。

REST API設定では、WooCommerce REST API経由でストアに接続するためのAPIキーを作成できます。詳細は[APIキーの生成](https://woocommerce.com/document/woocommerce-rest-api/#generate-api-keys)をご覧ください。

REST APIは一般的に開発者向けです。ただし、サービスによっては、ストアに接続するためにAPIキーの作成を求められる場合があります。REST APIはWordPress外部からストアデータへのアクセスを可能にするため、キーの作成と使用には注意が必要です。詳しくは[WooCommerce REST API](https://woocommerce.com/document/woocommerce-rest-api/)をご覧ください。

Webhookは、任意のURLに送信されるイベント通知です。Webhookをサポートするサードパーティサービスとの連携に使用できます。詳しくは、開発者向けドキュメント「WooCommerceでのWebhookの使用」をご覧ください。(https://developer.woocommerce.com/docs/working-with-webhooks-in-woocommerce/)

メンテナンスが終了し、2024 年 6 月 11 日にリリースが予定されている [WooCommerce 9.0](https://developer.woocommerce.com/2023/10/03/the-legacy-rest-api-will-move-to-a-dedicated-extension-in-woocommerce-9-0/) で削除される予定の Legacy REST API を有効にします。Legacy REST API を使用する必要がある場合は、詳細については [開発者ブログのこの投稿](https://developer.woocommerce.com/2024/05/14/goodbye-legacy-rest-api/) を参照してください。

WooCommerce.com セクションでは、WooCommerce の [使用状況トラッキング](https://woocommerce.com/usage-tracking/) を有効にすることができます。これにより、WooCommerce をさらに改善することができます。また、ストアに役立つ可能性のある公式拡張機能を状況に応じて提案する設定もあります。

これらの設定は、**WooCommerce > 設定 > 詳細設定 > 機能** にあります。ここで、安定版および試験運用版の WooCommerce 機能を有効にできます。

- **注文データストレージ** – 使用する注文データストレージ方法を選択します。詳細については、[高性能注文ストレージ](https://woocommerce.com/document/high-performance-order-storage/)のドキュメントをご覧ください。
- **アナリティクス** – [WooCommerce Analytics](https://woocommerce.com/document/woocommerce-analytics/)を有効または無効にします。
- **注文アトリビューション** – [注文アトリビューショントラッキング](https://woocommerce.com/document/order-attribution-tracking/)を有効または無効にします。

#### 実験的な機能

ここの機能は実験的または不完全なため、自己責任で有効にしてください。

- **新商品エディタ** (ベータ版) – [新商品エディタ (ベータ版)](https://woocommerce.com/document/new-product-editor-beta/) を有効または無効にします。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

