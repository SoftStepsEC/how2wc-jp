---
title: チェックアウトページでの無限読み込み/スピナー
url: https://woocommerce.com/document/endless-loadingspinner-on-the-checkout-page/
---

「注文内容の確認」ページでは、AJAX経由で支払い方法と合計金額が読み込まれます。この際、読み込み中を示すスピナーが一時的に表示されます。問題が発生した場合、このセクションが読み込まれない、またはスピナーが表示された状態のままになることがあります。

まず、**WooCommerce > ステータス** でエラーを確認する必要があります。多くの場合、エラーは強調表示されます。

一般的な原因と解決策を以下に示します。

**設定 > 一般** の URL は一致している必要があります。これは、AJAX リクエストが異なるドメイン間では機能しないためです。

詳細については、[WordPress とサイトの URL を更新する方法](https://wordpress.org/support/article/changing-the-site-url/) をご覧ください。

## その他のJavaScriptエラーと競合

テーマやプラグインはJavaScriptと競合する可能性があります。エラーを確認するには、ブラウザのエラーコンソールをご利用ください。

[テーマとプラグインの競合をテストする方法](https://woocommerce.com/document/how-to-test-for-conflicts/) の詳細をご覧ください。

ブラウザの開発者コンソールでXHRタブを開き、レスポンスを確認してください。想定されるレスポンスはJSONです。レスポンスがHTMLの場合、いくつかの原因が考えられます。多くの場合、WordPressインストールのルートディレクトリにあるindex.htmlファイルが原因です。

この問題は、index.html ファイルを削除するか、サーバー設定の indexes ディレクティブを調整して index.html よりも index.php を優先することで解決できます。一部のキャッシュプラグインは、JSON レスポンスの先頭に HTML を追加します。

-1 という応答が表示される場合もあります。これはセキュリティ エラーであり、キャッシュされた [nonce](https://codex.wordpress.org/WordPress_Nonces) によって発生します。

[他のプラグインをオフにして、デフォルトの WordPress テーマに切り替える](https://woocommerce.com/document/how-to-test-for-conflicts/)ことで競合を確認することもできます。これにより、多くの場合、問題が明らかになります。

一部のサーバーでは、チェックアウト関連のメール送信に問題が発生する場合があります。以下のフィルターを有効にすると、注文が完了するまでメールの送信を延期することができ、処理が迅速化されます。

`add_filter( 'woocommerce_defer_transactional_emails', '__return_true' );`

**注記**：

これは**開発者向け**ドキュメントです。コードの操作や潜在的な競合の解決に慣れていない場合は、大規模なプロジェクトの場合は[Woo エージェンシー パートナー](https://woocommerce.com/development-services/)にご相談いただくか、小規模なカスタマイズの場合は[Codeable](https://codeable.io/?ref=z4Hnp)でWooCommerce開発者を探すことをお勧めします。**サポートポリシー**に基づき、カスタマイズに関するサポートは提供できません。

このコードは、子テーマの`functions.php`ファイルに追加するか、[Code snippets](https://wordpress.org/plugins/code-snippets/)プラグインなど、カスタム関数を追加できるプラグインを使用する必要があります。親テーマの`functions.php`ファイルにカスタムコードを直接追加しないでください。テーマを更新すると、このファイルは完全に消去されます。

少なくとも64MBを推奨します。[WordPressのメモリ制限の引き上げ](https://woocommerce.com/document/increasing-the-wordpress-memory-limit/)をご覧ください。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

