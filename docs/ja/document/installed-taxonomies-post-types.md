---
title: インストールされた分類法と投稿タイプ
url: https://woocommerce.com/document/installed-taxonomies-post-types/
---

ここでは、WordPressサイト内の様々なコンテンツタイプを整理・管理するための基本となる、WooCommerce特有の分類法と投稿タイプについて詳しく説明します。これらの要素を理解することは、開発者やサイト管理者がWooCommerceを効果的に拡張、カスタマイズ、管理するために不可欠です。

WordPress 環境における 2 つの主要な構成要素は、[タクソノミー](https://wordpress.org/support/article/taxonomies/) と [投稿タイプ](https://wordpress.org/support/article/post-types/) です。

- **タクソノミー** カテゴリーやタグなどの投稿タイプをグループ化したもの。
- **投稿タイプ** 投稿タイプにより、WordPressはコンテンツタイプを区別します。例えば、WordPressではデフォルトで「投稿」「ページ」「メディア」など、異なる投稿タイプが用意されています。

WooCommerce は、いくつかの異なる投稿タイプと、それらの投稿タイプをグループ化するためのいくつかの分類法を作成します。

WooCommerce は次の投稿タイプと分類をインストールします。最初のレベルは投稿タイプで、2 番目のレベルは最上位の投稿タイプの分類です。

- 商品: product
- 商品カテゴリ: `product_cat`
- 商品タグ: `product_tag`
- 商品バリエーション: `product_variation` (UIからは非表示)
- 商品の表示設定: `product_visibility`
  
- ショップ注文（レガシー）: shop_order
- 注文ステータス: `shop_order_status`
- 注文返金: `shop_order_refund`
  
- ショップクーポン: `shop_coupon`
- ショップウェブフック: `shop_webhook`

WooCommerce は既存の [WordPress テーブル](https://codex.wordpress.org/Database_Description) を使用していくつかの情報を保存します。

- `wp_options` は、ストアの設定やストアに関する情報（ストアの住所、販売または発送先の国、**WooCommerce > 設定 > 一般** から設定するその他の情報など）を保存するために使用されます。
- `wp_posts` と `wp_postmeta` には、商品、クーポン、配送クラスに関する情報が含まれます。
- `wp_terms、wp_termmeta、wp_term_taxonomy、wp_term_relationships` は、商品の [タグ、カテゴリ、属性](https://woocommerce.com/document/managing-product-taxonomies/) や [配送クラス](https://woocommerce.com/document/product-shipping-classes/)、[税クラス](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/) などのタクソノミーを保存するために使用されます。
- `wp_commentmeta` は [製品レビュー](https://woocommerce.com/document/product-reviews/) を保存します。
- `wp_users` は、ユーザー名、メールアドレス、割り当てられたユーザーID番号などの顧客情報を保存します。
- `wp_usermeta` は、名前、配送先住所、請求先住所などの追加の顧客情報を保存します。

上記に加えて、WooCommerce は追加情報を保存するカスタム テーブルもいくつか作成します。

- `wp_woocommerce_payment_tokens` は、決済ゲートウェイで使用される決済トークンを保存します。この表示形式は、サイトで使用している決済ゲートウェイによって異なります。
- `wp_woocommerce_payment_tokenmeta` は、カード番号の下4桁、カードの種類、有効期限など、顧客の支払いに関する追加情報を表示します。
- `wp_woocommerce_sessions` は、サイト訪問者のアクティブなカートセッションを確認できます。
- `wp_woocommerce_shipping_zones`、`wp_woocommerce_shipping_zone_methods`、`wp_woocommerce_shipping_zone_locations` は、設定されている [配送ゾーン](https://woocommerce.com/document/setting-up-shipping-zones/)、各ゾーンの所在地、および各ゾーンで利用可能な配送方法を一覧表示します。
- `wp_woocommerce_tax_rates` と `wp_woocommerce_tax_rate_locations` は、設定されている [税率](https://woocommerce.com/document/setting-up-taxes-in-woocommerce/#setting-up-tax-rates) と、それらが設定されている地域の概要を提供します。
- `wp_woocommerce_api_keys` は、保存されている [REST API](https://woocommerce.com/document/woocommerce-rest-api/) キーを確認できます。
- `wp_woocommerce_attribute_taxonomies` は、WooCommerce サイトに保存されているすべての属性の概要を提供します。
- `wp_woocommerce_downloadable_product_permissions` は、どの顧客がどの [ダウンロード可能な製品](https://woocommerce.com/document/managing-products/virtual-downloadable/) のダウンロード権限を持っているかの記録を保存します。
- `wp_woocommerce_log` は WooCommerce からのログとイベント データを保存します。

2023年10月にリリースされたWooCommerce 8.2以降、[高性能注文ストレージ（HPOS）](https://woocommerce.com/document/high-performance-order-storage/#background)は正式に**安定**としてフラグ付けされ、**新規インストール**ではデフォルトで有効になっています。HPOSを使用して立ち上げたショップでは、`shop_order`投稿タイプを使用しません。注文は`_posts`テーブルに保存されないためです。ストアに最初に8.2未満のWooCommerceバージョンをインストールした場合、下位互換性と、よりパフォーマンスの高いHPOSへの移行については、[HPOSドキュメント](https://woocommerce.com/document/high-performance-order-storage/#how-to-enable-high-performance-order-storage)で読むことができます。

HPOSは、注文、注文先住所、専用インデックスなどのデータ専用のテーブルを導入します。これにより、読み取り/書き込み操作と、使用されるテーブルが削減されます。この機能により、あらゆる形態や規模のeコマースストアが**最大限のポテンシャルを発揮**できるようになります。

HPOS は、注文データを `_posts` テーブルと `_postmeta` テーブルに保存する代わりに、次の 4 つの専用注文テーブルに保存します。

- `_wc_orders`
- `_wc_order_addresses`
- `_wc_order_operational_data`
- `_wc_orders_meta`

**開発者の皆様へ:**HPOSで使用されるスキーマの詳細については、[HPOSデータベーススキーマ](https://developer.woocommerce.com/2022/09/15/high-performance-order-storage-database-schema/) の詳細を説明した開発者ブログ記事をご覧ください。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

