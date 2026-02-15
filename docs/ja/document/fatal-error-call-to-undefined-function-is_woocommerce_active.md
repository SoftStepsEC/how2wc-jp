---
title: 致命的なエラー: 未定義の関数 is_woocommerce_active() の呼び出し
url: https://woocommerce.com/document/fatal-error-call-to-undefined-function-is_woocommerce_active/
---

現在、次のエラーが発生する原因として 2 つの可能性が考えられます。

```
Fatal error: Call to undefined function is_woocommerce_active()
```

まず、[WooCommerce.com アカウントダッシュボード](https://woocommerce.com/my-account/my-subscriptions/) の *サブスクリプション* ページを確認し、すべての拡張機能（[WooSlider](https://woocommerce.com/document/wooslider-woocommerce-product-slideshow/) がインストールされている場合はそれも含む）が最新かどうかを確認してください。キーを有効化している場合は、自動更新通知が届きます。

キーをアクティブ化しておらず、**WooCommerce 2.0.5 以降** を使用している場合は、WP 管理ダッシュボードの *WooCommerce > ステータス* で拡張機能のアップデートが利用可能かどうかを確認してください。

**2.0.5 より前のバージョンの WooCommerce を使用している場合は、[WooCommerce.com アカウント ダッシュボード](https://woocommerce.com/my-account/downloads/) の *ダウンロード* ページを確認し、拡張機能を手動で最新バージョンに更新する必要があります。

拡張機能を手動で更新するには:

1. ダウンロードしたファイルを解凍し、[ファイル転送プロトコル](https://developer.wordpress.org/advanced-administration/upgrade/ftp/) (FTP) 経由でサイトにアップロードします。
2. 既存のファイルを上書きします。拡張機能を無効化したり、ファイルを削除したりする必要はありません。

**注意**: キーをアクティブ化しない限り、WP Admin 経由で WooCommerce.com Marketplace 拡張機能を手動で更新することはできません。FTP 経由で更新する必要があります。

一部のサードパーティ製テーマでは、このエラーが発生することが確認されています。マーケットプレイスから入手した拡張機能がすべて最新の状態であれば、デフォルトのテーマ（[Twenty Twenty-F​​ive](https://wordpress.org/documentation/article/twenty-twenty-five/)など）に切り替えて、拡張機能を再度有効化してください。有効化が完了したら、元のテーマに戻すことができます。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

