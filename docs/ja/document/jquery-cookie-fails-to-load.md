---
title: jQuery.cookie.js/jQuery.cookie.min.js スクリプトの読み込みに失敗しました
url: https://woocommerce.com/document/jquery-cookie-fails-to-load/
---

これはサーバー設定の問題です。ホスティング会社がお客様に代わってこの問題を解決する必要があります。問題はMOD_SECURITYコアルールセットが古いことにあります。

すべてが設計通りに動作するので、これが最良の選択肢です。サポートが必要な場合は、ホスティングプロバイダーにお問い合わせください。

## オプション 2: ファイルの名前を変更して functions.php を更新する

あるいは、WooCommerce によるファイルの処理方法を変更する必要があります。変更内容は上書きされるため、WooCommerce プラグインを更新するたびにこの変更を繰り返す必要があります。

これらのファイルの名前を変更します:

```
wp-content/plugins/woocommerce/assets/js/jquery-cookie/jquery.cookie.js
wp-content/plugins/woocommerce/assets/js/jquery-cookie/jquery.cookie.min.js

to:

wp-content/plugins/woocommerce/assets/js/jquery-cookie/jquery_cookie.js
wp-content/plugins/woocommerce/assets/js/jquery-cookie/jquery_cookie.min.js
```

テーマの functions.php ファイルに次のコードを追加します。

.gist テーブル { margin-bottom: 0; }

| | add_action( 'wp_enqueue_scripts', 'custom_frontend_scripts' );function custom_frontend_scripts() {global $post, $woocommerce; |
| | | | | $suffix = defined( 'SCRIPT_DEBUG' ) && SCRIPT_DEBUG ? : '.min'; |
| | wp_deregister_script( 'jquery-cookie' ); |
| | wp_register_script( 'jquery-cookie', $woocommerce->plugin_url() . '/assets/js/jquery-cookie/jquery_cookie' . $suffix . '.js', array( 'jquery' ), '1.3.1', true ); |
| | } |

最初の 2 つのオプションが利用できない場合は、ロードされるファイルの名前を変更するプラグインを使用できます。

- **WooCommerce 2.6.14以下**をご利用の場合: [woocommerce-jquery-cookie-fix.zip](http://cld.wthms.co/1hR5y/2rLEZX6V)
- WooCommerce 3.0.0以上をご利用の場合: [woocommerce-js-cookie-fix](https://github.com/rynaldos/woocommerce-js-cookie-fix)

注: 以前に適用した修正があれば削除してください。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

