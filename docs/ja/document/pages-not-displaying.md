---
title: WooCommerceページが表示されない
url: https://woocommerce.com/document/pages-not-displaying/
---

WooCommerce ページが正しくインストールされない、またはコンテンツが正しく表示されないなどの問題が発生している場合は、次の方法で解決できます。

1. 新しいページを作成します。
2. 正しいページのショートコードを追加します。
3. **公開** をクリックします。
4. WooCommerce 2.1.x より前のバージョンをお使いの場合は、*WooCommerce > 設定 > *タブ** に移動して、新しく作成したページを選択します (*タブ* は編集する WooCommerce セクションです)。
5. WooCommerce 2.1.x より後のバージョンをお使いの場合は、*WooCommerce > 設定 > 一般* に移動します。
6. **保存** をクリックします。

**注:** このドキュメントは、考えられるすべてのケースを網羅しているわけではありません。サイトに競合が発生していないかどうかを確認するには、[トラブルシューティングガイド](https://woocommerce.com/document/woocommerce-self-service-guide/)[i](https://woocommerce.com/document/woocommerce-self-service-guide/)[de](https://woocommerce.com/document/woocommerce-self-service-guide/)を確認することをお勧めします。

[WooCommerce 2.1](https://developer.woocommerce.com/2014/02/10/woocommerce-2-1-is-live/) より前は、アカウント管理ページと注文の「ありがとうございます」ページは個別のページとして使用されていました。バージョン2.1以降、これらのページはエンドポイントになりました。

[WooCommerce エンドポイントの詳細](https://developer.woocommerce.com/docs/woocommerce-endpoints/)をご覧ください。

**注:** WooCommerce は従来、ページに動的なコンテンツや機能を追加するためにショートコードを利用してきました。WordPress の進化に伴い、その焦点はショートコードから、よりインタラクティブで視覚的に統合されたブロックへと移行しました。[WooCommerce ブロックの詳細](https://woocommerce.com/document/woocommerce-store-editing/blocks/)をご覧ください。ブロックエディターはインタラクティブにカスタマイズ可能なブロックと強化された編集機能を提供していますが、多くのストアでは依然としてショートコードが多用されていることも認識しています。これらの従来のショートコードは、[ショートコードブロック](https://wordpress.org/documentation/article/shortcode-block/)内に追加することで引き続きご利用いただけます。

WooCommerce **2.1 以降** を使用している場合、ページショートコードは次のようになります。

- `[woocommerce_cart]`: カートページを表示します。
- `[woocommerce_checkout]`: チェックアウトページを表示します。
- `[woocommerce_order_tracking]`: 注文追跡フォームを表示します。
- `[woocommerce_my_account]`: ユーザーアカウントページを表示します。

以前は、WooCommerce **2.1 より前のバージョン** のページショートコードは次のとおりでした。

- `[woocommerce_edit_account]`: *アカウント編集*ページを表示します。
- `[woocommerce_edit_address]`: ユーザーアカウントの*住所編集*ページを表示します。
- `[woocommerce_change_password]`: *パスワード変更*ページを表示します。
- `[woocommerce_view_order]`: ユーザーアカウントの*注文表示*ページを表示します。
- `[woocommerce_logout]`: ログアウトページを表示します。
- `[woocommerce_pay]`: チェックアウトの*支払い*ページを表示します。
- `[woocommerce_thankyou]`: *注文受付*ページを表示します。
- `[woocommerce_lost_password]`: *パスワード紛失*ページを表示します。

[WooCommerce に含まれているショートコードを確認してください](https://woocommerce.com/document/woocommerce-shortcodes/)。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

