---
title: データ構造とストレージ
url: https://woocommerce.com/document/bundles/bundles-data-structures-storage/
---

コード、pre { フォントサイズ: 85% }

このドキュメントは、WooCommerce 製品バンドルを拡張またはカスタマイズしたいと考えている WooCommerce 開発者向けに書かれています。[PHP](http://php.net/) と [WordPress 開発](http://codex.wordpress.org/Developer_Documentation) に関する高度な知識が必要です。

商品バンドルは、WooCommerce コアのすべての商品タイプと同様に、`product` 投稿タイプの [カスタム投稿タイプ](https://codex.wordpress.org/Post_Types) エントリとしてデータベースに保存されます。この拡張機能は、`product_type` タクソノミーに `bundle` ターム値を追加することで、**商品バンドル** 商品タイプを導入します。

すべてのバンドルは、コアクラス `WC_Product` を拡張した `WC_Product_Bundle` クラスのインスタンスです。当然のことながら、バンドル型製品インスタンスでは `WC_Product` クラスのすべてのメソッドを使用できます。さらに、`WC_Product_Bundle` クラスは、製品バンドルオブジェクト固有のメソッドもいくつか提供しています。すべてのメソッドの詳細なリファレンスはこのドキュメントの範囲外です。各メソッドの詳細については、クラス自体を参照してください。

`WC_Product_Bundle` オブジェクトは、データベースへのオブジェクトプロパティの読み書きに独自のデータストアを使用します。次の表は、**Bundle** タイプに固有のプロパティとメタフィールドの一覧です。

| プロパティ | メタキー | 説明 |
| --- | --- | --- |
| price | _wc_pb_base_price | バンドルの基本価格。 |
| regular_price | _wc_pb_base_regular_price | バンドルの基本通常価格。 |
| sale_price | _wc_pb_base_sale_price | バンドルの基本セール価格。 |
| bundle_stock_quantity | _wc_pb_bundle_stock_quantity | バンドル製品の在庫要件と制限を考慮した、在庫に残っているバンドルの数量。 |
| bundled_items_stock_status | _wc_pb_bundled_items_stock_status | バンドルに含まれるバンドル製品の在庫状況。
値: instock | outofstock |
| bundled_items_stock_sync_status | _wc_pb_bundled_items_stock_sync_status | bundled_items_stock_status プロパティと bundle_stock_quantity プロパティを同期する必要があるかどうかを示します。プラグインはこのプロセスをバックグラウンドで管理し、すべてのバンドルの在庫状況と在庫数量が、その内容の在庫数量/ステータスの変更と常に同期されるようにします。
値: synced | unsynced |
| virtual_bundle | _wc_pb_virtual_bundle | 「仮想」チェックボックスの状態を管理します。「仮想」ボックスにチェックが入っている場合、バンドル自体に加えて、バンドルされているすべての製品が仮想として扱われます。virtual_bundle プロパティが true の場合、仮想プロパティも true になります。virtual_bundle プロパティが false の場合、仮想プロパティはバンドルが組み立て済みか未組み立てかを制御するために使用されます。詳細については、この表に続く例を参照してください。値: yes | no |
| aggregate_weight | _wc_pb_aggregate_weight |組み立てられたバンドルを作成するときに、このプロパティは、バンドルされた製品の重量を集計し、「商品データ」>「配送」で指定された重量に追加するかどうかを制御します。
値: yes | no |
| layout | _wc_pb_layout_style | レイアウト オプション。
値: default | tabular |
| group_mode | _wc_pb_group_mode | アイテムのグループ化オプションの値。
値: parent | noindent | none |
| editable_in_cart | _wc_pb_edit_in_cart | カート内で編集オプションの値。
値: yes | no |
| sold_individually_context | _wc_pb_sold_individually_context | 個別販売オプションの値。
値: product | configuration |
| add_to_cart_form_location | _wc_pb_add_to_cart_form_location | フォームの場所オプションの値。
値: default | after_summary |
| min_bundle_size | _wcpb_min_qty_limit | 最小バンドル サイズ オプションの値。 |
| max_bundle_size | _wcpb_max_qty_limit | 最大バンドル サイズ オプションの値。 |

**例: 物理/仮想バンドル**

バンドルされたアイテムに関連付けられたデータは、投稿メタテーブルには保存されません。代わりに、バンドルの親子関係を扱う際のスケーラビリティと速度を向上させるため、拡張機能はデータベースに3つのテーブルを追加します。

- `woocommerce_bundled_items`、
- `woocommerce_bundled_itemmeta`、
- `wc_order_bundle_lookup`。

テーブル名には、WP データベース テーブル プレフィックス (通常は `wp_`) が付加されます。

`woocommerce_bundled_items` テーブルは、単純なスキーマを使用して、バンドルとバンドル製品のすべての関連付けを保存するために使用されます。

| テーブル フィールド | 説明 |
| --- | --- |
| bundled_item_id | バンドル アイテムの一意の ID。 |
| product_id | バンドル アイテムに関連付けられた製品の ID。 |
| bundle_id | 「親」製品バンドルの ID。 |
| menu_order | 同じバンドル内の他のアイテムに対するバンドル アイテムの並べ替え順序。 |

`woocommerce_bundled_itemmeta` テーブルには、バンドルされたアイテムのオプションがすべてメタデータとして保存されます。これは、WordPress で `postmeta` テーブルが `posts` テーブルのメタデータを保存するのに使用される方法に似ています。

| テーブル フィールド | 説明 |
| --- | --- |
| meta_id | メタエントリの一意の ID。 |
| bundled_item_id | 関連付けられているバンドル アイテムの ID。 |
| meta_key | メタ キー。 |
| meta_value | メタ値。 |

データベーススキーマの詳細については、`/includes/class-wc-pb-install.php` を参照してください。

プラグインは、これらのテーブルを直接操作するための [データベース API](https://woocommerce.com/document/bundles/bundles-functions-reference/#database-api-methods) を提供します。これには次のものが含まれます。

- メタクエリをサポートするデータベースクエリ用のユーティリティ関数「query_bundled_items」。
- バンドルアイテムとメタを作成、更新、削除するためのユーティリティ関数が多数あります。

バンドルアイテムのデータを取得・保存するには、`WC_Bundled_Item_Data` クラスを利用することもできます。このクラスは、バンドルアイテムの [すべての CRUD](https://woocommerce.com/document/bundles/bundles-functions-reference/#bundled-item-crud-methods) (作成、読み取り、更新、削除) 操作を処理します。詳細については、[関数リファレンス](https://woocommerce.com/document/bundles/bundles-functions-reference/) ドキュメントの [バンドルアイテム CRUD](https://woocommerce.com/document/bundles/bundles-functions-reference/#bundled-item-crud-methods) クラスに関するセクションを参照してください。

より抽象度の高いレベルでは、バンドルされたアイテムは `WC_Bundled_Item` クラスのインスタンスとして表現されます。`WC_Bundled_Item` クラスのインスタンスはすべて、自身の初期化に必要なデータを取得するために `WC_Bundled_Item_Data` クラスのインスタンスに依存しています。`WC_Product_Bundle` オブジェクトが与えられた場合、`WC_Bundled_Item` オブジェクトのコレクションを取得する最も簡単な方法は、`WC_Product_Bundle::get_bundled_items` を呼び出すことです。

`WC_Bundled_Item` クラスは、特定のバンドルのコンテキスト内に関連するバンドル商品データへのアクセスを提供します。例えば、`is_in_stock` を使用すると、バンドル商品の在庫状況を取得できます。この際、最小購入数量オプションやバリエーションフィルターの有無も考慮されます。その他の例としては、`is_optional`、`get_title`、`get_description` などがあります。詳細については、`WC_Bundled_Item` クラスのインラインメソッドのドキュメントを参照してください。

カートコンテキストでは、`WC_Product_Bundle` オブジェクトは、投稿された設定データに応じて、`woocommerce_add_to_cart` アクションでバンドル商品をカートに追加するためのトリガーとして機能します。プラグインは、投稿された設定がカートに追加可能であることを確認するために、クライアント側とサーバー側の検証を独自に実行します。

カートでは、バンドルは**カートアイテムのグループ**として表示されます。

- 製品バンドル自体に関連付けられた **コンテナ** カート項目。
- それぞれバンドル製品に関連付けられた、複数の **バンドル** カート項目。

注文を行うと、同じアイテムのグループが、それらの関係を維持するために必要ないくつかの注文アイテム メタとともに、作成された注文に保存されます。

このアプローチのおかげで:

- すべての在庫管理は WooCommerce コアに中継されます。
- バンドル商品をカート/注文に追加するプロセスは、通常コアでトリガーされるフックをバイパスしないため、サードパーティ製プラグイン/拡張機能との互換性が大幅に簡素化されます。
- コンテナカート/注文アイテムを使用すると、アプリケーション層で子アイテムの物理プロパティを簡単にオーバーライドできます。これは、[複雑な配送要件](https://woocommerce.com/document/bundles/bundles-configuration/#shipping) のあるユースケースで役立ちます。
- カート内でバンドルレベルとバンドル商品レベルの価格を明確に区別することで、高度な価格設定スキームの実装が容易になり、各バンドル商品の個別の税率を維持できます。

親/子**カート アイテム** は、カート アイテムに次のフィールドを追加することによって識別されます。

| フィールド | タイプ | アイテム コンテキスト | 説明 |
| --- | --- | --- | --- |
| bundled_by | 文字列 | Bundled | このバンドル カート アイテムが属するコンテナ カート アイテムのカート アイテム ID。 |
| bundled_items | 配列 | Container | このバンドル コンテナ アイテムに関連付けられているすべてのバンドル カート アイテムのカート アイテム ID。 |
| stamp | 配列 | Bundled/Container | バンドル構成データを含む配列。a) グループ全体を一意に識別し、b) カート内検証を実行するために使用されます。 |
| bundled_item_id | 文字列 | Bundled | このバンドル カート アイテムに関連付けられているバンドル アイテム ID。上記の製品データ セクションのデータベース スキーマを参照してください。 |

このデータは、バンドルに関連付けられた**カートアイテムの親子関係を確立**するために内部的に使用されます。拡張機能は、以下の目的で使用できるグローバルユーティリティ関数を提供します。

- カートアイテムがバンドルアイテムかどうかを確認し、その親を取得します。
- カートアイテムがバンドルコンテナアイテムかどうかを確認し、その子を取得します。

詳細については、[関数リファレンス](https://woocommerce.com/document/bundles/bundles-functions-reference/)の[カート](https://woocommerce.com/document/bundles/bundles-functions-reference/#global-order-functions)セクションを参照してください。

親/子の**注文アイテム**は、次の注文アイテムメタを作成することによって識別されます。

| キー | タイプ | アイテム コンテキスト | 説明 |
| --- | --- | --- | --- |
| _bundle_cart_key | 文字列 | Bundled/Container | この注文アイテムを識別する元のカートアイテム ID (またはその他の一意のハッシュ)。 |
| _bundled_by | 文字列 | Bundled | このバンドル注文アイテムが属するコンテナ カートアイテムの一意のハッシュ。 |
| _bundled_items | シリアル化された配列 | Container | このバンドル コンテナアイテムに関連付けられているすべてのバンドルアイテムの一意のハッシュ。 |
| _stamp | シリアル化された配列 | Bundled/Container | バンドル構成データを含むシリアル化された配列。a) グループ全体を一意に識別し、b) 再注文時にカート内検証を実行するために使用されます。 |
| _bundled_item_id | 文字列 | Bundled | このバンドル注文アイテムに関連付けられたバンドルアイテム ID。上記の製品データ セクションのデータベース スキーマを参照してください。 |
| _bundled_item_priced_- _individually | 文字列 | バンドル | 注文時にアイテムが個別に価格設定されたかどうかを示します。 |
| _bundled_item_needs_- shipping | 文字列 | バンドル | 注文時にバンドルアイテムをバンドルから個別に配送する必要があったかどうかを示します。 |
| _bundle_weight | 数値 | コンテナ | 注文時のバンドルコンテナの単位あたりの総重量。可変コンテナ重量を使用する場合は、[配送] タブの [重量] フィールドで定義された値と異なる場合があります。 |

このデータは、バンドルに関連付けられた**注文アイテムの親子関係を確立**するために内部的に使用されます。拡張機能は、以下の目的で使用できるグローバルユーティリティ関数のセットを提供します。

- 注文アイテムがバンドルアイテムであるかどうかを確認し、その親を取得します。
- 注文アイテムがバンドルコンテナアイテムであるかどうかを確認し、その子を取得します。

詳細については、[関数リファレンス](https://woocommerce.com/document/bundles/bundles-functions-reference/)の[注文](https://woocommerce.com/document/bundles/bundles-functions-reference/#global-order-functions)セクションを参照してください。

ご購入前にご質問がございましたら、こちらの[販売前フォーム](https://woocommerce.com/contact-us/#sales-form)にご記入ください。既にご購入済みでサポートが必要な場合は、ヘルプデスクから[お問い合わせください](https://woocommerce.com/my-account/marketplace-ticket-form/)！

