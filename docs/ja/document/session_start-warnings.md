---
title: session_start 警告
url: https://woocommerce.com/document/session_start-warnings/
---

サイトのヘッダーに次のようなエラーが表示される場合:

```
Warning: session_start() [function.session-start]: open(xxx) failed: Permission denied (13) in xxx/wp-content/plugins/woocommerce/woocommerce.php on line 80
```

あなたのサーバーに責任があります。

PHPセッションが正しく設定されていないか、セッションディレクトリ（通常は/tmp）への書き込み権限がない可能性があります。この問題を解決するには、ホスティングプロバイダーにお問い合わせください。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

