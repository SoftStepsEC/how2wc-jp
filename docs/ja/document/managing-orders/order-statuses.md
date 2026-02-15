---
title: 注文ステータス
url: https://woocommerce.com/document/managing-orders/order-statuses/
---

すべての注文には、**ステータス** で現在の状態が示されます。注文ステータスは、注文の状態に関する貴重な情報を一目で確認できます。以下の動画と表では、WooCommerce における注文ステータスの概要と詳細をご覧いただけます。

注文ステータスは、「支払い保留中」から「完了」まで、注文の進行状況を示します。WooCommerce コアプラグインでは、以下の注文ステータスが使用されます。

このフローチャートは、注文が**支払い保留中**から**保留中**、**失敗**、または**処理中**、そして**完了**、**キャンセル**、または**返金**へとステータスが移行する様子を示しています。

WooCommerceでは、新規に作成された注文のデフォルトのステータスは「支払い保留中」です。支払い保留中ステータスは、送信済みだが支払いを待っている注文に適用されます。

しかし、WooCommerce Blocks をチェックアウトプロセスに使用する場合、買い物客がチェックアウトページに到達した時点で注文が作成されます。支払い保留ステータスは、これらの注文の状態を正確に反映しておらず、未完了または未送信の可能性があります。これに対応するため、注文が送信されるまでは「checkout-draft」ステータスが使用されます。

- **作成**: 顧客がWooCommerceブロックを使用してチェックアウトページに到達したときに開始されます。
- **コンテンツ**: 顧客の商品、選択した配送方法、および入力された住所情報が含まれます。
- **更新**: 顧客がカートブロックまたはチェックアウトブロックの情報を変更すると、ドラフト注文が動的に更新されます。
- **在庫確保**: ドラフト注文は、顧客のカートに含まれる在庫を10分間一時的に保留します。この保留により、顧客はチェックアウトセッション中に商品を購入できるようになります。これは[在庫保留設定](https://woocommerce.com/document/configuring-woocommerce-settings/products/#inventory)とは別のものです。 (この動作は修正に向けて議論中であり、スニペットを介して変更できます。詳細については、[この Github の問題](https://github.com/woocommerce/woocommerce/issues/44231#issuecomment-2109777214) を参照してください)

毎日スケジュールされた cron ジョブ (`woocommerce_cleanup_draft_orders`) は、アクティブではなくなったすべての下書き注文を削除します。

送信されるさまざまな注文メールの詳細については、[メール設定のドキュメント](https://woocommerce.com/document/configuring-woocommerce-settings/emails)をご覧ください。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

