---
title: テンプレートの構造とテーマによるテンプレートの上書き
url: https://woocommerce.com/document/template-structure/
---

<ul class="documentation_categories">
<li class="documentation_category">テーマ設定</li>
<li class="documentation_category">クラシックテーマの開発</li>
</ul>
**注意** このドキュメントでは、PHP テンプレートを使用するクラシックテーマについて言及しています。HTML テンプレートを使用するブロックテーマを開発している場合は、[ブロックテーマのテーマ設定に関するドキュメント](https://woocommerce.com/docs/theming/block-theme-development/theming-woo-blocks/)をご確認ください。概要

## 概要​

WooCommerce テンプレート ファイルには、ストアのフロントエンドと HTML メールのマークアップとテンプレート構造が含まれています。

## テンプレートリスト​

WooCommerceサイト上の各種テンプレートファイルは、FTPクライアントまたはホストのファイルマネージャーから「/wp-content/plugins/woocommerce/templates/」ディレクトリに保存されています。また、[GitHubリポジトリ](https://github.com/woocommerce/woocommerce/blob/trunk/docs/theme-development/template-structure.md)からもダウンロードできます。

注: 古いバージョンのテンプレート ファイルを探している場合は、次のパスで見つけることができます。

- バージョン 6.0.0 以降: https://github.com/woocommerce/woocommerce/tree/[VERSION_NUMBER]/plugins/woocommerce/templates
- たとえば、WooCommerce 9.4.0 のテンプレートファイルを見つけるには、[https://github.com/woocommerce/woocommerce/tree/9.4.0/plugins/woocommerce/templates](https://github.com/woocommerce/woocommerce/tree/9.4.0/plugins/woocommerce/templates) に移動します。
  
- 6.0.0 より前のバージョン: https://github.com/woocommerce/woocommerce/tree/[VERSION_NUMBER]/templates
- たとえば、WooCommerce 5.9.0 のテンプレートファイルを見つけるには、[https://github.com/woocommerce/woocommerce/tree/5.9.0/templates](https://github.com/woocommerce/woocommerce/tree/5.9.0/templates) に移動します。
  

## フックによるテンプレートの変更​

テンプレートファイルを開くと、すべてのテンプレートに*フック*が含まれていることに気づくでしょう。フックを使うと、テンプレートファイル自体を編集することなくコンテンツを追加・移動できます。フックとは、あるコードが別のコードと特定の定義済みの場所でやり取り・変更を行うための方法です。この方法を使うと、テーマ内の特定の場所に「フック」するコードスニペットを実装できます。テンプレートファイルは全く変更せず、子テーマの設定も不要なので、アップグレード時の問題を回避できます。

[/wp-content/plugins/woocommerce/templates/emails/admin-new-order.php](https://github.com/woocommerce/woocommerce/blob/8.9.0/plugins/woocommerce/templates/emails/admin-new-order.php) を見て、フックがどのようになっているか確認してみましょう。30行目から始まる以下のコードは、新規注文メールの注文詳細セクションを生成する役割を果たしています。

```
/* * @hooked WC_Emails::order_details() Shows the order details table. * @hooked WC_Structured_Data::generate_order_data() Generates structured data. * @hooked WC_Structured_Data::output_structured_data() Outputs structured data. * @since 2.5.0 */do_action( 'woocommerce_email_order_details', $order, $sent_to_admin, $plain_text, $email );
```

上記のコードは、下の画像で赤く強調表示されているブロックを出力します。これは、サイトでの注文が成功した後にショップ マネージャーが受信する新規注文メールです。

以下のコードは、必要な機能を構築するための出発点として使用できます。その後、コードスニペットプラグインに追加することで、テンプレート自体を編集することなく、テンプレート内の特定の場所の出力を変更できます。テンプレート内の他のフックについても、同様のことが当てはまります。

```
add_action( 'woocommerce_email_order_details', 'my_custom_woo_function');function my_custom_woo_function() {    /* Your code goes here */}
```

## ファイルを編集してテンプレートを変更する

プラグインや親テーマ内のファイルを直接編集すると、サイトの動作が停止する可能性のあるエラーが発生するリスクがあります。しかし、さらに重要なのは、この方法で行った変更は、プラグインやテーマがアップデートされると消えてしまうことです。アップデートとは、古いバージョンを完全に削除し、新しいバージョンに置き換えるプロセスです。

代わりに、[子テーマを設定する](https://developer.woocommerce.com/docs/how-to-set-up-and-use-a-child-theme/)という方法をお勧めします。これにより、自動的に更新されない上書き変更を行うための安全なディレクトリが作成されます。

この例では、子テーマを「storefront-child」と名付けます。「storefront-child」を使用することで、オーバーライドを使用することで、アップグレード時にも安全に編集を行うことができます。テンプレートを子テーマ内の「/storefront-child/woocommerce/」というディレクトリにコピーします。ファイル構造はそのままに、「/templates/」サブディレクトリは削除してください。

この例では、管理者の注文通知を上書きするには、`wp-content/plugins/woocommerce/templates/emails/admin-new-order.php` を `wp-content/themes/storefront-child/woocommerce/emails/admin-new-order.php` にコピーします。

コピーしたファイルは WooCommerce のデフォルトのテンプレート ファイルを上書きするので、コピーしたファイルに必要な変更を加え、それが結果の出力に反映されるのを確認できます。

**注** テンプレートがアップグレード対応であることの（望ましい）副作用として、WooCommerce コアテンプレートは更新されますが、カスタムオーバーライドは更新されないという点があります。システムステータスレポートに、「バージョン 3.5.0 は古くなっています。コアバージョンは 3.7.0 です」といった通知が表示される場合があります。その場合は、「古くなった WooCommerce テンプレートの修正」ガイドに従って、適切なバージョンに更新してください。

## カスタムテンプレートのテーマサポートを宣言する

テーマ開発者の方、またはカスタムテンプレートを含むテーマをご利用の場合は、`add_theme_support` 関数を使用して WooCommerce テーマのサポートを宣言する必要があります。GitHub の [テーマでの WooCommerce サポートの宣言](https://github.com/woocommerce/woocommerce/wiki/Declaring-WooCommerce-support-in-themes) をご覧ください。

テーマに `woocommerce.php` が含まれている場合、`woocommerce/archive-product.php` カスタムテンプレートをテーマ内で上書きすることはできません。これは、`woocommerce.php` が他のテンプレートファイルよりも優先されるためです。これは表示の問題を防ぐためです。

Wooストアの編集でサポートが必要ですか？WooExpert代理店がお手伝いします。WooExpertは、高度にカスタマイズされ、拡張性の高いオンラインストアの構築で実績のある信頼できる代理店です。[エキスパートを雇う](https://woocommerce.com/customizations/)

