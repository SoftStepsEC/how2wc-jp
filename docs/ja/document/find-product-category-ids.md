---
title: 製品カテゴリIDを検索する
url: https://woocommerce.com/document/find-product-category-ids/
---

一部のWooCommerceショートコードでは、カテゴリーリストを表示するためにカテゴリーIDが必要です。このドキュメントでは、商品カテゴリーのIDを見つける方法を説明します。

詳しくは[WooCommerceに含まれるショートコード](https://woocommerce.com/document/woocommerce-shortcodes/)をご覧ください。さらに良い方法としては、[WooCommerceに含まれるブロック](https://woocommerce.com/document/woocommerce-store-editing/blocks/)と、サイト全体の編集機能をサポートするテーマを組み合わせて使用​​することを検討してください。

製品カテゴリ ID を見つけるには:

1. **「商品」>「カテゴリー」** に移動します。
2. カテゴリー名に**マウスオーバー**します。
3. **カテゴリー** または **編集** リンクを選択します。
4. ブラウザのアドレスバーを**探します**。
5. そのアドレスバーで、URL の `tag_ID=` 部分を検索します。イコール記号の後の数字がカテゴリー ID です。例えば、このスクリーンショットでは、`tag_ID=16` という部分で、**16** がこの衣料品カテゴリーの ID です。

- **商品IDを確認するには**、[商品の追加と管理に関するドキュメントの商品IDセクション](https://woocommerce.com/document/managing-products/#product-id)をご覧ください。
- 注文IDを確認するには：
- 例：`https://woocommerce.com/wp-admin/post.php?post=3572&action=edit` の場合、注文IDは `3572` です。
  
1. サイトの管理画面から、**WooCommerce > 注文** に移動します。
2. 注文番号をクリックして、「**注文編集**」ページにアクセスします。
3. ページの URL を見つけます。
4. ページの URL で、クエリ文字列「post=」を探します。このイコール記号の後の数字が注文 ID です。
- 例: `https://woocommerce.com/wp-admin/post.php?post=3572&action=edit` の場合、注文 ID は `3572` です。
    
5. これは、多くの場合、注文概要ページの注文の**番号**と同じになりますが、サイトの設定によって異なる場合があります。
  

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

