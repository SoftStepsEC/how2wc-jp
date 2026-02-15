---
title: パーマリンク
url: https://woocommerce.com/document/permalinks/
---

*パーマリンク*はパーマネントリンクの略です。パーマリンクとは、ウェブサイトのコンテンツ（ページ、投稿、あるいはWooCommerceの場合は商品）を整理するために使用されるURL構造です。適切なURL構造は、潜在顧客や検索エンジンのクローラーにとって、効率的なナビゲーション、共有、参照を可能にします。

このページでは以下の内容を学びます:

- WooCommerce のパーマリンク分類または構造の仕組み。
- WooCommerce 製品のパーマリンクを設定する方法。

## タクソノミーパーマリンク

WooCommerce のパーマリンク設定は通常の WordPress 設定と同じ場所にあり、**WordPress > 設定 > パーマリンク** で見つけることができます。

パーマリンク構造はできる限り短くし、分類するコンテンツに関連するキーワードを含めることが効果的です。

**オプション** セクションには、WooCommerce 製品のカテゴリ、用語、属性のベースを制御する 3 つの設定があります。

- **商品カテゴリベース** – デフォルトの [商品カテゴリ](https://woocommerce.com/document/managing-product-taxonomies/#section-1) ベースは **product-category** です (例: `example.com/product-category/accessories`)。
- **商品タグベース** – デフォルトの [商品タグ](https://woocommerce.com/document/managing-product-taxonomies/#section-3) ベースは **product-tag** です (例: `example.com/product-tag/casual`)。
- **商品属性ベース** – デフォルトの [商品属性](https://woocommerce.com/document/managing-product-taxonomies/#section-6) ベースは空で、URL (例: `example.com/size/medium`) が表示されます。カスタムベース (例: `example.com/size/medium`) を追加すると、URL が返されます。 **attribute** は、URL を `yourdomain.com/attribute/size/medium` に変更します。

以下に示すように、**[製品] > [属性] > [属性名]** にある設定で [アーカイブを有効にする]** が有効になっている場合にのみ、上記の **製品属性ベース**URL 経由で属性にアクセスできます。

**WordPress > 設定 > パーマリンク > 製品パーマリンク** には、製品のパーマリンク ベースとして選択できる 4 つの設定があります。

- **デフォルト** – プレーンパーマリンクを使用する場合、*デフォルト* のみが利用可能なオプションです。ID ベースの URL（例：`example.com/?product=111`）を使用します。プレーンパーマリンク以外のパーマリンクを使用する場合、商品ベースは `example.com/product/hoodie-with-logo` になります。
- **ショップベース** – *ショップベース* はショップページ名を使用します。例：`example.com/shop/hoodie-with-logo`。
- **カテゴリ付きショップベース** – *カテゴリ付きショップベース* は、まずショップページ名を使用し、次に商品カテゴリ名を追加します。例：`yourdomain.com/shop/hoodies/hoodie-with-logo`。
- **カスタムベース** – *カスタムベース* は、商品名の前にカスタムテキストを設定します。例：`example.com/superstore/hoodie-with-logo`。

**注意:** **カスタムベース**の設定が[タクソノミーパーマリンク](https://woocommerce.com/document/permalinks/#section-2)の設定と競合しないようにしてください。例えば、**商品ベース**を「shop」に設定した場合、**商品カテゴリーベース**も「shop」に設定しないでください。これは一意でないため、競合が発生します。WordPressでは、*カテゴリー*と*商品*を区別するために、これらが一意である必要があります。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

