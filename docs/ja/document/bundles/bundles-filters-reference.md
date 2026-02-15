---
title: フィルターリファレンス
url: https://woocommerce.com/document/bundles/bundles-filters-reference/
---

このページは、WooCommerce 製品バンドルを拡張またはカスタマイズしたい開発者向けに書かれています。[PHP](http://php.net/) と [WordPress 開発](http://codex.wordpress.org/Developer_Documentation) に関する高度な知識が必要です。

このガイドでは、製品バンドルで利用できる最も便利なフィルターフックについて説明します。利用可能なすべてのフィルターを網羅したリファレンスではなく、特定のタスクを実行する方法に関するチュートリアルも含まれていません。

[データ構造とストレージ](https://woocommerce.com/document/bundles/bundles-data-structures-storage/)をお読みになり、[関数リファレンス](https://woocommerce.com/document/bundles/bundles-functions-reference/)を手元に置いておくことをお勧めします。プラグインのアーキテクチャと、使用したいフックに関連するオブジェクトについて理解を深めてください。

#### woocommerce_bundle_requires_input

**説明**

`WC_Product_Bundle::requires_input` の出力を変更します。これは、製品バンドルに、カートに追加するために構成が必要なフィールドがあるかどうかを示します。

**引数**

`array $quantities_array` – バンドル商品の最小/最大数量の配列。数量はまず文字列値 `min` と `max` でインデックス付けされ、次にバンドル商品IDでインデックス付けされます。`WC_Product_Bundle $bundle` – 商品バンドルオブジェクト。

#### woocommerce_bundled_items

**説明**

`WC_Product_Bundle` インスタンスで使用可能で、`WC_Product_Bundle::get_bundled_items` によって返されるバンドルされたアイテムのコレクションを変更します。

**引数**

`array $bundled_items` – バンドルに関連付けられた `WC_Bundled_Item` オブジェクトの配列。バンドルされたアイテム ID でインデックス付けされます。 `WC_Product_Bundle $bundle` – 製品バンドル オブジェクト。

#### woocommerce_bundle_is_editable_in_cart

**説明**

このフィルターを使用して、カートに追加されたバンドルをカート ページから編集できるかどうかを制御します。

**引数**

`array $is_editable_in_cart` – バンドルがカートページから編集できるかどうかを示します。 `WC_Product_Bundle $bundle` – 製品バンドルオブジェクト。 `array|false $cart_item` – カートコンテキストで `WC_Product_Bundle::is_editable_in_cart` が呼び出されたときにバンドルに関連付けられたコンテナカートアイテム。

#### woocommerce_bundle_cart_permalink_args

**説明**

このフィルターを使用して、カートからバンドルの設定を編集するときにバンドルのパーマリンクに追加される引数を変更します。

**引数**

`array $args` – パーマリンクに追加するパラメータ名/値。 `array|false $cart_item` – カートのコンテキストで `WC_Product_Bundle ::is_editable_in_cart` が呼び出されたときにバンドルに関連付けられるコンテナ カート項目。 `WC_Product_Bundle $bundle` – 製品バンドル オブジェクト。

#### woocommerce_bundled_item_discount_from_regular

**説明**

このフィルターを使用して、バンドル商品の割引を計算する際に使用する参照価格を変更します。

**引数**

`boolean $calc_discounts_from_regular` – 通常価格を基準にして割引商品価格を計算するかどうかを示します。デフォルトは `False` です。 `WC_Bundled_Item $bundled_item` – バンドル商品オブジェクト。

**例**

[このスニペット](https://woocommerce.com/document/bundles/bundles-snippets/#discount_over_sale_prices)では、フィルターを使用して通常価格に対する割引価格を計算します。

#### woocommerce_bundled_item_group_of_quantity

**説明**

これを使用して、バンドルされたアイテムの「グループ」数量を上書きします。

**引数**

`integer $group_of_quantity` – デフォルトの数量値。 `WC_product $product` – バンドルされた製品オブジェクト。 `WC_Bundled_Item|int $bundled_item_or_product` – バンドルされたアイテムまたは製品オブジェクト。

**例**

```
add_filter( 'woocommerce_bundled_item_group_of_quantity', 'filter_group_of', 10, 3 );

function filter_group_of( $group_of_quantity, $product, $bundled_item_or_product ) {
    return 1;
}
```

#### woocommerce_bundled_item_is_optional_checked

**説明**

オプションのバンドル項目のデフォルトのチェックボックスの状態をフィルターします。

**引数**

`integer $quantity_value -`デフォルトの数量値。`WC_Bundled_Item $bundled_item` – バンドルされたアイテム オブジェクト。

**例**

[このスニペット](https://woocommerce.com/document/bundles/bundles-snippets/#optional_checked)では、フィルターを使用して、オプションのバンドルアイテムがデフォルトで選択されるようにしています。

#### woocommerce_bundled_item_classes

**説明**

単一製品テンプレート内のバンドルされたアイテム コンテナー要素に割り当てられた HTML クラスをフィルターします。

**引数**

`array $classes` – クラス名。 `WC_Bundled_Item $bundled_item` – バンドルされたアイテムオブジェクト。

#### woocommerce_bundled_product_quantity

**説明**

デフォルトでは最小数量に等しい、バンドル製品のデフォルトの数量値を変更します。

**引数**

`integer $quantity_value` – デフォルトの数量値。 `integer $quantity_min` – デフォルトの数量値。 `integer $quantity_max` – デフォルトの数量値。 `WC_Bundled_Item $bundled_item` – バンドルされたアイテムオブジェクト。

#### woocommerce_bundles_optional_bundled_item_suffix

**説明**

オプションのバンドル項目に付加される「optional」サフィックスを変更します。

**引数**

`WC_Bundled_Item $bundled_item` – バンドルされたアイテムオブジェクト。 `WC_Product_Bundle $bundle` – 製品バンドルオブジェクト。

**例**

[このスニペット](https://woocommerce.com/document/bundles/bundles-snippets/#remove_optional_suffix)では、フィルターを使用して、オプションのバンドルアイテムのタイトルサフィックスを削除しています。

#### woocommerce_bundle_front_end_params

**説明**

このフィルターを使用して、単一製品のカート追加スクリプトに渡されるパラメータを変更します。

**引数**

`array $params` – フロントエンド スクリプトに渡されるパラメータの配列。

#### woocommerce_force_show_bundled_dropdown_variation_attribute_options

**説明**

このフィルターを使用すると、バンドルされた可変商品の属性オプションが常にドロップダウンメニューに表示されます。デフォルトでは、バンドルされた可変商品に、属性値が明確に定義されたアクティブなバリエーションが1つしかない場合、その属性選択ドロップダウンは非表示になり、事前に選択された値の説明に置き換えられます。

**引数**

`boolean $force_dropdowns` – 属性値の選択のためにドロップダウン メニューを強制的に表示するかどうかを示します。 `array $args` – フロントエンド スクリプトに渡されるパラメーターの配列。

#### woocommerce_bundle_show_bundled_product_attributes

**説明**

バンドル製品の属性を、その製品を含むバンドルの単一製品ページに表示するかどうかを制御します。

デフォルトでは、バンドルされた製品がそのバンドルの単一製品テンプレートで表示されるように設定されている場合、その属性はバンドルの属性の後に表示されます。

**引数**

`boolean $include` – バンドル製品の属性を表示するかどうかを示します。 `WC_Product_Bundle $bundle` – 製品バンドルオブジェクト。 `WC_Bundled_Item $bundle` – バンドルアイテムオブジェクト。

#### woocommerce_bundled_item_add_to_cart_validation

**説明**

このフィルターは、バンドル タイプの製品のカートへの追加検証を実行するときに適用され、バンドルされたアイテム レベルでカスタム検証ロジックを実行するために使用できます。

**引数**

`boolean $passes_validation` – 検証結果。 `WC_Product $bundle` – 検証対象のバンドル商品に関連付けられた商品オブジェクト。 `WC_Bundled_Item $bundled_item` – `WC_Bundled_Item` オブジェクト。 `integer $quantity` – バンドル商品の数量。 `integer|''|false $variation_id` – 該当する場合のバリエーション ID。 `array $configuration` – バンドル設定配列。

#### woocommerce_add_to_cart_bundle_validation

**説明**

このフィルターは、バンドル タイプの製品のカートに追加の検証を実行するときに適用され、成功した検証結果を変更する最後のチャンスを提供します。

**引数**

`boolean $passes_validation` – 検証結果。 `integer $bundle_id` – 製品バンドル ID。 `WC_PB_Stock_Manager $stock_mgr` – バンドル製品の在庫数量を検証するために使用される在庫マネージャー オブジェクト。 `array $configuration` – バンドル構成配列。

#### woocommerce_bundled_item_has_bundled_weight

**説明**

**組み立て済み**バンドルを作成する際、「組み立て済み重量」オプションを使用して重量の計算方法を制御できます。アセンブリの重量が静的な場合は「無視」オプションを選択し、動的に重量を計算する場合は「保持」オプションを選択します。「保持」を選択した場合、アセンブリの重量は以下の要素を加算して計算されます。

- 指定されたコンテナの**重量**、および
- すべての**組み立て済み**バンドルアイテムの重量。

このフィルターを使用すると、バンドルされた個々のアイテムの重量をプログラムで追加するか無視するかを制御できます。

**引数**

`boolean $add_weight_to_container` – このバンドル商品の重量を親商品の重量に追加するかどうかを示します。デフォルトは `false` です。 `WC_Product $product` – バンドル商品オブジェクト。 `integer $bundled_item_id` – 商品に関連付けられているバンドル商品のID。 `WC_Product_Bundle $bundle` – 商品バンドルオブジェクト。

#### woocommerce_bundled_cart_item

**説明**

このフィルターを使用して、セッションの読み込み時に再適用されるバンドル製品のカート項目データを変更します。

**引数**

`array $cart_item` – バンドル製品のカートアイテムデータ。 `WC_Product_Bundle $bundle` – 親製品バンドルオブジェクト。

#### woocommerce_bundle_container_cart_item

**説明**

このフィルターを使用して、セッションのロード時に再適用されるバンドル コンテナーのカート アイテム データを変更します。

**引数**

`array $cart_item` – バンドル コンテナ製品のカート アイテム データ。 `WC_Product_Bundle $bundle` – 製品バンドル オブジェクト。

#### woocommerce_bundled_item_cart_item_identifier

**説明**

このフィルターを使用すると、商品バンドルをカートに追加する際に、その設定データにカスタムフィールドを追加できます。バンドル商品にカスタム設定入力フィールドを追加する場合によく使用されます。

**引数**

`array $item_configuration` – バンドルされたアイテムの構成配列。 `integer $bundled_item_id` – バンドルされたアイテム ID。 `integer $bundle_id` – 製品バンドル ID。

**例**

このフィルターの使用方法は、Product Bundlesに含まれる`WC_PB_Addons_Compatibility`クラスで示されています。このクラスには、[Product Add-Ons](https://woocommerce.com/products/product-add-ons/)拡張機能の互換性コードが含まれています。このフィルターは、バンドルをカートに追加する前に、バンドルされたProduct Add-Onsフィールドに関連付けられた投稿データを読み取り、バンドルのカートIDを生成するハッシュ関数に渡すために使用されます。

#### woocommerce_bundled_item_cart_data

**説明**

コンテナ/親カートアイテムに既に保存されているデータをコピーすることで、バンドル/子カートアイテムのデータを変更する機会を提供します。一般的には、[woocommerce_bundled_item_cart_item_identifier](https://woocommerce.com/document/bundles/bundles-filters-reference/#woocommerce_bundled_item_cart_item_identifier) フィルターを使用して追加されたデータをコピーするために使用されます。

**引数**

`array $bundled_item_cart_data` – バンドル製品がカートに追加されたときに、そのカートアイテムデータに追加するカスタムフィールド。 `integer $cart_item_data` – カートに追加されたばかりのコンテナ/親のカートアイテムデータ。

**例**

このフィルターの使用方法は、Product Bundlesに含まれる`WC_PB_Addons_Compatibility`クラスで示されています。このクラスには、[Product Add-Ons](https://woocommerce.com/products/product-add-ons/)拡張機能の互換性コードが含まれています。このフィルターは、コンテナカートアイテムからバンドルされたProduct Add-Onsフィールドをコピーするために使用されます。

#### woocommerce_add_bundled_order_item_subtotals

**説明**

デフォルトでは、バンドルコンテナアイテムの注文アイテム小計は、i) バンドルの基本小計と、ii) 個別に価格設定されているバンドルアイテムの小計の合計として計算されます。また、個別に価格設定されているアイテムの小計には、「小計:」というプレフィックスが付きます。フィルターを使用すると、これを防ぐことができます。

**引数**

`boolean $add_subtotals` – 小計の表示方法を変更するかどうかを示します。デフォルトは `true` です。`array $container_item_data` – コンテナ/親注文項目。`WC_Order $order` – 注文オブジェクト。

**例**

[このスニペット](https://woocommerce.com/document/bundles/bundles-snippets/#prevent_subtotals_modifications) は、拡張機能がカート/注文内のアイテムの小計を変更しないようにする方法を示しています。

#### woocommerce_bundle_container_order_item_sku

**説明**

このフィルターを使用して、[get_product_from_item](https://woocommerce.com/document/bundles/bundles-functions-reference/#get_product_from_item) メソッドを使用して変更された**組み立てられた**製品バンドル オブジェクトの SKU を、バンドルに含まれるバンドル製品と数量のリスト ([個別配送](https://woocommerce.com/document/bundles/product-bundles-store-owners-guide/#shipping) されないバンドル アイテム) に基づいて変更します。

**引数**

`string $sku` – バンドルの SKU。 `WC_Product $product` – 製品バンドル オブジェクト。 `WC_Order_Item_Product $container_item` – コンテナ/親注文アイテム。 `array $assembled_items` – 出荷用にバンドルに物理的に組み立てられたバンドル注文アイテム。 `WC_Order $order` – 注文オブジェクト。

#### woocommerce_bundles_process_bundled_item_admin_data

**説明**

このフィルターを使用すると、バンドルアイテムの管理オプションに関連付けられたカスタム投稿フィールドをインターセプトして処理できます。ここで追加されたカスタムフィールドは、バンドルアイテムのカスタムメタとして保存されます。

**引数**

`array $processed_data` – 特定のバンドルアイテムの追加/更新に使用されるパラメータの配列。 `array $posted_data` – 特定のバンドルアイテムに関連付けられた投稿データの配列。 `integer|'' $bundled_item_id` – 更新時のバンドルアイテムの ID。初めて作成する場合は空。 `integer $bundled_id` – 製品バンドルの ID。

#### woocommerce_bundled_product_admin_html_tabs

**説明**

このフィルターを使用すると、デフォルトの **基本設定** タブと **詳細設定** タブに加えて、バンドルされたアイテムのカスタム管理オプションを表示する追加のタブを作成できます。

**引数**

`array $tabs` – 表示するタブセクションの配列。

ご購入前にご質問がございましたら、こちらの[販売前フォーム](https://woocommerce.com/contact-us/#sales-form)にご記入ください。既にご購入済みでサポートが必要な場合は、ヘルプデスクから[お問い合わせください](https://woocommerce.com/my-account/marketplace-ticket-form/)！

