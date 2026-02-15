---
title: Android向けWooCommerce
url: https://woocommerce.com/document/android/
---

公式の **WooCommerce for Android アプリ** は、[WooCommerce.app](https://woocommerce.app) 経由で Google Play ストアから無料で入手できます。

このガイドでは、ストアへの接続方法やアプリの使用方法など、セットアップの手順を説明します。

- Android 8.0以降

あなたのストアは次のいずれかである必要があります。

- [WordPress.com](http://wordpress.com/) で [WordPress.com](http://wordpress.com/) の [Entrepreneur プラン](https://wordpress.com/pricing/) を利用してホスティングされているか、
- [Woo Express プラン](https://woocommerce.com/express/) を利用しているか、
- WooCommerce 3.5 以降でセルフホスティングされているか。

*WordPress 5.6以降で稼働しているセルフホスト型ストアでは、アプリの使用にJetpackは必須ではありません。ただし、Jetpackプラグインをインストール、接続、有効化することで通知が有効になり、アプリとサイトの連携が向上します（Jetpackの詳細については、「Jetpackの使い方」をご覧ください）。*

アプリをインストールするには、次のいずれかを実行します。

- デバイスからGoogle Playストアにアクセスし、**WooCommerce by Automattic**を検索してアプリをインストールするか、
- デバイスからこのリンクを開いて開始します: [WooCommerce.app](https://woocommerce.app)

WooCommerce公式Androidアプリをインストールして起動すると、ウェルカム画面が表示されます。まずは**ストアのアドレスを入力**してください。

次の手順は、ストアの設定方法によって異なります。

**オプション 1:**ストアは WordPress.com でホストされているか、Jetpack プラグインまたは Jetpack 接続を使用するプラグインのいずれか ([Google Listings & Ads](https://href.li/?https://wordpress.org/plugins/google-listings-and-ads/)、[WooCommerce Payments](https://href.li/?https://wordpress.org/plugins/woocommerce-payments/)、[WooCommerce Shipping & Tax](https://href.li/?https://wordpress.org/plugins/woocommerce-services/)、またはいずれかの Jetpack 拡張機能) を介して **Jetpack** に接続された自己ホスト型ストアです。

この場合、アプリはストアが Jetpack に接続されていることを認識し、**WordPress.com** ログインフローを続行するように要求します。

1. WordPress.com アカウントのメールアドレスを入力し、「続行」をタップします。
2. WordPress.com のパスワードを入力し、「**続行**」をタップするか、「**メールでログインリンクを取得**」を選択します。
3. 複数のサイトを選択できる場合は、タップして希望するサイトを選択します。選択できない場合は、「続行」をタップします。
4. 「**マイストア**」ページが読み込まれ、アプリが WooCommerce ストアに接続されたことが示されます。

または、次の手順に従って QR コード経由でログインすることもできます。

1. 既存のメールアドレスを入力し、「**続行**」をタップします。
2. 「**マジックリンクでログイン**」をタップします。
3. 別のデバイスでメールを確認します。
4. 「**QRコードをスキャンしてログイン**」をタップし、メール内のコードをスキャンします。

**オプション 2:** ストアが自己ホストされており、Jetpack や Jetpack 接続を使用する Jetpack または WooCommerce 拡張機能がありません。

- サイトのアドレスを入力してください。
- アプリはサイトが Jetpack に接続されていないことを認識し、ユーザー名とパスワードの入力を求めます。
- ブラウザから WP-Admin ダッシュボードにログインするときに使用するユーザー名とパスワードを入力してください。

詳細については、こちらをご覧ください:

https://woocommercehalo.wordpress.com/faq/

WooCommerce アプリをストアから切断するには:

1. 画面右下のナビゲーションバーにある**メニューアイコン**をタップします。
2. 画面右上の**歯車アイコン**を選択して**設定**にアクセスします。
3. **設定画面**を一番下までスクロールします。
4. **ログアウト**をタップします。

すべてのストアが同じ Jetpack アカウントに接続されている限り、アプリ内で複数のストアを管理できます。

別のストアにアクセスするには:

1. 画面右下のナビゲーションバーにある**メニューアイコン**をタップします
2. 画面上部の**ドロップダウンアイコン**をタップします
3. アカウントで別のストアを選択します
4. **続行**をタップして切り替えを完了します

バージョン 7.6 以降、アプリは *同じ* Jetpack/WordPress.com アカウントに接続された *すべての* ストアのプッシュ通知をサポートすることに注意してください。

**管理者** または **ストア マネージャー** のユーザー ロールを持つ複数のユーザーが、自分のデバイスからストアを管理できます。

ストアが Jetpack に接続されている場合は、各ユーザーが次の手順を完了する必要があります。

1. ブラウザからWooCommerceウェブサイトにログインします。
2. **Jetpack → ダッシュボード** に移動し、**接続** を選択します。
3. 「**WordPress.comにリンク**」を選択します。
4. WordPress.comアカウントでログインします。
5. **Jetpack無料プラン** を選択します。
6. これで、ユーザーはWordPress.comアカウントでアプリにログインできるようになります。

ショップマネージャーが統計情報を表示できるようにするには、**Jetpack → 設定 → トラフィック** に移動して、統計情報の表示を有効にします。

ストアが Jetpack に接続されていない場合、管理者またはストア マネージャーの役​​割を持つ各ユーザーは、WP-Admin ダッシュボードにログインするために使用するのと同じ資格情報を使用してアプリにログインできます。

**マイストア**ページは、WooCommerce Androidアプリを起動した際のデフォルトビューです。以下の4つのメインセクションの1つです。

- **マイストア** – 当日、今週、今月、または今年の売上と売れ筋商品の概要を表示します。
- **注文** – 既存の注文を検索または絞り込んだり、新規注文の支払いを受け取ったりできます。
- **商品** – 既存の商品を検索または絞り込んだり、新規商品を追加したりできます。
- **メニュー** – ストアを切り替えたり、レビューや[設定](https://woocommerce.com/document/android-settings/)などにアクセスできます。

タブレットをご利用の場合は、**POSモード**のタブも表示されます。[POSモードの詳細については、こちらのガイドをご覧ください](https://woocommerce.com/document/woo-mobile-app-point-of-sale-mode/)。

ご自身で問題を解決できない場合は、上記のようにアプリ内の*サポートに問い合わせる*設定からチームにご連絡ください。

理由は 2 つあると考えられます。

- 利用可能なオプションのリストには、WordPress.com ストア、および WooCommerce と Jetpack プラグインがインストールされたセルフホストサイトのみが表示されます。
- 接続先のサイトには WooCommerce 3.5 以降がインストールされ、有効化されている必要があります。ストアがこの要件を満たしていない場合、「**WooCommerce へのアップデートが必要です**」というメッセージが表示されます。

Jetpackプラグインを使用してアプリをサイトに接続している場合は、Jetpack接続がアクティブで正常に動作していることを確認してください。[既知の問題](https://jetpack.com/support/getting-started-with-jetpack/known-issues/)を確認するか、[サイトの再接続](https://jetpack.com/support/reconnecting-reinstalling-jetpack/)をお試しください。

それでも問題が解決しない場合は、アプリ内から「メニュー」>「設定」>「ヘルプとサポート」>「サポートに問い合わせ」にアクセスし、お問い合わせフォームにご記入の上、サポート チームにお問い合わせください。

