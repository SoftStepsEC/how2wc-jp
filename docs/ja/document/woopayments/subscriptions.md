---
title: WooPayments: サブスクリプション
url: https://woocommerce.com/document/woopayments/subscriptions/
---

WooPayments は [WooCommerce Subscriptions 拡張機能](https://woocommerce.com/products/woocommerce-subscriptions/) と互換性があるため、顧客は WooPayments を使用して定期的な料金を支払うことができます。

WooPayments では、[代替支払い方法](https://woocommerce.com/document/woopayments/payment-methods/additional-payment-methods/) による 1 回限りの注文を受け付けることができますが、[自動サブスクリプション更新](https://woocommerce.com/document/woopayments/payment-methods/#express-checkout-methods) にはカード支払いと [エクスプレス チェックアウト方法](https://woocommerce.com/document/woopayments/payment-methods/#express-checkout-methods) のみを使用できます。

**注:** バージョン10.2.0より前のWooPaymentsには、WooCommerce Subscriptionsを必要としない組み込みのサブスクリプション機能がありました。この機能は[現在削除](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/#migrating-subscribers)されています。以下で説明するStripe Billing機能も同様ですが、使用するにはSubscriptions拡張機能がインストールされている必要があります。

お客様のカードが有効期限切れになっているにもかかわらず、サブスクリプションが引き続き機能している理由を疑問に思ったことはありませんか？これは、当社の「カードアカウントアップデーター」機能によるものかもしれません。この機能は、お客様の銀行がサブスクリプションで最初に使用したカードを別のカードに変更した場合でも、保存済みのカードで引き続き決済処理を実行できる機能です。

これを実現するために、[当社の決済パートナー](https://woocommerce.com/document/woopayments/account-management/partnership-with-stripe/)は銀行と直接連携し、お客様が新しいカードを受け取るたびに、銀行システム内のカード情報を自動的に更新します。（例えば、既存のカードの有効期限が切れた場合や、紛失・盗難の報告があった場合など）。

これにより、顧客は中断することなくサブスクリプションを継続でき、カードが交換されるたびに新しいカードの詳細を収集する必要性が軽減されます。

カードアカウントアップデータは、米国ではほとんどのAmerican Express、Visa、Mastercard、Discoverカードで広くサポートされています。海外でのサポートは国によって異なります。

この機能には料金はかからず、無効にする方法もありません。

[Subscriptions 拡張機能](https://woocommerce.com/products/woocommerce-subscriptions/)との基本的な互換性に加えて、WooPayments は米国に拠点を置く Subscriptions ユーザー向けにもう 1 つの機能も提供しています。それは、当社の決済パートナーが提供する Stripe Billing と呼ばれる課金エンジンを利用する機能です。

WooCommerce Subscriptions を使用すると、WooCommerce サイトから自動定期支払いが開始され、顧客がチェックアウト時に選択した決済ゲートウェイによって処理されます。これは「オンサイト」課金エンジンと呼ばれます。

別の方法としては、決済ゲートウェイ自体に定期支払いを開始させるという方法があります。これは「オフサイト」課金エンジンと呼ばれ、Stripe Billingの仕組みです。

詳細については、[Stripe Billing 設定の完全なガイド](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/)をご覧ください。

