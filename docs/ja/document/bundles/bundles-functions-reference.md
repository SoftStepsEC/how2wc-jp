---
title: 関数リファレンス
url: https://woocommerce.com/document/bundles/bundles-functions-reference/
---

このページは、WooCommerce 製品バンドルを拡張またはカスタマイズしたいと考えている WooCommerce 開発者向けに書かれています。[PHP](http://php.net/) と [WordPress 開発](http://codex.wordpress.org/Developer_Documentation) に関する高度な知識が必要です。

このガイドでは、製品バンドルで利用できる最も便利な機能の一部を紹介します。特定のタスクを実行する方法に関するチュートリアルは含まれていません。

このリファレンスを参照する前に、[データ構造とストレージ](https://woocommerce.com/document/bundles/bundles-data-structures-storage/)を読むことをお勧めします。プラグインのアーキテクチャと `WC_PB_Cart`、`WC_PB_Order`、`WC_PB_DB`、`WC_Bundled_Item_Data` オブジェクトについて理解を深めてください。

**グローバルカート機能**

| 名前 | 説明 |
| --- | --- |
| wc_pb_is_bundled_cart_item | カート アイテムがバンドルの一部であるかどうかを確認します。この関数は、カート アイテムのデータのみに頼るのではなく、親カート アイテムが実際に存在するかどうかも確認します。 |
| wc_pb_get_bundled_cart_item_container | バンドル カート アイテム (子) が属するコンテナ カート アイテム (親) を検索して返します。 |
| wc_pb_is_bundle_container_cart_item | カート アイテムがバンドル コンテナ カート アイテムであるかどうかを確認します。 |
| wc_pb_get_bundled_cart_items | バンドル コンテナ カート アイテム (親) に関連付けられているバンドル カート アイテム (子) を検索して返します。 |

**カート API メソッド**

| 名前 | 説明 |
| --- | --- |
| add_bundle_to_cart | バンドルを検証し、カートに追加します。バンドル設定配列が作成され、メソッドに渡される必要があります。 |
| validate_bundle_configuration | バンドル設定配列を検証します。 |

**グローバル注文関数**

| 名前 | 説明 |
| --- | --- |
| wc_pb_is_bundled_order_item | 注文品目がバンドルの一部かどうかを確認します。この関数は、注文品目のメタ情報のみに頼るのではなく、親注文品目が実際に存在するかどうかも確認します。 |
| wc_pb_get_bundled_order_item_container | バンドル注文品目 (子) が属するコンテナ注文品目 (親) を検索して返します。 |
| wc_pb_is_bundle_container_order_item | 注文品目がバンドル コンテナ注文品目かどうかを確認します。 |
| wc_pb_get_bundled_order_items | バンドル コンテナ注文品目 (親) に関連付けられているバンドル注文品目 (子) を検索して返します。 |

**注文APIメソッド**

| 名前 | 説明 |
| --- | --- |
| add_bundle_to_order | バンドルを検証し、注文に追加します。バンドル設定配列が作成され、メソッドに渡される必要があります。 |
| get_order_items | 配送設定に応じて、バンドルの親/子の注文アイテムを変更します。通常、注文データを外部のフルフィルメント、配送、または在庫管理サービスにエクスポートするときに、woocommerce_order_get_items フィルターに条件付きで接続されたコールバックとして、バンドルの正確な物理表現を再構築するために使用されます。 |
| get_product_from_item | バンドルの親/子の注文アイテムから構築された製品を変更します。通常、注文データを外部のフルフィルメント、配送、または在庫管理サービスにエクスポートするときに、woocommerce_get_product_from_item フィルターに条件付きで接続されたコールバックとして、バンドルの正確な物理表現を再構築するために使用されます。 |

**グローバル データベース関数**

| 名前 | 説明 |
| --- | --- |
| wc_pb_get_bundled_product_map | バンドルされた商品IDと、バンドルされた商品に関連付けられた商品バンドルIDのマップを返します。通常、商品がどのバンドルに属しているかを確認するために使用されます。 |

**データベース API メソッド**

| 名前 | 説明 |
| --- | --- |
| query_bundled_items | データベースからバンドルアイテムのデータを取得します。結果は複数の形式/タイプで返されます。メタクエリのサポートが含まれています。 |
| add_bundled_item | データベースにバンドルアイテムを作成します。 |
| get_bundled_item | データベースからバンドルアイテムを取得します。 |
| update_bundled_item | データベース内のバンドルアイテムを更新します。 |
| delete_bundled_item | データベースからバンドルアイテムを削除します。 |
| add_bundled_item_meta | バンドルアイテムのメタフィールドをデータベースに追加します。 |
| get_bundled_item_meta | データベースからバンドルアイテムのメタフィールドを取得します。 |
| update_bundled_item_meta | データベース内のバンドルアイテムのメタフィールドを更新します。 |
| delete_bundled_item_meta | バンドルされたアイテムのメタフィールドをデータベースから削除します。 |

**バンドルアイテムの CRUD メソッド**

| 名前 | 説明 |
| --- | --- |
| get_data | WC_Bundled_Item_Data オブジェクトに格納されているすべてのバンドル アイテム データを取得します。 |
| get_meta_data | WC_Bundled_Item_Data オブジェクトに格納されているすべてのバンドル アイテム メタデータを取得します。 |
| set_all | 指定されたデータを使用して、WC_Bundled_Item_Data オブジェクトに格納されているすべてのバンドル アイテム データを設定/更新します。 |
| set_meta_data | 指定されたデータを使用して、WC_Bundled_Item_Data オブジェクトに格納されているバンドル アイテム メタデータを設定/更新します。 |

この拡張機能は、バンドルに関連付けられた親/子カート項目を識別して操作できる次のグローバル ユーティリティ関数を提供します。

#### wc_pb_is_bundled_cart_item

**説明**

`boolean wc_pb_is_bundled_cart_item( 配列 $cart_item [, 配列 $cart_contents = false ] )`

カートアイテムがバンドルの一部であるかどうかを確認します。この関数は、カートアイテムのデータのみに頼るのではなく、親カートアイテムが実際に存在するかどうかも確認します。

**引数**

`array $cart_item` – チェックするカート項目。 `array $cart_contents` – 検索するカートの内容の配列 (オプション)。

**戻り値**

`boolean` – 説明を参照してください。

**使用法**

```
$result = wc_pb_is_bundled_cart_item( $cart_item );
```

#### wc_pb_get_bundled_cart_item_container

**説明**

`mixed wc_pb_get_bundled_cart_item_container( 配列 $cart_item [, 配列 $cart_contents = false ] [, ブール値 $return_id = false ] )`

バンドルされたカートアイテム（子）が属するコンテナカートアイテム（親）を検索して返します。渡されたカートアイテムがバンドルされたカートアイテムでない場合は、`false` 値が返されます。

**引数**

`array $cart_item` – コンテナが検索される（バンドルされた）カートアイテム。 `array $cart_contents` – 検索するカートの内容の配列（オプション）。 `boolean $return_id` – `true` に設定すると、関数はアイテム自体（見つかった場合）ではなく、見つかったコンテナアイテムのカート ID を返します（オプション）。

**戻り値**

`array|string|false` – 渡されたカートアイテムが実際にはバンドル（子）カートアイテムであり、コンテナアイテムが見つかった場合、この関数はコンテナアイテム（または、`$return_id` 引数が `true` の場合は、そのカートIDに対応する `string`）を返します。それ以外の場合は、ブール値 `false` が返されます。

**使用法**

```
$container_item = wc_pb_get_bundled_cart_item_container( $cart_item );
```

#### wc_pb_is_bundle_container_cart_item

**説明**

`ブール値 wc_pb_is_bundle_container_cart_item( 配列 $cart_item )`

カートアイテムがバンドルコンテナカートアイテムであるかどうかを確認します。バンドルされたカートアイテムの存在は確認しません。バンドル設定にバンドルアイテムが含まれていない場合もあります。

**引数**

`array $cart_item` – チェックするカート項目。

**戻り値**

`boolean` – 説明を参照してください。

**使用法**

```
$result = wc_pb_is_bundle_container_cart_item( $cart_item );
```

#### wc_pb_get_bundled_cart_items

**説明**

`配列 wc_pb_get_bundled_cart_items(配列 $cart_item [, 配列 $cart_contents = false ] [, ブール値 $return_ids = false ] )`

バンドルコンテナカートアイテム（親）に関連付けられたバンドルカートアイテム（子）を検索して返します。渡されたカートアイテムがバンドルコンテナカートアイテムでない場合は、空の `array` が返されます。

**引数**

`array $cart_item` – 子を検索するカート項目（コンテナ）。 `array $cart_contents` – 検索するカートの内容の配列（オプション）。 `boolean $return_ids` – `true` に設定すると、関数は実際の項目（見つかった場合）ではなく、見つかったバンドルされたカート項目（子）のカート ID を返します（オプション）。

**戻り値**

`array` – 渡されたカートアイテムが実際にはコンテナ（親）カートアイテムであり、それに関連付けられたバンドルカートアイテム（子）のコレクションが存在する場合、この関数は検出されたカートアイテム（または `$return_ids` 引数が `true` の場合はそれらのカートID）を含む `array` を返します。それ以外の場合は、空の `array` が返されます。

**使用法**

```
$bundled_items = wc_pb_get_bundled_cart_items( $cart_item );
```

前のセクションで説明したグローバルにアクセス可能なユーティリティメソッドに加えて、拡張機能のカートAPIには、**バンドル全体をプログラムで検証し、カートに追加するためのメソッド**も用意されています。このセクションで説明するメソッドは、`WC_PB()->cart` 経由でアクセスできる `WC_PB_Cart` インスタンスで呼び出すことができます。

#### バンドルをカートに追加

**説明**

`mixed add_bundle_to_cart( 整数 $product_id 、 整数 $quantity [、 配列 $configuration = array() ] [、 配列 $cart_item_data = array() ] )`

バンドルを検証し、カートに追加します。バンドル設定配列が作成され、メソッドに渡される必要があります。

**引数**

`integer $product_id` – カートに追加するバンドルの製品ID。`integer $quantity` – バンドルの数量。`array $configuration` – バンドル設定データ。バンドルアイテムIDでインデックス付けされたバンドルアイテム設定データの配列。バンドルアイテム設定データ値も配列であり、以下のスキーマに準拠する必要があります。

| フィールドキー | フィールドタイプ | 説明 |
| --- | --- | --- |
| product_id | 整数 | バンドル商品の ID。 |
| quantity | 整数 | バンドル商品の数量。 |
| variation_id | 整数 | 選択されたバリエーションの ID。可変タイプのバンドル商品にのみ適用されます。 |
| attribute | 配列 | バンドル商品が可変タイプの商品に関連付けられている場合に適用される、バリエーション属性名と値のインデックス。 |
| optional_selected | 文字列 | オプションのバンドル商品に適用され、バンドル商品をバンドルに含めるかどうかを示します。値: yes | no。 |
| discount | float | バンドル商品の割引。元のバンドル商品のメタ値を上書きします。「個別価格」オプションが有効になっている場合に適用されます。 |
| title | 文字列 | バンドル商品のタイトル。元のバンドル商品のメタ値を上書きします。「バンドル商品のタイトルを上書き」オプションが有効になっている場合に適用されます。 |

例：

```
$args = array(
    81 => array(
        'product_id' => 1543,
        'quantity' => 3,
    ),
    84 => array(
        'product_id' => 1386,
        'quantity' => 1,
        'variation_id' => 3535,
        'attributes' => array(
            'attribute_pa_attribute-1' => 'value-1b',
            'attribute_pa_attribute-2' => 'value-2b',
        ),

    )
);

$added = WC_PB()->cart->add_bundle_to_cart( 3520, 1, $args );
```

この例の商品バンドルには、IDが「81」と「84」の2つのバンドル商品が含まれており、それぞれ商品IDが「1543」と「1386」に関連付けられています。後者は可変商品であるため、「variation_id」フィールドと「attributes」フィールドが必要です。

`add_bundle_to_cart` に設定配列を渡すことは**必ずしも必須ではありません**。多くの場合、`add_bundle_to_cart` は、関連付けられたバンドルアイテムのタイプとメタに基づいて、有効なバンドル設定を自ら適切に構築しようとします。例えば、バンドルに可変ではなくオプションでもないアイテムが含まれている場合、設定配列を定義しなくてもバンドルをカートに安全に追加できます。同様に、バンドルアイテムの数量は常に、保存された最小数量メタ値にデフォルト設定されます。

`array $cart_item_data` – `WC_Cart::add_to_cart` に渡すカートアイテムデータフィールド (オプション)。

**戻り値**

`string|WP_Error` – 検証が成功した場合、このメソッドは追加されたバンドルコンテナアイテムのカートアイテムIDを返します。失敗した場合は、生成されたすべての検証エラーが含まれた `WP_Error` オブジェクトを返します。検証中に生成されたWooCommerceの通知は自動的には消去されず、次のフロントエンドリクエストで表示されることに注意してください。必要に応じて、`wc_clear_notices()` を呼び出して、WCセッションからそれらを消去してください。

**使用法**

```
$result = WC_PB()->cart->add_bundle_to_cart( $bundle_id, $quantity, $configuration );
```

#### バンドル構成の検証

**説明**

`boolean validate_bundle_configuration( 混合 $product 、整数 $quantity、配列 $configuration [、文字列 $context = 'add-to-cart' ] )`

バンドル設定を検証します。バンドル設定配列が作成され、メソッドに渡される必要があります。

**引数**

`integer|string|WC_Product $product` – 検証に使用する製品バンドル（またはそのID）。 `integer $quantity` – 検証中に使用するバンドルの数量。 `array $configuration` – バンドル設定配列。バンドルアイテムIDでインデックス付けされたバンドルアイテム設定データが含まれます。詳細については、[add_bundle_to_cart](https://woocommerce.com/document/bundles/bundles-functions-reference/#add_bundle_to_cart) を参照してください。 `string $context` – 検証コンテキスト（オプション、内部使用のみ）。

**戻り値**

`boolean` – 検証結果。

**使用法**

```
$result = WC_PB()->cart->validate_bundle_configuration( $bundle, $quantity, $configuration );
```

この拡張機能は、バンドルに関連付けられた親/子の注文項目を識別して操作できる次のグローバル ユーティリティ関数を提供します。

#### wc_pb_is_bundled_order_item

**説明**

`ブール値 wc_pb_is_bundled_order_item( 配列 $order_item , WC_Order $order )`

注文商品がバンドルの一部であるかどうかを確認します。この関数は、注文商品のメタ情報のみに頼るのではなく、親注文商品が実際に存在するかどうかも確認します。

**引数**

`array $order_item` – チェックする注文項目。 `WC_Order $order` – WooCommerce 注文オブジェクト。

**戻り値**

`boolean` – 説明を参照してください。

**使用法**

```
$result = wc_pb_is_bundled_order_item( $order_item, $order );
```

#### wc_pb_get_bundled_order_item_container

**説明**

`mixed wc_pb_get_bundled_order_item_container( 配列 $order_item 、 WC_Order $order [、 ブール値 $return_id = false ] )`

バンドルされた注文品目（子）が属するコンテナ注文品目（親）を検索して返します。渡された注文品目がバンドルされた注文品目でない場合は、`false` 値が返されます。

**引数**

`array $order_item` – コンテナが検索される（バンドルされた）注文アイテム。 `WC_Order $order` – 検索する WooCommerce 注文オブジェクト。 `boolean $return_id` – `true` に設定すると、関数はアイテム自体（見つかった場合）ではなく、見つかったコンテナ アイテムの注文アイテム ID を返します（オプション）。

**戻り値**

`array|integer|false` – 渡された注文項目が実際にはバンドル（子）注文項目であり、コンテナ項目が見つかった場合、この関数はコンテナ項目（または、`$return_id` 引数が `true` の場合は、その注文項目 ID に対応する `integer`）を返します。それ以外の場合は、ブール値 `false` が返されます。

**使用法**

```
$container_item = wc_pb_get_bundled_order_item_container( $order_item, $order );
```

#### wc_pb_is_bundle_container_order_item

**説明**

`ブール値 wc_pb_is_bundle_container_order_item( 配列 $order_item )`

注文品目がバンドルコンテナ注文品目であるかどうかを確認します。バンドルされた注文品目の存在は確認しません。バンドル設定にバンドル品目が全く含まれていない場合もあります。

**引数**

`array $order_item` – チェックする注文項目。

**戻り値**

`boolean` – 説明を参照してください。

**使用法**

```
$result = wc_pb_is_bundle_container_order_item( $order_item );
```

#### wc_pb_get_bundled_order_items

**説明**

`配列 wc_pb_get_bundled_order_items(配列 $cart_item 、 WC_Order $order [、ブール値 $return_ids = false ] )`

バンドルコンテナの注文項目（親）に関連付けられたバンドルされた注文項目（子）を検索して返します。渡された注文項目がバンドルコンテナの注文項目でない場合は、空の配列が返されます。

**引数**

`array $order_item` – 子アイテムを検索するカートアイテム（コンテナ）。 `WC_Order $order` – 検索する WooCommerce 注文オブジェクト。 `boolean $return_ids` – `true` に設定すると、関数は実際のアイテム（見つかった場合）ではなく、見つかったバンドルされた注文アイテム（子）の注文アイテム ID を返します（オプション）。

**戻り値**

`array` – 渡された注文項目が実際にはコンテナ（親）注文項目であり、それに関連付けられたバンドル注文項目（子）のコレクションが存在する場合、この関数は検出された注文項目（または `$return_ids` 引数が `true` の場合はそれらの注文項目 ID）を含む `array` を返します。それ以外の場合は、空の `array` が返されます。

**使用法**

```
$bundled_items = wc_pb_get_bundled_order_items( $order_item, $order );
```

前のセクションで説明したグローバルにアクセス可能なユーティリティメソッドに加えて、拡張機能の注文APIには、**バンドル全体をプログラムで検証し、注文に追加するためのメソッド**である`add_bundle_to_order`が追加されています。これは、`WC_PB()->order` を介してアクセスできる `WC_PB_Order` インスタンスで呼び出すことができます。

#### 注文にバンドルを追加する

**説明**

`mixed add_bundle_to_order( WC_Product_Bundle $product 、 WC_Order $order 、 整数 $quantity [、 配列 $args = array() ] )`

バンドルを検証し、注文に追加します。バンドル設定の配列が、`$args` 引数の `configuration` フィールドとしてメソッドに渡されます。指定されたバンドル設定の検証は、`WC_PB_Cart::validate_bundle_configuration` によって行われます。詳細は [こちら](https://woocommerce.com/document/bundles/bundles-functions-reference/#validate_bundle_configuration) に記載されています。

**引数**

`WC_Product_Bundle $product` – 注文に追加する製品バンドル。 `WC_Order $order` – バンドルを追加する注文。 `integer $quantity` – バンドルの数量。 `array $args` – バンドルコンテナの注文アイテムが追加されたときに、`WC_Order::add_product` の `$args` 引数に渡されるフィールド。バンドル構成データは、この引数の `configuration` フィールドとしてメソッドに渡されます。スキーマの詳細については、Cart API の [add_bundle_to_cart](https://woocommerce.com/document/bundles/bundles-functions-reference/#add_bundle_to_cart) メソッドを参照してください。さらに、`silent` フィールドは、次のフロントエンドリクエストで検証エラーを表示するかどうかを制御するために使用します。詳細については、以下の **戻り値** セクションを参照してください。

例：

```
$args = array(
    'configuration' => array(
        81 => array(
            'product_id' => 1543,
            'quantity'   => 3,
            'args'       => array()
        ),
        84 => array(
            'product_id'   => 1386,
            'quantity'     => 1,
            'variation_id' => 3535,
            'attributes'   => array(
                'attribute_pa_attribute-1' => 'value-1b',
                'attribute_pa_attribute-2' => 'value-2b'
            )
        )
    ),
    'silent' => false
);

$bundle = wc_get_product( 3520 );
$order  = wc_get_order( 3539 );

$added = WC_PB()->order->add_bundle_to_order( $bundle, $order, 1, $args );
```

`add_bundle_to_order` に設定配列を渡すことは**必ずしも必須ではありません**。多くの場合、`add_bundle_to_order` は、関連付けられたバンドルアイテムのタイプとメタに基づいて、有効なバンドル設定を自ら適切に構築しようとします。例えば、バンドルに可変ではなくオプションでもないアイテムが含まれている場合、設定配列を定義しなくてもバンドルを注文に安全に追加できます。同様に、バンドルアイテムの数量は常に、保存された最小数量メタ値にデフォルト設定されます。

バンドルコンテナアイテム（親）が注文に追加されると、`$args` 配列全体が `WC_Order::add_product` に渡されます。`WC_Order::add_product` の `$args` 引数にカスタムフィールドを渡す必要がある場合は、`add_bundle_to_order` の `$args` 引数にそれらを含めてください。

バンドル商品（子商品）を注文に追加するためにメソッドを呼び出す際に、`WC_Order::add_product` の `$args` 引数にカスタムフィールドを渡すこともできます。これは、メソッドに渡されるバンドル商品の設定データに `args` フィールドを追加することで実現できます。上記の例では、ID `81` のバンドル商品の設定に `args` フィールドが追加されています。

**戻り値**

`integer|WP_Error` – 検証が成功した場合、このメソッドは追加されたバンドルコンテナアイテムの注文アイテムIDを返します。失敗した場合は、生成されたすべての検証エラーがセットされた `WP_Error` オブジェクトを返します。

検証に失敗した場合、このメソッドはフロントエンドにWooCommerceの通知を表示せずに`WP_Error`オブジェクトを返します。次のフロントエンドリクエストですべての検証通知を表示するには、メソッドを呼び出す際に`$args[ 'silent' ]`フィールドを`false`に設定してください。

**使用法**

```
$result = WC_PB()->order->add_bundle_to_order( $bundle, $order, $quantity, $args );
```

#### get_order_items

**説明**

`mixed get_order_items( 配列 $order_items 、 WC_Order $order )`

配送設定に応じて、バンドルの親/子注文アイテムを変更します。バンドルの正確な物理表現を再構築するのに役立ちます。通常、注文データを外部のフルフィルメント、配送、または在庫管理サービスにエクスポートする際に、`woocommerce_order_get_items` フィルターに条件付きで接続されたコールバックとして使用されます。

方法：

- バンドルされたアイテムの合計をゼロに設定し、
- バンドルコンテナの合計に元の合計を加算します。

ここでの「組み立て済み」とは、[個別に発送](https://woocommerce.com/document/bundles/bundles-configuration/#shipping)されていないアイテムを指すことに注意してください。

**引数**

`array $order_items` – 変更されていない注文アイテムのコレクション。 `WC_Order $order` – 注文オブジェクト。

**戻り値**

`array` – 変更された注文項目のコレクション。

**使用法**

このメソッドは、製品バンドルに含まれる `WC_PB_Shipstation_Compatibility` クラスで使用され、[WooCommerce Shipstation Integration](https://woocommerce.com/products/shipstation-integration/) 拡張機能の互換性コードが含まれています。

詳細については、[こちらの注意事項](https://woocommerce.com/document/bundles/bundles-configuration/#external-order-fulfilment-note)をご参照ください。

```
$result = WC_PB()->order->get_order_items( $order_items, $order );
```

#### アイテムから製品を取得する

**説明**

`mixed get_product_from_item( WC_Product $product 、配列 $order_item 、 WC_Order $order )`

バンドルの親/子注文商品から構成される商品を変更します。バンドルの正確な物理表現を再構築するために使用されます。通常、注文データを外部のフルフィルメント、配送、または在庫管理サービスにエクスポートする際に、`woocommerce_get_product_from_item` フィルターに条件付きで接続されるコールバックとして使用されます。

この方法では、次の変更が適用されます。

- 製品オブジェクトがバンドル コンテナ アイテムに関連付けられている場合、その重量は、組み立てられたすべての子アイテムの重量を含めるように変更されます。
- 製品オブジェクトが組み立てられたバンドル/子アイテムに関連付けられている場合、仮想としてマークされます。

ここでの「組み立て済み」は、[個別発送](https://woocommerce.com/document/bundles/bundles-configuration/#shipping)されていないアイテムを指すために使用されていることに注意してください。

**引数**

`WC_Product $product` – 変更されていない製品オブジェクト。 `array $order_item` – 製品オブジェクトの作成元となった注文項目。 `WC_Order $order` – 注文オブジェクト。

**戻り値**

`WC_Product` – 変更された製品オブジェクト。

**使用法**

このメソッドは、製品バンドルに含まれる `WC_PB_Shipstation_Compatibility` クラスで使用され、[WooCommerce Shipstation Integration](https://woocommerce.com/products/shipstation-integration/) 拡張機能の互換性コードが含まれています。

詳細については、[こちらの注意事項](https://woocommerce.com/document/bundles/bundles-configuration/#external-order-fulfilment-note)をご参照ください。

```
$result = WC_PB()->order->get_product_from_item( $product, $order_item, $order );
```

この拡張機能は、データベース API を使用せずに、製品がどのバンドルに属しているかをすばやく見つけることができるグローバル データベース ユーティリティ関数として `wc_pb_get_bundled_product_map` を提供します。

#### wc_pb_get_bundled_product_map

**説明**

`配列 wc_pb_get_bundled_product_map( 混合 $product [, ブール値 $allow_cache = true ] )`

バンドルされた商品IDと、バンドルされた商品に関連付けられた商品バンドルIDのマップを返します。次の場合に便利です。

- 製品がどのバンドルに属しているかを確認します。
- 製品 ID が関連付けられているすべてのバンドルアイテム ID を取得します。

**引数**

`WC_Product|integer $product` – レコードを検索する製品（またはその ID）。 `boolean $allow_cache` – false に設定すると、内部の一時キャッシュがバイパスされ、データベース クエリが実行されます（オプション）。

**戻り値**

`array` – バンドルアイテムIDでインデックス付けされたバンドルIDの配列。同じ商品が1つのバンドルに複数回含まれる場合があり、もちろん複数のバンドルに存在する場合もあります。

**使用法**

```
$results = wc_pb_get_bundled_product_map( $product );
```

拡張機能は、[テーブル](https://woocommerce.com/document/bundles/bundles-data-structures-storage/#database-level)を操作するためのデータベース API を提供します。これには次のものが含まれます。

- `query_bundled_items`：メタクエリをサポートするデータベースクエリ用のユーティリティ関数。
- `WC_Bundled_Item_Data` CRUDクラス（次のセクションで説明）に依存する、バンドルアイテムとメタを作成、更新、削除するための多数のユーティリティ関数。

すべてのデータベース API 関数は静的であり、`WC_PB_DB` タイプで直接呼び出されることに注意してください。

#### クエリバンドルアイテム

**説明**

`配列 query_bundled_items(配列 $args)`

データベースからバンドルされたアイテムデータを取得します。結果は複数の形式/タイプで返されます。メタクエリのサポートも含まれます。

**引数**

`array $args` – クエリパラメータ:

| キー | タイプ | 説明 |
| --- | --- | --- |
| return | 文字列 | 返される結果配列のインデックス/コンテンツ/タイプを制御します。
値:

'all' – すべての woocommerce_bundled_items 列を配列形式で返します。結果は数値インデックスで表されます。
'ids' – バンドル商品 ID のみを返します。結果は数値インデックスで表されます。
'id=>bundle_id' – バンドル商品 ID とバンドル ID のマップを返します。
'id=>product_id' – バンドル商品 ID とバンドル商品 ID のマップを返します。
'objects' – 結果を数値インデックスで表された WC_Bundled_Item_Data オブジェクトとして返します。|
| bundled_item_id | integer|array | クエリに含めるバンドル商品 ID。|
| product_id | integer|array | クエリに含めるバンドル商品 ID。|
| bundle_id | integer|array | クエリに含めるバンドル商品 ID。|
| meta_query | array | メタクエリパラメータ。スキーマの詳細については、WP_Meta_Query のドキュメントを参照してください。 |

**例 #1**: バンドルされたアイテム ID のマップを取得します (ID が `99` のバンドルに含まれる製品 ID)。

```
$results = WC_PB_DB::query_bundled_items( array(
    'return'    => 'id=>product_id',
    'bundle_id' => array( 99 )
) );
```

**例 #2**: ID `41` の製品が追加されたバンドル ID をすべて取得し、最小数量を 1 より大きくします。

```
$results = WC_PB_DB::query_bundled_items( array(
    'return'     => 'id=>bundle_id',
    'product_id' => array( 41 ),
    'meta_query'      => array(
        array(
            'key'     => 'quantity_min',
            'value'   => 1,
            'compare' => '>'
        ),
    )
) );
```

**例 #3**: すべてのバンドルされたアイテム ID (バンドルを購入するのに十分な在庫がない製品 ID) のマップを取得します。

```
$results = WC_PB_DB::query_bundled_items( array(
    'return'     => 'id=>product_id',
    'meta_query' => array(
        array(
            'key'     => 'stock_status',
            'value'   => 'out_of_stock',
            'compare' => '='
        ),
    )
) );
```

**戻り値**

`array` – 結果の配列。インデックス/内容は `return` パラメータによって制御されます (上記の **引数** セクションに記載されています)。

**使用法**

```
$results = WC_PB_DB::query_bundled_items( $args );
```

#### バンドルアイテムの追加

**説明**

`mixed add_bundled_item( 配列 $data )`

データベースにバンドルされたアイテムを作成します。

**引数**

`array $data` – 作成されたバンドルアイテムに割り当てるバンドルアイテムデータとメタデータ。スキーマ:

| キー | タイプ | 説明 |
| --- | --- | --- |
| bundle_id | 整数 | バンドルアイテムが属するバンドルの ID。 |
| product_id | 整数 | バンドルアイテムに関連付けられたバンドル製品の ID。 |
| menu_order | 整数 | 同じバンドル内の他のアイテムに対するバンドルアイテムの並び順。 |
| meta_data | 配列 | メタフィールドのキー/値の配列。詳細については、「バンドルアイテムの CRUD メソッド」セクションを参照してください。 |

**戻り値**

`integer|false` – アイテムがデータベースに正常に保存された場合は作成されたバンドル アイテムの ID を返し、それ以外の場合は `false` を返します。

**使用法**

```
$result = WC_PB_DB::add_bundled_item( $data );
```

#### バンドルアイテムを取得する

**説明**

`mixed get_bundled_item(mixed $item)`

データベースからデータを取得した後、`WC_Bundled_Item_Data` オブジェクトをインスタンス化して返します。

**引数**

`integer|WC_Bundled_Item_Data $item` – インスタンス化する必要があるバンドルされたアイテムの ID、またはデータのコピー元となる既存の `WC_Bundled_Item_Data` オブジェクト。

**戻り値**

`WC_Bundled_Item_Data|false` – インスタンス化されたバンドル アイテムを返します。指定された引数が無効な場合は `false` を返します。

**使用法**

```
$item = WC_PB_DB::get_bundled_item( $item_id );
```

#### バンドルアイテムの更新

**説明**

`boolean update_bundled_item( 混合 $item 、配列 $data )`

`WC_Bundled_Item_Data` オブジェクトをインスタンス化し、その CRUD API を使用して、提供されたデータ配列のフィールドに基づいてデータベース エントリを更新します。

**引数**

`integer|WC_Bundled_Item_Data $item` – 更新が必要なバンドルアイテムのID、またはデータのコピー元（および更新元）となる既存の `WC_Bundled_Item_Data` オブジェクト。`array $data` – 更新が必要なフィールド、またはデータのコピー元となる既存の `WC_Bundled_Item_Data` オブジェクト。詳細については、[add_bundled_item](https://woocommerce.com/document/bundles/bundles-functions-reference/#add_bundled_item) メソッドの引数を参照してください。

**戻り値**

`boolean` – 更新操作の結果。

**使用法**

```
$result = WC_PB_DB::update_bundled_item( $item_id, $data );
```

#### バンドルアイテムの削除

**説明**

`void delete_bundled_item(混合$item)`

`WC_Bundled_Item_Data` オブジェクトをインスタンス化し、その CRUD API を使用してデータベース エントリを削除します。

**引数**

`integer|WC_Bundled_Item_Data $item` – 削除する必要があるバンドルされたアイテムの ID、またはデータのコピー元 (および削除元) となる既存の `WC_Bundled_Item_Data` オブジェクト。

**戻り値**

`void`

**使用法**

```
WC_PB_DB::delete_bundled_item( $item_id );
```

#### バンドルアイテムメタの追加

**説明**

`integer add_bundled_item_meta( 整数 $item_id 、文字列 $meta_key 、混合 $meta_value )`

バンドルアイテムのメタフィールドをデータベースに追加します。[add_metadata](https://codex.wordpress.org/Function_Reference/add_metadata) に依存します。

**引数**

`integer $item_id` – メタフィールドが追加されるバンドルアイテムの ID。 `string $meta_key` – メタフィールドのキー。 `mixed $meta_value` – メタフィールドの値。

**戻り値**

`integer` – 操作が成功した場合は作成されたメタフィールドの ID を返し、それ以外の場合は `0` を返します。

データベースでは、**一意のバンドルアイテムメタキー** のみが許可されます。

**使用法**

```
$result = WC_PB_DB::add_bundled_item_meta( $item_id, $meta_key, $meta_value );
```

#### get_bundled_item_meta

**説明**

`mixed get_bundled_item_meta( 整数 $item_id [, 文字列 $meta_key = '' ] )`

データベースからバンドルアイテムのメタフィールド値を取得します（`$meta_key`引数を省略した場合は、キーでインデックス付けされたすべてのメタフィールド値を取得します）。[get_metadata](https://codex.wordpress.org/Function_Reference/get_metadata)に依存します。

**引数**

`integer $item_id` – バンドルされたアイテムの ID。 `string $meta_key` – 値が要求されるメタキー (オプション)。

**戻り値**

`mixed|array|false` – 指定されたメタキーの値を返します。`$meta_key` 引数が省略されている場合は、キーでインデックスされたすべてのメタフィールドの値を返します。検索結果がない場合は、ブール値 `false` が返されます。

**使用法**

```
$value = WC_PB_DB::get_bundled_item_meta( $item_id, $meta_key );
```

#### バンドルアイテムメタの更新

**説明**

`boolean update_bundled_item_meta( 整数 $item_id 、文字列 $meta_key 、混合 $meta_value [、混合 $prev_value = '' ] )`

データベース内のバンドルアイテムのメタフィールド値を更新します。[update_metadata](https://codex.wordpress.org/Function_Reference/update_metadata) に依存します。

**引数**

`integer $item_id` – バンドルされたアイテムの ID。 `string $meta_key` – 値が更新されるメタキー。 `mixed $meta_value` – 新しいメタ値。

**戻り値**

`boolean` – 更新操作の結果。

**使用法**

```
$result = WC_PB_DB::update_bundled_item_meta( $item_id, $meta_key, $meta_value );
```

#### バンドルアイテムメタの削除

**説明**

`boolean delete_bundled_item_meta( 整数 $item_id 、文字列 $meta_key [、混合 $meta_value = '' ] [、ブール値 $delete_all = false ] )`

バンドルされたアイテムのメタフィールドをデータベースから削除します。[delete_metadata](https://codex.wordpress.org/Function_Reference/delete_metadata) に依存します。

**引数**

`integer $item_id` – バンドルされたアイテムの ID。 `string $meta_key` – 削除するメタキー。 `mixed $meta_value` – 指定されている場合、この値を持つメタフィールドのみを削除します (オプション)。 `mixed $meta_value` – 指定されている場合、`$item_id` 引数を無視して、バンドルされたすべてのアイテム ID の一致するすべてのメタフィールドを削除します (オプション)。

**戻り値**

`boolean` – 演算の結果。

**使用法**

```
$result = WC_PB_DB::delete_bundled_item_meta( $item_id, $meta_key );
```

この拡張機能は、バンドルアイテムデータのオブジェクトラッパーとして `WC_Bundled_Item_Data` クラスを使用します。インスタンス化された `WC_Bundled_Item_Data` オブジェクトは、それが表すバンドルアイテムに対するすべてのデータベース CRUD 操作も処理できるようになります。

ほとんどの場合、`WC_Bundled_Item_Data` オブジェクトをインスタンス化したり、それらのメソッドを直接呼び出したりする必要はありません。バンドルアイテムのデータベースをどうしても操作する必要がある場合は、バンドルアイテムを含む CRUD 操作にはデータベース API メソッドを使用することをお勧めします。

ただし、データベース API メソッドでは `WC_Bundled_Item_Data` オブジェクトが頻繁に使用されるため、`WC_Bundled_Item_Data` オブジェクトとデータを交換するために使用されるいくつかのメソッドを文書化しておくと便利です。

`WC_Bundled_Item_Data` 型と `WC_Bundled_Item` 型の違いを理解しておきましょう。前者はデータベースの CRUD 操作を処理するデータラッパーであり、後者のデータプロバイダーでもあります。後者はバンドルコンテキストで役立つ一連のメソッドを提供するプロダクトラッパーであり、アプリケーション層で拡張機能を使用する場合は、おそらくこちらを検討する必要があるでしょう。

これは `WC_Bundled_Item_Data` 型メソッドの網羅的なリファレンスではありません。ここで説明するメソッドは、オブジェクトデータを一括で設定/取得するために使用されるメソッドのみです。バンドルアイテムの作成と更新に関連するデータベースAPIメソッドを使用するには、交換されるデータの構造を理解する必要があります。

#### 取得データ

**説明**

`配列 get_data()`

オブジェクト内に存在するすべてのデータを返します。

**戻り値**

`array` – オブジェクトに含まれるデータ。バンドルアイテムIDを使用してインスタンス化した場合、オブジェクトには、データベースに書き込まれたすべてのバンドルアイテムデータ（関連するすべてのメタフィールドを含む）が含まれます。スキーマ：

| キー | タイプ | 説明 |
| --- | --- | --- |
| bundle_id | 整数 | バンドルアイテムが属するバンドルの ID。 |
| product_id | 整数 | バンドルアイテムに関連付けられたバンドル製品の ID。 |
| menu_order | 整数 | 同じバンドル内の他のアイテムに対するバンドルアイテムの並び順。 |
| meta_data | 配列 | メタフィールドのキー/値の配列。スキーマの詳細については get_meta_data を参照してください。 |

**使用法**

```
$data = $object->get_data();
```

#### get_meta_data

**説明**

`配列 get_meta_data()`

オブジェクト内に存在するすべてのメタデータを返します。

**戻り値**

`array` – オブジェクトに含まれるメタデータ。オブジェクトがバンドルされたアイテムIDを使用してインスタンス化された場合、このメソッドはデータベースに書き込まれたすべての関連メタフィールドを返します。スキーマ:

| キー | タイプ | 説明 |
| --- | --- | --- |
| quantity_min | 整数 | バンドル商品の最小数量。 |
| quantity_max | 整数 | バンドル商品の最大数量。 |
| override_title | 文字列 | バンドル商品のタイトルを上書きするかどうかを示します。

値: yes | no |
| title | 文字列 | バンドルされた製品のデフォルトのタイトルを上書きするときに使用するタイトル。 |
| override_description | 文字列 | バンドルされた製品の説明を上書きするかどうかを示します。

値: yes | no |
| description | 文字列 | バンドルされた製品のデフォルトの説明を上書きするときに使用する説明。 |
| optional | 文字列 | バンドルされたアイテムがオプションかどうかを示します。

値: yes | no |
| hide_thumbnail | 文字列 | 単一商品テンプレートでバンドル商品のサムネイルを非表示にするかどうかを示します。

値: yes | no |
| discount | mixed | 個別価格設定オプションが有効な場合に適用される割引。 |
| override_variations | 文字列 | デフォルトで利用可能なバリエーションをフィルタリングするかどうかを示します。

値: yes | no |
| allowed_variations | 配列 | フィルタリングが有効な場合のアクティブ/利用可能なバリエーション ID の配列。 |
| override_default_variation_attributes | 文字列 | デフォルトのバリエーション属性値をオーバーライドするかどうかを示します。

値: yes | no |
| default_variation_attributes | 配列 | 商品レベルで定義された属性を上書きするときに使用する、デフォルトのバリエーション属性のキー/値の配列。 |
| cart_visibility | 文字列 | カートテンプレートでのバンドル商品の表示/非表示。

値: visible | invisible |
| order_visibility | string | 注文/電子メール テンプレートでのバンドル アイテムの表示/非表示。

値: visible | invisible |
| single_product_visibility | string | 単一商品テンプレート内のバンドル商品の表示/非表示。

値: visible | invisible |

**使用法**

```
$meta_data = $object->get_meta_data();
```

#### すべて設定

**説明**

`配列set_all()`

指定された `$data` 配列のフィールドを使用して、オブジェクトのすべてのデータを設定/更新します。

**引数**

`array $data` – オブジェクトに設定/更新するデータ。スキーマの詳細については、[get_data](https://woocommerce.com/document/bundles/bundles-functions-reference/#get_meta_data) を参照してください。

**戻り値**

`void`

**使用法**

```
$object->set_all( $data );
```

#### メタデータの設定

**説明**

`void set_meta_data(配列 $data )`

指定された `$data` 配列のフィールドを使用して、オブジェクトのすべてのメタデータを設定/更新します。

**引数**

`array $data` – オブジェクトに設定/更新するメタデータ。スキーマの詳細については、[get_meta_data](https://woocommerce.com/document/bundles/bundles-functions-reference/#get_meta_data) を参照してください。

**戻り値**

`void`

**使用法**

```
$object->set_meta_data( $meta_data );
```

ご購入前にご質問がございましたら、こちらの[販売前フォーム](https://woocommerce.com/contact-us/#sales-form)にご記入ください。既にご購入済みでサポートが必要な場合は、ヘルプデスクから[お問い合わせください](https://woocommerce.com/my-account/marketplace-ticket-form/)！

