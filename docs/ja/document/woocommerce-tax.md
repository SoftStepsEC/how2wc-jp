---
title: WooCommerce 税務ガイド
url: https://woocommerce.com/document/woocommerce-tax/
---

**注記：**

新しいWooCommerce Shipping拡張機能とWooCommerce Shipping & Taxes拡張機能の両方が**有効化**されている場合、配送ラベル機能はWooCommerce Shippingが引き継ぎます。税金機能は引き続きWooCommerce Shipping & Taxes拡張機能によって提供されます。配送ラベルの作成方法については、必要に応じて新しい[WooCommerce Shipping](https://woocommerce.com/document/woocommerce-shipping/)ドキュメントをご参照ください。

このドキュメントでは、WooCommerce で税率を設定する方法と、プラットフォームがこれらの設定に基づいて税金/VAT/GST を処理する方法について説明します (いつ、何を請求するかについては**説明しません**)。

**当社は税務専門家ではありません**。当社のアドバイスはソフトウェアの使用方法に関するもののみを対象としています。税金／VAT／GSTなどの請求内容や請求時期に関するアドバイスについては、税務専門家または会計士にご相談ください。

すべてのビジネスは独自のものであり、ここですべての可能性を網羅することはできません。

WooCommerce Shipping & Tax拡張機能のインストール方法については、[WooCommerce Shipping & Taxページ](https://woocommerce.com/products/shipping/)をご覧ください。このドキュメントでは、拡張機能の税金機能について説明しています。WooCommerceにおける税金の一般的な設定の詳細については、[WooCommerceでの税金設定に関するドキュメント](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/)をご覧ください。

自動税金計算を有効にするには、まず**WooCommerce > 設定 > 一般**で**「税金と税金計算を有効にする」**がチェックされていることを確認してください。

税金を有効にすると:

1. **WooCommerce > 設定 > 税金** に移動します。
2. **「自動税金を有効にする」** を選択します。
3. **「変更を保存」** をクリックします。

自動税金設定を有効にすると、WooCommerce のコア税金設定が自動税金設定に「引き継がれる」ため、多くの設定が無効になります。つまり、以下のようになります。

- **「表示価格」**は**税抜**に設定されます
- 税金は**顧客の配送先住所に基づいて計算されます**

**重要な注意:** 自動税計算は、入力される税抜き価格によって決まります。

自動課税が有効になっている場合、以下が上書きされます:

- 税務ネクサスがある地域に手動で追加した税率
- これらの税率の「複合」と「送料」の切り替え

**バックアップの作成:** 自動税率に切り替えると、以前の税率のバックアップが作成され、サイトの `wp-content/uploads` フォルダに保存されます。

**「自動税金」** 機能は、次の国に拠点を置くストアをサポートしています。

- **アメリカ合衆国**
- **カナダ**
- **オーストラリア**
- **イギリス**

さらに、世界のその他の国々のリストも増え続けています:

- オーストリア
- ベルギー
- ブルガリア
- クロアチア
- キプロス
- チェコ共和国
- デンマーク
- エストニア
- フィンランド
- フランス
- ドイツ
- ギリシャ
- ハンガリー
- アイルランド
- イタリア
- ラトビア
- リトアニア
- ルクセンブルク
- マルタ
- オランダ
- ポーランド
- ポルトガル
- ルーマニア
- スロバキア
- スロベニア
- スペイン
- スウェーデン

**EU 推奨事項:** ストアが EU に拠点を置いている場合は、自動税金に加えて [EU VAT 番号拡張機能](https://woocommerce.com/products/eu-vat-number/) を使用することをお勧めします。

WooCommerce Tax 設定に関する問題を診断するには:

1. **WooCommerce > ステータス > WooCommerce Tax** に移動します。
2. 問題が発生している場合は、デバッグまたはログ記録を有効にしてください。

システム ステータス ページには、WooCommerce Tax の機能停止を引き起こす可能性のある問題が表示され、役立つデバッグ情報と、さらにサポートを受けるためのリンクが含まれています。

**最近の税金リクエスト:** **WooCommerce > ステータス > WooCommerce 税金** の **税金ログ** セクションで確認できます。

**古いリクエスト:** **WooCommerce > ステータス > ログ** に移動して表示できます。

注文の税額が $0.00 であっても、自動税金計算は正常に機能している可能性があります。米国に拠点を置いている場合、これをテストする良い方法は、**ストア住所**（**WooCommerce > 設定 > 一般** ページで確認できます）と同じ州の住所を使用して、サイトのチェックアウトページで税金を計算してみることです。これがデフォルトの「税のネクサス」であり、同じ州からの注文には税金が適用されるはずです。

ストアの拠点が米国にある場合、**「タックス・ネクサス」**（通常は実店舗）がある地域のお客様からのみ売上税を徴収する必要があります。WooCommerce Tax はデフォルトで、**WooCommerce > 設定 > 一般** ページにある**ストア住所**を「タックス・ネクサス」として使用します。

**追加の税務ネクサス：** 一部の米国州では、その州に物理的な拠点がない場合でも、年間の取引金額または注文総額が一定額を超えると税金が徴収されることがあります。税務ネクサスのステータスが不明な場合は、地元の公認会計士にご相談ください。

**税率の追加:** 他の州の税金を請求する必要がある場合は、自動税計算を使用してその州の税金も顧客に請求するだけでなく、その州の[税率](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#setting-up-tax-rates)を追加することもできます。州税ネクサスと仕向地税のルールの詳細については、[州別エコノミックネクサス法ガイド](https://blog.taxjar.com/economic-nexus-laws/)をご覧ください。

**デフォルトのNexusアドレスの上書き:** WooCommerce Taxバージョン`3.3.0+`をご利用の場合、`woocommerce_taxjar_nexus_address`フィルターを使用することで、APIリクエスト内のNexusアドレスを変更または無効化できます。このフィルターは、標準の`from_*`アドレスフィールドを置き換えます。このフィルターの使用方法の例をいくつか以下に示しますが、WooCommerce Taxバージョン`3.3.0`以降を使用していることを確認することが重要です。また、このような変更を行う前に必ずサイトをバックアップし、ステージング環境でカスタマイズを十分にテストしてから、本番サイトに展開してください。

- 例：Nexusアドレスの変更：woocommerce_taxjar_nexus_addressフィルターを使用してNexusアドレスを変更する場合、$nexus_address配列には以下のキーを含める必要があります。
- `country`: 2文字の国コード（必須）。
- `state`: 2文字の州/省コード（米国/カナダの場合は必須）。
- `zip`: 郵便番号（必須）。
- `city`: 市区町村名（必須）。
- `street`: 番地（任意）。
  

```
// Modify the nexus address.
add_filter( 'woocommerce_taxjar_nexus_address', function( $nexus_address, $body ) {
	$nexus_address['street'] = '123 Custom Street';
	return $nexus_address;
}, 10, 2 );
```

- **例: ネクサス アドレスを完全に無効にする:** ネクサス アドレスの送信を完全に無効にするには、false または空の配列を返します。これにより、リクエストでは代わりに標準の `from_*` アドレス フィールドが使用されるようになります。

```
// Disable nexus addresses entirely.
add_filter( 'woocommerce_taxjar_nexus_address', '__return_false' );
```

#### フロリダ州の配送税要件

[フロリダ州歳入局](https://floridarevenue.com/faq/Pages/FAQDetails.aspx?FAQID=1277&IsDlg=1)によると、顧客が商品を自分で受け取るか、第三者に商品を受け取って配送してもらうことで販売者に送料を支払わないようにする選択肢がない場合は、送料に売上税を課さなければなりません。

**デフォルトの動作:** ストア住所 (**WooCommerce > 設定 > 一般**) がフロリダに設定されている販売者の場合、バージョン 1.26.0 以降、フロリダの配送税がデフォルトで有効になっています。

**フロリダの配送税を無効にするには:** 無効にしたい場合は、フィルターを使用して無効にすることができます。

`add_filter('woocommerce_taxjar_enable_florida_shipping_tax', '__return_false');`

WooCommerce Tax バージョン 3.2.1 では、税率の保存方法と、**アナリティクス → 税金** レポートでの税率の表示方法が変更されました。税率は、地域ごとに 1 行にまとめられた形式ではなく、管轄レベルごとに分類された項目として保存されるようになりました。このセクションでは、この変更、税務レポートへの影響、既存の注文への影響について説明します。

#### 税率ラベルの変更点

WooCommerce Tax の以前のバージョンでは、すべての管轄区域の詳細を 1 つのラベルにまとめた 1 行で税率を表示していました。

- `米国-オクラホマ郡-ミッドウェスト市税-1`

バージョン 3.2.1 以降、WooCommerce Tax は税率を管轄レベルごとに個別の行に分割します。

- `US-OK-市税-1`
- `US-OK-郡税-2`
- `US-OK-特別税-3`
- `US-OK-州売上税-4`

**分析 → 税金** レポートでは、以前は 1 行しか表示されなかった取引ごとに、複数の明細項目が表示されるようになりました。

#### WooCommerce Taxが明細レートを保存するようになった理由

この変更により、以前のバージョンに存在していた 2 つの問題が解決されます。

- **送料税計算のバグ** — 明細表示により、WooCommerce Tax は送料に適用される管轄区域をきめ細かく制御できるようになり、送料税が誤って計算されるケースを修正しました。
- **表示設定変更時の税率データ消失** — **「税額合計を表示」** 設定を「明細表示」と「一括合計」の間で切り替えると、以前は保存されているすべての税率が消去されていました。税率を明細表示形式で保存することで、この問題は解消されます。

この変更は永続的であり、元に戻すことはできません。

#### 既存の注文は影響を受けません

WooCommerce Tax は既存の注文の税データを更新しません。更新前に行われた注文は、元の税率形式とラベルが維持されます。バージョン 3.2.1 以降に更新した後に行われた注文のみ、新しい明細形式が使用されます。

移行期間中、**アナリティクス → 税金** レポートには、旧形式のラベルと新形式のラベルが混在して表示される場合があります。これは想定内の動作です。

#### WooCommerce をバージョン 10.4.0 以降に更新します

WooCommerce コアバージョン 10.4.0 より前のバージョンでは、同じ地域に複数の税率優先順位がある場合、**アナリティクス → 税金** で合計金額が誤って計算されます。項目別税率は複数の優先順位を使用するため、WooCommerce Tax 3.2.1 以降を実行しているストアでは、正確な税申告を行うために **WooCommerce 10.4.0 以降** も実行する必要があります。

WooCommerce Taxでは、**WooCommerce > 設定 > 税金** にある**「税込価格」**設定はストア全体の設定で、すべての商品に適用されます。一部の商品は税込みで、他の商品は税込みで表示するといった、異なる設定を組み合わせることはできません。

#### 店舗全体で1つのアプローチを選択する

**オプション 1: すべての商品価格を税込みで入力する** 税込みで定義するとは、ストアの拠点国の税金を指します。

地域や税金に関係なく同じ価格を請求したい場合は、税金の差異を補うために基本価格が動的に調整されます。[この機能を有効にする方法については、こちらのリンクをご覧ください](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#prices-entered-with-tax)。

**オプション2: すべての商品価格を税抜きで入力する**

#### 異なる税務処理による製品の取り扱い

異なる税務処理で製品を処理する必要がある場合は、次の方法で処理できます。

- 商品ごとに異なる税区分を使用している
- 以下の[固有の税設定](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#unique-tax-setups)のいずれかがストアに該当するかどうかを確認してください

何らかの理由で店舗の住所を別の州に変更する必要がある場合は、使用している設定を確認することが重要です。

**店舗移転の手順:**

1. **ストアの住所を更新:** WooCommerce Taxはストアの住所を使用します（**WooCommerce > 設定 > 一般**）。そのため、この設定を使用してストアの新しい住所を追加することが重要です。
2. **既存の税率をクリア:** 標準税率（**WooCommerce > 設定 > 税金 > 標準税率** タブ）に追加したすべての情報も削除する必要があります。自動税率を使用している場合は、プラグインを新しい場所にリセットするために、それらの標準税率を削除する必要があります。

**エラー例:**

```
01-10-2018 @ 14:09:18 - Received (401): {"statusCode":401,"error":"Unauthorized","message":"Invalid token","attributes":{"error":"Invalid token"}}
01-10-2018 @ 14:09:21 - wcc_server_error_response Error: The WooCommerce Shipping & Tax server returned: Unauthorized Invalid token ( 401 ) (fetch_service_schemas_from_connect_server)
```

**解決策:** プロセスは同じなので、[WooPayments ドキュメントのこのガイド](https://woocommerce.com/document/woopayments/our-policies/connection/#resetting-the-connection)に従って、WordPress.com への接続をリセットしてください。

フロリダ州では、特定の住所に関連付けられた売上は、「課税対象」であっても、税金が 0 ドルになる場合があります。

**説明:** フロリダ州歳入局によると、特定の住所は州および地方自治体の売上税および使用税の免除対象となります。特定の住所と郵便番号の税率は、[Florida PointMatchウェブサイト](https://taxlaw.state.fl.us/PointMatch/)でご確認いただけます。

ショップが米国に所在し、WooCommerce Taxプラグインで自動税計算が有効になっているにもかかわらず、特定の住所の税率が間違っていると思われる場合は、[TaxJar Sales Tax Calculator](https://www.taxjar.com/sales-tax-calculator/)を使用して再確認できます。WooCommerce Taxプラグインは、TaxJarが提供する税率データベースを使用して税率を計算します。

**料金の確認方法:**

1. オンラインテスターで注文の請求先または配送先住所（税金設定に従って）を入力します。
2. データベースから直接返された料金を確認します。
3. オンラインテスターから返された料金がサイトに表示される料金と一致する場合、問題はプラグインのバグやエラーではありません。

**重要事項:**

- このデータベースから取得される税率は、ソース住所に一致する州、郡、または市から直接取得されます。
- 返された税率に誤りがあると思われる場合は、まずその住所の管轄機関に問い合わせて正しい税率を確認し、サポートチームに問題を報告する際にはこれらの参照情報をご提供ください。
- 5桁の郵便番号と9桁の郵便番号の税率が一致しない場合があります。繰り返しますが、この情報は住所が所在する州、郡、または市から直接取得されます。
- 郵便番号は大体1つの地域に該当する場合もありますが、郵便番号が長い場合は別の地域に該当する場合があります。これらの税率については各州に再度確認し、税率の誤りをサポートチームに報告する際にはこれらの参照情報をご提供ください。

[この問題](https://github.com/woocommerce/woocommerce/issues/12590)により、自動課税を有効にする米国領土を独立した国として削除し、米国州のリストに追加する必要があります。以下は、プエルトリコでこれを行うためのサンプルスニペットです。他の州も同じ形式で追加できます。

```
add_filter( 'woocommerce_countries', 'wc_remove_pr_country', 10, 1 );

function wc_remove_pr_country( $country ) {
    unset( $country['PR'] );
    return $country;
}

add_filter( 'woocommerce_states', 'wc_us_states_mods' );

function wc_us_states_mods( $states ) {
    $states['US'] = array(
        'AL' => __( 'Alabama', 'woocommerce' ),
        'AK' => __( 'Alaska', 'woocommerce' ),
        'AZ' => __( 'Arizona', 'woocommerce' ),
        'AR' => __( 'Arkansas', 'woocommerce' ),
        'CA' => __( 'California', 'woocommerce' ),
        'CO' => __( 'Colorado', 'woocommerce' ),
        'CT' => __( 'Connecticut', 'woocommerce' ),
        'DE' => __( 'Delaware', 'woocommerce' ),
        'DC' => __( 'District Of Columbia', 'woocommerce' ),
        'FL' => __( 'Florida', 'woocommerce' ),
        'GA' => _x( 'Georgia', 'US state of Georgia', 'woocommerce' ),
        'HI' => __( 'Hawaii', 'woocommerce' ),
        'ID' => __( 'Idaho', 'woocommerce' ),
        'IL' => __( 'Illinois', 'woocommerce' ),
        'IN' => __( 'Indiana', 'woocommerce' ),
        'IA' => __( 'Iowa', 'woocommerce' ),
        'KS' => __( 'Kansas', 'woocommerce' ),
        'KY' => __( 'Kentucky', 'woocommerce' ),
        'LA' => __( 'Louisiana', 'woocommerce' ),
        'ME' => __( 'Maine', 'woocommerce' ),
        'MD' => __( 'Maryland', 'woocommerce' ),
        'MA' => __( 'Massachusetts', 'woocommerce' ),
        'MI' => __( 'Michigan', 'woocommerce' ),
        'MN' => __( 'Minnesota', 'woocommerce' ),
        'MS' => __( 'Mississippi', 'woocommerce' ),
        'MO' => __( 'Missouri', 'woocommerce' ),
        'MT' => __( 'Montana', 'woocommerce' ),
        'NE' => __( 'Nebraska', 'woocommerce' ),
        'NV' => __( 'Nevada', 'woocommerce' ),
        'NH' => __( 'New Hampshire', 'woocommerce' ),
        'NJ' => __( 'New Jersey', 'woocommerce' ),
        'NM' => __( 'New Mexico', 'woocommerce' ),
        'NY' => __( 'New York', 'woocommerce' ),
        'NC' => __( 'North Carolina', 'woocommerce' ),
        'ND' => __( 'North Dakota', 'woocommerce' ),
        'OH' => __( 'Ohio', 'woocommerce' ),
        'OK' => __( 'Oklahoma', 'woocommerce' ),
        'OR' => __( 'Oregon', 'woocommerce' ),
        'PA' => __( 'Pennsylvania', 'woocommerce' ),
        'PR' => __( 'Puerto Rico', 'woocommerce' ),
        'RI' => __( 'Rhode Island', 'woocommerce' ),
        'SC' => __( 'South Carolina', 'woocommerce' ),
        'SD' => __( 'South Dakota', 'woocommerce' ),
        'TN' => __( 'Tennessee', 'woocommerce' ),
        'TX' => __( 'Texas', 'woocommerce' ),
        'UT' => __( 'Utah', 'woocommerce' ),
        'VT' => __( 'Vermont', 'woocommerce' ),
        'VA' => __( 'Virginia', 'woocommerce' ),
        'WA' => __( 'Washington', 'woocommerce' ),
        'WV' => __( 'West Virginia', 'woocommerce' ),
        'WI' => __( 'Wisconsin', 'woocommerce' ),
        'WY' => __( 'Wyoming', 'woocommerce' ),
        'AA' => __( 'Armed Forces (AA)', 'woocommerce' ),
        'AE' => __( 'Armed Forces (AE)', 'woocommerce' ),
        'AP' => __( 'Armed Forces (AP)', 'woocommerce' ),
    );
    return $states;
}
```

ラベルのご購入代金を安全にお支払いいただくため、WordPress.comアカウントに接続し、サイトとユーザーアカウントを認証いたします。[利用規約](https://woocommerce.com/terms-conditions/)はこちらをご覧ください。

**影響を受ける日付:** 2021年7月1日

2021年7月1日、欧州連合（EU）の付加価値税（VAT）eコマースパッケージの一環として、新しい課税ルールが施行されました。WooCommerce Taxをご利用の場合、新しい変更は以下の種類の販売者に影響します。

- **EU加盟店** で、EU内で10,000ユーロを超える越境ECを提供している場合
- **EU域外加盟店** で、EU内で販売し、チェックアウト時にVATを徴収することを選択した場合

#### 追加リソース

- WooCommerce ブログで詳細をご覧ください: [EU の新税制：OSS と IOSS がストアに与える影響](https://woocommerce.com/posts/new-eu-tax-regulations-what-oss-and-ioss-means-for-your-store/)
- 欧州委員会にお問い合わせください: [越境 E コマース向け VAT の近代化](https://ec.europa.eu/taxation_customs/business/vat/modernising-vat-cross-border-ecommerce_en)

**重要な免責事項:** いつものように、あなたのビジネスが規制とベストプラクティスに従っていることを確認するために、税務専門家に相談することをお勧めします。

**このドキュメントには何か不足していますか? まだ質問があり、サポートが必要ですか?**

- ご購入をご希望の拡張機能やテーマについてご質問がある場合は、[お問い合わせ](https://woocommerce.com/contact-us/#sales-form) ください。
- 既にこの製品をご購入済みでサポートが必要な場合は、[サポートページ](https://woocommerce.com/my-account/create-a-ticket/) からハピネスエンジニアにご連絡ください。製品ドロップダウンから製品名を選択してください。

