---
title: スケジュールされたアクション
url: https://woocommerce.com/document/understanding-the-woocommerce-system-status-report/scheduled-actions/
---

スケジュールされたアクションは、WooCommerce の注文通知と支払い処理に関連するバックグラウンドタスクを管理します。これらのアクションを明確に理解することで、ストアの運営効率が向上し、注文の更新漏れや顧客へのメールの遅延といった問題を回避できます。

スケジュールされたすべてのアクションは、ストアの WP 管理ダッシュボードの **WooCommerce > ステータス > スケジュールされたアクション** で確認できます。

スケジュールされたアクションがどのように機能するかを説明する前に、cron と WP-Cron の両方を理解しておくと役立ちます。

Cronは、サーバーのメンテナンスタスクを自動化するためによく使用される、時間ベースのタスクスケジューリングツールです。[WP-Cron](https://developer.wordpress.org/plugins/cron/#what-is-wp-cron)は、WordPressでスケジュールされたタスクを処理する方法です。

WP-Cronは、ウェブサイトへの訪問者がページをリクエストするたびに実行されます。これにより、WordPressはスケジュールされたタスクをバックグラウンドで実行できるようになり、ページの読み込み時間やサイトのパフォーマンスへの影響を最小限に抑えます。また、WP-Cronはテーマやプラグインの更新チェック、メールの送信、WooCommerceのセール価格のスケジュール設定も行います。

WP-Cronはサイトのトラフィックに依存しているため、ストアへのトラフィックが少ない場合はスケジュールされたタスクの実行が遅れる可能性があります。逆に、トラフィックが過度に多い場合はパフォーマンスの問題が発生する可能性があります。

[WP Crontrol](https://wordpress.org/plugins/wp-crontrol/) は、cron イベントの表示、トリガー、トラブルシューティングに役立つ無料のツールです。

WP-Cron に関するさらに詳しい情報:

- [WP-Cron のデバッグ](https://woocommerce.com/document/subscriptions/develop/complete-guide-to-scheduled-events-with-subscriptions/#debugging-wp-cron)
- [WP-Cron を実際の cron ジョブに置き換える](https://woocommerce.com/document/automatewoo/replace-wordpress-cron-real-cron-job/)

[アクションスケジューラ](https://actionscheduler.org/) は、WordPress 内で大量のタスクを処理するための、スケーラブルで追跡可能なジョブキューです。数百万件もの WooCommerce Subscriptions の支払い、WooCommerce Webhook、そして他の拡張機能／プラグインのイベントやメールの管理に広く利用されています。

アクションスケジューラは、タスクを20個ずつバッチ送信することで、PHPメモリの枯渇を防ぎます。複数のバッチを同時に処理でき、最大5つのキューを同時に処理できます。

アクションスケジューラは、WordPressのカスタム投稿タイプ「scheduled-action」を使用して、**フック名**、**引数**、そして将来のタスクの**スケジュールされた時間**などの詳細を保存します。アクションスケジューラは、WordPressに組み込まれたWP-Cronによってトリガーされる`action_scheduler_run_schedule`フックへのコールバックとして自身をアタッチすることで実行されます。

基本的に、WP-Cron はアクション スケジューラをアクティブ化します。

トリガーされると、アクションスケジューラは実行準備が整った「スケジュールされたアクション」投稿を探します。デフォルトではWP-Cronに依存しているため、サイトのトラフィックにも依存します。[カスタムサーバーサイドcronジョブを設定](https://woocommerce.com/document/automatewoo/replace-wordpress-cron-real-cron-job/)することで、WP-Cronを独立して実行し、トラフィックへの依存を回避して信頼性を高めることもできます。

前述のように、スケジュールされたアクションは、ストアの WP 管理ダッシュボードの **WooCommerce > ステータス > スケジュールされたアクション** で確認できます。

ここから、次のことができます。

- 保留中のアクションを実行します。
- 特定のステータス（進行中のすべてのアクションなど）のスケジュール済みアクションを表示します。
- 失敗したアクションのログエントリを表示します。
- フック名、スケジュール日、またはグループ名でスケジュール済みアクションを検索します。

WP-Cron、スケジュールされたアクション、一般的な問題のトラブルシューティングのヒントに関する追加情報については、以下をご覧ください。

- [アクションスケジューラ](https://actionscheduler.org/)
- [WP-Cron を実際の cron ジョブに置き換える](https://woocommerce.com/document/automatewoo/replace-wordpress-cron-real-cron-job/)
- [WP-Cron のデバッグ](https://woocommerce.com/document/subscriptions/develop/complete-guide-to-scheduled-events-with-subscriptions/#debugging-wp-cron)
- [AutomateWoo: パフォーマンス](https://woocommerce.com/document/automatewoo/performance/)
- [サブスクリプションを使用したスケジューライベントの完全ガイド](https://woocommerce.com/document/subscriptions/develop/complete-guide-to-scheduled-events-with-subscriptions/)
- [WordPress 開発者ハンドブック: Cron](https://developer.wordpress.org/plugins/cron/)

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

