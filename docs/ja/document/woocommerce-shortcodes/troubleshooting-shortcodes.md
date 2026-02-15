---
title: ショートコードのトラブルシューティング
url: https://woocommerce.com/document/woocommerce-shortcodes/troubleshooting-shortcodes/
---

このページでは、WooCommerce ショートコードが期待どおりに動作しない一般的な理由をいくつか紹介します。

ショートコードが正しく貼り付けられているのに正しく表示されない場合は、ショートコードが `<pre>` タグで囲まれていないことを確認してください。

これらのタグを削除するには、ページを編集し、[**テキスト**] タブをクリックします。

よくある問題は、**波型**引用符 (`“`) ではなく、**直線**引用符 (`"`) が使用されている場合です。ショートコードを正しく機能させるには、直線引用符を使用する必要があります。

SKU ショートコード (例: `[products skus="sku-name"]`) を使用する場合は、*製品データ > 可変製品 > バリエーション > バリエーション名 > SKU* のバリエーション名 SKU は使用しないでください。

解決策としては、代わりに**親変数製品**の*製品データ*メタボックス（*製品データ > 変数製品 > 在庫 > SKU*）のSKUを使用することです。

**注:**[サポートポリシー](https://woocommerce.com/support-policy/)に基づき、カスタマイズに関するサポートは提供できません。スニペットのカスタマイズや機能拡張が必要な​​場合は、資格のあるWordPress/WooCommerce開発者にご相談ください。[Codeable](https://codeable.io/?ref=z4Hnp)または[Woo Agency Partner](https://woocommerce.com/development-services/)のご利用を強くお勧めします。

**製品カテゴリリスト**ブロックには、最上位カテゴリとサブカテゴリを含むすべての製品カテゴリのリストが表示されます。最上位カテゴリのみを表示することはできません。

以下のスニペットは、新しいショートコード「[top_level_product_categories_list]」を追加します。このショートコードは**最上位の商品カテゴリーの箇条書きリスト**のみを出力します。[子テーマ](https://developer.woocommerce.com/docs/how-to-set-up-and-use-a-child-theme/)の`functions.php`ファイルに追加するか、コードスニペット拡張機能/プラグイン経由で追加してください。

| | <?php |
| | /* |
| | * ショートコードは [top_level_product_categories_list] です |
| | */ |
| | add_shortcode('top_level_product_categories_list', 'wc_shortcode_top_level_product_categories_list'); |
| | | | | | function wc_shortcode_top_level_product_categories_list() { |
| | | | | | | ob_start(); |
| | | | | | $args = array( |
| | 'taxonomy' => 'product_cat', |
| | 'parent' => 0 |
| | ); |
| | | | | | | $product_categories = get_categories($args); |
| | | | | | | echo '<ul>'; |
| | | | | | | foreach ($product_categories as $category) { |
| | echo '<li><a href="' . get_term_link($category->slug, 'product_cat') . '">' . $category->name . '</a></li>'; |
| | } |
| | | | | echo '</ul>'; |
| | | | | | return ob_get_clean(); |
| | } |

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

