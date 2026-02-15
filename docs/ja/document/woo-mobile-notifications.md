---
title: Wooモバイルアプリの通知
url: https://woocommerce.com/document/woo-mobile-notifications/
---

Woo モバイル アプリのプッシュ通知を使用すると、オンライン ストアをより効率的に管理し、タイムリーな意思決定を行ってビジネスを円滑に進め、顧客を満足させることができます。

これらの通知はモバイルデバイスに直接送信されるため、注文の迅速な処理と発送、顧客からのフィードバックへの対応、遅延の削減、潜在的なエラーの防止に役立ちます。また、販売記録としても機能し、在庫管理と収益の正確な追跡に役立ちます。

Wooモバイルアプリの通知を設定するには、以下の手順に従ってください。モバイルアプリの通知を受信できない場合は、以下の手順に従ってトラブルシューティングを行ってください。

1. [ストアの通知を有効にする](https://woocommerce.com/document/woo-mobile-notifications/#enable-store-notifications)
2. [ストアをJetpackに接続する](https://woocommerce.com/document/woo-mobile-notifications/#connect-to-jetpack)
3. [モバイルデバイスで通知を有効にする](https://woocommerce.com/document/woo-mobile-notifications/#enable-notifications-on-your-mobile-device)
4. [アプリのログを確認する](https://woocommerce.com/document/woo-mobile-notifications/#check-the-app-logs)
5. [Androidの設定を確認する](https://woocommerce.com/document/woo-mobile-notifications/#section-6)

まず、サイトのWP管理ダッシュボードで[メールによるストア通知](https://woocommerce.com/document/configuring-woocommerce-settings/emails/#email-notifications)が正しく設定されていることを確認してください。問題が発生した場合は、[メールに関するトラブルシューティングガイド](https://woocommerce.com/document/email-faq/)をご確認ください。

次に、サイトが[Jetpackに接続](https://jetpack.com/support/getting-started-with-jetpack/)されていることを確認してください。Jetpackへの接続は[モバイルアプリの使用に必須](https://woocommercehalo.wordpress.com/faq/)ですが、Jetpackの有料プランに加入する必要はありません。

問題が発生した場合は、[サイトの再接続](https://jetpack.com/support/reconnecting-reinstalling-jetpack/)を試すか、競合するプラグインと拡張機能に関する[既知の問題](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)を確認してください。

#### Androidの場合

設定アプリで、*通知 > アプリ通知 > WooCommerce* に移動します。(この場所は、使用している Android デバイスによって異なる場合があります。) **すべての WooCommerce 通知** オプションがオンになっていることを確認してください。

#### iOSの場合

設定アプリで、*通知 > WooCommerce* に移動し、**通知を許可** オプションを切り替えます。

次の情報を探します。

#### Androidの場合

```
> Refreshing FCM token
> FCM token retrieved
> Sending FCM token to our remote services
```

#### iOSの場合

```
2021/10/26 11:57:48:617 am  📱 Registering for Remote Notifications...
2021/10/26 11:57:48:706 am  📱 Device Token Received: [32762876ghgwsyt87613g3169287648723y44784]
2021/10/26 11:57:49:190 am  📱 Successfully registered Device ID 43793459 for Push Notifications
```

プッシュ通知でまだ問題が発生する場合は、[プラグインとテーマの競合テスト](https://woocommerce.com/document/how-to-test-for-conflicts/)を実行して問題の原因を見つけることができます。

Androidデバイスは、バッテリーの消費を抑えるために、追加のバッテリーおよび省電力機能を使用しています。これらの機能により、Woo Mobileアプリからの通知を含む、デバイスが受信する通知が制限される場合があります。以下の手順に従って、これらの設定を無効にできます。また、[Android Policeの通知に関するトラブルシューティングについてはこちら](https://www.androidpolice.com/android-notification-problems-fixes/)もご覧ください。

#### バッテリーセーバーまたは省電力モード

1. スマートフォンの**設定**メニューを開きます。
2. 下にスクロールして**バッテリー**を選択します。
3. **バッテリーセーバー**を選択します。
4. **バッテリーセーバー**を使用する**トグルスイッチをオフにします。

#### アダプティブバッテリーモード

1. スマートフォンの**設定**メニューを開きます。
2. 下にスクロールして**バッテリー**を選択します。
3. **自動調整設定**を選択します。
4. **自動調整バッテリー**のトグルスイッチをオフにします。

Jetpackプラグインを使用してモバイルアプリをサイトに接続している場合は、Jetpack接続がアクティブで正常に機能していることを確認してください。[よくある問題を確認する](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)、または[サイトを再接続する](https://jetpack.com/support/reconnecting-reinstalling-jetpack/)を行ってください。

それでも問題が解決しない場合は、*メニュー > 設定 > ヘルプとサポート > サポートに問い合わせ* して、アプリ内からサポートにお問い合わせください。

