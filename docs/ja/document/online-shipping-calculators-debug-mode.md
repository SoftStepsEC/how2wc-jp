---
title: オンライン配送計算ツールとデバッグモード
url: https://woocommerce.com/document/online-shipping-calculators-debug-mode/
---

WooCommerce インストールによって提供される配送コストが予想よりも高いか低い場合は、使用している配送プラグインの設定セクション内でデバッグ モードを有効にすることをお勧めします。

このオプションを有効にすると、製品をカートに追加すると、ほとんどの場合、カート ページやチェックアウト ページに、配送料が予想と異なる理由や、配送料がまったく表示されない理由を説明する有用な情報が表示されます。

WooCommerceサイトに表示される送料と、運送会社のオンライン料金計算ツールで計算された送料を比較することをお勧めします。ほぼすべての運送会社がこのようなツールを提供していますが、配送方法の設定で有効になっているものと完全に同じ値を使用することが重要です（運送会社は料金を変更する可能性があるため）。また、使用するパッケージ、総重量、総寸法が正しいことを確認してください。

問題が発生した場合は、次の点を確認してください。

- **重量と寸法** はすべての商品に入力する必要があります。API が料金を正しく返すためにはこれらが必要です。商品に配送情報を追加する方法の詳細については、[配送用に商品に寸法と重量を追加する](https://woocommerce.com/document/adding-dimensions-and-weights-to-products-for-shipping/) ドキュメントをご覧ください。
- **使用されている梱包** は正しいです。デバッグ出力ではパッケージの重量と寸法が表示されます。また、プラグインによっては、より明確にするためにデバッグ出力に「Packed」行が表示される場合もあります。箱詰めに関する詳細は、[箱詰め計算について](https://woocommerce.com/document/understanding-box-packing-calculations/) ドキュメントをご覧ください。
- **通貨** は正しく設定されています。プラグインによっては、ショップで特定の通貨を使用する必要があります。この場合、特定のプラグインのドキュメントに記載されており、**WooCommerce > 設定 > 一般** 設定ページでショップの通貨を確認または変更できます。
- **ショップの拠点所在地** は正しいです。プラグインによっては、ショップに特定の拠点所在地が必要です。ショップの拠点所在地は、**WooCommerce > 設定 > 一般** で確認または変更してください。
- **API キー** は正しいです。正しくない場合は、API レスポンスセクションに「認証失敗」というエラーメッセージが表示されます。
- **wp_remote_get()** 関数がサーバー上で有効になっています。**WooCommerce > システムステータス > サーバー環境** ページで、サイトのシステムステータスレポートの「リモート取得」セクションにチェックマークが付いていることをご確認ください。チェックマークが付いていない場合は、ホスティング会社に連絡してサポートを受けてください。
- **SOAP** がサーバー上でインストールされ、[有効](https://www.php.net/manual/en/class.soapclient.php) になっています。サイトのシステムステータスレポート（**WooCommerce > システムステータス > サーバー環境**ページ）の「SoapClient」セクションの横にチェックマークが付いていることをご確認ください。チェックマークが付いていない場合は、ホスティング会社に連絡してサポートを受けてください。

オンライン計算機: [https://www.fedex.com/ratefinder/home](https://www.fedex.com/ratefinder/home)

オンライン計算機: [http://postcalc.usps.com/](http://postcalc.usps.com/)

オンライン計算機: [https://wwwapps.ups.com/ctc/request?loc=en_US&WT.svl=PNRO_L1](https://wwwapps.ups.com/ctc/request?loc=en_US&WT.svl=PNRO_L1)

オンライン計算機: [http://auspost.com.au/apps/postage-calculator.html](http://auspost.com.au/apps/postage-calculator.html)

オンライン計算機: [http://www.canadapost.ca/cpotools/apps/far/business/findARate?execution=e1s1](http://www.canadapost.ca/cpotools/apps/far/business/findARate?execution=e1s1)

オンライン計算機: [https://www.nzpost.co.nz/tools/rate-finder](https://www.nzpost.co.nz/tools/rate-finder)

オンライン計算機: [https://eshiponline.purolator.com/ShipOnline/Estimates/Estimate.aspx?lang=e](https://eshiponline.purolator.com/ShipOnline/Estimates/Estimate.aspx?lang=e)

オンライン計算機: [http://www.royalmail.com/price-finder](http://www.royalmail.com/price-finder)

2015 年定額料金: [http://www.royalmail.com/sites/default/files/Royal-Mail-UK-and-international-parcel-and-letter-prices-30-March-2015.pdf](http://www.royalmail.com/sites/default/files/Royal-Mail-UK-and-international-parcel-and-letter-prices-30-March-2015.pdf)

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

