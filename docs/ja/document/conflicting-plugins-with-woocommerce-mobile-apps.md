---
title: プラグインが WooCommerce モバイルアプリと競合しています
url: https://woocommerce.com/document/conflicting-plugins-with-woocommerce-mobile-apps/
---

場合によっては、拡張機能やプラグインとの競合が発生し、WooCommerce モバイル アプリがデータを正しく取得して表示できなくなることがあります。

これらの競合は、サードパーティ製のプラグインや拡張機能がWooCommerceコアプラグインと様々な方法で相互作用することで発生する可能性があります。スムーズなエクスペリエンスを確保するには、潜在的な競合を認識し、効果的なトラブルシューティング方法を知ることが重要です。

以下は、互換性の問題があることがわかっているプラ​​グインと拡張機能のリストです。

- [Solid Security](https://wordpress.org/plugins/better-wp-security/) (旧称 iThemes Security): このプラグインで、*システム調整* の **長い URL 文字列をフィルター** オプションが無効になっていることを確認してください。
- [Booster for WooCommerce](https://wordpress.org/plugins/woocommerce-jetpack/): 接続の問題が発生します。
- [WP Go Maps](https://wordpress.org/plugins/wp-google-maps/) (旧称 WP Google Maps): 商品画像のアップロード時に問題が発生します。
- [Weglot](https://wordpress.org/plugins/weglot/): このプラグインで、`/xmlrpc.php` が [自動翻訳から除外](https://support.weglot.com/article/95-how-to-exclude-urls-blocks-words-from-translation) されていることを確認してください。
- [WooCommerce 用商品ラベル（セールバッジ）](https://wordpress.org/plugins/aco-product-labels-for-woocommerce/): 接続の問題が発生します。
- [WordPress と WooCommerce の無駄なデータ消費を無効化](https://wordpress.org/plugins/disable-dashboard-for-woocommerce/): WooCommerce 統計情報を無効化します。
- [WPML](https://wpml.org/): ログインの問題が発生します。
- [CleanTalk によるスパム対策、アンチスパム、ファイアウォール](https://wordpress.org/plugins/cleantalk-spam-protect/): モバイルアプリで注文情報を取得する際に問題が発生します。
- [Woody コードスニペット](https://wordpress.org/plugins/insert-php/): このプラグインで追加されたスニペットは、モバイルアプリで問題を引き起こす可能性があります。
- [Envira Gallery 用 WooCommerce アドオン](https://enviragallery.com/addons/woocommerce-addon/): 注文に商品を追加する際に問題が発生する可能性があります。
- [Speed Booster Pack](https://speedboosterpack.com/) – モバイルアプリと Woo サイトのチェックアウトページで問題が発生します。
- [商品の動的価格設定と割引](https://woocommerce.com/products/product-dynamic-pricing-and-discounts/): モバイルアプリで商品が読み込まれません。
- [wePOS – WooCommerce 用 POS (Point of Sales)](https://wordpress.org/plugins/wepos/): モバイルアプリで商品が読み込まれません。
- [WP Blog Post Layouts](https://wordpress.org/plugins/wp-blog-post-layouts/): モバイルアプリで商品が読み込まれません。
- [FOX – Currency Switcher Professional for WooCommerce](https://wordpress.org/plugins/woocommerce-currency-switcher/): 統計情報に誤った通貨が表示されます。
- [CURCY – Multi-Currency for WooCommerce](https://wordpress.org/plugins/woo-multi-currency/): モバイルアプリに誤った通貨が表示されます。
- [ElasticPress](https://wordpress.org/plugins/elasticpress/): 検索機能が動作せず、SKUによる検索のみ動作します。
- [Airlift](https://airlift.net/): Jetpack APIレスポンスにコメントを挿入することで、サイト接続を切断します。
- [All-In-One Security (AIOS) – Security and Firewall](https://wordpress.org/plugins/all-in-one-wp-security-and-firewall/): 「ログインロックアウト」により接続に問題が発生します。
- [PayPal WooCommerce 向け決済プラグイン](https://wordpress.org/plugins/pymntpl-paypal-woocommerce/): アプリ使用時に決済ゲートウェイ機能が中断されます。*注: 公式 PayPal 決済プラグインには互換性の問題はありません。*
- [WP 2FA – WordPress 向け 2 要素認証](https://wordpress.org/plugins/wp-2fa/): `two_factor_user_api_login_enable` フィルターが true を返さない限り、2 要素認証を有効にしているユーザーによる REST API および XML-RPC ログイン試行をブロックします。

- [チェックアウトフィールドエディタ](https://woocommerce.com/products/woocommerce-checkout-field-editor/): チェックアウト時に、カスタムフィールド（カスタム請求先住所情報など）はモバイルアプリでは表示されません。
- [商品ベンダー](https://woocommerce.com/products/product-vendors/): モバイルアプリからストアにアクセスできるのは、ショップマネージャーと管理者のみです。この拡張機能を使用して作成されたベンダーは、モバイルアプリを使用できません。

- [iBidテーマ](https://modeltheme.com/portfolio/ibid-multi-vendor-wordpress-auction-theme/): モバイルアプリで商品が読み込まれません。
- [Lafkaテーマ](https://themeforest.net/item/lafka-fast-food-restaurant-woocommerce-theme/23969682): モバイルアプリで商品が読み込まれず、変動商品の注文数量も正しく表示されません。
- [Jetpackの既知の問題](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)のリストをご覧ください。

### 対面支払いの競合

- [Dokan](https://dokan.co/wordpress/): 加盟店がM2カードリーダーを接続できないようにします。
- [YITH Point Of Sale For WooCommerce (POS)](https://yithemes.com/themes/plugins/yith-point-of-sale-for-woocommerce/): サポートされていません。

Jetpackプラグインを使用してモバイルアプリをサイトに接続している場合は、Jetpack接続がアクティブで正常に機能していることを確認してください。[よくある問題を確認する](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)、または[サイトを再接続する](https://jetpack.com/support/reconnecting-reinstalling-jetpack/)を行ってください。

それでも問題が解決しない場合は、*メニュー > 設定 > ヘルプとサポート > サポートに問い合わせ* して、アプリ内からサポートにお問い合わせください。

