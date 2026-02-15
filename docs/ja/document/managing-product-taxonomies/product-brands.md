---
title: 製品ブランド
url: https://woocommerce.com/document/managing-product-taxonomies/product-brands/
---

WooCommerce のブランドは、それぞれに名前、説明、画像を割り当てて、ショップのブランドを作成するための追加の便利な方法を提供します。

ブランドの追加を開始するには:

1. **WooCommerce >** **商品 > ブランド** に移動します。インターフェースの見た目と操作方法は、カテゴリやタグを追加する場合と似ています。左側のフォームでブランドを追加すると、右側に表示されます。
2. **名前と説明を入力** します。画像は任意です。ブランドは階層化でき、「親」ブランドの下に「子」ブランドを指定できます。
3. **「新しいブランドを追加」** を選択して保存します。

ブランドを変更するには、名前にマウスを移動して**編集**または**削除**をクリックします。ブランドはドラッグアンドドロップで**並べ替え**ることもできます。

*ご存知ですか？* 商品にブランドを割り当てると、商品ページにブランド名スキーマが追加され、SEO対策に役立ちます。ちなみに、商品にブランドを割り当てる手順は、カテゴリーやタグを追加する手順と同じです。

1. **WooCommerce > 商品** へ移動します。
2. ブランドを割り当てる**商品を選択**します。
3. 右側のサイドバーにある**ブランド**ボックスを見つけます。
4. 商品に割り当てる**ブランドのボックスにチェックを入れます**。
5. 変更を保存するには**更新または公開**します。

サイト全体でブランドを様々な方法で表示するには、以下のショートコードをご利用いただけます。これらのショートコードは複雑なコードを呼び出す方法であり、数回のキー操作で多くのオプションを提供します。

ショートコードを使用するには、「[」で始まり「]」で終わるテキストをコピーし、エディターに貼り付けます。例えば、「[product_brand]」は、単一商品ページにブランドの画像を表示します。

#### 製品ブランド

単一のブランドの画像とアーカイブページへのリンクを表示します。これは単一の商品ページでのみ機能し、投稿や他のWordPressページでは機能しません。このショートコードを使用して単一のページにブランドを表示した場合、すべてのブランドではなく、1つのブランドのみが取得されることに注意してください。

```
array(
      'width' => '64px',
      'height' => '64px',
      'class' => 'aligncenter'
 )
```

**ショートコードの例:**

```
[product_brand class="alignright"]
```

#### ブランド製品

特定のブランドのすべての製品を表示します。

```
array(
      'per_page' => '12',
      'columns' => '4',
      'orderby' => 'title',
      'order' => 'asc',
      'category' => 'boots,sandals',
 )
```

**ショートコードの例:**

```
[brand_products brand="hiro-shoes" per_page="12" columns="4"]
```

#### 製品ブランドリスト

すべてのブランドの A-Z インデックスとアーカイブ ページへのリンクを表示します。

```
array(
      'show_top_links' => 'true',
      'show_empty_brands' => 'false'
 )
```

**ショートコードの例:**

```
[product_brand_list show_empty_brands="true"]
```

#### 製品ブランドのサムネイル

すべての製品ブランドのサムネイルのリストとアーカイブへのリンクを表示します。

```
array(
      'columns' => '12',
      'show_empty' => 'true',
      'orderby' => 'name',
      'exclude' => '2,5,8', // Category IDs to exclude
      'number' => '' // Number of brands to show.
 )
```

**ショートコードの例:**

```
[product_brand_thumbnails number="12" show_empty="false"]
```

#### 製品ブランドのサムネイルの説明

すべての製品ブランドのサムネイルのリストを、ブランドの説明とアーカイブへのリンクとともに表示します。

```
array(
      'columns' => '12',
      'show_empty' => 'true',
      'orderby' => 'name',
      'exclude' => '2,5,8', // Category IDs to exclude
      'number' => '' // Number of brands to show.
 )
```

**ショートコードの例:**

```
[product_brand_thumbnails_description number="12" show_empty="false"]
```

ショートコードを複数の製品ページに表示するには、次のように **do_shortcode** 関数を使用して、テンプレートまたはフックに追加する必要があります。

```
echo do_shortcode('[product_brand width="64px" height="64px" class="alignright"]')
```

状況によっては、次に示すように、製品に関連付けられたブランドイメージを製品ページに表示したい場合があります。

これを実装するには、単一の製品ベースで実装するか、すべての製品に適用するかの 2 つの方法があります。

#### 単一の製品に適用するには

商品本体エリアにショートコードを追加できます

```
[product_brand width="64px" height="64px" class="alignright"]
```

この例では、商品のブランドにリンクし、幅と高さをピクセル単位で指定（それぞれ64ピクセル）し、右側に揃えます。「class」フィールドは必須ではありません。デフォルトでは「aligncenter」に設定されていますが、leftまたはrightを指定することもできます。

#### すべての製品に適用するには

まず、子テーマで編集を行っていることを確認します。

これにより、アップデートによって作業内容が削除されるリスクなしに、コンテンツをカスタマイズできます。子テーマのカスタマイズ方法の詳細については、[子テーマのチュートリアル](http://woothemes.zendesk.com/entries/22505632-How-to-setup-and-use-a-child-theme)をご覧ください。または、[WordPress Codex](http://codex.wordpress.org/Child_Themes)で子テーマの仕組みについて詳しくお読みください。

子テーマで、functions.php ファイルに移動し、次のスニペットを追加します。

| | add_action( 'woocommerce_single_product_summary', 'wc_ninja_add_brand_to_product_page', 19 ); |
| | function wc_ninja_add_brand_to_product_page() { |
| | echo do_shortcode('[product_brand width="64px" height="64px" class="alignright"]'); |
| | } |

[Code Snippets](https://wordpress.org/plugins/code-snippets/)のようなプラグインを使用してこのスニペットを追加することもできます。

これにより、次のロゴの位置が実現します。このロゴはすべての製品ページに表示され、ブランドに合わせて動的に変化します。

デフォルトでは、カスタムコードなしでは商品ページにブランド名を追加できません。以下のスニペットを使用すればブランド名を表示できますが、サポート対象外となります。

まず、子テーマで編集を行っていることを確認します。

これにより、アップデートによって作業内容が削除されるリスクなしに、コンテンツをカスタマイズできます。子テーマのカスタマイズ方法の詳細については、[子テーマのチュートリアル](http://woothemes.zendesk.com/entries/22505632-How-to-setup-and-use-a-child-theme)をご覧ください。または、[WordPress Codex](http://codex.wordpress.org/Child_Themes)で子テーマの仕組みについて詳しくお読みください。

子テーマで、functions.php ファイルに移動し、次のスニペットを追加します。

| | <?php |
| | | | | | /* |
| | * 7行目の `1` を増やしてブランド名の位置を移動します |
| | */ |
| | | | | add_action( 'woocommerce_single_product_summary', 'wc_brands_add_brand_name', 1 ); |
| | | | | | function wc_brands_add_brand_name() { |
| | global $product; |
| | $brands = implode(', ', wp_get_post_terms($product->get_id(), 'product_brand', ['fields' => 'names'])); |
| | echo "<p>Brand: " . $brands . "</p>"; |
| | } |

[Code Snippets](https://wordpress.org/plugins/code-snippets/)のようなプラグインを使用してこのスニペットを追加することもできます。

以下にリストされているブランド ウィジェットをサイトに追加する方法の詳細については、[WooCommerce に含まれるウィジェット](https://woocommerce.com/document/woocommerce-widgets/) を参照してください。

このウィジェットには、現在表示されているブランド アーカイブの説明が表示されます。

このウィジェットは、ブランド別に商品を分類するための**階層型ナビゲーション**を提供します。このウィジェットは[他の階層型ナビゲーションWooCommerceウィジェット](https://woocommerce.com/document/woocommerce-widgets/#section-2)と連携し、必要に応じて使用できます。

このウィジェットにはサムネイル付きのブランドがリストされます。

バージョン1.5以降はREST APIをサポートしています

ブランドREST APIを使用すると、ブランドを個別に、または一括で作成、表示、更新、削除できます。エンドポイントは `/wp-json/wc/v1/products/brands` で、基本的に `/wp-json/wc/v1/products/categories` を模倣しています。[商品カテゴリREST API](https://woocommerce.github.io/woocommerce-rest-api-docs/#product-categories) のドキュメントも参照できます。

`/products/brands` エンドポイントに加えて、`/products` エンドポイントも更新され、レスポンスに `brands` が表示され、`brands` の JSON リクエストがチェックされるようになりました。

- すべての製品ブランドを取得する: `curl https://example.com/wp-json/wc/v2/products/brands -u consumer_key:consumer_secret`
- 製品ブランドを作成する: `curl -X POST https://example.com/wp-json/wc/v2/products/brands \ -u consumer_key:consumer_secret \ -H "Content-Type: application/json" \ -d '{ "name": "Apple", "image": { "src": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/768px-Apple_logo_black.svg.png" } }'`
- 製品ブランドを削除する: `curl -X DELETE https://example.com/wp-json/wc/v2/products/brands/9?force=true -u consumer_key:consumer_secret`
- 製品にブランドを設定します: `curl -X PUT https://example.com/wp-json/wc/v2/products/123 \ -u consumer_key:consumer_secret \ -H 'Content-Type: application/json' \ -d '{"brands": [48, 49]}'` 注: 製品にブランドを設定する場合、URL は `products/123` である必要があります。ここで `123` は更新する製品の ID です。

商品URLに商品ブランドを表示するには、**設定 > パーマリンク** にアクセスし、必要に応じて `%product_brand%` を **商品パーマリンク** 設定に追加してください。注: `%product_brand%` には、`shop` をベースとして指定する必要があります: `/shop/%product_brand%`

WooCommerce に組み込まれている [製品のインポート/エクスポート機能](https://woocommerce.com/document/product-csv-importer-exporter/) は、ブランドが分類法に保存されている一方で、現在はデフォルト フィールド + メタ フィールドのみを処理するため、[製品 CSV インポート スイート](https://woocommerce.com/products/product-csv-import-suite/) 拡張機能と機能が同等ではありません。

そのため、商品CSVインポートスイートはまさにこの作業に最適なツールです。CSVファイルに「tax:product_brand」という見出しの列を追加し、その列にブランド名を入力することで、ブランド情報が商品に紐付けられます。

はい。**WooCommerce Brands** をインストールすると、商品編集ページの **Google Listings and Ads** タブにブランド属性の新しいオプションが表示されます。各商品を編集し、ブランド属性を「From WooCommerce Brands」に設定できます。

テーマの `functions.php` ファイルに以下を追加します。

| | add_filter( 'woocommerce_sortable_taxonomies', 'wt_sort_brands' ); |
| | function wt_sort_brands( $sortable ) { |
| | $sortable[] = 'product_brand'; |
| | return $sortable; |
| | } |

ブランドのサムネイルは、バックエンドに表示される順序と同じ順序で整理されます。

各ブランドには独自のアーカイブがあり、http://domain.com/`brand`/brand-slug/ で閲覧できます。上記のURL構造の `brand` セクションは、テーマの `functions.php` ファイルまたはカスタム機能プラグインに以下のスニペットを追加することで調整できます。

| | function customise_product_brand_slug ( $tax ) { |
| | $tax['rewrite']['slug'] = 'custom-slug'; // 'custom-slug' を任意のスラッグに置き換えます。 |
| | return $tax; |
| | } |
| | add_filter( 'register_taxonomy_product_brand', 'customise_product_brand_slug' ); |

**設定 > パーマリンク** に移動し、上記のコードスニペットを追加して再度保存してください。これにより、パーマリンクが更新され、新しいブランドスラッグが使用できるようになります。

以下のコードスニペットで、ご自身のBrands親ページのページIDを取得し、適切なページIDに置き換えてください。例ではIDが14のページを使用しましたが、ご自身のページIDに変更してください。以下のコードを子テーマの`functions.php`ファイル、またはカスタム機能プラグインに追加してください。

| | function wc_custom_brands_breadcrumb( $crumbs, $breadcrumb ){ |
| | | | | | // ブランドのトップ アーカイブとして機能するページの ID |
| | $page_url = get_the_permalink(14); |
| | | | | | foreach( $crumbs as $key => $crumb ){ |
| | if( $crumb[0] === __('Brands') ) { |
| | // 上記のスニペットでスラッグを変更した場合 |
| | // パンくずリストには引き続き Brand と表示されるため、 |
| | // 以下の 'Name' を希望のパンくずリスト テキストに置き換えます |
| | // それ以外の場合は、次のコード行を完全に削除します |
| | $crumbs[$key][0] = __( 'Name', 'woocommerce' ); |
| | $crumbs[$key][1] = $page_url; |
| | } |
| | } |
| | | | | return $crumbs; |
| | } |
| | add_filter( 'woocommerce_get_breadcrumb', 'wc_custom_brands_breadcrumb', 20, 2 ); |

| | <?php |
| | if ( is_plugin_active( 'woocommerce-brands/woocommerce-brands.php' ) ) { |
| | | | | | add_action( 'woocommerce_shop_loop_item_title', 'add_brands_to_product_loop' ); |
| | | | | // 商品ループにブランドを追加します。 |
| | function add_brands_to_product_loop() { |
| | $terms = get_the_terms( get_the_ID(), 'product_brand' ); |
| | if ( ! empty( $terms ) && ! is_wp_error( $terms ) ) { |
| | $term = join( ', ', wp_list_pluck( $terms, 'name' ) ); |
| | echo esc_html( $term ); |
| | } |
| | } |
| | } |

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

