---
title: ショップ通貨
url: https://woocommerce.com/document/shop-currency/
---

WooCommerceでは、ストア開設時に複数の通貨オプションから選択できます。このドキュメントでは、以下の手順について説明します。

- ショップの基本通貨の設定方法
- 基本通貨以外の通貨で商品を表示するための提案
- 為替レートと手数料に関する基本情報

各WooCommerceストアは**1つの基本通貨**を設定できます。この通貨はストア全体に表示されるだけでなく、お支払いにも使用されます。

ストアの通貨を設定するには:

1. WordPress管理画面から、**WooCommerce > 設定 > 一般** に移動し、画面の一番下までスクロールします。
2. 通貨オプションで、必要に応じて通貨設定を行います。
- **通貨**: ストアの商品に表示される通貨を選択します。
- **通貨位置**: 通貨記号を価格の左側に配置するか右側に配置するかを選択します。
- **千の位の区切り**: 千の位の区切りに使用する文字を選択します。
- **小数点の区切り**: 小数点の区切り文字を選択します。
- **小数点以下の桁数**: 小数点以下の桁数を選択します。
  
3. **変更を保存** を選択します。

使用したい通貨がドロップダウン メニューにリストされていない場合は、このチュートリアルに従って [カスタム通貨を追加](https://woocommerce.com/document/add-a-custom-currency-symbol/) し、ストアに追加してください。

**サポート範囲:**

**サポートポリシー**に基づき、カスタマイズに関するサポートは提供できません。スニペットのカスタマイズや機能拡張が必要な​​場合は、[Woo エージェンシー パートナー](https://woocommerce.com/development-services/) または [Codeable](https://www.codeable.io/partners/woocommerce/?ref=qGefA6#tiers) の WooCommerce 開発者にご相談いただくことをお勧めします。

WooCommerce では、**ストアごとに1つの基本通貨** のみを設定できます。商品を複数の通貨で表示したい場合（または、ショップの基本通貨とは異なる通貨で顧客に支払いを許可したい場合）は、複数通貨対応の拡張機能/プラグインを追加する必要があります。

目標を達成するために適切な拡張機能を選択できるよう、複数通貨設定を選択する理由を評価することをお勧めします。

追加通貨のオプションは次のとおりです。

- [WooPayments](https://woocommerce.com/products/woopayments/) を使用すると、[マルチ通貨機能](https://woocommerce.com/document/woopayments/currencies/multi-currency-setup/) を無料で利用でき、顧客は希望する通貨で商品を閲覧・決済できます。
- [通貨換算ウィジェット](https://woocommerce.com/products/currency-converter-widget/) は価格表示のみを変更します。請求通貨は変更されず、ストアの基本通貨が引き続き使用されます。通貨換算ウィジェットを使用すると、ストアを単一通貨で運営できるため、ストア管理、会計、および一般的なメンテナンスが簡素化されます。また、顧客は商品カタログを母国通貨で閲覧できるようになります。
- [TIV Multi-Currency for WooCommerce](https://woocommerce.com/products/multi-currency/) を使用すると、顧客は希望する通貨で決済できます。
- [MultilingualPress](http://multilingualpress.org/) を使用すると、コンテンツ、商品、価格を複数の言語と通貨で表示できます。
- [Currency Switcher for WooCommerce](https://woocommerce.com/products/currency-switcher-for-woocommerce/) を使用すると、顧客が通貨を切り替えられるウィジェットをサイトに追加できます。

**注記：**

Woo が開発または管理していないサードパーティ製の拡張機能/プラグインについては、サポートを提供できません。ご質問やサポートのご要望は、拡張機能/プラグインの開発者にお問い合わせください。

ストアの基本通貨以外の通貨で顧客に販売する前に、為替レート（または発生する可能性のある追加料金）について必ずデューデリジェンスを行ってください。

顧客のデビットカードまたはクレジットカードの標準通貨以外の通貨で支払う場合、カード発行会社が追加料金を課すこともあります。

**WooCommerce は為替レートや手数料を請求しません**。これらの手数料は、通貨交換を行う主体が負担します。これは、実装方法に応じて、決済代行業者または顧客の銀行のいずれかになります。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

