---
title: 遅いサイトのトラブルシューティング
url: https://woocommerce.com/document/troubleshooting-a-slow-site/
---

遅い WooCommerce サイトのトラブルシューティングの最初のステップは、根本原因を特定することです。

[WP Super Cache](http://wordpress.org/plugins/wp-super-cache/) などのキャッシュプラグインを使用すると、サイトのパフォーマンスを最適化できます。[Jetpack のサイトアクセラレータ](https://jetpack.com/features/design/content-delivery-network/) や [Cloudflare](https://www.cloudflare.com/) などのコンテンツ配信ネットワーク (CDN) を使用して、サイトをさらに高速化することもできます。

ただし、キャッシュプラグインは設定が間違っていると、サイトが正しく読み込まれない（または全く読み込まれない）可能性があるので注意してください。導入後は、設定を必ず再確認し、正しく動作していることを確認してください。

ご利用のホスティングプランがサイトのパフォーマンスに与える影響について、ホスティングプロバイダーにお問い合わせください。共有サーバー上の安価なホスティングプランよりも、高品質な専用ホスティングをお勧めします。[WooCommerceホスティングソリューションのおすすめはこちら](https://woocommerce.com/hosting-solutions/)。

フロントエンドのサイトパフォーマンスが遅くなる一般的な原因は画像サイズです。商品やブログの画像のファイルサイズは、サイトの読み込み速度に直接影響します。

[Jetpack Boost](https://jetpack.com/boost/) や [Smush](http://wordpress.org/plugins/wp-smushit/) などのサードパーティ製ツールを使用すると、WordPress 内で画像を最適化できます。

[WooCommerce でぼやけた画像を修正するためのガイドをご覧ください](https://woocommerce.com/document/using-the-appropriate-product-image-dimensions/)。

縮小は、コードファイルのサイズを縮小することで、サイトの読み込み速度を向上させます。HTML、CSS、JavaScriptファイルから、スペース、改行、コメントなどの不要な文字を削除しますが、機能には影響を与えません。ファイルサイズの縮小により、ダウンロードと実行時間が短縮され、ウェブサイト全体のパフォーマンスとユーザーエクスペリエンスが向上します。

サイト上のファイルを縮小するには、さまざまな[サードパーティ製プラグイン](https://wordpress.org/plugins/search/minify/)から選択できます。

[サイトの WordPress メモリ制限を増やす](https://woocommerce.com/document/increasing-the-wordpress-memory-limit/) 必要がある場合もあります。

サイトの速度低下は、拡張機能やプラグインの読み込みに関連している場合があります。

これをテストするには、すべての拡張機能とプラグインを無効化し、潜在的な原因が見つかるまで一つずつ有効化していきます。サードパーティ製の[Plugin Organizer](https://wordpress.org/plugins/plugin-organizer/)を使用して有効化の順序を制御し、ページ/投稿ごとにプラグインのオン/オフを切り替えることもできます。

テーマをテストするには、一時的にWordPressのデフォルトのテーマ（[Twenty Twenty-F​​ive](https://wordpress.org/themes/twentytwentyfive/)など）に切り替えてサイト内を移動してみてください。パフォーマンスの改善に気づいた場合、問題はテーマに関連している可能性があります。

- [Pingdom ウェブサイトスピードテスト](http://tools.pingdom.com/fpt/)
- [Google PageSpeed ツール](https://developers.google.com/speed/pagespeed/)

- [専用の簡易メール転送プロトコル (SMTP) プロバイダー経由で電子メールを送信する](https://woocommerce.com/document/email-smtp-providers/)など、不要な機能はすべて別のサーバーまたはサードパーティ サービスにオフロードします。

- [WooCommerce ストアの速度を向上させる 10 の方法](https://woocommerce.com/posts/ten-ways-to-speed-up-your-woocommerce-store/)
- [WooCommerce パフォーマンスのベストプラクティス](https://developer.woocommerce.com/docs/best-practices/performance/performance-best-practices/)
- [WordPress.org パフォーマンス最適化のヒント](https://developer.wordpress.org/advanced-administration/performance/optimization/)

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

