---
title: コア税金のトラブルシューティング
url: https://woocommerce.com/document/troubleshooting-core-taxes/
---

このドキュメントには、WooCommerce の税金に関連する問題に対するトラブルシューティングの提案が記載されています。

WooCommerceプラグインは、[基本税率](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/)をサポートしています。これらの組み込み税オプションは**Core Taxes**と呼ばれます。Core Taxesを使用すると、**WooCommerce > 設定**の「税」タブで基本的な税オプションを設定できます。また、[このセクションを使用](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#configuring-tax-options)を使用して、地域や商品の種類ごとに手動で税率表を設定することもできます。

自動税額計算を有効にするには、追加のプラグインをインストールする必要があります。**WooCommerce Taxプラグイン**は無料で、多くの国で簡単な状況での自動税額計算を提供します。より高度な税金計算プラグインは、より高度なシナリオや特定の商品、特定の用途向けに提供されています。

このドキュメントでは、主に WooCommerce のコア税率機能に関連する問題に焦点を当て、他のプラグインやより複雑な設定に関するヘルプをどこで見つけられるかについての提案を提供します。

このセクションでは、コア WooCommerce 税テーブルの使用時に発生する可能性のある一般的な問題について説明します。

税金の計算エラーは、基本的な税金設定が誤っているために最も頻繁に発生します。

#### 税金計算の有効化

**WooCommerce > 設定 > 一般** で [税率と計算を有効にする](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#enabling-taxes) オプションがオンになっていることを確認します。

#### デフォルトの顧客の所在地

[設定が誤っている](https://woocommerce.com/document/configuring-woocommerce-settings/general/#general-options)場合、初めての訪問者は住所を入力する前に誤った税金計算が表示される可能性があります。設定で「Geolocate」を使用する場合は、[MaxMind](https://docs.google.com/document/d/1GKwihbAWBzhwAjE-fO-5Kyy4RTofLXrw2diSFeFeqAg/edit?tab=t.0) を有効にする必要がありますのでご注意ください。

#### 税金を計算する

[この設定](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#calculate-tax-based-on)は、税金を顧客の配送先住所、請求先住所、またはストアの住所のどれに基づいて計算するかを決定します。この設定が正しくない場合、WooCommerce は誤った地域に基づいて税率を表示する可能性があります。

**基本的な税金設定が正しいことを確認するには:**

1. **WooCommerce > 設定 > 税金** に移動します。
2. 「税額計算の基準」が適切なオプションに設定されていることを確認します。
- **顧客の配送先住所** – 商品の発送先に基づいて税金を計算する場合
- **顧客の請求先住所** – デジタル商品の場合、または配送先住所が収集されていない場合
- **ショップの基本住所** – すべての購入者に同じ税率を請求する場合のみ
  

WooCommerce の[税金計算](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/how-taxes-work-in-woocommerce/)は、特定のロジックに基づいて取引に適用される税率を決定します。税率が誤っている場合は、その計算メカニズムを理解することで問題の原因を特定しやすくなります。

WooCommerce は、いくつかの要素を順番に考慮しながら、階層的に税金の計算を処理します。

**税率を確認するには:**

#### ステップ1: 税額表を特定する

定義された税金クラスに基づいて、カート内の各製品に使用する税金テーブルを特定します。

#### ステップ2: 位置の一致を確認する

各商品の表を確認し、課税対象地域（設定に応じて、店舗住所、顧客の請求先住所、または顧客の配送先住所）に一致する地域があるかどうかを確認してください。以下の項目に誤字脱字がないか再度ご確認ください。

**国と州コード:**

- 国コードと州/省コードは標準的な2文字のコードである必要があります

**郵便番号:**

- 郵便番号にはワイルドカード（`90*`）または範囲（`90210-90215`）を含めることができます。
- 問題が疑われる場合は、セミコロンで区切られたリストまたは個別の行として、個々のコードを入力してください。

**都市名:**

- WooCommerce は、チェックアウトページで入力された正確な文字列に基づいてのみ都市を照合します。
- よくある不一致には、略語や別のスペル（例：「ST CHARLES」と「SAINT CHARLES」、「New York」と「NYC」）などがあります。
- 税率を正しく適用するために、一般的な都市名のバリエーションについて、税率表に複数の行を追加することを検討してください。

#### ステップ3: 優先順位の競合を処理する

課税対象地域が税額表の複数の行に該当する場合は、優先順位ごとに 1 つの税率を選択します。

例えば：

- 優先度1の税率表に複数の行が存在する場合、現在の課税所在地に一致する最上位の行のみを選択して適用します。
- 優先度2にさらに行が存在する場合、現在の所在地に一致する最上位の2級税率のみを選択して追加適用します。これをすべての優先度レベルで繰り返します。

#### ステップ4: 価格表示設定との統合

これらの計算を、設定した[価格表示設定](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#display-prices-during-cart-and-checkout)と統合します。

**重要:** トラブルシューティングを行う際には、WooCommerce が各優先度レベルの適切な税金テーブルで最初に一致する税金の場所で停止することを認識することが重要です。つまり、税金ルールの順序は、適用される税率に大きな影響を与える可能性があります。

追加の[高度なコア税金テーブルの例はこちら](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/)をご覧ください。

チェックアウト時に送料に税金が適用されない場合は、通常、設定ミスが原因です。WooCommerceのコア税システムでは、送料の税金を正しく適用するためにいくつかの設定を調整する必要があります。AvalaraやTaxJarなどのプラグインを使用していない場合は、以下の手順に従って問題を解決してください。

#### ステップ1: 配送方法の税金ステータスを確認する

**WooCommerce > 設定 > 配送 > [配送先地域]** にある各[定額コア配送方法](https://woocommerce.com/document/flat-rate-shipping/)の**税金ステータス**が明示的に**課税対象**に設定されていることを確認してください。「なし」に設定されている場合、WooCommerceは他の設定に関係なく、配送料の税金を計算しません。

#### ステップ2: 配送税クラスを設定する

**WooCommerce > 設定 > 税金** の「税金オプション」セクションで、「配送税区分」が適切な値に設定されていることを確認してください。この値は以下のとおりです。

**カート商品と同じ** – 送料はカートの中身に適用されている最優先の税区分を継承します。つまり、

- カート内のすべての商品が同じ税率クラスに該当する場合、配送税率はその税率表から取得されます。
- カート内の商品に複数の税率クラスがあり、そのうちの1つが標準税率クラスに該当する場合、配送には標準税率が適用されます。
- カート内の商品に複数の税率クラスがあり、そのうちの1つが標準税率クラスに該当しない場合、カート内の少なくとも1つの商品と一致する[追加税率](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#additional-tax-classes)リストの最上位の税率クラスが配送料として適用されます。[例はこちら](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#shipping-tax-class)

**特定の税金クラス** (例: 標準、割引率) – カートの内容に関係なく、配送料はそのクラスを使用して課税されます。

#### ステップ3: 税金テーブルの構成を確認する

配送料に使用される可能性のあるすべての税率表に、「配送」チェックボックスがオンになっている行が含まれていることを確認してください。税率表は**WooCommerce > 設定 > 税金**タブにあります。タブ上部に小さなリンクとして「標準料金」などのさまざまな料金表が表示されているか確認してください。

**以下を確認してください:**

- 税率が顧客の所在地と一致している
- 「配送」列にチェックが入っている
- チェックボックスがオフになっている場合、税率が他の一致する税率によって上書きされていない

**重要:** 適用可能な料金で配送が許可されていない場合は、配送方法と配送クラスが正しく設定されていても、配送料は課税されません。

#### ステップ4: 商品レベルの税金設定を確認する

**「商品 > 商品の編集 > 商品データ > 全般」** で商品レベルの税金設定を確認します。

カートに非課税商品のみが含まれており、「カート商品と同じ」配送税クラスを使用している場合、WooCommerce は配送に税金を適用しません。

**注文内の少なくとも 1 つの製品を確認してください:**

- 税金ステータスが**課税対象**に設定されている
- 税金区分が正しく割り当てられている（例：標準）

**WooCommerce > 設定 > 一般 > デフォルトの顧客所在地** で Geolocate を有効にしている場合、WooCommerce は訪問者の所在地を自動的に特定し、所在地固有の税率と配送オプションを表示しようとします。

ただし、顧客が住所を入力するまで税金が表示されない場合や、価格が正しく表示されない場合は、次のいずれかが原因であることが多いです。

#### MaxMind Geolocation が正しく設定されていません

WooCommerce の Geolocate は、顧客の位置情報を取得するために MaxMind GeoIP データベースを使用しています。正しく機能させるには、このデータベースを [MaxMind ライセンスキーを使用してダウンロードし、リンク](https://woocommerce.com/document/maxmind-geolocation-integration/) する必要があります。

WooCommerce は必要なデータベースファイルを自動的にダウンロードして更新します。設定が完了すると、ストアは MaxMind を使用して顧客の位置情報を取得できるようになります。

#### 税込価格設定の複雑さ

ストアが税込価格を表示するように設定されていて、複数の国に販売している場合、以下の要因によって価格の表示が異なる場合があります。

- 顧客の位置情報に基づく国
- Geolocateが顧客の位置を正確に特定したかどうか
- 顧客がチェックアウト時に住所を既に入力しているかどうか

顧客が所在地を確認するまで（例：配送先住所や請求先住所を入力するなど）、税込価格はストアの基本所在地税率がデフォルトとなるか、Geolocate が正しく機能していない場合は税金がまったく表示されないことがあります。

#### Geolocate のベストプラクティス

- MaxMind Geolocation が常に設定され、有効になっていることを確認してください。
- フルページキャッシュまたは CDN レベルのキャッシュを使用する場合は、**Geolocate（ページキャッシュサポート付き）** を有効にすることを検討してください。
- 国際販売の場合は、税込価格設定に注意してください。表示される税額は、検出または確認された場所によって異なる場合があります。

[WooCommerce Tax](https://woocommerce.com/document/woocommerce-shipping-and-tax/woocommerce-tax/) プラグインを使用して税金を自動計算している場合、次のような問題がよく発生します。

- **米国の一部の州で税金が計算されない** (通常は[税務ネクサス](https://stripe.com/en-ca/resources/more/nexus-tax-101)がどこにあるかが問題です)
- **税込価格表示設定が無効になっている**
- **米国領土で税金が計算されない**

これらの問題をデバッグする方法については、[WooCommerce Tax トラブルシューティング ガイド](https://woocommerce.com/document/woocommerce-tax/) をご覧ください。

ステージングサイトは、安全なテストとデバッグのために使用する、ライブWooCommerceストアのクローンです。顧客への影響やライブデータへのリスクを負うことなく、税金の計算ミスや潜在的な競合などの問題を再現できます。

**ステージングサイトテストの利点:**

- ステージング環境で問題を特定できれば、ハピネスエンジニアが問題をより迅速に再現し、対処すべき問題を報告できます。
- ステージングサイトで問題が発生しない場合は、WooCommerce の設定の問題ではなく、ライブサイトでの競合が発生している可能性があります。

**ステージングサイトの作成方法:** ほとんどのホスティングプロバイダーはワンクリックでステージング環境を提供しています。また、[WP Staging](https://wordpress.org/plugins/wp-staging/)などのプラグインを使用して作成することもできます。詳細な手順については、以下の記事をご覧ください。

- [WordPressステージングサイトとは何か？そしてどのように設定するのか？](https://wordpress.org/support/article/wordpress-staging-site/)
- [競合のテスト方法](https://woocommerce.com/document/how-to-test-for-conflicts/)

#### テストにブループリントを使用する

**WooCommerce 9.9以降：** [Blueprints](https://woocommerce.com/document/woocommerce-blueprints/)は、ストア設定のインポートとエクスポートを行うツールです。テストサイトを素早く構築するのにも役立ちます。Blueprintsは**WooCommerce > 設定 > 詳細設定 > Blueprint**にあります。

ブループリントを使用すると、トラブルシューティングのためにストア設定（税金設定を含む）をエクスポートし、新しく作成した WordPress/WooCommerce サイトにインポートしてテストし、同様の競合テストを実行して基本的な税金設定が正しいことを確認できます。

キャッシュによって古いコンテンツが提供され、税金の計算に影響する可能性があります。この問題に対処するには、以下の手順を実行してください。

1. **すべてのキャッシュをクリアする** – ブラウザ、プラグイン、サーバーレベルのキャッシュを含む
2. **動的ページを除外する** – カート、チェックアウト、マイアカウントをキャッシュから除外する
3. **WooCommerceセッションとCookieがキャッシュされていないことを確認する**

WooCommerce のキャッシュ プラグインの構成の詳細については、[WooCommerce のキャッシュ プラグインを構成する方法の開発者向けドキュメント](https://woocommerce.com/document/configuring-caching-plugins/) を参照してください。

次のような場合、税金の請求はすぐに複雑になる可能性があります。

- 複数の地域または国で税金を請求する必要がある
- 郡税や市税など、住所に大きく依存する税金を請求する必要がある
- 特定の商品区分に対して異なる税率で税金を請求する必要がある
- 非営利団体など、特定の顧客に免税を適用できる必要がある
- さまざまなプラットフォームや統合からデータを集計できる高度なレポート機能が必要である

このような場合、手動で税額表を管理するのは労力がかかる可能性があります。ストアの税制要件が複雑な場合は、より高度な税額計算プラグインが必要になる場合があります。

**重要な免責事項：** 当社は税務の専門家ではありません。当社のアドバイスは、当社のソフトウェアの使用方法に関するもののみを対象としています。税金／VAT／GSTなどの課税対象や時期に関するアドバイスについては、税務専門家または会計士にご相談ください。事業はそれぞれ異なるため、ここですべての可能性を網羅することはできません。

これら3つのオプションはすべて、サービス料金が発生する外部アカウントが必要です。料金は、月間のAPI呼び出し回数と必要な年間申告件数に基づいて算出されます。これらの外部サービスによってアクセシビリティサポートの内容が異なる場合がありますので、各サービスのドキュメントをご確認いただくか、サポートチームにお問い合わせください。

#### 高度な自動税金計算プラグインの比較

また、買い物客の役割、国、購入数量に基づいて、一部の買い物客に免税措置を講じる必要がある場合もあります。

#### EUのVAT免除

一般的な使用例としては、EU 企業が有効な VAT 番号を提供し、ストアの本国以外に所在している場合に、その EU 企業を VAT (付加価値税) から免除することが挙げられます。

**利用可能なプラグイン:**

- **EU VAT番号** – このプラグインは、英国企業のEU VAT番号確認には対応していません。
- **EU/UK VAT検証マネージャー** – これはWooCommerceによって開発またはサポートされていないサードパーティ製プラグインです。ご質問やサポートについては、このプラグインの公開フォーラムをご利用ください。

#### その他の一般的な免税シナリオ

- **WooCommerce の免税** – 特定のユーザーロールまたは特定の顧客を免税対象として設定します
- **ロールベースの税金** – ユーザーロールに基づいて、税金を内税または税抜で表示します
- **障害者向け VAT 免除** – 慈善団体や障害のある顧客向けに VAT 免除を設定します
- **究極の免税** – 国に基づいて顧客の税金を免除し、他の顧客がフォームから免税ステータスを申請できるようにします

複雑な免税シナリオ向けのその他の税金関連プラグインは、[マーケットプレイス](https://woocommerce.com/product-category/woocommerce-extensions/) で見つかります。

WooCommerce の税金を外部システム（会計ツールやレポートツールなど）と同期する場合、設定と互換性はその特定の統合によって異なります。

#### Xero 統合

Xero と税務情報を同期する方法の詳細については、以下をご覧ください。

- [設定が正しく行われていることを確認してください](https://woocommerce.com/document/xero/)
- デバッグを有効にしてログを確認してください
- [よくある問題の解決策はこちら](https://woocommerce.com/document/xero/#troubleshooting)
- [よくあるXeroログのエラーメッセージはこちら](https://woocommerce.com/document/xero/#common-error-messages)

#### QuickBooks との統合

**WPSwingsによるWooCommerce向けQuickBooks統合:**

- [WPSwings サポート](https://wpswings.com/contact-us/) にお問い合わせください

**MyWorks Software による WooCommerce 用 QuickBooks Sync:**

- [MyWorks サポート](https://myworks.software/support) にお問い合わせください

WooCommerce の税金を外部システム（会計ツールやレポートツールなど）と同期する場合、設定と互換性はその特定の統合によって異なります。

税務情報の同期の詳細については、以下をご覧ください。

**重要な免責事項：** これは高度なユースケースを想定しており、すべてのストアに適しているとは限りません。カスタムコードはアクセシビリティやコンプライアンスに影響を与える可能性があります。実際のサイトで使用する前に、支援技術でテストしてください。

**安全ガイドライン:**

- 親テーマの`functions.php`ファイルにカスタムコードを直接追加しないでください。テーマのアップデート時に上書きされてしまいます。
- 代わりに、子テーマの`functions.php`ファイルにコードを追加するか、[Code Snippetsプラグイン](https://wordpress.org/plugins/code-snippets/)などのカスタムスニペットをサポートするプラグインを使用してください。
- カスタムコードを本番サイトに適用する前に、必ずステージングサイトでテストしてください。

**注:**このドキュメントは、高度なトラブルシューティングに役立つガイドとして提供されています。ただし、記載されている手順は[サポートポリシー](https://woocommerce.com/support-policy/)の対象外であり、実装に関する直接的なサポートは提供できません。資格のあるWordPress/WooCommerce開発者のサポートをご希望の場合は、[Codeable](https://codeable.io/?ref=z4Hnp)または[Woo Agency Partner](https://woocommerce.com/development-services/)を強くお勧めします。

店舗が商品価格を税込みで入力し、地域によって異なる税率を適用している場合、適用される税率に応じて価格が変動するように見えます。実際には、基本価格は変わりませんが、税金が合計金額に影響します。[詳細な説明はこちらのリンクをご覧ください](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#prices-entered-with-tax)。

一部の販売者は、税率の変更に合わせて商品の基本価格を動的に変更し、税率に関わらず合計金額を一定に保つことを希望しています。この機能を有効にするには、以下のスニペットを使用します。

```
add_filter( 'woocommerce_adjust_non_base_location_prices', '__return_false' );
```

以下のスニペットは、小計が指定された最小値に達した場合にのみ税金を加算するストアの場合に便利です。以下のコードスニペットでは、最小値はストアの通貨の110です。必要に応じてスニペットを調整してください。

```
add_filter( 'woocommerce_product_get_tax_class', 'big_apple_get_tax_class', 1, 2 );

function big_apple_get_tax_class( $tax_class, $product ) {
    if ( WC()->cart->subtotal <= 110 ) {
        $tax_class = 'Zero Rate';
    }

    return $tax_class;
}
```

一部の販売業者は、卸売ステータスまたは免税に対応するために、顧客の役割に基づいて異なる税率を適用することを要求する場合があります。

このスニペットでは、「管理者」権限を持つユーザーにゼロ税率クラスが割り当てられます。要件に応じて調整してください。

```
/**
 * Apply a different tax rate based on the user role.
 */
function wc_diff_rate_for_user( $tax_class, $product ) {
    if ( is_user_logged_in() && current_user_can( 'administrator' ) ) {
        $tax_class = 'Zero Rate';
    }

    return $tax_class;
}

add_filter( 'woocommerce_product_get_tax_class', 'wc_diff_rate_for_user', 1, 2 );
add_filter( 'woocommerce_product_variation_get_tax_class', 'wc_diff_rate_for_user', 1, 2 );
```

値が0の税金はデフォルトで非表示になっています。以下のスニペットを追加すると、表示されなくなります。

```
add_filter( 'woocommerce_order_hide_zero_taxes', '__return_false' );
```

WooCommerce の税設定の一つでは、サフィックスを使用して商品価格に追加情報を追加できます。これは可変商品のバリエーションで使用できますが、バリエーションが多いとウェブサイトのパフォーマンスに影響を与える可能性があるため、メインのバリエーションレベルでは無効になっています。

変動商品の場合、関連価格の出力メソッドはフィルターフックを介してカスタマイズできます。このフィルターを使用して実装できるカスタマイズが必要になります。

```
add_filter( 'woocommerce_show_variation_price', '__return_true' );
```

カート ページとチェックアウト ページの合計に影響を与えずにカスタム税金行を表示するには、次のスニペットを使用します。

```
// Show shipping and product taxes separately
function custom_display_tax_rows() {
    // Get the cart instance
    $cart = WC()->cart;

    // Get the shipping tax total
    $shipping_tax_total = $cart->get_shipping_tax();

    // Get the product tax total
    $product_tax_total = $cart->get_cart_contents_tax();

    // Calculate the total tax (excluding shipping tax)
    $total_tax = $product_tax_total;

    // Display custom rows for Shipping Tax, Product Tax, and Total Tax
    if ( $shipping_tax_total > 0 ) {
        echo '<tr class="shipping-tax-row">';
        echo '<th>' . __( 'Shipping Tax', 'your-text-domain' ) . '</th>';
        echo '<td>' . wc_price( $shipping_tax_total ) . '</td>';
        echo '</tr>';
    }

    if ( $product_tax_total > 0 ) {
        echo '<tr class="product-tax-row">';
        echo '<th>' . __( 'Product Tax', 'your-text-domain' ) . '</th>';
        echo '<td>' . wc_price( $product_tax_total ) . '</td>';
        echo '</tr>';
    }

    // Display the total tax only if it's greater than zero
    if ( $total_tax > 0 ) {
        echo '<tr class="order-tax-row">';
        // You might want to show something here; this row is currently empty.
        echo '</tr>';
    }
}

// Hook the function to run when the cart is displayed
add_action( 'woocommerce_cart_totals_after_shipping', 'custom_display_tax_rows', 5 );

// Hook the function to run when the checkout is displayed
add_action( 'woocommerce_review_order_before_order_total', 'custom_display_tax_rows', 5 );
```

WooCommerceは、ストアの設定、税区分、および端数処理の設定に基づいて税金を計算します。特に税込価格設定を使用している場合、複数の数量をカートに追加した場合など、場合によっては端数処理に若干の誤差が生じることがあります。これは通常、税金の計算方法と端数処理方法に起因するもので、eコマースプラットフォーム全体でよく見られる現象です。

#### 丸め設定

税金の端数処理方法は、**WooCommerce > 設定 > 税金** の「端数処理」オプションで制御できます。

**行ごとの丸め (デフォルト):** 税金は、合計を加算する前に、行項目ごとに計算され、丸められます。

**小計レベルの四捨五入:** 税金はすべての項目の小計から計算され、一度四捨五入されます。

どちらのオプションを使用するかは、税務管轄区域と商品の価格設定方法によって異なります。小計レベルでの四捨五入は、税額合計のわずかな差異を軽減できますが、商品ごとの税額内訳を比較する際に差異が生じる可能性があります。

#### 1つずれた丸め

価格に税込み価格があり、お客様が複数の数量を購入された場合、四捨五入による誤差（例：合計金額が0.01ずれる）が発生することがあります。これは、税額が単位ごとに計算され、各商品に個別に四捨五入が適用される場合に発生します。

#### 表示設定の不一致

WooCommerce は、以下の設定にわたって一貫した構成に依存します。

- 税込価格を入力する
- ショップで価格を表示する
- カートとチェックアウト時に価格を表示する

これらの設定に不一致がある場合（例：税込みで入力したのに税抜きで表示された場合）、WooCommerce は拡張精度を使用して価格を逆計算するため、端数処理に差異が生じる可能性があります。設定が不一致の場合、管理画面に警告バナーが表示されます。「推奨設定を使用する」プロンプトを使用して、この問題を解決できます。

#### 丸め動作のカスタマイズ

厳格な四捨五入の要件があるストア向けに、WooCommerce は開発者が価格と税金の動作をオーバーライドできるフィルターを提供しています。サイトはそれぞれ異なるため、このコードは商品、価格、そしてショップの税金ルールによって異なります。必要な正確な四捨五入を実現するには、試行錯誤が必要です。

たとえば、次のコードは、数量を乗算する前に単位ごとに丸めを強制します。これは、特定のショップとその製品に対して機能しました。

```
add_filter( 'woocommerce_get_price_excluding_tax', 'custom_rounding_per_unit', 10, 3 );
function custom_rounding_per_unit( $price, $qty, $product ) {
    return round( $price / $qty, 2 ) * $qty;
}
```

[一般的な税金のトラブルシューティング シナリオ](https://woocommerce.com/document/troubleshooting-core-taxes/#common-issues-with-core-tax-tables)を試しても問題が解決しない場合は、次の情報を提供して [WooCommerce サポート](https://woocommerce.com/my-account/create-a-ticket/) にお問い合わせください。

**サポートリクエストに必要な情報:**

- 目標の概要（期待される結果と実際の動作の比較）
- 問題を再現するための手順のリスト
- ステージングサイトと問題の影響を受ける製品へのリンク（または、サイトの[ブループリント](https://woocommerce.com/document/woocommerce-blueprints/)をお送りいただければ、設定を再現してテストできます）
- システムステータスレポートのコピー（[WooCommerce > ステータス > システムステータス > システムレポートの取得](https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/#system-status)からアクセスできます）
- 最新のエラーログ：WooCommerce Tax に関する問題については、[ログ記録が有効](https://woocommerce.com/document/woocommerce-shipping-and-tax/woocommerce-tax/#troubleshooting) になっていることを確認し、最新のエラーログを添付してください。 **WooCommerce > ステータス > WooCommerce 配送と税金**

#### WooCommerceマーケットプレイスプラグイン

[WooCommerceマーケットプレイス](https://woocommerce.com/product-category/woocommerce-extensions/)に掲載されている税務拡張機能（WooCommerce Tax、TaxJar、Avalara for WooCommerce、Stripe Taxなど）をご利用の場合は、[WooCommerceサポート](https://woocommerce.com/my-account/create-a-ticket/)にお問い合わせください。これらのプラグインは、開発者との協力により積極的にサポートおよびメンテナンスされています。

#### サードパーティ製プラグイン

WooCommerceマーケットプレイスで入手できない税務プラグイン（他のソースからダウンロードしたものやカスタム開発されたものなど）をご利用の場合は、プラグインの開発者から直接サポートを受ける必要があります。これらのプラグインは独立してメンテナンスされているため、インストール、設定、トラブルシューティングのサポートは開発者に最も適しています。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

このページでアクセシビリティの問題が発生した場合は、[WooCommerce サポートに問い合わせ](https://woocommerce.com/accessibility/)ください。

