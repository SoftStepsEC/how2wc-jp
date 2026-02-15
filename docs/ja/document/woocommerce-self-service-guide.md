---
title: WooCommerceセルフサービスガイド
url: https://woocommerce.com/document/woocommerce-self-service-guide/
---

WooCommerce のトラブルシューティングと競合テストは、サイトで問題が発生している原因を突き止めるのに役立ちます。WooCommerce ストアで問題が発生していますか？私たちは、その解決をお手伝いします。

ほとんどの問題の原因は次のとおりです。

- サイトのソフトウェアが古い
- テーマとの競合
- 他のプラグインとの競合

ソフトウェアを最新の状態に保つことで、ウェブサイトをハッキングから守ることができます。WordPress、WooCommerce、WooCommerce.com Marketplaceの拡張機能、そしてテーマやその他のプラグインの最新バージョンには、現在発生している問題を解決するバグ修正が含まれていることがよくあります。これは、トラブルシューティングと競合テストの基礎となります。

ウェブサイトに更新があるかどうかを確認するには、**WooCommerce > ステータス > システム ステータス** に移動します。重要な通知は赤で強調表示されます。

[WooCommerce システム ステータス レポートを理解する方法](https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/)。

更新プロセスが可能な限りスムーズに実行されるようにするには、次の点に注意してください。

1. サイト、データ、ファイルの完全バックアップを作成します。
- ホスティング会社にサポートを依頼するか、
- [Jetpack バックアップ](https://jetpack.com/support/restoring-with-jetpack-backup/) を使用します（無料です）
  
2. **ダッシュボード > プラグイン** に移動し、古くなったサードパーティ製プラグインを更新します。WooCommerce はまだ更新しないでください。
3. WooCommerce.com で購入した拡張機能を更新します。[WooCommerce.com アカウント](https://woocommerce.com/my-account/) から拡張機能をダウンロードし、ファイル転送プロトコル (FTP) を使用して **/wp-content/plugins/** で手動でプラグインを上書きすることもできます。
4. **WordPress ダッシュボード > プラグイン** に移動し、**WooCommerce** を [最新の安定バージョン](https://wordpress.org/extend/plugins/woocommerce/changelog/) に更新します。
5. **WordPress** を最新バージョンに更新します。**WordPress ダッシュボード** の通知で、更新が利用可能かどうかがわかります。
6. **テーマ** を最新バージョンに更新します。最新バージョンを使用しているかどうかは、作成者に確認してください。

[WooCommerce の更新方法を学ぶ](https://woocommerce.com/document/how-to-update-woocommerce/)。

お問い合わせのほぼ半数は、サードパーティ製のテーマやプラグインとの競合によって発生する問題に関するものです。競合を特定するには、トラブルシューティングと競合テストが最善の方法です。

テーマとプラグインの競合をトラブルシューティングするには:

1. **デフォルトのWordPressテーマに切り替えて**、問題がまだ発生しているかどうかを確認してください。問題が解決しない場合は、テーマの開発者に問題についてお問い合わせください。問題を解決できるアップデートが提供されている可能性があります。デフォルトのテーマを使用しても問題が解決しない場合は、次の手順に進んでください。
2. すべてのプラグインを一時的に無効にしてください（WooCommerceと問題の原因となっているWooCommerce.com拡張機能を除く）。これで問題は解決しましたか？
- **はい**の場合、無効にしたプラグインのいずれかと競合している可能性があります。どのプラグインと競合しているかを特定するには、プラグインを1つずつ再有効化し、問題が発生したときに実行した操作を繰り返し、問題がいつ再発するかを確認してください。
- **いいえ**で、追加のプラグインを有効化していないデフォルトのテーマを使用しても問題が解決しない場合は、次の手順に進んでください。サードパーティ製のプラグインやテーマについてはサポートを提供できませんのでご了承ください。競合テストの結果、問題が WooCommerce ソフトウェアとサードパーティのプラグインまたはテーマとの競合であることが判明した場合は、問題のプラグインまたはテーマの開発者に問い合わせてください。
  
3. 調査とアドバイスのため、ハピネスエンジニアにご連絡ください。サポートリクエストには、できるだけ多くの情報をご記入ください。以下の質問にお答えいただくと、サポートがスムーズに進みます。
- 問題に気づいたのはいつですか？
- 最近、ウェブサイトにアップデートを適用しましたか？
- テーマやデザインを変更しましたか？
- 新しいプラグインをインストールしましたか？
- 複数のデバイスで問題が再現しますか？
- 問題は1つのブラウザで発生していますか？それともすべてのブラウザで発生していますか？
- 具体的なエラーメッセージが表示されていますか？スクリーンショットを撮って共有してください。
  

[テーマとプラグインの競合をテストする方法を参照してください](https://woocommerce.com/document/how-to-test-for-conflicts/)。

致命的なエラーメッセージには通常、原因となっているプラ​​グインやテーマの名前を含むパスが表示されます。これにより、修正すべき箇所や内容を特定しやすくなります。

WooCommerce システムステータスレポートは、バージョン、テンプレートのオーバーライド、メモリに関する豊富な情報を提供します。アクセスするには、**WooCommerce > ステータス > システムステータス** に移動してください。

対応が必要な項目は赤でハイライト表示されます。これには、[メモリの更新](https://codex.wordpress.org/Editing_wp-config.php#Increasing_memory_allocated_to_PHP)、ページの正しい作成、古いプラグインの更新などが含まれます。[システムステータスレポートの見方](https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/)をご覧ください。

ヒントやコツについては、[遅いサイトのトラブルシューティングに関するガイド](https://woocommerce.com/document/troubleshooting-a-slow-site/)をご覧ください。

zipファイルはWordPress管理画面の**プラグイン > 新規追加**から直接アップロードできます。新しいバージョンのプラグインをアップロードする場合は、自動的に更新が適用されます。

FTP経由でプラグインを手動で更新するには、ダウンロードファイルを解凍し、FTP経由でファイルをアップロードして既存のファイルを上書きします。**プラグインを無効化したりファイルを削除したりする必要はありません**。WooCommerceプラグインは、サブスクリプションを有効化しない限り、WordPress管理画面から自動更新することはできません。FTP経由で更新する必要があります**。

WooCommerce.com 公式マーケットプレイスから購入した拡張機能とテーマのサブスクリプションでは、手動で入力したキーは使用されません。これらの製品のサブスクリプションを有効化するには、[WooCommerce.com アカウントをストアに接続](https://woocommerce.com/document/managing-woocommerce-com-subscriptions/#connect-your-site-woocommercecom-account)してください。

以下のこともできます:

- 購入した拡張機能とテーマを手動でダウンロードするには、[マイダウンロード](https://woocommerce.com/my-account/downloads/)にアクセスしてください。
- 拡張機能とテーマの更新を管理するには、[マイサブスクリプション](https://woocommerce.com/my-account/my-subscriptions/)をご覧ください。

新機能のご要望やカスタマイズに関するサポートは、[サポートポリシー](https://woocommerce.com/support-policy/)の対象外となります。カスタマイズや特定の機能に関するお問い合わせは、[Codeable](https://www.codeable.io/partners/woocommerce/?ref=qGefA6)までご連絡ください。

WooCommerce.com マーケットプレイス公式拡張機能および WooCommerce コアに関するアイデアや機能リクエストは、[機能リクエストボード](https://woocommerce.com/feature-requests/woocommerce/) に直接投稿できます。フィードバックやアイデアには最優先で対応いたします。

ご利用のプラグインのバージョンと比較して、WooCommerceデータベースのバージョンが古いため、最新バージョンに更新する必要があります。詳しくは[WooCommerceの更新方法 - データ更新のお知らせ](https://woocommerce.com/document/how-to-update-woocommerce/#db-update)をご覧ください。

商品のバリエーション、税率、その他の大規模なデータセットが保存されないことに気付いた場合は、[大量のデータが保存されない問題 (バリエーション、税率など)](https://woocommerce.com/document/problems-with-large-amounts-of-data-not-saving-variations-rates-etc/) の解決策を参照してください。

上記のトラブルシューティング手順を実行した後も解決しない WooCommerce コアプラグイン (**拡張機能やテーマではありません**) のバグが見つかった場合は、[WooCommerce GitHub リポジトリ](https://github.com/woocommerce/woocommerce/issues/) で開発者に報告してください。

[ドキュメント](https://woocommerce.com/learn/)では、すべてのプラグイン、拡張機能、テーマについて詳しく解説しています。コンテンツの改善と操作性の向上に尽力しています。

以下に、役立つリソースをいくつか示します。

- [WooCommerce のトラブルシューティング](https://woocommerce.com/documentation/woocommerce/get-help/troubleshooting-get-help/)
- [可変商品の使い方](https://woocommerce.com/document/variable-product/)
- [翻訳/ローカライズ](https://woocommerce.com/document/woocommerce-localization/)
- [ぼやけた商品画像の修正](https://woocommerce.com/document/using-the-appropriate-product-image-dimensions/)
- [古くなった WooCommerce テンプレートの修正](https://woocommerce.com/document/fix-outdated-templates-woocommerce/)

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

