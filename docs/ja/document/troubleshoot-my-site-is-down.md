---
title: 「サイトがダウンしている」という問題のトラブルシューティング
url: https://woocommerce.com/document/troubleshoot-my-site-is-down/
---

WordPressサイトは時折ダウンすることがあります。このガイドは、トラブルシューティングを始めるためのものです。ダウンとは、エラーによってサイトが読み込まれなくなったり、リクエストに適切に応答できなくなったりすることです。

次のいずれかが表示される場合があります。

- エラーメッセージ（通常は重大なエラーまたは致命的なエラー）が表示される白い画面
- テキストが全く表示されない白い画面（これは「White Screen of Death（死のホワイトスクリーン）」またはWSODと呼ばれます）。

**まず、エラーを特定してください。**ページ上にすでにエラーが表示されている場合は、後でトラブルシューティングを行うために、それをコピー＆ペーストして安全な場所に保管してください。そうでない場合は、以下の方法で詳細情報を確認できます。

- **サイト管理者のメールアドレスを確認してください**。致命的なエラーが発生した際に、WordPress からエラーの詳細が記載されたデバッグメールが送信されている可能性があります。
- **PHP ログを確認してください。**ほとんどのホスティングサービスのコントロールパネルまたはファイル転送プロトコル (FTP) 経由でアクセスできます。不明な場合は、ホスティング会社に詳細を確認してください。
- **デバッグモードを有効にしてください。**WordPress には、空白ページではなくエラーメッセージを表示するデバッグモードがあります。詳しくは [WordPress でのデバッグ](https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/) をご覧ください。問題が解決したら、デバッグモードを無効にすることをお勧めします。

**次に、解決策を検索するか、ヘルプを求めます。**エラーの内容がわかったら、次の手順から選択できます。

- オンライン検索から始めると、問題の診断に役立つ場合がありますが、インターネットで見つけたアドバイスに従う際には注意が必要です。特に、よく理解していない技術的な修正やデータベースの変更に関するアドバイスがある場合は注意が必要です。
- エラーが最近追加または更新されたプラグイン/拡張機能を示している場合は、[手動で削除](https://wordpress.org/documentation/article/manage-plugins/#manual-uninstallation)を試すことができます。方法がわからない場合は、ホスティングサービスにお問い合わせください。これでサイトがオンラインに戻った場合は、プラグインの開発者にエラーについて問い合わせることを検討してください。
- 問題が WooCommerce コアまたはいずれかの拡張機能に関連していると思われる場合は、[フォーラムを確認する](https://wordpress.org/support/plugin/woocommerce/)か、[サポートに問い合わせる](https://woocommerce.com/my-account/contact-support/)。

サイトがオンラインに戻ったら、多くの問題は競合が原因である可能性があります。競合状況を確認することで、根本的な問題を特定できる可能性があります。サイトが完全にバックアップされたら、[競合テストガイド](https://woocommerce.com/document/how-to-test-for-conflicts/)をご確認ください。

WooCommerce に関連するエラーの一般的な情報については、[PHP エラーのトラブルシューティング](https://woocommerce.com/document/troubleshoot-php-errors/)の記事をご覧ください。

WordPress に影響するさまざまな PHP エラーやその他のエラーについて詳しく知りたい場合は、WordPress.org の [高度な管理ハンドブック](https://developer.wordpress.org/advanced-administration/) の [一般的な WordPress エラー](https://developer.wordpress.org/advanced-administration/wordpress/common-errors/) をご覧ください。

