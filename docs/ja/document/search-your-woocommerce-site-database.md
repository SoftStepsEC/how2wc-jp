---
title: WooCommerceサイトのデータベースを検索する
url: https://woocommerce.com/document/search-your-woocommerce-site-database/
---

WooCommerce サイトで WordPress データベースを検索すると、製品の詳細、注文履歴、顧客データなどの重要な情報をすばやく見つけて管理できます。

**注:**このドキュメントは、高度なトラブルシューティングに役立つガイドとして提供されています。ただし、記載されている手順は[サポートポリシー](https://woocommerce.com/support-policy/)の対象外であり、実装に関する直接的なサポートは提供できません。資格のあるWordPress/WooCommerce開発者のサポートをご希望の場合は、[Codeable](https://codeable.io/?ref=z4Hnp)または[Woo Agency Partner](https://woocommerce.com/development-services/)を強くお勧めします。

WooCommerceデータベースでは、特定のテーブルに重要な情報が整理・保存されています。重要なデータがどこにあるか、簡単にご紹介します。

- **注文と注文情報**: [HPOS (High Performance Order Storage) を有効化](https://woocommerce.com/document/high-performance-order-storage/#order-data-storage) している場合、カスタム注文テーブルに注文情報が保存されます。有効化されていない場合は、`wp_posts` (注文データ用) や `wp_postmeta` (商品価格、注文ステータスなどの注文詳細用) などのテーブルに保存されます。
- **商品とバリエーション**: `wp_posts` テーブル (商品リスト用) と `wp_postmeta` テーブル (価格、SKU、属性などの詳細情報用) にあります。このテーブルには、バリエーションも個別のエントリとして保存されます。
- **配送設定**: 通常、`wp_options` (一般的な配送設定用) と `wp_postmeta` (注文固有の配送詳細用) にあります。
- **税設定**: 税率、ルール、その他の設定を含む `wp_options` に保存されます。
- **顧客情報**: `wp_users` (登録ユーザーの場合) と `wp_usermeta` (請求先住所や配送先住所などのユーザー詳細情報の場合) に保存されます。

[WooCommerce Subscriptions](https://woocommerce.com/document/subscriptions/develop/data-structure/)、[AutomateWoo](https://woocommerce.com/document/automatewoo/performance/)、[Product Bundles](https://woocommerce.com/document/bundles/bundles-data-structures-storage/)、[Composite Products](https://woocommerce.com/document/composite-products-data-structures-storage/) などの一部の WooCommerce 拡張機能は、追加のカスタム投稿タイプまたはカスタムテーブルを作成します。詳細については、ご利用の拡張機能のドキュメントページをご覧ください。

**サイトのデータベースに変更を加えると、サイト全体に大きな影響を与える可能性があることにご注意ください。データベースに変更を加える前に必ずサイトのバックアップを作成し、不明な点がある場合はホスティングプロバイダーにお問い合わせください。**

ほとんどのホスティングプロバイダーは、サイトのデータベースにアクセスするためのphpMyAdminというツールを提供しています。ただし、ホスティング会社にどのようなツールが提供されているか確認することをお勧めします。

この例では、データベース内の製品を検索します。

以下の例では、商品「ロゴ付きTシャツ」にパーマリンク「t-shirt-with-logo」があり、ブラウザのアドレスバーには商品の投稿IDが35と表示されています。

前述のように、製品はデータベースの `wp_posts` テーブルに保存されます。

1. サイトのデータベースにアクセスしたら、`wp_posts` テーブルを見つけます。

1. 「検索」をクリックし、`post_type` に「product」と入力して「Go」をクリックします。これにより、`wp_posts` の行の表示が製品のみに絞り込まれます。

1. 次に、「フィルター行」ボックスに検索クエリを入力します。商品「ロゴ付きTシャツ」の場合、「ロゴ」という検索語を入力すると、タイトルにその検索語が含まれる商品が検索結果に表示されます。商品の投稿ID（35）またはパーマリンク（「t-shirt-with-logo」）を検索した場合も、この商品が検索結果に表示されます。

4. 探している製品が見つかったら、データベース内から直接編集、コピー、または削除できます。

まだ質問があり、サポートが必要ですか?

- ヘルプデスクからハピネスエンジニアに[お問い合わせ](https://woocommerce.com/my-account/create-a-ticket/)ください。WooCommerce.comで開発または販売されている拡張機能、およびJetpack/WordPress.comをご利用のお客様には、サポートを提供しています。
- お客様でない場合は、[WooCommerceサポートフォーラム](https://wordpress.org/support/plugin/woocommerce/)でサポートを探すか、Wooエージェンシーパートナーにご依頼いただくことをお勧めします。これらのエージェンシーは、高度にカスタマイズされ、拡張性の高いオンラインストアの構築で実績のある信頼できるエージェンシーです。[Wooエージェンシーパートナーの詳細](https://woocommerce.com/development-services/)

