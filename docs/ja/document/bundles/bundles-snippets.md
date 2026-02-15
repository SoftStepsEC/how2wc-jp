---
title: スニペット
url: https://woocommerce.com/document/bundles/bundles-snippets/
---

これらのスニペットを使用して、WooCommerce 製品バンドルの外観と機能をカスタマイズします。

スニペットを使用するには、リンクされたファイルをダウンロードし、他のプラグインと同様に有効化してください。または、コードをサイトにコピーすることもできます。これらのスニペットは、サイトのテーマファイルやfunctions.phpファイルを変更するのではなく、別の[スニペットプラグイン](https://wordpress.org/plugins/search/snippets/)に追加することをお勧めします。

**注**: [サポートポリシー](https://woocommerce.com/support-policy/)に基づき、カスタマイズに関するサポートは提供できません。スニペットのカスタマイズや機能拡張が必要な​​場合は、資格を有するWordPress/WooCommerce開発者にご相談ください。[Codeable](https://codeable.io/?ref=z4Hnp)、または[認定WooExpert](https://woocommerce.com/experts/)のご利用を強くお勧めします。

デフォルトでは、オプションのバンドルアイテムのチェックボックスはオフになっています。これは次のスニペットで変更できます。

| | <?php |
| | /** |
| | * プラグイン名: WooCommerce Product Bundles – オプションアイテムをデフォルトでチェック |
| | * プラグイン URI: https://woocommerce.com/products/product-bundles/ |
| | * 説明: このプラグインを使用すると、オプションのバンドルアイテムをデフォルトでチェック/選択できます。 |
| | * バージョン: 1.1 |
| | * 作成者: WooCommerce |
| | * 作成者 URI: https://woocommerce.com/ |
| | * 開発者: Manos Psychogyiopoulos |
| | * |
| | * 最低要件: 4.1 |
| | * テスト済み: 5.3 |
| | * |
| | * 著作権: © 2021 Automattic. |
| | * ライセンス: GNU General Public License v3.0 |
| | * ライセンス URI: http://www.gnu.org/licenses/gpl-3.0.html |
| | */ |
| | |
| | add_filter( 'woocommerce_bundled_item_is_optional_checked', 'wc_pb_is_optional_item_checked', 10, 2 ); |
| | | | | | function wc_pb_is_optional_item_checked( $checked, $bundled_item ) { |
| | | | | | if ( ! isset( $_GET[ 'update-bundle' ] ) ) { |
| | $checked = true; |
| | } |
| | | | | | return $checked; |
| | } |

オプションとしてマークされたバンドルアイテムのタイトルの横に「-optional」サフィックスを追加するには、次のスニペット/プラグインを使用します。

| | <?php |
| | /** |
| | * プラグイン名: WooCommerce Product Bundles. |
| | * プラグイン URI: https://woocommerce.com/products/product-bundles/ |
| | * 説明: このスニペットを使用して、バンドルされたアイテムのタイトルの横に「- オプション」サフィックスを追加します |
| | * バージョン: 1.0 |
| | * 作成者: WooCommerce |
| | * 作成者 URI: https://woocommerce.com/ |
| | * 開発者: Jason Kytros |
| | * |
| | * 最低要件: 2.6.0 |
| | * テスト済み: 5.7 |
| | * |
| | * 著作権: © 2017-2021 Automattic. |
| | * ライセンス: GNU General Public License v3.0 |
| | * ライセンス URI: http://www.gnu.org/licenses/gpl-3.0.html |
| | */ |
| | |
| | "add_filter( 'woocommerce_bundles_optional_bundled_item_add_suffix', '__return_true' ); |

デフォルトでは、バンドル商品の割引はセール価格と共存でき、バンドル商品の最終価格がさらに下がります。

あるいは、セール価格を無視し、バンドル商品の通常価格よりもバンドル商品の割引を適用することもできます。これは、次のスニペットで可能です。

| | <?php |
| | /** |
| | * プラグイン名: WooCommerce Product Bundles – 通常価格からの割引 |
| | * プラグイン URI: https://woocommerce.com/products/product-bundles/ |
| | * 説明: このスニペットを使用して、バンドル商品の割引を通常価格に適用します。 |
| | * バージョン: 1.0 |
| | * 作成者: WooCommerce |
| | * 作成者 URI: https://woocommerce.com/ |
| | * 開発者: Manos Psychogyiopoulos |
| | * |
| | * 最低要件: 3.8 |
| | * テスト済み: 5.3 |
| | * |
| | * 著作権: © 2021 Automattic. |
| | * ライセンス: GNU General Public License v3.0 |
| | * ライセンス URI: http://www.gnu.org/licenses/gpl-3.0.html |
| | */ |
| | | | | // このスニペットを使用するには、このファイルをプラグインディレクトリにダウンロードして有効化するか、この行の下のコードを (子) テーマの functions.php ファイルにコピーします。 |
| | | | | | add_filter( 'woocommerce_bundled_item_discount_from_regular', 'wc_pb_bundled_item_discount_from_regular', 10, 2 ); |
| | | | | | function wc_pb_bundled_item_discount_from_regular( $from_regular, $bundled_item ) { |
| | return true; |
| | } |

最新バージョンの製品バンドルを使用していることを確認してから、次のスニペット/プラグインを使用します。

| | <?php |
| | /** |
| | * プラグイン名: WooCommerce Product Bundles – Prevent Range-Format Prices |
| | * プラグイン URI: https://woocommerce.com/products/product-bundles/ |
| | * 説明: このスニペットを使用して、製品バンドルでバンドル価格が範囲形式で表示されないようにします。 |
| | * バージョン: 1.0 |
| | * 作成者: WooCommerce |
| | * 作成者 URI: https://woocommerce.com/ |
| | * 開発者: Manos Psychogyiopoulos |
| | * |
| | * 最低要件: 4.1 |
| | * テスト済み: 5.3 |
| | * |
| | * 著作権: © 2021 Automattic. |
| | * ライセンス: GNU General Public License v3.0 |
| | * ライセンス URI: http://www.gnu.org/licenses/gpl-3.0.html |
| | */ |
| | |
| | // このスニペットを使用するには、このファイルをプラグインディレクトリにダウンロードして有効化するか、この行の下のコードを (子) テーマの functions.php ファイルにコピーします。 |
| | | | | | add_filter( 'woocommerce_bundle_force_old_style_price_html', '__return_true' ); |

次のスニペットは、バンドルされたアイテムの列の数を 4 に調整する方法を示しています。

| | <?php |
| | /** |
| | * プラグイン名: WooCommerce Product Bundles – バンドルアイテムのグリッドレイアウトの列数 |
| | * プラグイン URI: http://woocommerce.com/products/product-bundles/ |
| | * 説明: このスニペットを使用して、「グリッド」レイアウトオプションを使用するときに、バンドルアイテムの列数を変更します。 |
| | * バージョン: 1.0 |
| | * 作成者: WooCommerce |
| | * 作成者 URI: http://woocommerce.com |
| | * 開発者: Jason Kytros |
| | * |
| | * |
| | * 著作権: © 2021 Automattic. |
| | * ライセンス: GNU General Public License v3.0 |
| | * ライセンス URI: http://www.gnu.org/licenses/gpl-3.0.html |
| | */ |
| | |
| | add_filter( 'woocommerce_bundled_items_grid_layout_columns', 'wc_pb_grid_layout_change_number_of_columns', 10, 2 ); |
| | | | | function wc_pb_grid_layout_change_number_of_columns( $columns, $bundle ) { |
| | return 4; |
| | } |

[商品のグループ化](https://woocommerce.com/document/bundles/bundles-configuration/#grouping-options)で**グループ化**が選択されている場合、カート/注文テンプレート内の親/子の明細項目の小計が合計され、親商品の実際の小計が集計された小計に置き換えられます。また、個別価格の商品の小計はインデントされ、**小計:** というプレフィックスが付きます。

これを防ぐには、次のスニペット/プラグインを使用します。

| | <?php |
| | /** |
| | * プラグイン名: WooCommerce Product Bundles – Prevent Subtotals Aggregation |
| | * プラグイン URI: https://woocommerce.com/products/product-bundles/ |
| | * 説明: 商品バンドルがカート/注文テンプレートでアイテムの小計を集計して表示しないようにします。バージョン 5.5 以上が必要です。 |
| | * バージョン: 1.0 |
| | * 作成者: WooCommerce |
| | * 作成者 URI: https://woocommerce.com/ |
| | * 開発者: Manos Psychogyiopoulos |
| | * |
| | * 最低要件: 4.1 |
| | * テスト済み: 5.3 |
| | * |
| | * 著作権: © 2021 Automattic. |
| | * ライセンス: GNU General Public License v3.0 |
| | * ライセンス URI: http://www.gnu.org/licenses/gpl-3.0.html |
| | */ |
| | |
| | add_filter( 'woocommerce_bundles_group_mode_options_data', 'sw_pb_group_mode_options_data' ); |
| | | |
| | function sw_pb_group_mode_options_data( $data ) { |
| | $data[ 'parent' ][ 'features' ] = array( 'parent_item', 'child_item_indent' ); |
| | return $data; |
| | } |

デフォルトでは、製品バンドルの在庫はバンドルされたアイテムの残りの在庫に基づいて計算されます。

代わりに、**商品データ > 在庫** で定義されている親アイテムの在庫に基づいてバンドルの在庫を計算するには、次のスニペットを使用します。

| | <?php |
| | /** |
| | * プラグイン名: WooCommerce Product Bundles |
| | * プラグイン URI: https://woocommerce.com/products/product-bundles/ |
| | * 説明: このスニペットを使用して、親商品の在庫残数を非表示にします |
| | * バージョン: 1.0 |
| | * 作成者: WooCommerce |
| | * 作成者 URI: https://woocommerce.com/ |
| | * 開発者: Jason Kytros |
| | * |
| | * 最低要件: 2.6.0 |
| | * テスト済み: 5.7 |
| | * |
| | * 著作権: © 2021 Automattic |
| | * ライセンス: GNU General Public License v3.0 |
| | * ライセンス URI: http://www.gnu.org/licenses/gpl-3.0.html |
| | */ |
| | | | | add_filter( 'woocommerce_bundle_display_bundled_items_stock_quantity', 'wc_sw_hide_bundled_items_stock_quantity' ); |
| | function wc_sw_hide_bundled_items_stock_quantity() { |
| | return false; |
| | } |

### 各バンドル販売に表示される短い説明を非表示にします

各バンドル販売に表示される短い説明を非表示にするには、次のスニペットを使用します。

| | <?php |
| | /** |
| | * プラグイン名: WooCommerce Product Bundles. |
| | * プラグイン URI: https://woocommerce.com/products/product-bundles/ |
| | * 説明: このスニペットを使用して、バンドルされた商品の短い説明を非表示にします |
| | * バージョン: 1.0 |
| | * 作成者: WooCommerce |
| | * 作成者 URI: https://woocommerce.com/ |
| | * 開発者: Jason Kytros |
| | * |
| | * 最低要件: 2.6.0 |
| | * テスト済み: 5.7 |
| | * |
| | * 著作権: © 2021 Automattic. |
| | * ライセンス: GNU General Public License v3.0 |
| | * ライセンス URI: http://www.gnu.org/licenses/gpl-3.0.html |
| | */ |
| | | | | add_filter( 'wc_pb_bundle_sell_data_item_args', 'sw_pb_hide_bundle_sells_description', 10, 3 ); |
| | | | | | function sw_pb_hide_bundle_sells_description( $args, $bundle_sell_id, $product ) { |
| | $args[ 'meta_data' ][ 'override_description' ] = 'yes'; |
| | return $args; |
| | } |

### バンドル販売レイアウトをグリッドに設定する

デフォルトの Bundle-Sells レイアウトを変更し、**グリッド** レイアウトで表示するには、次のスニペットを使用します。

| | <?php |
| | /** |
| | * プラグイン名: WooCommerce Product Bundles |
| | * プラグイン URI: https://woocommerce.com/products/product-bundles/ |
| | * 説明: このスニペットを使用して、バンドル販売のレイアウトをグリッドに変更します |
| | * バージョン: 1.0 |
| | * 作成者: WooCommerce |
| | * 作成者 URI: https://woocommerce.com/ |
| | * 開発者: Jason Kytros |
| | * |
| | * 最低要件: 2.6.0 |
| | * テスト済み: 5.7 |
| | * |
| | * 著作権: © 2021 Automattic |
| | * ライセンス: GNU General Public License v3.0 |
| | * ライセンス URI: http://www.gnu.org/licenses/gpl-3.0.html |
| | */ |
| | | | | add_filter( 'wc_pb_bundle_sells_dummy_bundle', 'wc_sw_bs_change_layout' ); |
| | | | | | function wc_sw_bs_change_layout( $bundle ) { |
| | $bundle->set_layout( 'grid' ); |
| | | | | | return $bundle; |
| | } |

### バンドル販売レイアウトを表形式に設定する

デフォルトの Bundle-Sells レイアウトを変更し、**表形式** レイアウトで表示するには、次のスニペットを使用します。

| | * プラグイン URI: https://woocommerce.com/products/product-bundles/ |
| | * 説明: このスニペットを使用して、バンドル販売のレイアウトを表形式に変更します |
| | * バージョン: 1.0 |
| | * 作成者: WooCommerce |
| | * 作成者 URI: https://woocommerce.com/ |
| | * 開発者: Jason Kytros |
| | * |
| | * 最低要件: 2.6.0 |
| | * テスト済み: 5.7 |
| | * |
| | * 著作権: © 2021 Automattic. |
| | * ライセンス: GNU General Public License v3.0 |
| | * ライセンス URI: http://www.gnu.org/licenses/gpl-3.0.html |
| | */ |
| | |
| | add_filter( 'wc_pb_bundle_sells_dummy_bundle', 'wc_sw_bs_change_layout' ); |
| | | | | function wc_sw_bs_change_layout( $bundle ) { |
| | $bundle->set_layout( 'tabular' ); |
| | | | | | return $bundle; |
| | } |

### バンドル製品の完全な説明を表示する

デフォルトでは、バンドルされたアイテムには、対応するシンプル/可変製品の簡単な説明が表示されます。

完全な説明を表示するには、次のスニペットを使用します。

| | <?php |
| | /** |
| | * プラグイン名: WooCommerce Product Bundles |
| | * プラグイン URI: https://woocommerce.com/products/product-bundles/ |
| | * 説明: このスニペットを使用して、バンドルされた製品の完全な説明を表示します |
| | * バージョン: 1.0 |
| | * 作成者: WooCommerce |
| | * 作成者 URI: https://woocommerce.com/ |
| | * 開発者: Jason Kytros |
| | * |
| | * 最低要件: 2.6.0 |
| | * テスト済み: 5.7 |
| | * |
| | * 著作権: © 2021 Automattic |
| | * ライセンス: GNU General Public License v3.0 |
| | * ライセンス URI: http://www.gnu.org/licenses/gpl-3.0.html |
| | */ |
| | |
| | add_action( 'init', 'sw_pb_wc_replace_bundled_items_description' ); |
| | | | | | function sw_pb_wc_replace_bundled_items_description() { |
| | remove_action( 'woocommerce_bundled_item_details', 'wc_pb_template_bundled_item_description', 20, 2 ); |
| | add_action( 'woocommerce_bundled_item_details', 'wc_pb_template_bundled_item_full_description', 20, 2 ); |
| | } |
| | |
| | 関数 wc_pb_template_bundled_item_full_description( $bundled_item, $bundle ) { |
| | wc_get_template( 'single-product/bundled-item-description.php', 配列 ( |
| | 'description' => $bundled_item->product->get_description() |
| | ), false, WC_PB()->plugin_path() . '/templates/' ); |
| | } |

デフォルトでは、バンドルされたアイテムはモバイル画面のリストに表示されます。

ただし、バンドルされたアイテムをデスクトップと同じレイアウトでモバイルに表示することが望ましい場合もあると認識しています。これを実現するには、次のスニペットをご利用ください。

```
add_filter( 'woocommerce_bundle_front_end_params', 'sw_pb_change_responsive_breakpoint' );
function sw_pb_change_responsive_breakpoint( $frontend_params ) {
	$frontend_params[ 'responsive_breakpoint' ] = 0;
	return $frontend_params;
}
```

### 商品ページでバンドル商品の前に「カートに追加」ボタンを移動する方法

**注意**: 次のソリューションは、製品バンドル ページでのみ機能し、バンドル販売機能では機能しません。

すべてのバンドルアイテムの前に [**カートに追加**] ボタンを表示するには、[WooCommerce Product Bundles – Top Add to Cart Button](https://href.li/?https://github.com/somewherewarm/woocommerce-product-bundles-top-add-to-cart-button#woocommerce-product-bundles---top-add-to-cart-button) を使用できます。これは、[WooCommerce Product Bundles](https://href.li/?https://woocommerce.com/products/product-bundles/) の無料ミニ拡張機能で、製品バンドルページの上部に [カートに追加] ボタンセクションを追加します。

あるいは、すべてのバンドルされたアイテムの前に **1 つの「カートに追加」** ボタンを表示するには、次のスニペットを使用します。

```
add_action( 'woocommerce_before_add_to_cart_form', 'sw_pb_move_add_to_cart_button', 100 );

function sw_pb_move_add_to_cart_button() {
	global $product;

	if ( ! is_a( $product, 'WC_Product' ) ) {
		return;
	}

	if ( ! $product->is_type( 'bundle' ) ) {
		return;
	}
	
	remove_action( 'woocommerce_bundles_add_to_cart_wrap', 'wc_pb_template_add_to_cart_wrap' );
	add_action( 'woocommerce_before_bundled_items', 'wc_pb_template_add_to_cart_wrap' );
}
```

このスニペットをインストールすると、バンドルされたアイテムのフォームの真上に [**カートに追加**] ボタンが表示されます。

間にスペースを追加するには、次の CSS スニペットも追加することをお勧めします。

```
.bundle_form .bundle_wrap {  	
    margin-bottom: 10% !important;  
}
```

デフォルトでは、WooCommerce コアはカート内の各商品に**クロスセル**を表示します。商品バンドルをカートに追加すると、親バンドルごとに1つのカート商品が作成され、バンドル商品ごとに1つのカート商品が作成されます。そのため、バンドル自体にリンクされたクロスセルと、バンドルされた個々の商品にリンクされたクロスセルの両方がカートに表示されます。

バンドル製品にリンクされた**クロスセル**が表示されないようにするには、次のスニペットを使用します。

```
add_filter( 'woocommerce_cart_crosssell_ids', 'sw_pb_remove_bunlded_item_crossells', 10, 2 );

function sw_pb_remove_bunlded_item_crossells( $cross_sells, $cart ) {

	$cross_sells = array();
	$in_cart     = array();
	if ( ! $cart->is_empty() ) {
		foreach ( $cart->get_cart() as $cart_item_key => $values ) {
			if ( $values['quantity'] > 0 ) {
				if ( wc_pb_is_bundled_cart_item( $values ) ) {
					continue;
				}
				$cross_sells = array_merge( $values['data']->get_cross_sell_ids(), $cross_sells );
				$in_cart[]   = $values['product_id'];
			}
		}
	}
	$cross_sells = array_diff( $cross_sells, $in_cart );
	return $cross_sells;
}
```

### モバイル画面の表形式レイアウトでカスタムテーマの問題を解決する方法

過去にストアオーナー様から、カスタムテーマを使用したモバイル画面で表形式レイアウトがうまく機能しないという報告をいただいております。よくある問題の一つとして、表の一部が切れてしまったり、画面に完全に収まっていないように見えることが挙げられます。

モバイル画面での表形式レイアウトの動作を次のように変更します。

- 「標準」レイアウトに似ており、
- 小さなページに適しています。

次の CSS スニペットを使用できます。

```
@media (max-width: 568px) {
  .woocommerce #content div.product .bundle_form div.bundled_product_summary .bundled_product_images, .woocommerce div.product .bundle_form div.bundled_product_summary .bundled_product_images, .woocommerce-page #content div.product .bundle_form div.bundled_product_summary .bundled_product_images, .woocommerce-page div.product .bundle_form div.bundled_product_summary .bundled_product_images {
    width: 100%;
    float: left;
    margin-left: 0;
    margin-right: 0; }
  .bundle_form div.bundled_product_summary:not(.thumbnail_hidden) .details {
    width: 100%;
    float: left;
    margin-left: 0;
    margin-right: 0; }
  .bundle_form div.bundled_product_summary .bundled_product_images {
    max-width: 50%; }
  .bundle_form div.bundled_product_summary .bundled_product_images img {
    margin-bottom: 1em; }
  .bundle_form table.bundled_products td {
    display: block; }
  .bundle_form table.bundled_products thead {
    display: none; }
  .bundle_form table.bundled_products tr td.bundled_item_images_col {
    width: 100%;
    padding-bottom: 0; }
  .bundle_form table.bundled_products tr td.bundled_item_images_col, .bundle_form table.bundled_products tr td.bundled_item_details_col {
    padding-bottom: 0; }
  .bundle_form table.bundled_products tr td.bundled_item_images_col {
    width: 100%; }
  .bundle_form table.bundled_products tr td.bundled_item_qty_col {
    max-width: 100%;
    text-align: left; } }
```

```
add_filter( 'woocommerce_product_is_visible', 'wc_hide_insufficient_stock_bundles_from_upsells', 10, 2 );

function wc_hide_insufficient_stock_bundles_from_upsells( $visible, $product_id ) {

	if ( ! $visible ) {
		return $visible;
	}

	$product_type = WC_Data_Store::load( 'product' )->get_product_type( $product_id );

	if ( 'bundle' === $product_type ) {

		$bundle = wc_get_product( $product_id );

		if ( 'yes' === get_option( 'woocommerce_hide_out_of_stock_items' ) && ! $bundle->is_in_stock() ) {
			$visible = false;
		}
	}
	return $visible;
}
```

オプションの在庫切れバンドルアイテムをバンドルから削除するには、次のスニペットを使用します。

```
add_filter( 'woocommerce_bundled_items', 'sw_remove_out_of_stock_items', 10, 2 );

function sw_remove_out_of_stock_items( $bundled_items, $bundle ) {
    foreach ( $bundled_items as $key => $bundled_item ) {
        if ( $bundled_item->is_optional() || $bundled_item->get_quantity( 'min' ) == 0 ) {
            if ( 'outofstock' === $bundled_item->product->get_stock_status() ) {
                unset( $bundled_items[ $key ] );
            }
        }
    }
    return $bundled_items;
}
```

**注意**: 在庫切れの必須商品は削除できません。削除すると、カートへの追加検証エラーが発生します。

### カート内のバンドル商品の数量の変更を防止する

バンドルがカートに追加された後に顧客がバンドルの設定を変更できないようにするには、次のスニペットを使用します。

```
add_filter( 'woocommerce_cart_item_quantity', 'wc_cart_item_quantity', 15, 3 );   

function wc_cart_item_quantity( $product_quantity, $cart_item_key, $cart_item ) {                                      
    if ( is_cart() && wc_pb_is_bundled_cart_item( $cart_item ) ) {
        $product_quantity = sprintf( '%2$s ', $cart_item_key, $cart_item['quantity'] );
    }
    return $product_quantity;
}
```

### バンドルアイテムの画像のサイズを変更する

WordPress に画像をアップロードすると、次の 4 つの追加画像サイズが自動的に生成されます。

- **サムネイル** (150ピクセル四方)
- **中** (幅と高さは最大300ピクセル)
- **大** (幅と高さは最大1024ピクセル)
- **フル** (アップロードした元のサイズ)

WooCommerce ではさらに 3 つの画像サイズが追加されます。

- **woocommerce_thumbnail** – ショップページなどの商品グリッドで使用します。デフォルトでは幅600ピクセルで、一貫性を保つために正方形にトリミングされます。アスペクト比はカスタマイズ可能です。
- **woocommerce_single** – 単一商品ページで使用します。アップロードされた商品画像全体を、デフォルトではトリミングされずに表示します。デフォルトでは幅600ピクセルです。
- **woocommerce_gallery_thumbnail** – メイン商品画像の下にあるギャラリーナビゲーションで使用します。常に正方形にトリミングされ、デフォルトで100×100ピクセルです。

バンドル商品の画像はデフォルトで**大きい**サイズで表示されます。これを変更するには、以下のフィルターを使用してください。

```
add_filter( 'bundled_product_large_thumbnail_size', 'sw_wc_pb_change_thumbnail_size', 10, 1 );function sw_wc_pb_change_thumbnail_size( $thumbnail_size ) {        return 'woocommerce_gallery_thumbnail';}
```

### バンドルアイテムの前にタイトル/見出しを追加する方法

次のコード スニペットを使用すると、**製品バンドル** 製品タイプで作成されたバンドル製品の前にタイトルを追加できます。

```
add_action( 'woocommerce_before_bundled_items', 'wc_display_bundled_items_heading' );

function wc_display_bundled_items_heading() {
	echo '<h3> Bundled items: </h3>';
}
```

個別に価格設定され、最大数量が1を超えるバンドル商品には、価格文字列に「each」というサフィックスが表示されます。このサフィックスをカスタム文字列に置き換えるには、次のスニペットを使用します。

```
add_filter( 'woocommerce_bundled_item_price_html', 'sw_pb_remove_pc', 10, 3 );

function sw_pb_remove_pc( $price_html, $price, $bundled_item ) {
	$price_html = str_replace( 'each', 'test', $price_html );
	return $price_html;
}
```

**注意**; このスニペットを使用する前に、`test` を必要なカスタム文字列に置き換えてください。

### 製品バンドル JavaScript API の使い方

Product Bundles JavaScript API を使用するカスタム コードの作成を開始するには、次のテンプレートを使用できます。

```
add_action( 'wp_footer', function() {
	?>
	<script type="text/javascript">
		jQuery( function( $ ) {

			$( '.bundle_data' ).on( 'woocommerce-product-bundle-initialized', function( event, bundle ) {
				// Write your custom code here. 
			} );
		} );
	</script>
	<?php
} );
```

バンドルされたアイテムに関連付けられたダウンロード可能なファイルを削除するには、次のスニペットを使用します。

```
 add_filter( 'woocommerce_order_get_downloadable_items', 'sw_pb_remove_bundled_items_files', 10, 2 );

function sw_pb_remove_bundled_items_files( $downloads, $order ) {

	$downloads = array();

	foreach ( $order->get_items() as $item ) {
		if ( ! is_object( $item ) ) {
			continue;
		}

		if ( wc_pb_is_bundled_order_item( $item ) ) {
			continue;
		}

		if ( $item->is_type( 'line_item' ) ) {
			$item_downloads = $item->get_item_downloads();
			$product        = $item->get_product();
			if ( $product && $item_downloads ) {
				foreach ( $item_downloads as $file ) {
					$downloads[] = array(
						'download_url'        => $file['download_url'],
						'download_id'         => $file['id'],
						'product_id'          => $product->get_id(),
						'product_name'        => $product->get_name(),
						'product_url'         => $product->is_visible() ? $product->get_permalink() : '', // Since 3.3.0.
						'download_name'       => $file['name'],
						'order_id'            => $order->get_id(),
						'order_key'           => $order->get_order_key(),
						'downloads_remaining' => $file['downloads_remaining'],
						'access_expires'      => $file['access_expires'],
						'file'                => array(
							'name' => $file['name'],
							'file' => $file['file'],
						),
					);
				}
			}
		}
	}
	return $downloads;
}
```

デフォルトでは、バンドルの在庫状況は次の場合にのみ更新されます。

- バンドル商品として追加された商品の在庫が変更された場合、または
- バンドル商品として追加された商品が削除された場合（ただし、**ゴミ箱に移動**された場合は**削除されません**）。

バンドルアイテムとして追加された商品がゴミ箱に移動されたときに、バンドルの在庫状況も更新したい場合は、次のスニペットを使用します。

```
add_action( 'wp_trash_post', function( $id ) {
	if ( $id > 0 ) {

		$post_type = get_post_type( $id );

		if ( 'product' === $post_type ) {
			$bundled_item_ids = array_keys( wc_pb_get_bundled_product_map( $id, false ) );

			if ( ! empty( $bundled_item_ids ) ) {
				foreach ( $bundled_item_ids as $bundled_item_id ) {
					WC_PB_DB::bulk_delete_bundled_item_stock_meta( array( $bundled_item_id ) );
				}
			}
		}
	}
} );
```

ご購入前にご質問がございましたら、こちらの[販売前フォーム](https://woocommerce.com/contact-us/#sales-form)にご記入ください。既にご購入済みでサポートが必要な場合は、ヘルプデスクから[お問い合わせください](https://woocommerce.com/my-account/marketplace-ticket-form/)！

