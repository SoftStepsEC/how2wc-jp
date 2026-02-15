---
title: WooCommerceサーバーの推奨事項
url: https://woocommerce.com/document/server-requirements/
---

WooCommerceサーバーの推奨事項は、サイトを成功させ、長く使い続けるための設定ガイドです。WordPressサイトを稼働させているサーバーが最小要件を満たしていない場合、WooCommerce自体を含む多くのプラグインが期待どおりに動作しません。WooCommerceサーバーの推奨事項と以下の追加項目をご確認ください。

WooCommerce を利用したオンラインストアを立ち上げる最初のステップは、WordPress と WooCommerce プラグインをインストールすることです。**ただし、その前にホスティング環境を確認してください。これらの要件を満たしていない場合、サイトのセキュリティとパフォーマンスが低下します。

**WooCommerce を実行するには、ホストが以下をサポートしていることをお勧めします:**

- [WordPress](https://href.li/?http://WordPress.org) の最新バージョン
- [PHP](https://href.li/?https://www.php.net/) バージョン 8.3 以上
- [MySQL](https://href.li/?https://www.mysql.com/) バージョン 8.0 以上、または [MariaDB](https://href.li/?https://mariadb.org/) バージョン 10.6 以上
- [HTTPS](https://href.li/?https://wordpress.org/news/2016/12/moving-toward-ssl/) のサポート
- WordPress の [メモリ制限](https://href.li/?https://woocommerce.com/document/increasing-the-wordpress-memory-limit/) が 256 MB 以上

WooCommerce を実行するには、最も堅牢で機能豊富なサーバーとして [Apache](https://href.li/?https://httpd.apache.org/) または [Nginx](https://href.li/?https://nginx.org/) が推奨されますが、PHP と MySQL をサポートするサーバーであればどれでも構いません。[WordPress の要件](https://href.li/?https://wordpress.org/about/requirements/) については、こちらをご覧ください。

**注:** 古いバージョンの PHP または MySQL しか使用していないレガシー環境をご利用の場合、WooCommerce は PHP 7.4 以降および MySQL バージョン 5.67 以上（または MariaDB バージョン 10.4 以上）でも動作します。ただし、これらのバージョンは公式にサポート終了となっており、サイトがセキュリティ上の脆弱性にさらされる可能性があります。

他に必要となる可能性のあるオプションとしては、次のものがあります。

- cURL または fsockopen のサポート。WooCommerce およびいくつかの連携機能（例: [PayPal IPN](https://woocommerce.com/document/paypal-standard/#section-6)）で使用されています。
- 一部の WooCommerce.com 拡張機能では SOAP サポートが必要です。
- 英語以外の言語でストアを運営している場合は、マルチバイト文字列のサポートが必要です。
- WordPress の「pretty」パーマリンクを使用する場合は、[パーマリンクの使用](https://wordpress.org/support/article/using-permalinks/#using-pretty-permalinks) に記載されている追加要件もご確認ください。
- [グローバル SQL](https://href.li/?https://dev.mysql.com/doc/refman/8.0/en/sql-mode.html) モード オプション: `ERROR_FOR_DIVISION_BY_ZERO`、`NO_ENGINE_SUBSTITUTION`、`NO_ZERO_DATE`、`NO_ZERO_IN_DATE`、`STRICT_ALL_TABLES`

WooCommerce をインストールした後、[システム ステータス ページ](https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/) を使用して、サーバー上にリストされているアイテムがあるかどうかを確認します。

WooCommerceサイトのサーバー設定を更新する前に、サイトとファイルのバックアップを作成することが重要です。サーバー環境の変更は、サイトのパフォーマンスと機能に大きな影響を与える可能性があります。

サーバー設定を変更する必要がある場合は、まずホスティングプロバイダーに連絡してください。プロバイダーが設定を更新してくれる場合もあれば、ツールを使って自分で変更する方法を案内してくれる場合もあります。

`.htaccess` ファイル内の `post_max_size`、`max_input_vars`、`max_execution_time` などの PHP 設定を手動で調整することもできます。このファイルには、ホスティングプロバイダーのファイルマネージャーまたは FileZilla などの FTP クライアントからアクセスできます。このファイルへのアクセスや変更についてサポートが必要な場合は、ホスティングプロバイダーにお問い合わせください。

WooCommerce サーバーの推奨事項を満たす新しいホストが必要ですか? [ホスティング パートナーはこちら](https://woocommerce.com/hosting-solutions/)、または [専用の WordPress Web ホストはこちら](https://wordpress.org/hosting/) でご確認ください。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

