---
title: WooCommerceのキャッシュプラグインの設定方法
url: https://woocommerce.com/document/configuring-caching-plugins/
---

<ul class="documentation_categories">
<li class="documentation_category">ベストプラクティス</li>
<li class="documentation_category">パフォーマンス</li>
</ul>
## キャッシュからページを除外する

多くの場合、キャッシュプラグインを使用している場合は、これらのページが既に除外されています。そうでない場合は、キャッシュシステムのそれぞれの設定で、以下のページをキャッシュから除外してください。

- カート
- マイアカウント
- チェックアウト

これらのページは、現在の顧客とそのカートに固有の情報を表示するため、動的に維持する必要があります。

## WooCommerceセッションをキャッシュから除外する

使用しているキャッシュシステムがデータベースキャッシュを提供している場合は、`_wc_session_` をキャッシュ対象から除外すると効果的かもしれません。これはプラグインまたはホストのキャッシュ方法によって異なりますので、各システムの具体的な手順またはドキュメントを参照してください。

## WooCommerce クッキーをキャッシュから除外する

WooCommerce の Cookie は、顧客のカート内の商品を追跡し、顧客がサイトを離れた後もカートの情報をデータベースに保存し、最近閲覧したウィジェットの動作をサポートします。以下は、WooCommerce がこれらの目的で使用する Cookie のリストです。これらの Cookie はキャッシュから除外できます。

| クッキー名 | 有効期間 | 目的 |
| --- | --- | --- |
| woocommerce_cart_hash | セッション | WooCommerce がカートの内容/データが変更されたかどうかを判断するのに役立ちます。 |
| woocommerce_items_in_cart | セッション | WooCommerce がカートの内容/データが変更されたかどうかを判断するのに役立ちます。 |
| wp_woocommerce_session_ | 2 日 | 各顧客の一意のコードが含まれており、データベース内で各顧客のカートデータがどこにあるかがわかります。 |
| woocommerce_recently_viewed | セッション | 最近閲覧した商品ウィジェットを強化します。 |
| store_notice[通知 ID] | セッション | 顧客がストア通知を閉じることができます。 |

すべてのオプションを網羅することはできませんが、人気のキャッシュプラグインに関するヒントをいくつか追加しました。より具体的なサポートについては、ご利用のキャッシュプラグインの統合を担当するサポートチームにお問い合わせください。

### W3 合計キャッシュ縮小設定​

Minify 設定の「無視されるコメント ステム」オプションに 'mfunc' を追加してください。

### WP-ロケット

WooCommerceはWP-Rocketと完全に互換性があります。プラグインの設定で、以下のページ（カート、チェックアウト、マイアカウント）がキャッシュされないようにしてください。

JavaScript ファイルの縮小は避けることをお勧めします。

### WP スーパーキャッシュ

WooCommerce は WP Super Cache とネイティブに互換性があります。WooCommerce は WP Super Cache に情報を送信し、カート、チェックアウト、マイアカウントページをデフォルトでキャッシュしないようにします。

### ニス​

```
if (req.url ~ "^/(cart|my-account|checkout|addons)") {  return (pass);}if ( req.url ~ "\\?add-to-cart=" ) {  return (pass);}
```

## トラブルシューティング

### Varnish 設定が WooCommerce で機能しないのはなぜですか?

WordPress.org サポート フォーラムの次の投稿「Cookie が Varnish コーディングにどのように影響するか」を確認してください (https://wordpress.org/support/topic/varnish-configuration-not-working-in-woocommerce)。

```
Add this to vcl_recv above "if (req.http.cookie) {":# Unset Cookies except for WordPress admin and WooCommerce pages if (!(req.url ~ "(wp-login|wp-admin|cart|my-account/*|wc-api*|checkout|addons|logout|lost-password|product/*)")) { unset req.http.cookie; } # Pass through the WooCommerce dynamic pages if (req.url ~ "^/(cart|my-account/*|checkout|wc-api/*|addons|logout|lost-password|product/*)") { return (pass); } # Pass through the WooCommerce add to cart if (req.url ~ "\?add-to-cart=" ) { return (pass); } # Pass through the WooCommerce APIif (req.url ~ "\?wc-api=" ) { return (pass); } # Block access to php admin pages via website if (req.url ~ "^/phpmyadmin/.*$" || req.url ~ "^/phppgadmin/.*$" || req.url ~ "^/server-status.*$") { error 403 "For security reasons, this URL is only accessible using localhost (127.0.0.1) as the hostname"; } Add this to vcl_fetch:# Unset Cookies except for WordPress admin and WooCommerce pages if ( (!(req.url ~ "(wp-(login|admin)|login|cart|my-account/*|wc-api*|checkout|addons|logout|lost-password|product/*)")) || (req.request == "GET") ) { unset beresp.http.set-cookie; }
```

### パスワードのリセットがループに陥るのはなぜですか?

これは、「マイ アカウント」ページがキャッシュされているためです。サーバー側キャッシュを備えた一部のホストでは、my-account.php がキャッシュされるのを防げません。

パスワードをリセットできず、ログイン画面に戻り続ける場合は、ホストに問い合わせて、このページがキャッシュから除外されていることを確認してください。

