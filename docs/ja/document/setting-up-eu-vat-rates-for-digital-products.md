---
title: デジタル製品に対するEUのVAT税率の設定
url: https://woocommerce.com/document/setting-up-eu-vat-rates-for-digital-products/
---

**2026年から始まるVATの更新:** ヨーロッパのいくつかの国は新年に税制を更新しており、そのほとんどが1月1日に発効します。

- リトアニア、オランダ、スロバキア、フィンランド、ドイツ、オーストリアにおけるVAT関連の変更。
- スペインは、2027年までに企業に対し、請求書追跡に関するVERI*FACTU標準への準拠を義務付けています。移行をスムーズに行うために、以下の便利な拡張機能のご利用をお勧めします。
- [Verifactu](https://quaderno.io/es/integraciones/verifactu/) by Quaderno
- [FacturaDirecta Integration for WooCommerce](https://woocommerce.com/products/facturadirecta-integration/) by Kamalyon
  

これらの変更点と Woo ストアの準備方法については、ブログ記事をご覧ください: [2026 年の EU 税制変更に向けてビジネスを準備する](https://woocommerce.com/posts/2026-eu-tax-changes/)

EUのデジタル商品に関するVAT法は2015年1月1日に改正され、B2C取引にのみ適用されます。デジタル商品にかかるVATは顧客の所在地に基づいて計算する必要があり、IPアドレスや請求先住所などからその証拠を収集する必要があります。さらに、WooCommerceストアでVAT率を設定し、正しい金額を請求する必要があります。

このガイドは現状のまま提供され、このシナリオにおけるデジタル商品固有の税率の設定方法を示しています。一般的な税率の設定については、以下をご覧ください。

- [WooCommerce での税金の設定](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#shipping-tax-class)
- [WooCommerce での税金の仕組み](https://woocommerce.com/document/how-taxes-work-in-woocommerce/)
- [WooCommerce で特定の税金を設定する方法](https://woocommerce.com/document/configuring-specific-tax-setups-in-woocommerce/)

デジタル製品に対する EU VAT 率の設定に関する詳細と情報については、[欧州委員会税務・関税同盟ウェブサイト](https://ec.europa.eu/taxation_customs/business/vat/telecommunications-broadcasting-electronic-services/content/guide-vat-mini-one-stop-shop-moss_en) の VAT MOSS (ミニワンストップショップ) をご覧ください。

このドキュメントでは、WooCommerce で税率を設定する方法と、プラットフォームがこれらの設定に基づいて税金/VAT/GST を処理する方法について説明します (いつ、何を請求するかについては**説明しません**)。

**当社は税務専門家ではありません**。当社のアドバイスはソフトウェアの使用方法に関するもののみを対象としています。税金／VAT／GSTなどの請求内容や請求時期に関するアドバイスについては、税務専門家または会計士にご相談ください。

すべてのビジネスは独自のものであり、ここですべての可能性を網羅することはできません。

デジタル商品のみを販売する場合は、WooCommerce の **標準税率** に VAT 税率を追加できます。

デジタル製品と通常の製品の両方を販売/配布している場合は、新しい**追加税区分**（例:**デジタル商品**）を作成して使用できます。

新しい税金クラスで EU VAT 税率を設定するには:

1. **WooCommerce > 設定 > 税金** に移動します。
2. **追加の税区分** 設定を選択します。
3. リストに新しい税区分を追加します（例：**デジタル商品**）。
4. 下にスクロールして **変更を保存** をクリックします。

税金オプションの変更を保存した後、この税金クラスに税率を割り当てる必要があります。

## EUのVAT率の設定

次のステップは、EU VAT 税率を WooCommerce に入力することです。

最新のVAT率は[Europaウェブサイト](https://europa.eu/youreurope/business/taxation/vat/vat-rules-rates/index_en.htm#inline-nav-6)でご確認いただけます。VAT率が変更された場合は、ストアのVAT率を更新する必要があります。

1. **WooCommerce > 設定 > 税金 > デジタル商品** に移動します。
2. すべての EU 加盟国の税率を**入力します**。[WooCommerce での税率設定](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#setting-up-tax-rates) のガイドをご覧ください。

最終更新時点での標準 VAT 税率は次のとおりです。

あるいは、正しい形式のCSVファイルをお持ちの場合は、VAT率をインポートして時間を節約できます。上記の税率を、税区分**デジタル商品**でCSV形式で以下に示します：[vat_rates.csv](https://woocommerce.com/wp-content/uploads/2021/01/vat_rates.csv)

このファイルをインポートするには:

1. この例では、税率（**デジタル商品の税率**セクション）に移動します。
2. 税率表の右下にある**CSVをインポート**ボタンを選択します。
3. インポーターが表示され、**参照…**ボタンをクリックするとファイルセクションが表示されます。
4. ダウンロードしたCSVファイルを選択し、**ファイルをアップロードしてインポート**ボタンをクリックします。

税率画面で税率がアップロード、インポート、または入力されると、表にそれぞれのデータが表示されます。**国コード**列には国コード、**税率%**列にはそれぞれの税率、**税金名**には**VAT**、**優先度**は**1**、**配送**はすべての税率でチェックされています。

EUのVAT税率が設定されている場合、デジタル商品税区分の商品を購入した顧客には、店舗の所在地ではなく、顧客の所在地に基づいて税金が請求されます。これは、**税金オプション > 税金の計算基準** が **顧客の配送先住所** または **顧客の請求先住所** に設定されている場合に限ります。

この税金クラスを WooCommerce のデジタル製品に適用するには:

1. **「商品」>「すべての商品」** に移動します。
2. 商品を編集します。
3. **「商品データ」>「一般セクション」>「税区分」** に移動し、ドロップダウンから該当する区分を選択します。
4. 商品を **更新** して変更を保存します。

商品を一括編集することもできます。

1. **「商品」>「すべての商品」** に移動します。
2. 一括編集する各商品の左側にあるボックスに**チェック**を入れます。
3. 一括操作のドロップダウンから**「編集」** を選択します。
4. ドロップダウンの右側にある**「適用」** ボタンをクリックします。

**適用** をクリックすると、一括編集ビューが表示されます。

1. **税区分** ドロップダウンから税区分を選択します。
2. **一括編集ビュー** の左下にある **更新** をクリックして、選択した商品に税区分を適用します。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

