---
title: パフォーマンス
url: https://woocommerce.com/documentation/woocommerce/site-admin/performance/
---

## ドキュメント

- [高性能注文ストレージ](https://woocommerce.com/document/high-performance-order-storage/) 高性能注文ストレージ (HPOS) (旧称カスタム注文テーブル) は、eコマースのニーズに合わせて特別に設計されたソリューションで、分かりやすく堅牢なデータベース構造を提供します。WooCommerce の CRUD (Create, Read, Update, Delete) 設計を採用し、WooCommerce クエリに最適化されたカスタムテーブルに注文データを保存することで、ストアのパフォーマンスへの影響を最小限に抑えます。高性能注文ストレージの新機能 […]
- [動作が遅いサイトのトラブルシューティング](https://woocommerce.com/document/troubleshooting-a-slow-site/) WooCommerce サイトの速度低下をトラブルシューティングする最初のステップは、根本原因を特定することです。キャッシュと CDN WP Super Cache などのキャッシュプラグインを使用すると、サイトのパフォーマンスを最適化できます。 Jetpack のサイトアクセラレータや Cloudflare などのコンテンツ配信ネットワーク (CDN) を使用してサイトを高速化することもできます […]
- [WP_options テーブルとサイト速度](https://woocommerce.com/document/wp_options-table-and-site-speed/) WordPress サイトの動作が遅い場合、wp_options テーブルが見落とされがちです。このテーブルには、パーマリンク、サイト設定、スケジュール投稿、ウィジェットの詳細など、重要なサイトデータが保存されています。WooCommerce サイトの速度低下のトラブルシューティングで最も一般的な手順を既に試している場合は、wp_options テーブルを確認することをお勧めします。ほぼすべてのページ […]
- [大量のデータ（バリエーション、税率など）が保存されない問題](https://woocommerce.com/document/problems-with-large-amounts-of-data-not-saving-variations-rates-etc/) 商品のバリエーション、税率、その他の大量のデータセットが保存されない場合、Suhosin（PHPのセキュリティモジュール）がPOSTデータの保存を妨げている可能性があります。この問題は、PHPバージョン5.3.9以降のサーバーやmod_securityを実行しているサーバーでも発生する可能性があります。Suhosinの設定 Suhosinが有効になっている場合は、設定が必要な場合があります […]
- [チェックアウトページでの読み込み/スピナーが無限に表示される](https://woocommerce.com/document/endless-loadingspinner-on-the-checkout-page/) 「注文確認」ページでは、支払い方法/合計金額がAJAX経由で読み込まれます。このため、読み込み中のスピナーが一時的に表示されます。問題が発生すると、このセクションの読み込みに失敗するか、スピナーが表示されたままになることがあります。まず、WooCommerce > ステータスでエラーを確認してください。多くの場合、エラーはハイライト表示されます。一般的な原因と解決策は以下に記載されています。AJAX […]
- [jQuery.cookie.js/jQuery.cookie.min.js スクリプトの読み込みに失敗する](https://woocommerce.com/document/jquery-cookie-fails-to-load/) これはサーバー設定の問題であるため、ホスティング会社に解決を依頼する必要があります。問題は、MOD_SECURITY コアルールセットが古いことです。オプション 1: ホスティング会社にルールセットを更新してもらう。これは間違いなく最良の方法です。そうすれば、すべてが設計どおりに動作するようになります。ホスティング会社にお問い合わせください […]

