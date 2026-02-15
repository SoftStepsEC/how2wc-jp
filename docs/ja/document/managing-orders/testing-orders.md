---
title: テスト注文
url: https://woocommerce.com/document/managing-orders/testing-orders/
---

テスト注文を作成することは、新しい支払い方法の評価、チェックアウトプロセスの見直し、その他の注文関連の連携を評価するための効果的な方法です。また、問題のトラブルシューティングにも役立ちます。

通常の注文と同様に、テスト注文でも注文メールが送信され、WooCommerce アナリティクスなどに表示されます。

多くの決済ゲートウェイでは、手数料や料金が発生することなくテスト決済を処理できるサンドボックスまたはテストモードを提供しています。注文やチェックアウトをテストする際には、このモードを有効にすることをお勧めします。

現在、テスト注文には**視覚的な違いや特別なステータス**はありません。そのため、他のWooCommerce拡張機能、プラグイン、またはサービスでは、これらのテスト注文と実際の注文を区別できない可能性があります。

各拡張機能、プラグイン、または統合のドキュメントを必ず確認し、テストシナリオの処理方法を理解してください。要件によっては、テスト注文を行う前に特定の統合を無効にする必要がある場合があります。完了したら、テスト注文を削除して削除し、誤って処理、発送されたり、ストアのアナリティクスに表示されたりするのを防ぎましょう。

**ヒント:** テスト注文のメール送信を防ぐには、[Disable Emails](https://wordpress.org/plugins/disable-emails/)などのサードパーティ製プラグインをご利用ください。ただし、このプラグインは[SMTPプロバイダー](https://woocommerce.com/document/email-smtp-providers/#dedicated-smtp-provider)経由のメール送信を防止できない場合があります。

**重要:** ライブサイトでのテスト支払いによる予期しない問題を回避するには、[ステージングサイト](https://woocommerce.com/posts/what-is-staging-site-wordpress-how-to-set-one-up/) でのみテストを実行してください。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

