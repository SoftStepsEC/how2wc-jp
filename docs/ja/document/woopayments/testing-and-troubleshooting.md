---
title: WooPayments: テストとトラブルシューティング
url: https://woocommerce.com/document/woopayments/testing-and-troubleshooting/
---

**このページのスペイン語版 |スペイン語のページのバージョンを確認**

WooPaymentsには、実際の決済処理を開始する前にストアでテストするためのツールがいくつか含まれています。また、まれではあるものの、時々発生するWooPaymentsのエラーのトラブルシューティングに役立つ便利なガイドもご用意しています。

支払い失敗（「拒否」とも呼ばれます）は、様々な理由で発生する可能性があります。ほとんどの場合、カード発行会社が請求を拒否したか、他のシステムによってブロックされたことが原因です。WooPayments の実際のエラーを示すことは稀です。

支払いが失敗する理由の詳細については、[このドキュメント](https://woocommerce.com/document/woopayments/managing-money/#failed-payments)を参照してください。

WooPaymentsは信頼性が高く、他のプラグインとの幅広い互換性を持つように設計されていますが、複雑なソフトウェアでは問題が発生する可能性があります。[セルフサービスガイド](https://woocommerce.com/document/woocommerce-self-service-guide/)では、よくある問題の解決方法を説明しています。

WooPayments を WordPress.com に接続できない場合は、[ドキュメントのこのセクション](https://woocommerce.com/document/woopayments/our-policies/connection/#troubleshooting) で役立つヒントをご覧ください。

[お問い合わせ](https://woocommerce.com/my-account/create-a-ticket/)[弊社](https://woocommerce.com/my-account/contact-support/)[サポートスタッフ](https://woocommerce.com/my-account/create-a-ticket/)までご連絡いただくことも可能です。お問い合わせの前に、多くの問題を診断するために必要となる一般的な手順として、[ログ記録を有効にする](https://woocommerce.com/document/woopayments/settings-guide/#debug-mode)ことをおすすめします。

デフォルトでは、WooPayments はクレジットカードやデビットカードなどの実際の支払い方法に対して実際の料金を請求します。

WooPaymentsは、実際の決済プロセスを可能な限り忠実にシミュレートする、簡単に有効化できるテストモードも提供しています。これにより、実際の決済手段に課金することなく、WooPaymentsの様々な機能をサイトで試すことができます。

テスト モードを有効にして使用する方法については、[テスト モードの使用ガイド](https://woocommerce.com/document/payments/testing/)をご覧ください。

実際の決済処理を必要としないサイトでWooPaymentsを試用したい場合は、[テストアカウント](https://woocommerce.com/document/woopayments/testing-and-troubleshooting/test-accounts/)をご利用いただけます。これは、ステージングサイトなどで便利です。

テストアカウントを使用すると、個人情報を必要としないサンドボックス形式のアカウントを作成できます。このアカウントはテスト取引の処理に使用できます。テストモードでのみ動作し、実際の取引は実行できません。

WordPress 開発者や、クライアントのサイトを制作する代理店の方は、[役立つガイドライン](https://woocommerce.com/document/woopayments/account-management/developer-or-agency-setup/)もいくつかありますので、ぜひ参考にしてください。

[セーフモード](https://woocommerce.com/document/woopayments/testing-and-troubleshooting/safe-mode/) は、重複したサイトが同じ WooPayments アカウントに接続されている場合に発生する問題を防ぐのに役立ちます。これは、ステージングサイトから本番サイトにサイトを複製したり、ステージングサイトから本番サイトにサイトを複製したりする際に発生する可能性があります。セーフモードのトリガーとなる要因と問題の解決方法については、上記のリンク先のガイドをご覧ください。

セーフモードを意図的に起動することはほぼありません。代わりに、ステージングサイトで[テストアカウント](https://woocommerce.com/document/woopayments/testing-and-troubleshooting/#sandbox-mode)を使用することをお勧めします。

テストアカウントまたはテストモードのライブアカウントを使用して行われたすべてのテスト注文では、`_wcpay_mode` メタキーが `test` に設定されます。これにより、WooPayments のテスト終了後にテスト注文を素早く見つけ、クリーンアップすることができます。

パフォーマンス向上のため、WooPayments は一部の情報を WordPress データベースにキャッシュします。サポートチームからキャッシュのクリアをお願いする場合があります。キャッシュのクリア方法は以下の通りです。

1. **WooCommerce > ステータス > ツール** ページに移動します。
2. 下にスクロールして、**WooPayments アカウントのキャッシュをクリア** ツールに移動します。
3. **クリア** をクリックします。

このツールはキャッシュされたアカウントの詳細をクリアし、WooPayments サーバーからすぐに更新されるようになります。

WooPaymentsプラグインは、サイト上の他の決済ゲートウェイやプラグインとの互換性の問題を引き起こすことなく、シームレスに有効化・無効化できるように設計されています。サイトのデータベースからWooPaymentsデータを削除する場合は、以下の手順を慎重に実行してください。

1. **WooPaymentsプラグインをアンインストールする** – まず、WordPressサイトからWooPaymentsプラグインをアンインストールして削除します。
2. **データベースでWooPaymentsデータを検索する** – サイトのデータベースで、`wp_options`テーブル内の`option_name`に`wcpay`が含まれるエントリを検索します。これらのエントリを削除することも検討できますが、慎重に進めてください。

**以下の点にもご注意ください:**

- WooPayments は独自のデータベーステーブルを作成しません。
- `wp_woocommerce_payment_tokens` テーブルと `wp_woocommerce_payment_tokenmeta` テーブルは WooCommerce コアに属します。**これらのテーブルは削除しないでください**。使用する決済ゲートウェイに関係なく、WooCommerce の機能に不可欠です。
- WooPayments は、注文に関連する支払い情報として、`wp_postmeta` テーブルにカスタム値を保存します。
- WooPayments は、設定と状態の管理に `wp_options` テーブルのエントリを使用します。ただし、取引の詳細はお客様のデータベースではなく、WooPayments のサーバーに保存されます（Stripe 経由）。

- **データの削除は避けてください** データベースレコードの削除は、意図しない問題を引き起こす可能性があるため、強くお勧めしません。
- **サイトのバックアップ** データベースに変更を加える前に、必ずサイトのバックアップを作成してください。手順が不明な場合は、ホスティングプロバイダーにお問い合わせください。
- **サポート範囲** サイトのデータベースへの変更は、当社の[サポートポリシー](https://woocommerce.com/support-policy/)の対象外です。これらの手順の実装に関する直接的なサポートは提供できません。

資格のある WordPress/WooCommerce 開発者からのサポートをご希望の場合は、[Codeable](https://codeable.io/?ref=z4Hnp) または [Woo エージェンシー パートナー](https://woocommerce.com/development-services/) を強くお勧めします。

**このドキュメントには何か不足していますか? まだ質問があり、サポートが必要ですか?**

- ご購入をご希望の拡張機能やテーマについてご質問がある場合は、[お問い合わせ](https://woocommerce.com/contact-us/#sales-form) ください。
- 既にこの製品をご購入済みでサポートが必要な場合は、[サポートページ](https://woocommerce.com/my-account/create-a-ticket/) からハピネスエンジニアにご連絡ください。製品ドロップダウンから製品名を選択してください。

