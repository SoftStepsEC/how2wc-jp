---
title: WordPressコンテンツのバックアップ
url: https://woocommerce.com/document/backup-wordpress-content/
---

WooCommerce と WordPress で運営されている各ストアには、データとコンテンツが保存される **2 つの場所** があります。

1. テーマ、プラグイン、アップロードされたコンテンツが保存される「wp-content」フォルダ。
2. 商品、注文、投稿、ページなどが整理され、保存されるデータベース。

では、コンテンツをどのように保護し、バックアップを維持すればよいのでしょうか?

最も効率的で信頼性の高い方法は、[自動バックアップ サービス](https://jetpack.com/pricing/woocommerce-backup/) を使用することです。[Jetpack VaultPress Backup](https://jetpack.com/pricing/woocommerce-backup/) をお勧めします。

Jetpack Vaultpress Backup を使用すると、次のようなメリットがあります。

- データベース、コンテンツ、メディア、プラグイン、テーマ、設定を含む**サイト全体**の自動定期バックアップ。
- WooCommerce 向けにカスタマイズされた機能：
- すべての注文と商品を最新の状態に保ちながら、サイトを過去の状態に復元できます。
- 顧客データを保護し、GDPR に準拠します。
- WooCommerce のカスタムテーブルバックアップ。
  
- サイトのすべてのアクティビティと記録された変更の完全なリスト。
- 即時復元。何か問題が発生した場合は、ワンクリックで以前のバージョンにすぐに戻すことができます。
- 24時間365日対応の専門サポートに直接アクセスできます。

サイトのコンテンツを手動でバックアップするには、2 つの手順があります。

1. ストアのWP管理ダッシュボードで、**「ツール」>「エクスポート」** に移動し、すべての**サイトコンテンツ**（投稿、ページ、コメントなど）をXMLファイルにエクスポートします。
2. **テーマと拡張機能/プラグインファイル** をバックアップするには、ファイル転送プロトコル（FTP）経由でサイトにログインし、`wp-content` **フォルダ** 内のファイルを探します。テーマをカスタマイズした場合は、テーマファイルのバックアップを作成することを**強く推奨** します。

- [WordPress のバックアップ](https://developer.wordpress.org/advanced-administration/security/backup/#Backing_Up_Your_WordPress_Site) (WordPress Codex)
- [バックアップ](https://jetpack.com/upgrade/backup/) と [セキュリティ](https://jetpack.com/features/security/) (Jetpack)

Jetpack のお客様には、[専門家による優先サポート](https://jetpack.com/features/security/expert-priority-support/) を提供しています。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

