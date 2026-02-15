---
title: 注文完了メールにダウンロードリンクが含まれていない
url: https://woocommerce.com/document/completed-order-email-doesnt-contain-download-links/
---

一部のWooCommerceインストールでは、次のような問題が発生する場合があります。顧客がダウンロード可能な商品を購入した場合、**注文完了メール**に、購入した商品をダウンロードするための**ダウンロードリンク**が含まれていません。**この場合のメールは以下のようになります。

次のように見えるはずです:

これは、**wp_woocommerce_downloadable_product_permissions** という SQL テーブルがデータベースに存在しないために発生します。

WooCommerce を有効化すると、データベースにいくつかの新しい SQL テーブルが追加されます。すべてのテーブルのリストは [こちら](https://woocommerce.com/document/installed-database-tables/) でご確認いただけます。ただし、WordPress SQL テーブルのプレフィックスが長すぎる場合、このプロセスが失敗することがあります。**テーブル名は 64 文字を超えることはできません**。

以下の表は、データベース内の各識別子の最大長を示しています。表の最大長は64文字です。

| 識別子 | 最大長 (文字数) |
| --- | --- |
| データベース | 64 |
| テーブル | 64 |
| 列 | 64 |
| インデックス | 64 |
| 制約 | 64 |
| ストアドプログラム | 64 |
| ビュー | 64 |
| エイリアス | 256 |
| 複合文ラベル | 16 |

WordPress SQL テーブル プレフィックスは WordPress のインストール中に定義され、**wp-config.php** というファイルに保存されます。

この問題を解決するには、WordPress SQL テーブルのプレフィックスの名前を変更するという唯一の解決策があります。

これは、[WordPress.org プラグイン ディレクトリ](https://wordpress.org/plugins/search/DB+Prefix/) のプラグインを使用して実行できます。

または、手動で行うこともできます。その場合は、phpMyAdminなどのツールを使用してすべてのテーブル名を変更し、テーブルのプレフィックスを短くして、**wp-config.php** のプレフィックスの値を更新する必要があります。これを完了したら、WooCommerceを無効化してから再度有効化してください。データが失われることはありませんのでご安心ください。WooCommerceを再度有効化すると、不足しているSQLテーブルが強制的に作成されるはずです。

この方法がよくわからない場合は、WordPress データベースのプレフィックスを変更する方法に関するガイドを検索してください。

**このような操作を行う前に、データベースとサイトのバックアップを作成してください。**

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

