---
title: WooCommerce設定の構成
url: https://woocommerce.com/document/configuring-woocommerce-settings/
---

サイトの WP 管理ダッシュボードで **WooCommerce > 設定** に移動すると、利用可能なさまざまな種類の設定に関連するタブが表示されます。

- [一般](https://woocommerce.com/document/configuring-woocommerce-settings/#general)
- [商品](https://woocommerce.com/document/configuring-woocommerce-settings/#products)
- [税金](https://woocommerce.com/document/configuring-woocommerce-settings/#tax)
- [配送](https://woocommerce.com/document/configuring-woocommerce-settings/#shipping)
- [お支払い](https://woocommerce.com/document/configuring-woocommerce-settings/#payments)
- [アカウントとプライバシー](https://woocommerce.com/document/configuring-woocommerce-settings/#accounts-and-privacy)
- [メール](https://woocommerce.com/document/configuring-woocommerce-settings/#emails)
- [統合](https://woocommerce.com/document/configuring-woocommerce-settings/#integration)
- [サイトの表示設定](https://woocommerce.com/document/configuring-woocommerce-settings/#site-visibility)
- [詳細設定](https://woocommerce.com/document/configuring-woocommerce-settings/#advanced)

**注記：**

WooCommerce は拡張性に優れたオープンソースソフトウェアです。拡張機能やプラグインは、WooCommerce の設定ページに追加の設定やタブを追加することがよくあります。以下の画像や以降のページで説明されている設定以外に追加の設定がある場合は、拡張機能/プラグイン、テーマ、またはカスタムコードによって追加された可能性があります。

ストアの一般設定は、WP Admin の **WooCommerce > 設定 > 一般** で確認できます。

これらの設定には、ストアの所在地、注文の販売場所と発送場所、デフォルトの顧客所在地として使用する場所、税金とクーポンの有効化または無効化、ストアの通貨オプションが含まれます。

詳細については、[一般設定](https://woocommerce.com/document/configuring-woocommerce-settings/general/)を参照してください。

WP Admin の **WooCommerce > 設定 > 製品** で製品設定を見つけて編集します。

これらの設定により、どのページをメインショップページとして設定するか、製品の寸法に使用する測定単位、製品レビューの設定、在庫管理、在庫通知、ダウンロード可能な製品の処理方法などが決まります。

詳細については、[製品設定](https://woocommerce.com/document/configuring-woocommerce-settings/products/)を参照してください。

**注記：**

**税金** 設定リンクを表示するには、**WP Admin > WooCommerce > 設定 > 一般** で税金を有効にする必要があります。

WP Admin の **WooCommerce > 設定 > 税金** で税金設定を見つけて編集します。

WooCommerce に組み込まれている税金設定では、ショップでの税金の表示方法と計算方法を選択できます。また、特定の地域に税率を追加したり、特定の商品や送料に異なる税率を適用する税区分を追加したりすることも可能です。

詳細については、[WooCommerce の税金設定](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/) を参照してください。

WP Admin の **WooCommerce > 設定 > 配送** で配送設定を見つけて編集します。

WooCommerce には、幅広いユースケースをカバーするいくつかの組み込み配送設定と配送方法があります。

メインの配送設定画面は**配送ゾーン**の設定です。配送ゾーンとは、特定の配送方法とその料金が適用される地理的な地域と考えてください。

詳細については、[配送ゾーンの設定](https://woocommerce.com/document/setting-up-shipping-zones/)をご覧ください。

**配送設定** ページには次の設定が含まれています。

- 計算
- カートページで送料計算機能を有効にする
- 住所が入力されるまで送料を非表示にする
- 送料無料が利用可能な場合、送料を非表示にする
  
- 配送先
- デフォルトで顧客の請求先住所または配送先住所に配送するか、ユーザーの請求先住所のみに配送するかを選択します。
  
- デバッグモード
- デバッグモードを有効にすると、サイトのフロントエンドに顧客の配送ゾーンが表示され（下図参照）、送料キャッシュがバイパスされます。トラブルシューティングのために有効にしてください。
  

配送クラスを使用すると、配送方法によって、異なるクラスまたは製品タイプごとに異なる料金を設定できるようになります。

[商品の配送クラス](https://woocommerce.com/document/product-shipping-classes/)について詳しくご覧ください。

ローカルピックアップを利用すると、顧客は配送を必要とせず、注文品を自分で受け取ることができます。現在、無料のWooCommerceプラグインコアでローカルピックアップを実装する方法は2つあります。

- ブロック版のチェックアウトフローにネイティブに統合された、モダンで合理化されたエクスペリエンスです。詳しくは[WooCommerce Blocks: Local Pickup](https://woocommerce.com/document/woocommerce-blocks-local-pickup/)をご覧ください。
- WooCommerceのコア配送方法として配送エリアに追加できるレガシーバージョンです。これは、チェックアウトのショートコード版とブロック版のどちらでも機能します。詳しくは[レガシー配送方法: Local Pickup](https://woocommerce.com/document/local-pickup/)をご覧ください。

混乱を避けるため、現地受け取りには 1 つの方法のみを使用することをお勧めします。

WP Admin で、**WooCommerce > 設定 > 支払い** に移動して、有効にする支払いゲートウェイを指定し、その設定を構成します。

**有効** トグルを使用してゲートウェイをオンまたはオフにします。

追加の設定が必要な支払い方法を有効にしようとすると、その支払い方法の設定画面にリダイレクトされます。

**決済ゲートウェイ名**をクリックすると、設定または調整画面が表示されます。設定を行う別の方法として、該当する決済ゲートウェイの**設定**または**管理**ボタンをクリックすることもできます。

インストールされたゲートウェイはテーブルにリストされており、**ドラッグ アンド ドロップ** してチェックアウト時に顧客に表示される順序を制御できます。

支払いゲートウェイの詳細については、次のページを参照してください。

- [プレミアム決済ゲートウェイオプション](https://woocommerce.com/document/premium-payment-gateway-extensions/)
- [WooCommerceに含まれる無料決済ゲートウェイ](https://woocommerce.com/documentation/plugins/woocommerce/getting-started/sell-products/core-payment-options/https://woocommerce.com/documentation/woocommerce/getting-started/sell-products/core-payment-options/)

アカウントとプライバシーの設定は、WP Admin の **WooCommerce > 設定 > アカウントとプライバシー** で確認できます。

ここでは、ゲストチェックアウトを有効または無効にしたり、顧客アカウントの作成を制御したり、個人データをショップから保持または削除する方法を制御したり、プライバシー ポリシーの通知を設定したりできます。

詳細については、[アカウントとプライバシー設定](https://woocommerce.com/document/configuring-woocommerce-settings/accounts-and-privacy/)を参照してください。

WP Admin の **WooCommerce > 設定 > メール** でメール設定を見つけます。

ストアのメールテンプレートのデザイン要素を編集したり、ストアの送信アドレスを変更したり、WooCommerce が送信する各メールの設定を構成（または無効化）したりできます。

詳細については、[メール設定](https://woocommerce.com/document/configuring-woocommerce-settings/emails/)を参照してください。

統合設定は、WP Admin の **WooCommerce > 設定 > 統合** で見つかります。

ここで[MaxMind ジオロケーション統合](https://woocommerce.com/document/maxmind-geolocation-integration/)のライセンスキーを入力します。拡張機能、プラグイン、テーマ、その他の統合によって、このタブに設定が追加される場合もあります。

サイトの表示設定から、**近日公開** **モード** を有効にして、構築中のストアをプライベート リンク経由で共有できるようになります。

[近日公開モード](https://woocommerce.com/document/configuring-woocommerce-settings/coming-soon-mode/) の詳細をご覧ください。

詳細設定は、WP Admin の **WooCommerce > 設定 > 詳細** で確認できます。

詳細設定では、WooCommerce ページの設定、REST API を使用した外部アプリケーションの統合、ストアへのカスタム Webhook の追加、高パフォーマンス注文ストレージ (HPOS) や新しい製品エディターなどの新機能や実験的な機能の有効化を行うことができます。

詳細については、[詳細設定](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/)を参照してください。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

