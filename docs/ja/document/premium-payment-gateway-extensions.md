---
title: どの支払い方法が私に適していますか?
url: https://woocommerce.com/document/premium-payment-gateway-extensions/
---

WooCommerceには、顧客に支払いオプションを提供するための幅広い[決済ゲートウェイオプション](https://woocommerce.com/product-category/woocommerce-extensions/payment-gateways)が用意されています。[WooPayments](https://woocommerce.com/document/premium-payment-gateway-extensions/#woocommerce-payments)（一部の地域で利用可能）を含む、支払い方法の選択方法については、以下をお読みください。

このページでは以下の内容を学びます:

- 決済ゲートウェイとは何か。
- 決済ゲートウェイを選ぶ際に考慮すべき点。
- 必要な決済ゲートウェイの数。
- 無​​料ゲートウェイと有料ゲートウェイの見分け方。
- 決済ゲートウェイにおけるプライバシーに関する考慮事項。

WooCommerce の用語で言う決済ゲートウェイとは、WooCommerce が顧客を決済プロセッサに接続し、商品やサービスの支払いができるようにする WordPress プラグインです。

- すべての決済代行業者には、通常「マーチャントアカウント」と呼ばれるアカウントが必要です。
- 各決済代行業者には、利用規約と手数料（プラグイン本体の料金とは別）があります。アカウント要件、利用規約、手数料についてご質問がある場合は、決済代行業者に直接お問い合わせください。
- 一部の決済代行業者では、アカウントの種類、取引の種類、リダイレクト方法などに応じて複数のオプションが用意されています。

決済ゲートウェイを選択して設定する際には、以下の点を考慮することが重要です。

- **費用**
- **所在地**
- **セキュリティ**
- [Woo サブスクリプションのサポート](https://woocommerce.com/document/premium-payment-gateway-extensions/#support-for-subscriptions) [Woo サブスクリプション](https://woocommerce.com/products/woocommerce-subscriptions/) (該当する場合)

初期費用と継続費用は決済処理業者ごとに異なり、次のようなものが含まれます。

- 決済ゲートウェイ拡張機能/プラグインが無料ではない場合の費用。
- 決済ゲートウェイ会社/決済代行会社が請求する登録料。
- 月額または年額のサブスクリプション料金。
- 取引手数料。

店舗の所在地と通貨は重要な要素です。決済ゲートウェイ会社／決済処理会社は、特定の国に拠点を置く加盟店にのみサービスを提供している場合があります。例えば、米ドルのみに対応し、米国の店舗オーナーのみを受け付けている場合、カナダやヨーロッパの店舗オーナーは利用できません。

ただし、世界中のお客様がゲートウェイを利用してチェックアウトと支払いを行うことができます。詳しくは、[海外で販売する際の支払いに関する考慮事項](https://woocommerce.com/2016/09/international-payment-tips/)および[決済ゲートウェイの選び方](https://woocommerce.com/posts/how-to-choose-payment-gateway/)をご覧ください。

- **リダイレクト**: お客様は支払い処理のために決済ゲートウェイサイトに転送され、その後、チェックアウトを完了するためにお客様のサイトにリダイレクトされます。
- **直接**: お客様はお客様のサイトで直接購入と支払いを行い、[PCIコンプライアンス](https://woocommerce.com/document/pci-dss-compliance-and-woocommerce/)の一環として[SSL証明書](https://woocommerce.com/document/ssl-and-https/)が必要となります。

支払いを受け入れるショップのオーナーには、電子メール アドレス、配送先住所、請求情報などの顧客の機密情報を保護する責任があります。

これを実現するために、ほとんどの決済ゲートウェイではSSL証明書が必要です。SSL証明書は、サイトと顧客、そしてサイトと決済代行業者間の通信を暗号化します。詳しくは[SSLに関するよくある質問](https://woocommerce.com/document/ssl-faq/)をご覧ください。

サイトを安全に保護するためのその他の対策は、PCIデータセキュリティ基準（PCI-DSS）に準拠しています。PCI-DSSは、クレジットカード情報を保存、処理、または送信するすべての事業者に適用されます。詳しくは、[PCI-DSS準拠とWooCommerce](https://woocommerce.com/document/pci-dss-compliance-and-woocommerce/)をご覧ください。

決済ゲートウェイのセキュリティについて詳しく知りたい場合は、[WooCommerce サイトとデータ セキュリティに関する FAQ](https://woocommerce.com/document/woocommerce-security-faq/#section-5) をご覧ください。

[Woo Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/)拡張機能（別途購入）などを使用して、サイトで定期支払いを販売する場合は、手動または自動の定期支払いをサポートする決済ゲートウェイを選択する必要があります。詳しくは、[サブスクリプションの支払い方法とゲートウェイ](https://woocommerce.com/document/subscriptions/payment-gateways/)をご覧ください。

WooCommerceのデフォルト設定である[直接銀行振込](https://woocommerce.com/document/bacs/)のような手動決済ゲートウェイを使用する場合でも、サイトで支払いを受け取るには少なくとも1つの支払い方法が必要です。厳選された支払いオプションを提供することで、顧客がいつでもチェックアウトして支払いを完了できる可能性が高まります。

多くの決済ゲートウェイでは、標準のクレジットカードフィールドに加え、Apple Pay や Google Pay でチェックアウトできる「エクスプレス」決済ボタンも提供しています。

ただし、決済ゲートウェイや決済手段を多すぎると、顧客が選択肢に圧倒され、サイト管理が複雑になる可能性があります。ショップの要件、ビジネスニーズ、顧客の好みに合わせて、提供する決済手段を慎重に選定してください。

[WooCommerce のセットアップ](https://woocommerce.com/document/woocommerce-setup-wizard/#set-up-payments)を実行すると、ストアの場所に基づいて、[Core Payment Options](https://woocommerce.com/documentation/plugins/woocommerce/getting-started/sell-products/core-payment-options/)や [WooPayments](https://woocommerce.com/products/woocommerce-payments/)などのさまざまな支払いゲートウェイが提供されます。

別のものを使用したい場合は、**プレミアム** ゲートウェイを選択して購入できます。

**コア決済オプション**はWooCommerceに組み込まれた無料の決済方法で、[代金引換](https://woocommerce.com/document/cash-on-delivery/)、[小切手決済](https://woocommerce.com/document/cheque/)、[銀行振込（BACS）](https://woocommerce.com/document/bacs/)が含まれます。これらのゲートウェイ自体には、有効化費用や利用料はかかりません。

**WooCommerce.com では独自の WooPayments を提供しています**! WooPayments は無料でインストールでき、セットアップ料金や月額料金はかかりません。従量制手数料は、米国発行のカードの場合、1 取引あたりわずか 2.9% + $0.30 から始まります。[取引手数料についての詳細](https://woocommerce.com/document/woopayments/fees-and-debits/fees/)をご覧ください。WooPayments は [他の 17 か国](https://woocommerce.com/document/payments/countries/) で利用可能であり、その数は拡大しています。[WooPayments](https://woocommerce.com/payments/) の詳細については、こちらをご覧ください。また、サポートされている国にいない場合は、[お住まいの地域をお知らせください](https://woocommerce.com/payments/#request-invite)。次にどの国に対応するかがわかります。

有料決済オプションは、[プレミアム決済ゲートウェイ拡張機能](https://woocommerce.com/product-category/woocommerce-extensions/payment-gateways) を通じてご利用いただけます。これらの拡張機能をご利用いただくには、WooCommerce.com への年間サブスクリプション（サポートとアップデートの利用）に加え、決済代行業者の標準取引手数料が必要です。検索ページの左側のサイドバーでは、様々なオプションでさらに絞り込みが可能です。

ヨーロッパの顧客に販売する場合、決済ゲートウェイの選択において、欧州一般データ保護規則（GDPR）の枠組みを考慮する必要があります。GDPRとユーザーのプライバシーに関する懸念事項の詳細については、[WooCommerceとGDPR](https://woocommerce.com/gdpr/)をご覧ください。

チェックアウト時に収集される顧客情報は、決済ゲートウェイによって異なります。[BACS](https://woocommerce.com/document/bacs/)などの手動決済ゲートウェイをご利用の場合、サイトとは独立して銀行口座を確認するため、サイト側で支払い処理は行われません。StripeやPayPalなどの他の決済ゲートウェイでは、サイトから決済代行業者に情報を渡す必要があります。信頼できる決済代行業者を選択し、顧客データへの影響を考慮するのは、お客様ご自身の責任です。

- 送信される情報の内容を把握する。
- 顧客に、データの取り扱いについて通知する。
- 決済代行業者がその情報をどのように利用するかを理解する。

例えば、[WooCommerce Stripe拡張機能](https://woocommerce.com/products/stripe/)は、特定の顧客情報をStripeに送信します（詳細は[Stripe](https://stripe.com/)のドキュメントをご覧ください）。このプロセスについては、サイトのプライバシーポリシーで開示する必要があります。

選択した決済ゲートウェイには、顧客データの取り扱い方法に関する情報が記載されているはずです。決済処理業者のウェブサイトを確認し、プライバシーポリシーとGDPRについて詳しく確認してください。

決済ゲートウェイが GDPR を適用する方法の詳細については、[公式決済拡張機能を使用する際のプライバシーに関する考慮事項](https://woocommerce.com/document/privacy-payments/) を参照してください。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

