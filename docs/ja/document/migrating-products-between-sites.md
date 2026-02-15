---
title: サイト間での製品の移行
url: https://woocommerce.com/document/migrating-products-between-sites/
---

データポータビリティは、WooCommerceやWordPressのようなプラットフォームの根本的な利点です。WooCommerceは、販売者が自社データを完全に所有し、管理することを可能にします。これにより、必要に応じて異なるシステム間でデータを自由に転送・活用できるようになります。このドキュメントでは、WooCommerce製品のエクスポートと移行に関するいくつかのオプションについて説明します。

WooCommerce 製品は「投稿」の一種として保存されるため、WordPress の投稿を移行するのと同じ方法でサイト間で製品を移行できます。

商品はサイトのデータベース内の `_posts` テーブルに保存され、商品メタデータは `_postmeta` テーブルに保存されます。また、用語や[組織タクソノミー](https://woocommerce.com/document/managing-product-taxonomies/)といった要素との関連性も存在します。これらは投稿と同じ構造に従っているためです。WordPressのデータスキーマに関する詳細は、[データベースの説明](https://codex.wordpress.org/Database_Description)をご覧ください。

製品データのインポート/エクスポート、またはサイト全体とデータベースの移行を支援する優れたオプションがいくつかあります。

製品データを含む XML ファイルをエクスポートするには:

1. **[ツール] > [エクスポート]** に移動し、移行するコンテンツを選択します。

1. **「エクスポートファイルをダウンロード」**ボタンをクリックします。XMLファイルがコンピューターにダウンロードされます。
2. コンテンツの移行先サイトに移動し、**「ツール」>「インポート」**に移動します。
3. **WordPress**を選択し、指示に従います。

詳細については、[WordPress.org のコンテンツのインポートに関する記事](http://codex.wordpress.org/Importing_Content#WordPress) をご覧ください。

商品データをインポート、エクスポート、変更、統合するために、WooCommerce には主要な商品タイプをはじめ、多くの商品タイプに対応するCSVインポーターとエクスポーターが組み込まれています。組み込みの[商品CSVインポーターとエクスポーター](https://woocommerce.com/document/product-csv-importer-exporter/)に関する詳細なドキュメントをご覧ください。

高度な商品データをお持ちの方、拡張機能から追加の商品タイプを追加したい方、あるいは変動する商品を統合するためのより効率的なワークフローが必要な方は、プレミアム拡張機能[商品CSVインポートスイート](https://woocommerce.com/products/product-csv-import-suite/)をご利用ください。プレミアム拡張機能には、WooCommerceストア上のすべての商品をワンクリックで削除できるツールなど、便利な追加機能が多数含まれています。

これらのツールは両方とも CSV データで動作し、データの移行や、CSV からの初回の製品インポートに使用できます。

## Jetpack VaultPress Backup で（すべての）データを移行する

[Jetpack VaultPress Backup](https://woocommerce.com/products/jetpack-backup/) は、セルフホスト型 WordPress サイト向けのサブスクリプション型のセキュリティおよびバックアップサービスです。Jetpack VaultPress Backup は WooCommerce のライブバックアップをサポートしており、WordPress ウェブサイトを別のホストに移行する際に使用できます。Jetpack VaultPress Backup を使用すると、以下のことが可能になります。

- すべての注文と顧客データを最新の状態に保ちながら、サイトを過去の状態に復元します
- サイト全体を新しいホストまたはサーバーにクローンします
- 顧客データを保護し、GDPRに準拠します
- カスタムWooCommerceテーブルをバックアップおよび復元します

詳細については、[Jetpack バックアップ: 新しいホストへの移行](https://jetpack.com/support/backup/cloning/) をご覧ください。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

