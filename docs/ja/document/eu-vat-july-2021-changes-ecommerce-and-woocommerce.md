---
title: EU VAT 2021年7月の変更、eコマース、WooCommerce
url: https://woocommerce.com/document/eu-vat-july-2021-changes-ecommerce-and-woocommerce/
---

2021年7月1日、欧州連合（EU）は付加価値税（VAT）に関する新しい規制を導入しました。EU域内で国境を越えて販売を行う事業者、またはEU域内に輸入を行う事業者は、この規制に従う必要があります。

このドキュメントでは、主要な変更点と新たな変更のシナリオについて解説しますが、網羅的なものではありません。通貨記号はユーロ（EUR）（€）を使用します。

WooCommerce で税金を設定する方法に関する一般的なアドバイスについては、[税金の設定](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/) および [特定の税金設定を構成する方法](https://woocommerce.com/document/configuring-specific-tax-setups-in-woocommerce) のドキュメントを確認してください。

これらの変更は**企業対顧客（B2C）販売**にのみ影響します。企業対企業（B2B）販売のルールは変更ありません。

**WooCommerce 販売業者は EU 規制を遵守する責任があります。** WooCommerce Inc. も WooCommerce Ireland Limited も、EU が定義するマーケットプレイスまたはファシリテーターではありません。

- EU加盟店については、EU域内における商品の遠隔販売に関する既存の基準が廃止され、EU全体で10,000ユーロという新たな基準が適用されます。
- 22ユーロ以下の小口貨物の輸入におけるVAT免除が廃止されました。これにより、EU域内で輸入されるすべての商品がVATの課税対象となります。
- 加盟店は、新しい[ワンストップショップ](https://ec.europa.eu/taxation_customs/business/vat/oss_en) (OSS) または[輸入ワンストップショップ](https://ec.europa.eu/taxation_customs/business/vat/ioss_en) (IOSS) を利用することで、EU加盟国ごとにVAT申告書を1通提出するだけで済みます。

このドキュメントでは、**3 つの異なるシナリオ** に焦点を当てます。

1. [EU加盟店がEU加盟店に販売する場合：10,000ユーロのしきい値未満](https://woocommerce.com/document/eu-vat-july-2021-changes-ecommerce-and-woocommerce/#eu-merchant-selling-to-another-eu-shopper-under-the-10k-threshold)
2. [EU加盟店がEU加盟店に販売する場合：10,000ユーロのしきい値を超える](https://woocommerce.com/document/eu-vat-july-2021-changes-ecommerce-and-woocommerce/#eu-merchant-selling-to-another-eu-shopper-above-the-10k-threshold)
3. [EU加盟店以外がEU加盟店に販売する場合] EU](https://woocommerce.com/document/eu-vat-july-2021-changes-ecommerce-and-woocommerce/#noneu-merchant-selling-into-the-eu)

**主な変更点:**

- EU加盟店の場合、EU域内における商品の遠隔販売に対する既存の基準額は廃止され、EU全体で10,000ユーロという新たな基準額に置き換えられました。
- このシナリオの要件を満たす加盟店は、引き続き、出荷元となるEU加盟国のVAT率を、出荷先となるすべてのEU加盟国に対して請求し、現地の税務当局への納税を継続できます。

**これらの販売者への影響:**

- 販売者は、EU加盟国へのすべての注文に対して、同一の現地VAT税率を適用できます。
- 販売者は、この免税の対象となるかどうかを確認する必要があります。

**このシナリオで WooCommerce マーチャントが検討できる次のステップ:**

- WooCommerce の税金設定を更新し、すべての EU 加盟国の VAT 税率を自国と同じ税率に設定します。
- 販売者は引き続き、WooCommerce Analytics の [税金および VAT 関連レポート](https://woocommerce.com/document/woocommerce-analytics/#taxes-report) をご利用いただけます。
- 販売者は [EU VAT 番号](https://woocommerce.com/products/eu-vat-number/) 拡張機能を使用して、EU 加盟店に VAT を支払わないオプションを提供できます。

**主な変更点:**

- 現行の各国別の遠隔販売基準は、EU全体で10,000ユーロという新たな基準に置き換えられました。
- 加盟店は、EU全体でのすべての売上をOSSで報告できます。これにより、各国の遠隔販売基準に基づいて各国でVAT申告を登録する必要がなくなりました。

**これらの販売者への影響:**

適用される VAT 率は顧客の国の VAT 率となります。

**このシナリオで WooCommerce マーチャントが検討できる次のステップ:**

- WooCommerce の税金設定を更新し、各 EU 加盟国の VAT 率を特定の VAT 率に設定します。
- 販売者は引き続き、WooCommerce Analytics の [税金および VAT 関連レポート](https://woocommerce.com/document/woocommerce-analytics/#taxes-report) を利用できます。
- 販売者は [EU VAT 番号](https://woocommerce.com/products/eu-vat-number/) 拡張機能を使用して、EU 加盟店に VAT を支払わないオプションを提供できます。

**主な変更点:**

- EUへ発送されるすべての注文はVATの対象となります。22ユーロまでの小口貨物に対する免税は廃止されます。
- 150ユーロを超える購入については、配達時にVATをお支払いいただきます。
- 販売業者は新しいIOSS申告をご利用ください。

**これらの販売者への影響:**

販売者は、チェックアウト時にVATを徴収するかどうかを決定する必要があります。VATは以下の基準に基づいて徴収されます。

- 150ユーロ未満の注文の場合、販売者はチェックアウト時にVATを徴収し、その後IOSSを使用して毎月VAT申告を行うことができます。
- 輸出品に対してチェックアウト時にVATが徴収されない場合、お客様は配達時に配送業者からVATを請求されます。
- 150ユーロを超える注文の場合、お客様はVATを支払います。

**このシナリオで WooCommerce マーチャントが検討できる次のステップ:**

- WooCommerce の税金設定を更新し、各 EU 加盟国の VAT 率をその特定の VAT 率に設定します。
- また、自国以外からの注文に対する VAT 請求額を 150 ユーロに制限する必要がある場合もあります。
- 販売者は引き続き WooCommerce Analytics の [税金および VAT 関連レポート](https://woocommerce.com/document/woocommerce-analytics/#taxes-report) をご利用いただけます。
- 販売者は [EU VAT 番号](https://woocommerce.com/products/eu-vat-number/) 拡張機能を使用して、EU 加盟店に VAT を支払わないオプションを提供できます。
- 販売者はストアの [利用規約](https://woocommerce.com/document/configuring-woocommerce-settings/advanced/#terms-and-conditions) を更新し、VAT は購入時ではなく配送時に徴収されることを買い物客に明確に伝える必要があります。
- オプションとして、販売者は [Avalara AvaTax Cross-Border](https://www.avalara.com/us/en/products/industry-solutions/cross-border-solutions.html) などのサービスを使用して、商品を自動的に分類し、チェックアウト時に VAT を計算し、当局に申請することができます。

米国では、州をまたぐ税金も同様に複雑です。[WooCommerce Tax](https://woocommerce.com/products/tax/) は標準的なユースケースに対応しています。WooCommerce Tax では要件を満たせなくなった場合は、[TaxJar for WooCommerce](https://woocommerce.com/products/taxjar/) や [Avalara for WooCommerce](https://woocommerce.com/products/woocommerce-avatax/) などのソリューションのご利用をお勧めします。

EU では、役立つ統合がいくつかあり、利用可能になったらさらに追加される予定です。

- [Avalara AvaTaxCross-Border](https://www.avalara.com/us/en/products/global-commerce-offerings/avatax-cross-border.html)は、EU域内で販売を行う販売業者向けにご利用いただけます。商品を自動的に分類し、チェックアウト時にVATを計算し、当局に申告します。
- [TaxJar](https://woocommerce.com/products/taxjar/)は、EU域内よりも米国に拠点を置く販売業者に適しています。

- EU加盟店が別のEU加盟店に販売する場合：10,000ユーロのしきい値未満
- 加盟店は引き続きWooCommerce Shipping & Taxの税金機能を利用できます。加盟店のEU加盟国に基づいて標準VAT率を計算します。
- ただし、いくつかの制限があります。
- 標準以外のカテゴリーに対しては、異なるVAT率を返すことはできません。
- 加盟店の売上が10,000ユーロのしきい値を超えたかどうかは追跡されません。
    
  
- EU加盟店が別のEU加盟店に販売：10,000ユーロのしきい値を超える
- これらの加盟店は**WooCommerce Shipping & Tax** を使用しないでください。誤ったVAT税率が返されます。
- これは、拡張機能が加盟店の10,000ユーロのしきい値を超えていることを考慮せず、引き続き現地のVAT税率を返すためです。
  
- EU域外の加盟店がEU域内で販売する場合：
- チェックアウト時にVATを徴収することを**選択した**加盟店の場合、EU域内への配送にかかるVAT率の計算に**WooCommerce Shipping & Tax**は使用できません。0%の税率が返されます。
- VATを**徴収しない**ことを選択した加盟店は、引き続きWooCommerce Shipping & Taxをご利用いただけます。お客様は配送時にこれらの関税と手数料をお支払いいただきます。
  

- [WooCommerce で特定の税金設定を構成する方法](https://woocommerce.com/document/configuring-specific-tax-setups-in-woocommerce): より一般的な [WooCommerce での税金の設定](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/) の追加ドキュメントで、上記のシナリオのいくつかを設定する手順を説明します。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

