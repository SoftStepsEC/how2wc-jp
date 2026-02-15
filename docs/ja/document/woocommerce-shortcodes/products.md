---
title: 商品のショートコード
url: https://woocommerce.com/document/woocommerce-shortcodes/products/
---

WooCommerce は主に[ブロック](https://woocommerce.com/document/woocommerce-store-editing/)を使用して、インタラクティブかつカスタマイズ可能な商品表示設定を提供していますが、従来の**商品ショートコード**をショートコードブロックに追加することで、ストアで引き続き使用できます。このドキュメントでは、利用可能な WooCommerce の商品関連ショートコードを一覧表示し、説明します。

**注記：**

コア WooCommerce プラグインには、ショートコードに比べてより強力で柔軟な製品ブロックがいくつか含まれています。[WooCommerce ブロックの詳細](https://woocommerce.com/document/woocommerce-blocks/)をご覧ください。

`[products]` ショートコードは、WooCommerce で最も強力なショートコードの一つです。投稿ID、SKU (Stock Keeping Unit)、カテゴリー、属性別に商品を表示でき、ページネーション、ランダムソート、商品タグもサポートされています。

これにより、次のような複数のショートコードが不要になります。

- `[注目商品]`
- `[セール商品]`
- `[売れ筋商品]`
- `[最近の商品]`
- `[商品属性]`
- `[評価の高い商品]`

`[products]` ショートコードでは以下の属性を使用できます。

これらの属性は、`[products]` ショートコード内での製品の表示、順序付け、配置方法を変更します。

- `limit`: 表示する商品数。商品リストの場合はデフォルトは `-1`（全商品表示）、カテゴリーの場合は `-1`（全商品表示）です。
- `columns`: 表示する列数。デフォルトは `4` です。
- `paginate`: ページ区切りを切り替えます。`limit` と組み合わせて使用​​します。デフォルトは `false` です。ページ区切りを有効にするには `true` に設定します。
- orderby: 表示される商品を1つ以上のオプションで並べ替えます。複数のオプションを指定するには、スラッグをスペースで区切って指定します。使用可能なオプションは以下のとおりです。
- `title`: 商品のタイトル。他の属性が指定されていない場合、これがデフォルトの `orderby` モードです。
- `date`: 商品の公開日。
- `id`: 商品の投稿ID。
- `menu_order`: 設定されている場合、メニューの順序（小さい数字が先に表示されます）。
- `popularity`: 購入数。
- `rand`: ページの読み込み時に商品をランダムに並べ替えます（キャッシュを使用するサイトでは、特定の順序が保存される可能性があるため、機能しない場合があります）。
- `rating`: 商品の平均評価。
  
- `order`: `orderby` で設定された方法を使用して、商品の順序が昇順 (`ASC`) か降順 (`DESC`) かを指定します。デフォルトは `ASC` です。
- `skus`: 商品の SKU をカンマ区切りでリストします。
- `category`: カテゴリースラッグをカンマ区切りでリストします。
- `tag`: タグスラッグをカンマ区切りでリストします。
- `class`: カスタム CSS を使用してターゲットを指定および変更できる HTML ラッパークラスを追加します。
- `on_sale`: セール中の商品を取得します。`best_selling` や `top_rated` と組み合わせて使用​​しないでください。
- `best_selling`: ベストセラー商品を取得します。`on_sale` や `top_rated` と組み合わせて使用​​しないでください。
- `top_rated` は、評価の高い製品を取得します。`on_sale` または `best_selling` と組み合わせて使用​​しないでください。

`orderby` 属性を含めない場合、システムはデフォルトの並べ替え順序（最初に [メニュー順](https://woocommerce.com/document/managing-products/#advanced-section)、次にタイトル順）で商品を表示します。

これらの属性は、`[products]` ショートコードに表示される製品を決定します。

- `attribute`: 指定された属性スラッグを使用して商品を取得します。
- `terms`: `attribute` で使用する属性用語のコンマ区切りリスト。
- terms_operator: 属性用語を比較する演算子。使用可能なオプションは次のとおりです。
- `IN`: 選択した属性を持つ商品を表示します。これが `terms_operator` のデフォルト値です。
- `NOT IN`: 選択した属性に含まれない商品を表示します。
- `AND`: 選択したすべての属性を持つ商品を表示します。
  
- tag_operator : タグを比較するために使用します。使用可能なオプションは以下のとおりです。
- `IN`: 選択したタグに該当する商品を表示します。これが `tag_operator` のデフォルト値です。
- `NOT IN`: 選択したタグに該当しない商品を表示します。
- `AND`: 選択したすべてのタグに該当する商品を表示します。
  
- visibility: 選択した表示設定に基づいて商品を表示します。利用可能なオプションは以下のとおりです。
- `visible`: ショップと検索結果に表示される商品。これがデフォルトの `visibility` オプションです。
- `catalog`: ショップでのみ表示されますが、検索結果には表示されません。
- `search`: 検索結果でのみ表示されますが、ショップでは表示されません。
- `hidden`: ショップと検索の両方から非表示になり、直接URLでのみアクセスできる商品。
- `featured`: おすすめ商品としてマークされている商品。
  

- `category`: 指定されたカテゴリースラッグを使用して商品を取得します。
- `tag`: 指定されたタグスラッグを使用して商品を取得します。
- cat_operator: カテゴリー用語を比較する演算子。使用可能なオプションは次のとおりです。
- `IN`: 選択したカテゴリー内の商品を表示します。これが `cat_operator` のデフォルト値です。
- `NOT IN`: 選択したカテゴリーに含まれない商品を表示します。
- `AND`: 選択したすべてのカテゴリーに属する商品を表示します。
  

- `ids`: カンマ区切りの投稿IDリストに基づいて商品を表示します。
- `skus`: カンマ区切りのSKUリストに基づいて商品を表示します。

**注記：**

表示されるはずの商品が表示されていない場合は、「カタログの表示設定」で「非表示」に設定されていないことを確認してください。

製品IDを確認するには、「製品」画面に移動し、製品行にマウスを移動します。製品IDは、以下のように製品タイトルの下に表示されます。

これらの属性は、上記の商品コンテンツ属性と併用できません。競合が発生し、表示されない可能性があります。以下の特殊属性は**いずれか1つのみ**使用してください。

- `best_selling`: `true` に設定すると、ベストセラー商品が表示されます。
- `on_sale`: `true` に設定すると、セール中の商品が表示されます。

以下に、`[product]` ショートコードと属性 (`args`) の使用方法の例をいくつか示します。

セール商品を4つランダムに表示する方法は次のとおりです。

```
[products limit="4" columns="4" orderby="popularity" class="quick-sale" on_sale="true" ]
```

このショートコードは、4つの商品を4列（1行）で明示的に指定し、セール中の人気商品を表示します。また、カスタムCSSを使用してターゲット設定や変更が可能な「quick-sale」CSSクラスも追加します。

注目商品を 1 行に 2 つずつ、最大 4 つ表示する方法は次のとおりです。

```
[products limit="4" columns="2" visibility="featured" ]
```

このショートコードは、最大4つの商品を2列に読み込み、それらを必ずおすすめ商品として表示するよう指定しています。`orderby`属性を使用していないため、ショートコードは商品をデフォルトの並び順（[メニュー順](https://woocommerce.com/document/managing-products/#advanced-section)、次にタイトル順、`order`属性が使用されていないためデフォルトでAからZの順）で表示します。

最も売れている商品 3 つを 1 列に表示するには、次のようにします。

```
[products limit="3" columns="3" best_selling="true" ]
```

#### シナリオ4: 最新製品

この例では、最新の商品を一番最初に表示します。つまり、1行に4つの商品を表示します。これを実現するために、`Post ID`（新しい投稿ごとに増加し、商品ページの作成時に生成されます）と、orderコマンド、および`orderby`コマンドを使用します。フロントエンドからは投稿IDを確認できないため、画像の上にID番号を重ねて表示しています。

```
[products limit="4" columns="4" orderby="id" order="DESC" visibility="visible"]
```

パーカーとシャツを表示し、アクセサリーは表示しないようにする方法をご紹介します。4つずつ2列に表示するように設定します。

```
[products limit="8" columns="4" category="hoodies, tshirts" cat_operator="AND"]
```

あるいは、これらのカテゴリに含まれない製品のみを表示する場合は、`cat_operator` を `NOT IN` に更新します。

```
[products limit="8" columns="4" category="hoodies, tshirts" cat_operator="NOT IN"]
```

**注:** 制限が `8` に設定されていても、その条件に適合する製品は 4 つだけなので、4 つの製品が表示されます。

衣料品にはそれぞれ、季節に応じて「春夏」または「秋冬」の属性が付与されています。アクセサリーの中には、一年中着用できるため、両方の属性を持つものもあります。この例では、1行に3つの商品があり、「春夏」の商品がすべて表示されています。属性スラッグは「season（季節）」、属性用語は「warm（暖かい）」と「cold（寒い）」です。また、商品は新しい順に並べ替えられています。

```
[products columns="3" attribute="season" terms="warm" orderby="date"]
```

あるいは、温暖な気候の製品以外のすべてを表示する場合は、`terms_operator` として `NOT IN` を追加できます。

```
[products columns="3" attribute="season" terms="warm" terms_operator="NOT IN"]
```

**注:** 「NOT IN」を使用すると、「春夏」と「秋冬」の両方の季節に該当する商品が除外されます。これらの共通アクセサリーを含む、寒い季節に適したすべてのギアを表示したい場合は、「warm」という用語を「cold」に変更してください。

```
[products tag="hoodie"]
```

**サポート範囲:**

**サポートポリシー**に基づき、カスタマイズに関するサポートは提供できません。スニペットのカスタマイズや機能拡張が必要な​​場合は、[Woo エージェンシー パートナー](https://woocommerce.com/development-services/) または [Codeable](https://www.codeable.io/partners/woocommerce/?ref=qGefA6#tiers) の WooCommerce 開発者にご相談いただくことをお勧めします。

`[products]` ショートコードを使用すると、上記の定義済み値で商品を並べ替えることができます。また、以下のコードを使用して、**カスタムメタフィールド** で商品を並べ替えることもできます（この例では価格順）。

```
add_filter( 'woocommerce_shortcode_products_query', 'woocommerce_shortcode_products_orderby' );

function woocommerce_shortcode_products_orderby( $args ) {

    $standard_array = array('menu_order','title','date','rand','id');

    if( isset( $args['orderby'] ) && !in_array( $args['orderby'], $standard_array ) ) {
        $args['meta_key'] = $args['orderby'];
        $args['orderby']  = 'meta_value_num'; 
    }

    return $args;
}
```

このスニペットをテーマフォルダの `functions.php` ファイルに配置し、`meta_key` を編集してカスタマイズする必要があります。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

