---
title: アプリにログインする方法
url: https://woocommerce.com/document/android-ios-apps-login-help-faq/
---

ご希望のアプリストアからアプリを[ダウンロード](https://woocommerce.com/mobile/)してインストールし、アプリを開いたら、[ログイン]ボタンをクリックします。

ブラウザでサイトにアクセスできる場合は、すでにサイトアドレスをお持ちです。アドレスバー（ブラウザアプリでストア名を入力する場所）から取得できます。

これは、顧客がウェブ上でストアを閲覧するためにアクセスするアドレスと同じです。

そのアドレスを入力またはコピーして、アプリに入力します。

WooCommerce ストアのアドレスを入力して「続行」ボタンをタップした後にエラーが発生する場合は、次の手順に従ってください。

- インターネット接続が機能していることを確認してください。モバイルデバイスのウェブ **ブラウザ** から WooCommerce ストアのアドレスを開いて、インターネット接続が機能していることを確認してください。
- アプリがサイトにアクセスするには、サイトが稼働している必要があります。メンテナンスモードになっているサイト、まだ公開されていないサイト、またはエラーが発生しているサイトはアプリで動作しません。
- ウェブブラウザでストアのアドレスを開いてもこの画面にエラーメッセージが表示される場合は、アプリの「ヘルプ > サポートにお問い合わせ」からサポートチームにお問い合わせください。

WooCommerce アプリは、接続を確立してサインインするために、ウェブサイトと通信できる必要があります。そのためには、Woo アプリにサイトの URL を入力すると、次のエンドポイントにリクエストが送信されます: [https://public-api.wordpress.com/rest/v1.1/connect/site-info/?url=https://example.com](https://public-api.wordpress.com/rest/v1.1/connect/site-info/?url=https://example.com)

検出は、次の各テストを試すことによって機能します。

- **XML-RPC テスト** – WordPress サーバーは **/xmlrpc.php** の `demo.sayHello` メソッドを呼び出して、「Hello!」というレスポンスを期待します。
- **フォールバック チェック** – XML-RPC が失敗した場合、**/wp-admin/index.php** をチェックして、ページソースに "[wordpress.org](http://wordpress.org/)" が含まれているかどうかを確認します。

これらのテストの両方が失敗した場合、アプリはサイトが WordPress サイトではないと想定し、接続できません。

この問題を解決するには、[Jetpack IP アドレス](https://jetpack.com/support/how-to-add-jetpack-ips-allowlist/) がサイトと通信できるようにホワイトリストに登録されていることを確認してください。ホスティングプロバイダーや Cloudflare などの CDN サービスによってブロックされている可能性があります。

[新しいストアを開始するためのさまざまなオプションを見つける](https://woocommerce.com/hosting-solutions/)。

Woo モバイル アプリにログインしてストアを管理するには、次の 2 つの方法があります。

- WordPress.com アカウントを使用して Jetpack 経由で接続します。
- サイトの認証情報フローと WP-Admin のユーザー名とパスワードを使用します。

以下で各オプションについて個別に説明します。

**注:** Jetpack フローを介してアプリにログインすると、アプリからログアウトせずに複数のストアにアクセスできる機能、新しい注文やレビューのプッシュ通知、サイト訪問者の統計、Blaze キャンペーンを作成するためのアクセスなど、より多くの機能が利用できるようになります。

WooCommerce モバイルアプリは、ウェブサイトへの接続を確立する必要があります。これは、WooCommerce ストアにとって注文と売上データがモバイルデバイスに送信されるため重要です。サイトで [Jetpack プラグイン](https://jetpack.com/support/getting-started-with-jetpack/) を使用している場合、または **Jetpack 接続パッケージ** を使用する WooCommerce 拡張機能を使用している場合、WooCommerce アプリは Jetpack に関連付けられた WordPress.com アカウントでログインするように求めます。オプションで [ストアの認証情報でログイン](https://woocommerce.com/document/android-ios-apps-login-help-faq/#enter-store-credentials) することもできます。

詳細については、[WordPress.com アカウントとは何ですか?](https://woocommerce.com/document/what-is-a-wordpress-com-account/) ガイドをご覧ください。

#### Jetpack 接続を使用した拡張機能

次の拡張機能には Jetpack 接続パッケージが含まれます。

- [WooCommerce 向け Google](https://woocommerce.com/products/google-listings-and-ads/)
- [Jetpack バックアップ](https://wordpress.org/plugins/jetpack-backup/)
- [Jetpack ブースト](https://wordpress.org/plugins/jetpack-boost/)
- [Jetpack プロテクト](https://wordpress.org/plugins/jetpack-protect/)
- [Jetpack 検索](https://wordpress.org/plugins/jetpack-search/)
- [Jetpack ソーシャル](https://wordpress.org/plugins/jetpack-social/)
- [Jetpack VideoPress](https://wordpress.org/plugins/jetpack-videopress/)
- [WooPayments](https://woocommerce.com/products/woopayments/)
- [WooCommerce配送](https://woocommerce.com/products/shipping/)

WordPress.com のメールを見つけるには 2 つの方法があります。

**自己ホスト型サイトの場合**: アカウントは、**Jetpack セクション -> ダッシュボード -> アカウント接続** で見つかります。

**WordPress.com サイトの場合:** アカウントのメールの詳細については、**https://wordpress.com/me** ページを確認してください。

WooCommerce.com アカウントをお持ちで、すでに WordPress.com にログインしている場合は、[こちら](https://woocommerce.com/document/log-into-woocommerce-com-with-wordpress-com/#section-2) に記載されている手順に従って、WordPress.com アカウントを WooCommerce.com に接続してください。

#### WordPress.com のパスワードを覚えていません

WordPress.com のパスワードを忘れた場合は、画面下部の「またはマジックリンクでログイン」（iOS）/「マジックリンクでログイン」（Android）ボタンをタップして、マジックリンク ログイン オプションを使用してログインすることをお勧めします。

WordPress.com に登録したメールアドレスにメールが届きます。メール内のリンクをタップして WooCommerce アプリにログインしてください。

または、「パスワードをリセット」ボタンをタップしてパスワードリセットのプロセスを開始することもできます。パスワードリセットのプロセスに関する詳細は、[アカウント復旧](https://wordpress.com/support/account-recovery/#password-reset-process)サポートガイドをご覧ください。

#### メールでログインリンクをリクエストしましたが、メールが見つかりません。なぜですか？

アプリに表示されるメールアドレスが正しいことをご確認ください。メールが届くまで数分かかる場合もあります。Gmailアドレスをご利用の場合は、**Updates**フォルダと**Spam**フォルダの両方でマジックリンクメールをご確認ください。

#### ログイン リンクはどのメール アドレスに送信されますか?

ログイン リンクは、WordPress.com アカウントに使用されているアドレスに電子メールで送信されます。

Jetpack プラグインをインストールせずに WooCommerce アプリを使用する場合、またはこの方法でサインインする場合は、**WP-Admin** へのサインインに使用するのと同じ資格情報を使用してモバイル アプリにもサインインできます。

**ご注意:** Jetpack プラグイン、または Jetpack 接続を使用するプラグインをご利用の場合は、WordPress.com アカウントでサインインするよう求められます。ログイン画面で「ストアの認証情報でサインイン」を選択し、以下の手順に従ってサインインしてください。

ストアの資格情報を使用して接続するには:

1. アプリを起動し、「ログイン」をタップします。
2. ストアのアドレスを入力し、「続行」をタップします。
3. アプリがアクティブな Jetpack 接続を検出しない場合は、ストアの認証情報を使用してログインするよう求められます。

ストア認証情報とは、Web上のWooCommerceストアにログインする際に使用する**ユーザー名**と**パスワード**のことです。認証情報を忘れてしまった場合は、以下のガイドにアクセスを回復するための様々な方法をご確認ください。

[https://wordpress.org/support/article/resetting-your-password/](https://wordpress.org/support/article/resetting-your-password/)

WooCommerce アプリは、サイトの WP Admin のユーザー名とパスワードを使用して認証するために、サイトの WordPress ログイン ページ (通常は `/wp-login.php`) にアクセスする必要があります。

まず、サイトアドレスに「/wp-login.php」を追加して、デフォルトのWordPressログインページで同じユーザー名とパスワードでログインできることを確認してください。ホスティング会社によっては、コントロールパネルからストアにアクセスするための認証情報を顧客に提供しているものの、デフォルトのWordPressログインページからは提供していない場合があります。

`wp-login.php` 経由でログインできない場合は、ホストに問い合わせてサポートを受けてください。

アプリケーションパスワードは、WordPressサイトによって生成されるトークン（文字列）です。サードパーティのシステムやアプリは、WordPress APIを介して安全にサイトと通信することができ、サイトの認証情報は公開されません。Jetpackに接続されていないWooCommerceストアの場合、Woo Mobileアプリは接続を維持しデータを同期するために、サイトからアプリケーションパスワードを要求します。

このエラーが表示された場合、セキュリティプラグインまたはサイトの設定によってアプリケーションのパスワード機能がブロックされている可能性があります。サイトのセキュリティプラグインを無効にして、アプリへのログインを再度お試しください。それでも問題が解決しない場合は、ホスティングサービスにお問い合わせください。

アプリがアカウントを認証すると、**管理者** または **ショップ マネージャー** のみがアプリ内でストアを管理できるため、ユーザー ロールを確認するプロセスが実行されます。

このエラーが表示された場合は、次のトラブルシューティング手順を実行してください。

1. WordPress管理画面の「ユーザー」→「プロフィール」で、ユーザー権限が「管理者」または「ショップマネージャー」になっていることを確認してください。
2. WordPress APIへのアクセスをブロックする可能性のあるセキュリティプラグインを使用している場合は、プラグインを無効にしてもう一度お試しください。
3. ユーザー権限や権限を編集するプラグインを使用している場合は、デフォルトの「管理者」または「ショップマネージャー」権限を持つ別のアカウントを作成してみてください。

WP Admin またはログインページのカスタム設定が原因でアプリにログインできない場合、アプリはウェブブラウザで再試行するための代替案を提示します。非標準の WP Admin またはログインページの例としては、以下のようなものがあります。

- ログインページにキャプチャまたは認証を追加しました。
- ログインページをカスタマイズまたは編集しました。
- WP 管理ページをカスタマイズまたは編集しました。

入力したパスワードが間違っている場合にも、このログイン フローが表示されることがあります。

正常にサインインするには、WP-Admin ページにログインし、アプリのアクセスを承認するために、さらに 2 つの手順を実行する必要があります。

それでもウェブビューでログインできない場合は、一時的にデフォルトのWP Adminまたはログインページに戻して、もう一度お試しください。アプリはカスタマイズされたサイトにも最大限対応していますが、一部のプラグインや設定はWoo Mobileアプリと互換性がありません。アクセス認証を試みた後、404エラーが表示される場合があります。その場合は、ホスティング会社にお問い合わせの上、サポートを受ける必要があります。

この問題は、WooCommerce モバイルアプリのアプリケーションパスワードが生成された際に、予期しないエラーによって処理が中断された場合に発生する可能性があります。アプリケーション名は一意である必要があるため、アプリに再度ログインすると、サイトからこのエラーが返されます。

この問題を解決するには、WP Admin -> Users -> Profile に移動し、Application Password セクションまでスクロールして、次のいずれかのようなアプリケーション名の「Revoke」ボタンをクリックします。

- `com.woocommerce.android.app`
- `com.automattic.woocommerce.ios`

一般的に、ストアの資格情報に関するログイン問題の一般的な原因は次のとおりです。

1. カスタムの WordPress 管理画面またはログインページ
2. アプリケーションパスワード機能が無効になっている
3. WordPress API が無効になっている
4. セキュリティプラグインまたは設定により、アプリがプログラム的にアカウントを認証できない

上記のような機能を持つセキュリティプラグインをご利用の場合は、一時的に無効にして、アプリからログインできるかどうか確認することをお勧めします。また、ホスティングサービスに問い合わせて、制限がサーバー設定に起因していないかどうかを確認することもお勧めします。

あるいは、Jetpackプラグインを使ってアプリに接続してみるのも良いでしょう。Jetpackを使ってアプリに接続すると、アプリ内で訪問者の統計情報を確認したり、注文のプッシュ通知を受け取ったり、WordPress.comアカウントを使って1回のログインで複数のサイトを管理したりできるようになります。Jetpackプラグインを使う場合は、以下のガイドの手順に従ってJetpackを設定してください。

[https://woocommerce.com/document/jetpack-setup-instructions-for-the-woocommerce-mobile-app](https://woocommerce.com/document/jetpack-setup-instructions-for-the-woocommerce-mobile-app)

Jetpack プラグインをインストールして WordPress.com アカウントに接続したら、サイトのアドレスを入力して WooCommerce モバイル アプリに接続した後、Jetpack に接続するために使用したのと同じ WordPress.com アカウントを使用してログインするように求められます。

WooCommerce モバイル アプリへのログインに使用した WordPress.com アカウントのメールを使用して、デスクトップからストアにアクセスできることを確認します。

#### 自己ホスト型サイトの場合

サイトに WooCommerce と Jetpack プラグインがすでにインストールされている場合は、WordPress.com アカウントを Jetpack プラグインに接続していることを確認してください。

Jetpack を確認して WordPress.com アカウントに接続するには、次の手順に従ってください。

1. デスクトップからストアのwp-adminページにアクセスします。適切な「ロール」をお持ちの場合は、デスクトップブラウザに次のURLを入力することで「wp-admin」ページにアクセスできます。[yourstore.com]/wp-admin/
2. Jetpackのダッシュボードページに移動します。Jetpackメニューは左上隅にあります。
3. 「接続」セクションまでスクロールダウンし、「アカウント接続」を確認します。WordPress.comアカウントに接続していない場合は、以下の画面が表示されます。
4. 「*WordPress.comアカウントを接続*」リンクをタップし、指示に従います。

WordPress.com アカウントを接続して承認すると、アプリに再度ログインしてストアを選択できるようになります。

理由は 2 つあると考えられます。

- 利用可能なオプションのリストには、WordPress.com ストアと、WooCommerce および Jetpack プラグインがインストールされたセルフホストサイトのみが表示されます。
- 接続先のサイトには WooCommerce 3.5 以降がインストールされ、有効化されている必要があります。ストアがこの要件を満たしていない場合は、「**WooCommerce へのアップデートが必要です**」というメッセージが表示されます。WooCommerce は常に最新バージョンの使用をお勧めします。

Jetpack は、セルフホストサイトから WordPress.com アカウントへの接続を可能にし、異なるサーバー構成やアーキテクチャ間で共通の認証インターフェースを提供する WordPress プラグインです。WooCommerce モバイルアプリでは、以下の機能にアクセスするために Jetpack プラグインが必要です。

- 新規注文やレビューなどのプッシュ通知
- サイト訪問者の統計情報
- アプリ内から複数のストアを管理できる機能
- Blazeキャンペーンを作成できる機能

Jetpack を使わなくても、WooCommerce ストアを WooCommerce モバイルアプリに接続できます。詳しくは、[ストアの認証情報の入力](https://woocommerce.com/document/android-ios-apps-login-help-faq/#section-8) セクションをご覧ください。

サイトの Jetpack 接続に問題がある場合は、Jetpack のドキュメントで [Jetpack 接続の問題を修正する](https://jetpack.com/support/getting-started-with-jetpack/fixing-jetpack-connection-issues/) 方法を確認してください。これには、サイトを WordPress.com アカウントに接続する際に発生する可能性のある [特定のエラー メッセージ](https://jetpack.com/support/getting-started-with-jetpack/troubleshoot-jetpack-connection-error-messages/) も含まれます。

[Jetpack サポート](https://jetpackme.wordpress.com/contact-support/?rel=support) に問い合わせてサポートを受けることもできます。

**セルフホストサイトの場合**

WordPress.com アカウントを使ってストアにアクセスできることを確認してください。デスクトップブラウザからサイトの `wp-admin` にアクセスすることで確認できます。

WordPress.com アカウントをサイトの Jetpack に接続するには、[こちら](https://jetpack.com/support/getting-started-with-jetpack/) の手順に従ってください。

**WordPress.comサイトの場合**

WordPress.com でホストされているサイトの場合、Jetpack への接続は自動的に行われます。WordPress.com アカウントを使用してストアにアクセスできることを確認してください。デスクトップブラウザからサイトの `wp-admin` にアクセスすることで確認できます。それでもこの画面にエラーメッセージが表示される場合は、アプリの「ヘルプ > サポートにお問い合わせ」からサポートチームにお問い合わせください。

招待されたユーザーの Jetpack 接続ステータスは、`wp-admin` の `ユーザー` ページから確認できます。

招待されたユーザーがJetpack接続を確立している場合、行の末尾に緑色のJetpackロゴが表示されます。以下のスクリーンショットで赤い丸で囲まれた部分をご覧ください。

Jetpack 経由で WordPress.com アカウントにまだアカウントを接続していない場合は、Jetpack の [追加ユーザーガイド](https://jetpack.com/support/transfer-your-jetpack-connection-or-plan-to-another-user/additional-users/) を参照してください。

WordPress サイトに WooCommerce ストアを作成するには、WooCommerce プラグインをインストールする必要があります。

#### モバイルアプリから

次の手順は、モバイル アプリからサイトに WooCommerce プラグインをインストールするのに役立ちます。

##### iOS

1. エラー画面から「WooCommerce をインストール」ボタンをタップしてください。
2. 「WooCommerce セットアップ」画面が表示されます。ログインを求められた場合は、WordPress.com アカウントでログインしてください。
3. WooCommerce プラグインページに移動したら、「インストールと有効化」ボタンをタップしてインストールプロセスを開始します。
4. インストールと有効化が完了するまでお待ちください。モバイルアプリが WooCommerce のインストールを確認すると、自動的にモバイルアプリ内に移動します。
5. インストール中に問題が発生した場合は、アプリ内の「ヘルプ > サポートにお問い合わせ」からサポートチームにお問い合わせください。

#### デスクトップブラウザから

サイトに WooCommerce プラグインをインストールするには、次の手順に従ってください。

1. デスクトップからストアのwp-adminページにアクセスします。適切な権限をお持ちの場合は、デスクトップブラウザに次のURLを入力することで「wp-admin」ページにアクセスできます。[yourstore.com]/wp-admin/
2. 左側のメニューから「プラグイン -> 新規追加」を選択します。
3. 「WooCommerce」を検索し、「今すぐインストール」をクリックしてインストールを開始します。
4. インストールが完了したら「有効化」をタップし、指示に従ってストアの設定を行います。

Jetpackプラグインを使用してアプリをサイトに接続している場合は、Jetpack接続がアクティブで正常に動作していることを確認してください。[既知の問題](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)を確認するか、[サイトの再接続](https://jetpack.com/support/reconnecting-reinstalling-jetpack/)をお試しください。

それでも問題が解決しない場合は、アプリ内から「メニュー」>「設定」>「ヘルプとサポート」>「サポートに問い合わせ」にアクセスし、お問い合わせフォームにご記入の上、サポート チームにお問い合わせください。

