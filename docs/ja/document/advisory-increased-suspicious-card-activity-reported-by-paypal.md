---
title: 警告：PayPal が報告した不審なカード利用の増加
url: https://woocommerce.com/document/advisory-increased-suspicious-card-activity-reported-by-paypal/
---

PayPal は最近、市場全体の商店に影響を与える不審なカード活動が増加していると報告しました。

この通知は、WooCommerce ストアが状況を理解し、適切なセキュリティ対策を講じ、チェックアウト フローが保護された状態を維持できるようにするために役立ちます。

この勧告は、[PayPal Payments プラグイン](https://woocommerce.com/products/woocommerce-paypal-payments/) と PayPal の組み込み不正防止機能を使用しているストアに特に適用されます。PayPal Payments を使用している WooCommerce ストアは、PayPal の CAPTCHA 機能を含む PayPal の不正防止ツールを利用するために、設定を更新するか、プラグインの最新バージョンにアップグレードする必要がある場合があります。

ストアのセキュリティは当社の最優先事項ですので、以下の情報を確認することをお勧めします。

PayPalは、市場全体で不審なカード取引が増加していることを検出しました。PayPalが推奨するセキュリティ対策の一環として、PayPal Paymentsプラグイン内の特定の不正防止ツール（PayPalのCAPTCHAを含む）は、チェックアウト時のリスクを軽減するのに役立ちます。

現在使用している PayPal Payments プラグインのバージョンに応じて、必要な手順が異なる場合があります。

製品内に次のような通知が表示される場合があります。

> PayPalは、市場における不審なカード取引の増加を検出しました。PayPal決済設定で不正防止機能を有効にするには、PayPal決済のCAPTCHAを有効にしてください。

ストアを保護するために:

- PayPalの不正防止機能を有効にするには、[PayPal Payments](https://woocommerce.com/products/woocommerce-paypal-payment) でCAPTCHAを有効にしてください。
- 通知内のリンクにある設定手順に従ってください。
- または、PayPal Paymentsの設定ページ（`admin.php?page=wc-settings&tab=integration&section=ppcp-recaptcha`）に直接アクセスしてください。

このCAPTCHA機能はPayPalによって提供されており、PayPal Paymentsプラグインの設定から設定できます。これはチェックアウトのセキュリティをさらに強化するもので、PayPalによって推奨されています。

次のプラグイン更新がリリースされた後、通知が届きます。

> PayPal Payments v3.3.0以降には、重要な不正行為対策機能が含まれています。チェックアウトの安全性を確保するため、PayPal Paymentプラグインを最新バージョンに更新してください。

強くお勧めします:

- [PayPal Payments](https://woocommerce.com/products/woocommerce-paypal-payments/) を最新バージョンにアップデートしてください。
- 変更ログとアップデートの詳細は、こちらでご確認ください: `plugin-install.php?tab=plugin-information&plugin=woocommerce-paypal-payments&section=changelog&TB_iframe=true&width=772&height=800`

アップグレードすると、ストアは PayPal の CAPTCHA を含む PayPal の最新の不正防止ツールにアクセスできるようになります。

バージョンに関係なく、PayPal Payments プラグインを使用する際にストアを保護するためのベスト プラクティスは次のとおりです。

- PayPal Paymentsプラグインを最新バージョンに更新してください
- PayPalの不正防止設定（PayPalのCAPTCHAを含む）を有効にしてください
- WordPress管理画面で、強力で固有のパスワードと2要素認証を使用してください
- WooCommerce.comやWordPress.orgなど、信頼できるソースからのプラグインのみをインストールしてください
- ストアで異常な注文や失敗した取引の急増がないか監視してください

PayPal 支払いまたは PayPal の CAPTCHA 機能に関してご質問や問題が発生した場合は、[サポート チームにお問い合わせください](https://woocommerce.com/my-account/contact-support/?select=woocommerce-paypal-payments#contact-us)。

WooCommerce のセキュリティに関する一般的なガイダンスについては、いつでも WooCommerce.com アカウントから [サポート チームにお問い合わせ](https://woocommerce.com/my-account/contact-support/)いただけます。

あなたのセキュリティは私たちの最優先事項です。

