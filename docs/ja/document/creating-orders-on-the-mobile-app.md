---
title: モバイルアプリで注文を作成または編集する
url: https://woocommerce.com/document/creating-orders-on-the-mobile-app/
---

最新バージョンのモバイル アプリ (バージョン `8.9.0` 以上) では、注文を作成できます。

**注:**最高のエクスペリエンスを得るには、[ストアを WooCommerce の最新バージョンに更新することをお勧めします。](https://woocommerce.com/document/how-to-update-woocommerce/)

モバイル アプリは現在以下をサポートしています:

- [新規注文の作成](https://woocommerce.com/document/creating-orders-on-the-mobile-app/#create-a-new-order)
- [商品とバリエーションの追加](https://woocommerce.com/document/creating-orders-on-the-mobile-app/#adding-products-product-variations)
- [商品の削除](https://woocommerce.com/document/creating-orders-on-the-mobile-app/#removing-a-product)
- [カスタム配送方法の設定](https://woocommerce.com/document/creating-orders-on-the-mobile-app/#setting-a-custom-shipping-method)
- [カスタム配送方法の削除](https://woocommerce.com/document/creating-orders-on-the-mobile-app/#deleting-the-custom-shipping-method)
- [カスタム金額の設定](https://woocommerce.com/document/creating-orders-on-the-mobile-app/#setting-a-custom-order-fee)
- [カスタム金額の削除](https://woocommerce.com/document/creating-orders-on-the-mobile-app/#deleting-the-custom-order-fee)
- [顧客情報（請求先住所と配送先住所）の設定](https://woocommerce.com/document/creating-orders-on-the-mobile-app/#setting-customer-details)
- [顧客提供メモの設定](https://woocommerce.com/document/creating-orders-on-the-mobile-app/#setting-customer-provided-notes)
- [新規注文の完了]注文の作成](https://woocommerce.com/document/creating-orders-on-the-mobile-app/#completing-the-new-order-creation)
- [注文の編集](https://woocommerce.com/document/creating-orders-on-the-mobile-app/#editing-the-order)
- [注文ステータスの設定](https://woocommerce.com/document/creating-orders-on-the-mobile-app/#setting-the-order-status) (編集のみ)

注文を作成するには、次の手順に従ってください。

1. 「注文」タブの右上にある**+**アイコンをタップします。
2. 「**新規注文**」画面が表示されます。

- **商品**セクションの**+商品を追加**ボタンをタップします。
- 追加したい商品を検索して選択します。
- **商品を追加**をタップします。
- 商品カードを展開し、必要に応じて**数量ステッパーまたはテキストボックス**を使用して数量を調整します。

バーコードスキャンは、**Android** ではアプリバージョン `13.8` 以降、iOS ではバージョン `14.1` 以降でご利用いただけます。この機能を使用すると、デバイスのカメラで商品のバーコードを素早くスキャンし、注文に追加できます。なお、この機能はストアの商品SKUに一致するバーコード番号のみに対応しています。

**注:** モバイルアプリのバーコードスキャナーは現在、在庫タブの**SKU**フィールドに追加されたコードでのみ動作します。WooCommerceコアの新しい**GTIN、UPC、EAN、またはISBN**フィールドは、まだモバイルアプリに統合されていません。

開始するには、[注文] タブの上部にある **バーコード** アイコンをタップし、製品のバーコードをスキャンして新しい注文に追加します。

または、[新規注文] 画面で、[**+ 商品を追加**] の横にある [**バーコード**] アイコンをタップして商品をスキャンし、注文に追加することもできます。

- 削除したい商品をタップしてカードを展開します。
- **注文から商品を削除** ボタンをタップします。

- **お支払い**セクションで、「+ **送料を追加**」ボタンをタップします。
- 表示されたフォームに、請求したい金額と、必要に応じて送料の名前を入力します。
- **完了**ボタンをタップして変更を保存します。
- 展開矢印をタップすると、送料を含む合計金額の詳細が表示されます。

- 合計パネルを展開した状態で、**配送** の鉛筆ボタンをタップします。
- **注文から配送を削除** ボタンをタップします。

- **お支払い**セクションで、+ **カスタム金額を追加**ボタンをタップします。
- カスタム金額の種類、注文の割合、または特定の金額を選択します。
- 表示されたフォームに、希望する手数料を入力します。
- 必要に応じて名前を追加します。
- **カスタム金額を追加**ボタンをタップして変更を保存します。

注: 割引を適用する代わりに、負の値を入力することもできます。

- **カスタム金額** セクションで、削除したい金額の横にある **鉛筆** ボタンをタップします。
- **カスタム金額を削除** ボタンをタップします。

- + **顧客情報を追加** ボタンをタップします。
- 表示されたフォームに、顧客に必要な情報をすべて入力します。すべて任意ですが、少なくとも1つは必須です。
- 別の配送先住所を追加する場合は、下部のスイッチを切り替えて別のフォームを有効にすることができます。
- **完了** ボタンをタップして変更を保存します。

- **顧客メモ** セクションで、+ **メモを追加** ボタンをタップします。
- 表示されたフォームに、顧客メモとして送信するテキストを入力します。
- **完了** ボタンをタップして変更を確定します。

- ご注文が完了したら、**「お支払いを受け取る」** ボタンをタップしてすぐに店頭でお支払いいただくか、右上にある **「作成」** ボタンを使用してお支払いをお受けせずに注文を作成できます。
- お支払いをお受けいただく場合は、サイトとお住まいの地域で設定されているお支払い方法に応じて、現金、スキャン決済、カード決済などのお支払い方法を選択できます。
- ご注文の作成後、注文の詳細画面にリダイレクトされ、[注文を履行](https://woocommerce.com/document/woocommerce-ios/#orders) するために必要な操作を行うことができます。
- 編集も可能です

最新のモバイル アプリ バージョン (`9.7.0` 以降) では、注文を編集できます。

- 注文の詳細画面で、ナビゲーションバーの右上にある「**編集**」ボタンをタップします。
- 必要な項目を編集します。変更は注文にすぐに保存されます。
- 「**完了**」をタップして編集フォームを閉じます。

- 注文編集画面の最初のセクションにある**編集**ボタンをタップして、注文ステータスを更新します。
- 利用可能なすべてのステータスが表示された画面が表示され、そこから選択できます。
- いずれかのステータスを選択すると、注文ステータスがすぐに更新されます。

タブレットでは、スペースに余裕がある場合は、関連する画面を並べて表示します。これにより、注文の作成と編集がより迅速に行えます。すべての画面の操作方法は同じですが、一度に多くの画面を表示できます。画面例を以下に示します。

Jetpackプラグインを使用してアプリをサイトに接続している場合は、Jetpack接続がアクティブで正常に動作していることを確認してください。[既知の問題](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)を確認するか、[サイトの再接続](https://jetpack.com/support/reconnecting-reinstalling-jetpack/)をお試しください。

それでも問題が解決しない場合は、アプリ内から「メニュー」>「設定」>「ヘルプとサポート」>「サポートに問い合わせ」にアクセスし、お問い合わせフォームにご記入の上、サポート チームにお問い合わせください。

