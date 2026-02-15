---
title: バーコードとQRコードスキャナー
url: https://woocommerce.com/document/barcode-and-qr-code-scanner/
---

**POS (Point of Sale) モードで物理スキャナーを使用したいですか?** [こちらのドキュメントをご覧ください。](https://woocommerce.com/document/point-of-sale-mode-barcode-scanning/)

WooCommerce モバイル アプリは、Android と iOS の両方のプラットフォームで最も広く使用されているバーコード形式をサポートしています。

この強力なツールを使えば、**注文**画面から直接[新規注文を作成](https://woocommerce.com/document/creating-orders-on-the-mobile-app/#section-3)できるため、ワークフローが効率化されます。注文作成プロセス中に注文に商品を追加したり、商品画面から商品を素早く見つけたりできます。

**注:**モバイルアプリのバーコードスキャナーは、商品の**在庫**タブの**SKU**フィールドまたは**GTIN、UPC、EAN、ISBN**フィールドのいずれかに追加されたコードに対応しています。**GTIN、UPC、EAN、ISBN**フィールドは新しいフィールドであり、特に標準的な小売バーコードを使用している場合は、すべてのストアにとってより適切な選択肢です。新しいフィールドを使用する場合は、SKUを人間が判読できる識別子として使用できます。

バーコードは商品とバリエーションの両方に設定できます。GTIN、UPC、EAN、ISBNなど、チェックデジットや国コードを使用するバーコード形式の場合は、設定するバーコードにそれらを含めてください。

製品とバリエーションの両方のバーコードは、手動で入力するか、アプリ内でスキャンして追加できます。

バーコードは、**商品**タブの*在庫*セクションで設定できます。バリエーションの場合は、各バリエーションの*在庫*セクションを個別に開くことができます。

Android デバイスは、[ML Kit](https://developers.google.com/ml-kit/vision/barcode-scanning/android) を使用してバーコードを認識およびデコードします。

- QRコード
- アズテックコード
- データマトリックス
- PDF417
- UPC-A
- UPC-E
- EAN-8
- EAN-13
- Code 39
- Code 93
- Code 128
- インターリーブド2/5 (ITF)
- Codabar

- 1文字のみの1次元バーコード。
- 6文字未満のITF形式のバーコード。
- FNC2、FNC3、またはFNC4でエンコードされたバーコード。
- 拡張チャネル解釈（ECI）モードで生成されたQRコード。

iOS デバイスは、[Vision フレームワーク](https://developer.apple.com/documentation/vision/) を使用してバーコードを認識およびデコードします。

- Aztec
- Codabar
- Code 39
- チェックサム付き Code 39
- Code 39 Full ASCII
- チェックサム付き Code 39 Full ASCII
- Code 93
- Code 93i
- Code 128
- データマトリックス
- EAN-8
- EAN-13
- GS1 DataBar
- GS1 DataBar Expanded
- GS1 DataBar Limited
- Interleaved 2 of 5 (I2of5)
- Interleaved 2 of 5 (I2of5) チェックサム付き
- ITF-14
- MicroPDF417
- MicroQR
- Modified Plessey (MSI Plessey)
- PDF417
- QR
- UPC-E

残念ながら、Apple の公式ドキュメントには、サポートされていないバーコードの種類に関する具体的な情報は記載されていません。

Jetpackプラグインを使用してモバイルアプリをサイトに接続している場合は、Jetpack接続がアクティブで正常に機能していることを確認してください。[よくある問題を確認する](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)、または[サイトを再接続する](https://jetpack.com/support/reconnecting-reinstalling-jetpack/)を行ってください。

それでも問題が解決しない場合は、*メニュー > 設定 > ヘルプとサポート > サポートに問い合わせ* して、アプリ内からサポートにお問い合わせください。

