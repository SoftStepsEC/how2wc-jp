---
title: カードテスト攻撃を防ぎ、対処するにはどうすればよいでしょうか?
url: https://woocommerce.com/document/how-do-i-prevent-and-respond-to-card-testing-attacks/
---

**攻撃を受けていますか?**カードテストへの対応方法については、[このセクション](https://woocommerce.com/document/how-do-i-prevent-and-respond-to-card-testing-attacks/#how-to-respond)を参照してください。

カードテストとは、誰かが大量のクレジットカードデータを盗み出し、そのうちのどれが有効かを判断しようとする詐欺の一種です。通常、このような不正行為では、カード所有者や銀行による検知を逃れるため、異なるカードで少額の購入を複数回行います。購入が成功すると、攻撃者はカードが有効であることを認識します。これにより、カードデータを「検証済み」として高値で販売したり、より大規模な不正購入に利用したりすることが可能になります。

この行為は「カーディング」や「カードチェック」などとも呼ばれます。この種の攻撃は、正当なカード所有者が自分のアカウントでこの不正な行為を発見した場合、取引手数料の増加、チャージバック、または紛争につながる可能性があり、店舗の評判を損なう可能性があります。

カードテスト攻撃の可能性は稀ではありますが、オンラインビジネスを運営する上で避けられないものです。当社の決済ソリューションであるWooPaymentsには、こうした攻撃の影響を防止または制限するための[いくつかの対策](https://woocommerce.com/document/woopayments/fraud-and-disputes/fraud-prevention/)が組み込まれていますが、最終的には加盟店が自らの不正防止対策に責任を負います。

幸いなことに、カード テスト攻撃がサイトに損害を与えるのを防ぐ方法があります。

カードテストの一般的な兆候の一つとして、*失敗*ステータスの注文数が大幅に増加することが挙げられます。これらの注文には、カードが拒否されたことを示すメモが複数含まれている場合があります。これは、カードテスターが短期間のうちに数百（あるいは数千！）もの盗難カード番号を使ってサイトを攻撃することがよくあるためです。

これらの注文は、売上の損失を意味するものではなく、正当な購入者が注文できないようなチェックアウトの問題が原因でもありません。ただし、カードテストは、[異議申し立て](https://woocommerce.com/document/payments/disputes/)や[支払い拒否](https://woocommerce.com/document/woopayments/managing-money/#failed-payments)率の増加など、ビジネスに他の問題を引き起こす可能性があり、評判に悪影響を与え、解決に時間と労力がかかる可能性があります。

[WooPayments](https://woocommerce.com/products/woopayments/) をご利用の場合は、[こちら](https://woocommerce.com/document/woopayments/fraud-and-disputes/card-testing/) に、このような状況に対処する方法に関するアドバイスが記載された具体的なガイダンスがあります。

別の支払いゲートウェイを使用している場合:

- **最も重要な点** すべての取引を確認し、不正と思われる取引は返金してください。これは紛争を防ぐために非常に重要であり、緊急に行う必要があります。
- カードテストの防止に役立つプラグインのインストールを検討してください。これらのプラグインは、以下の[カードテストの防止](https://woocommerce.com/document/how-do-i-prevent-and-respond-to-card-testing-attacks/#preventing-card-testing)セクションに記載されています。
- この種のテストの影響を受けやすい特定の低価格商品（例えば「寄付」や「希望価格」商品など）がある場合は、一時的に非公開にして購入できないようにすることを検討してください。
- サイトで[ゲストチェックアウト](https://woocommerce.com/document/configuring-woocommerce-settings/accounts-and-privacy/#guest-checkout-and-accounts)を防止することも可能です。
- 決済プロバイダーに連絡して、アカウントのセキュリティを強化してください。たとえば、決済プロバイダーが実施している不正防止対策を更新または見直してください。

上記の対策でカード テスト攻撃に対応するだけでなく、カード テストの継続を防ぐために役立つ拡張機能と手順がいくつかありますので、以下に示します。

**注:**不正と思われる取引を返金した場合でも、決済サービスプロバイダーが当該取引の取引手数料を返金しない場合があります。手数料の返金をご希望の場合は、決済サービスプロバイダーにお問い合わせください。対応可能な場合があります。

私たちはコミュニティや決済パートナーと協力して、カードテスト攻撃を防ぐための新たな戦略を開発していますが、どんな不正防止システムも完璧ではないことをご理解いただくことが重要です。カードテスト攻撃からストアを守るために、ご自身でできる追加対策をいくつかご紹介します。

- CAPTCHA を実装します。[reCaptcha for WooCommerce](https://woocommerce.com/products/recaptcha-for-woocommerce/) や [Google reCaptcha for WooCommerce](https://woocommerce.com/products/google-recaptcha-for-woocommerce/) などの拡張機能を使用すると、迅速かつ簡単に CAPTCHA を実装できます。どちらのプラグインも、チェックアウトプロセスに必須のボット検出メカニズムを追加し、自動不正行為の防止に役立ちます。Google reCaptcha v2 (Checkbox) のみをサポートする無料プラグインは、[WordPress.org で入手可能](https://wordpress.org/plugins/recaptcha-woo/) です。
- [Cloudflare Turnstile](https://www.cloudflare.com/application-services/products/turnstile/) は、CAPTCHA プラグインに代わる新しいプラグインで、軽量でプライバシー重視のボット検出ソリューションを提供します。 Turnstile をチェックアウトプロセスに統合することで、ユーザーエクスペリエンスを損なうことなくセキュリティを強化でき、自動不正行為からストアを保護できます。Turnstile は、WordPress.org の [Simple Cloudflare Turnstile](https://wordpress.org/plugins/simple-cloudflare-turnstile/) プラグインと併用すれば無料でご利用いただけます。[有料オプション](https://woocommerce.com/products/enhanced-cloudflare-turnstile/) は WooCommerce.com マーケットプレイスでもご利用いただけます。
- [WooCommerce Anti-Fraud](https://woocommerce.com/products/woocommerce-anti-fraud/) は、複雑なルールを設定できる拡張機能です。ルールがトリガーされると、違反行為をブロックします。この拡張機能は、WooPayments に組み込まれているルールよりも強力で柔軟性に優れています。
- [WooCommerce向けAnti-Fraud Shield](https://woocommerce.com/products/anti-fraud-shield-for-woocommerce/) は、高度にカスタマイズ可能な不正検出・防止技術を提供します。カードテストの手間を削減し、不正な注文を手動または自動でブロックするのに役立ちます。

上記のプラグインのいずれかをインストールする場合は、必ずドキュメントをよくお読みください。プラグインが正しく設定されていない場合、保護効果はほとんど、あるいは全く得られません。

他にも役立つかもしれないヒントがいくつかあります。

- 最低購入金額のない「好きな金額で支払う」商品や寄付商品は避けてください。詐欺師は、カード所有者に気づかれないような少額の取引を行うために、これらの商品を利用することがよくあります。
- サイトが攻撃を受けているにもかかわらず、大量の「失敗した」注文が表示されていない場合は、お支払い方法の「**保存済みカードによる支払いを有効にする**」設定を無効にすると改善する可能性があります（サポートされている場合）。詐欺師がサイトのアカウントにカードを追加して認証しようとしている場合、この設定が効果的となることがあります。

取引を注意深く監視し、適切なセキュリティ対策を実施し、疑わしいアクティビティに迅速に対応することで、カードテスト攻撃から店舗を保護し、顧客の信頼と信用を維持することができます。

