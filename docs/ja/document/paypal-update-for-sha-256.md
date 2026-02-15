---
title: Paypal の SHA-256 アップデート
url: https://woocommerce.com/document/paypal-update-for-sha-256/
---

この文書は、PayPalから「即時対応が必要です: PayPalサービスのアップグレード」という件名のメールを受け取った方を対象としています。

PayPalはwww.paypal.comの証明書をSHA-256にアップグレードします。このエンドポイントは、インスタント・ペイメント・ノニケーション（IPN）製品を利用する加盟店にも使用されます。

WooCommerce PayPal 標準ゲートウェイ自体に変更は必要ありません。ただし、ホスティングプロバイダーが新しい証明書をサポートしていることを確認してください。

ホストが SHA-256 をサポートしていない場合、顧客は引き続き支払いを行うことができますが、PayPal IPN は手動による介入なしに注文を「保留中」から「処理中」に更新することはできません。

PayPal SandboxはすでにSHA-256にアップデートされています。PayPal Sandboxを使用して注文を行うことで、ご自身のサイトをテストできます。また、[こちらのツール](https://gist.github.com/mikejolley/0941e0882efcad64ea40)を使用すると、PayPalが本番環境で変更を行った後も、PayPal IPNが引き続きサイトで機能するかどうかを確認できます。

ツールを使用するには、右下にある「ZIPをダウンロード」ボタンをクリックしてください。

他のプラグインと同じようにインストールしてください。インストールしたら、リンクをクリックするだけです。

成功または失敗のメッセージが表示されます

チェックが失敗した場合は、ホストに連絡する必要があります。これは WooCommerce または WordPress の問題ではありません。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

