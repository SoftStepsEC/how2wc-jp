---
title: 注文から個人データを削除する
url: https://woocommerce.com/document/managing-orders/removing-personal-data-from-orders/
---

WooCommerce には、注文から顧客データを削除できる設定がいくつかあります。

- **一括編集** は、注文を一括で手動で匿名化する必要がある場合に便利です。
- WordPress のコア機能である **アカウント消去リクエスト** は、**個人データ保持設定** は、選択した期間が経過すると個人データを自動的に消去します。

このオプションを有効にすると、一括編集を使用して、一度に多数の注文を手動で匿名化できます。

このオプションを有効にするには:

1. ストアのWP管理ダッシュボードで、*WooCommerce > 設定* に移動し、**アカウントとプライバシー** タブをクリックします。
2. このページで、**注文から個人データを一括削除できるようにする** チェックボックスをオンにします。
3. **変更を保存** をクリックします。

個人データを削除するオプションが注文時に利用できるようになります。

1. ストアのWP管理ダッシュボードで、*WooCommerce > 注文*に移動します。
2. 個人データを削除する必要がある注文を選択します。
3. **一括操作**ドロップダウンフィールドから、**個人データを削除**を選択します。
4. **適用**ボタンをクリックします。

個人データが削除されると、下の画像に示すように、削除された情報が **[削除済み]** に置き換えられた注文が *注文* 画面に表示されます。

個別の注文では、以下の画像に示すように個人データが削除されます。

- 注文は**ゲスト**顧客に割り当てられました。
- 請求情報は**[deleted]**に置き換えられました。
- メールアドレスは[deleted@site.invalid](mailto:deleted@site.invalid)になりました。
- 電話番号は**+ 0 000 000 0000**に変更されました。

注文はこのように匿名化されるため、販売統計は影響を受けません。

WordPressでは、*ツール > 個人データの消去*からリクエストに応じてユーザーの詳細を削除できます。このデータ削除は、当該ユーザーの指示に関連付けることもできます。

WooCommerceには、アカウント削除リクエストを処理する際に、注文内の個人データを保持するか削除するかを選択する設定があります。詳細については、[WooCommerceのアカウントとプライバシー設定を確認する](https://woocommerce.com/document/configuring-woocommerce-settings/accounts-and-privacy/)をご覧ください。

WooCommerceでは、ストアで注文データをどれくらいの期間保存するかを決めることができます。プライバシーポリシーで、サイトがデータを保存する期間を指定する必要があります。現地の法律に照らして、適切な期間を検討してください。

WooCommerce のスケジュールされた個人データ削除オプションとその使用方法の詳細については、[WooCommerce の個人データ保持オプションを確認してください](https://woocommerce.com/document/configuring-woocommerce-settings/accounts-and-privacy/#personal-data-retention)。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

