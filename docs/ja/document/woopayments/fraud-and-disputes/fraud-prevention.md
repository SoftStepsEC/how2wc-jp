---
title: WooPayments には不正防止機能が組み込まれていますか?
url: https://woocommerce.com/document/woopayments/fraud-and-disputes/fraud-prevention/
---

WooPaymentsは[Stripeとの提携](https://woocommerce.com/document/woopayments/account-management/partnership-with-stripe/)により構築されており、同社の不正防止システムである[Radar](https://stripe.com/radar)を使用しています。Radarは、WooPayments経由で行われた注文に対してリアルタイムの不正検出とリスク評価を提供し、Radarが不正の可能性が高いと判断した注文をブロックします。

[カード検証チェック](https://woocommerce.com/document/woopayments/fraud-and-disputes/card-verification-checks/)も、すべてのクレジットカードまたはデビットカード取引に対して実行されます。

WooPaymentsには独自の[不正防止設定](https://woocommerce.com/document/woopayments/fraud-and-disputes/fraud-protection/)があり、特定の条件を満たす注文をブロックすることができます。もちろん、店舗のニーズに合わせて検出ルールをカスタマイズすることも可能です。

WooPaymentsは、取引を「高リスク」とフラグ付けすることがあります。これは、取引に疑わしい兆候がいくつかあるものの、自動的にブロックされるほどリスクが高くない場合に発生します。

- 注文ページに「高リスク」の請求が表示されている
- 取引表に「高リスク」の請求が表示されている
- 取引詳細ページに「高リスク」の請求が表示されている

*高リスク*取引の場合、注文を処理する前に顧客に連絡を取るようにしてください。連絡が取れない場合は、予防措置として注文の返金を検討してください。

ただし、完璧な不正防止システムは存在しないことをご承知おきください。稀ではありますが、加盟店がカードテスト攻撃の影響を受ける場合があります。カードテストと、そのような攻撃への対応方法については、[こちらのドキュメント](https://woocommerce.com/document/woopayments/fraud-and-disputes/card-testing/)をご覧ください。

WooPaymentsは加盟店エクスペリエンスの向上に引き続き取り組んでおり、プラグインをご利用のストア向けに不正検出機能の拡充を検討しています。ご意見・ご感想がございましたら、[アイデアボード](https://woocommerce.com/feature-requests/woopayments/)までお気軽にお寄せください。

