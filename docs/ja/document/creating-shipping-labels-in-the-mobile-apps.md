---
title: モバイルアプリで配送ラベルを作成する
url: https://woocommerce.com/document/creating-shipping-labels-in-the-mobile-apps/
---

WooCommerceモバイルアプリは、[WooCommerce Shipping & Tax](https://woocommerce.com/document/woocommerce-shipping-and-tax)または[WooCommerce Shipping](https://woocommerce.com/products/shipping/)拡張機能をインストールしたストアの配送ラベルの購入と印刷をサポートしています。このガイドでは、モバイルデバイスから直接配送ラベルを購入して印刷するための手順を段階的に説明します。

ストアに WooCommerce Shipping & Tax 拡張機能をインストールする方法については、[インストール ガイド](https://woocommerce.com/document/woocommerce-shipping-and-tax/#section-2) をご覧ください。

1. 開始するには、**注文**タブに移動し、処理する注文を選択し、**配送ラベルを作成**を選択します。ボタンが見つからない場合は、[トラブルシューティングセクション](https://woocommerce.com/document/creating-shipping-labels-in-the-mobile-apps/#troubleshooting)で詳細をご確認ください。

2. **発送元** に店舗の住所を入力してください。海外への配送の場合は、電話番号が必要になります。

3. **発送先** に配送先の住所を入力します。**完了** をタップして住所を確認します。

住所が確認できない場合は、入力された住所が正しいことを再度ご確認いただくか、お客様に確認を依頼してください。画面下部の「**入力した住所を使用**」をタップすると、住所入力を続行できます。

4. **パッケージの詳細** を選択して、パッケージの梱包と重量を更新します。必要に応じて商品を別のパッケージに移動し、それぞれの梱包を選択します。

また、[**選択したパッケージ**] > [**新しいパッケージを作成**] を選択して、新しいカスタム パッケージを追加したり、運送業者が提供する箱や封筒のリストから選択したりすることもできます。

5. 海外への発送の場合は、**税関**の情報を確認または更新します。

6. 荷物の**運送業者と料金**を選択し、署名が必要かどうかを選択します。

7. **お支払い方法**を確認するか、新しいクレジットカードを追加します。また、下部のスイッチを切り替えることで、ラベル購入の領収書をメールで受け取るかどうかを選択することもできます。

8. 購入情報を確認し、注文を完了としてマークし、顧客に通知するかどうかを選択します。下部のスイッチを切り替えます。「**購入ラベル**」ボタンをタップして続行します。

購入が完了すると、**配送ラベルを印刷**画面が表示されます。ラベルを印刷するか、後で印刷するために保存するかを選択できます。

iOSでは、印刷機能はAirPrintで処理されます。iPhoneおよびiPadからの印刷方法の詳細については、[Appleのユーザーガイド](https://support.apple.com/ja-jp/guide/iphone/iph92628b8f/ios)をご覧ください。

Android端末からの印刷方法の詳細については、[Googleのサポートページ](https://support.google.com/android/answer/10177839)をご確認ください。

ラベルに別途税関申告書が付属している場合は、ラベルを印刷した後、申告書を印刷するための別の画面に移動します。

ご購入いただいたラベルは、ご注文の詳細ページからもご確認いただけます。各ラベルの詳細を確認したり、再印刷したり、必要に応じて払い戻しを申請したりできます。ラベルに別途税関申告書が付属している場合は、こちらで印刷することもできます。

以下の条件に該当する場合、「配送ラベルを作成」​​ボタンが表示されます。

- ストアが米国（プエルトリコ、バージン諸島、その他の米国領土を含む）にあること
- ストアの通貨が米ドルであること
- 注文に含まれる少なくとも1つの商品が、WooCommerce の基準で「配送が必要」と判断されていること（通常は非仮想商品を指します）

配送ラベルの発送元と配送先の住所を編集する際に、このエラーが発生する場合があります。これは、USPSで住所を確認できなかったことを意味します。住所が誤って入力されているか、郵便局によって「配達可能」とみなされていない可能性があります。

[USPS郵便番号検索ツール](https://tools.usps.com/go/ZipLookupAction) を使って住所をご確認ください。住所が認識されない場合は、お客様にご連絡いただくことをおすすめします。

ツールが住所を認識した場合、WooCommerce Shipping に問題がある可能性があります。該当する住所情報を添えて[チケットを作成](https://woocommerce.com/my-account/create-a-ticket/?ticket-area%3Dwoocommerce-extensions%26ticket-product%3Dwoocommerce-services-extension)していただき、調査いたします。

配送料が計算されない原因はいくつかありますが、最も一般的な原因は荷物のサイズと重量です。選択した荷物と入力した重量が正しいことをご確認ください。

USPS APIサービスに問題がある可能性もあります。ほとんどの問題は、WooCommerce > ステータス > WooCommerce Shipping & Tax のデバッグログを確認することで診断できます。

その他の問題については、[WooCommerce 配送のトラブルシューティング](https://woocommerce.com/document/woocommerce-shipping-and-tax/woocommerce-shipping/#section-11)および[よくある質問](https://woocommerce.com/document/woocommerce-shipping-and-tax/woocommerce-shipping/#section-20)をご覧ください。

Jetpackプラグインを使用してアプリをサイトに接続している場合は、Jetpack接続がアクティブで正常に動作していることを確認してください。[既知の問題](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)を確認するか、[サイトの再接続](https://jetpack.com/support/reconnecting-reinstalling-jetpack/)をお試しください。

それでも問題が解決しない場合は、アプリ内から「メニュー」>「設定」>「ヘルプとサポート」>「サポートに問い合わせ」にアクセスし、お問い合わせフォームにご記入の上、サポート チームにお問い合わせください。

