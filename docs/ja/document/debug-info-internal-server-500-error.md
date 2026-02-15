---
title: HTTP 500 内部サーバーエラー — 詳細情報の取得
url: https://woocommerce.com/document/debug-info-internal-server-500-error/
---

HTTP 500 内部サーバーエラーは、よく発生するエラーです。多くの場合、一時的なものであり、一般的なサーバーエラー応答です。

一般的に、HTTP 500 内部サーバーエラーの出力は詳細な情報ではなく、問題の原因を絞り込むのに役立ちません。ライブサイトや本番サイトでは、以下に示すような一般的なエラーを表示するのがベストプラクティスと考えられています。

```
Internal Server Error

The server encountered an internal error or misconfiguration and was unable to complete your request.

Please contact the server administrator at [support email] and inform them of the time the error occurred, and anything you might have done that may have caused the error.

More information about this error may be available in the server error log.

[server/port information]
```

永続的な内部サーバー エラーが発生した場合は、トラブルシューティングを行うためにさらに情報が必要になります。

WordPress デバッグ モードを有効にするには:

1. [セキュアファイル転送プロトコル](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol) (SFTP) を使用してサイトに接続します。
2. `wp-config.php` というファイルを開きます。
3. 次のコード行を探します: `define('WP_DEBUG', false);`
4. 値を `false` から `true` に変更します。
5. ファイルを保存します。

**注意:** 上記の行の値がすでに `true` に設定されている場合、別の拡張機能、プラグイン、またはサーバー構成によってエラー出力が抑制されている可能性があります。

エラーが発生したページを更新すると、より詳細なエラーメッセージが表示されるようになり、トラブルシューティングに役立ちます。[WordPress のデバッグについて詳しくはこちら](https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/)

これはサーバーレベルのエラーなので、多くの場合、サーバーエラーログに詳細が記載されています。ホスティングプロバイダーがログを提供している場合は、通常、詳細の確認をお手伝いします。

