---
title: WooPayments: サブスクリプション向けStripe課金
url: https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/
---

[Subscriptions 拡張機能](https://woocommerce.com/products/woocommerce-subscriptions/)との基本的な互換性に加えて、WooPayments は米国に拠点を置く Subscriptions ユーザー向けにもう 1 つの機能も提供しています。それは、当社の決済パートナーが提供する Stripe Billing と呼ばれる課金エンジンを利用する機能です。

**注:** バージョン10.2より前のWooPaymentsでは、Subscriptionsプラグインを必要としない統合型サブスクリプション機能が提供されていました。しかし、この機能は現在、すべての加盟店に対して削除されています。Stripe Billing機能も同様の機能を備えていますが、使用するにはSubscriptions拡張機能をインストールする必要があります。

WooCommerce Subscriptions を使用すると、WooCommerce サイトから自動定期支払いが開始され、顧客がチェックアウト時に選択した決済ゲートウェイによって処理されます。これは「オンサイト」課金エンジンと呼ばれます。

別の方法としては、決済ゲートウェイ自体に定期支払いを開始させるという方法があります。これは「オフサイト」課金エンジンと呼ばれ、Stripe Billingの仕組みです。

オンサイト課金エンジンを使用する利点は次のとおりです。

- **豊富な機能** Subscriptionsプラグインの高度な機能の多くは、オンサイト課金エンジンを使用するサブスクリプションでのみご利用いただけます。
- **複雑さの軽減** お客様のサイトが、どのような支払いをいつ行うべきかに関する「信頼できる情報源」となります。同期が必要な別のシステムは必要ありません。
- **サポート性の向上** 定期的な請求データはすべてお客様のサイトに保存されるため、何か問題が発生した場合でも、簡単に修正できます。
- **幅広い地域で利用可能** Stripe Billingは米国のWooPayments加盟店のみが利用可能ですが、Subscriptions拡張機能は世界中の加盟店でご利用いただけます。
- **追加料金なし** Subscriptionsプラグインはシンプルな年間料金でご利用いただけますが、Stripe Billingを使用すると、サブスクリプション取引ごとに手数料が発生します。

オフサイト課金エンジンの唯一の利点は次のとおりです。

- **信頼性。** サイトが長期間 (数日間など) オフラインになった場合でも、オフサイトの課金エンジンで定期的なサブスクリプションの支払いを受け付けることができます。

ただし、この「信頼性」にはいくつかの厄介な欠点があることに注意してください。

- まず、サイトがオフラインの状態で決済ゲートウェイに更新処理を任せると、決済システムには更新情報が作成されますが、WooCommerce 自体には作成されません。この情報の不一致は、修正が非常に困難で時間のかかる作業になる可能性があります。
- 次に、事業を閉鎖したり、サイトを閉鎖したりする場合、事前にすべての更新をキャンセルしない限り、*更新は引き続き発生する*ことを忘れがちです。多くの販売者は、サイトを削除することですべての更新支払いが自動的に停止されると考えています。*オフサイト課金エンジンではそうではありません！*
- オンサイトエンジン使用中にサイトがオフラインになった場合でも、サイトがオンラインに戻ると、未処理のサブスクリプション更新は中断したところから再開されます。つまり、支払いが遅れることはあっても、完全にスキップされることはありません。

WooPayments の Stripe Billing 機能を使用するには:

- [WooCommerce Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/) がインストールされ、有効になっている必要があります。
- WooPayments アカウントは米国に拠点を置いている必要があります。

これらの基準を満たしていない場合、Stripe Billing オプションは利用できません。

Stripe Billingオプションを有効にすると、Stripe Billingエンジンを使用するサブスクリプション商品または更新に追加料金が発生します。この料金は、サブスクリプション項目だけでなく、*注文全体*に適用されます。詳細は[手数料ページ](https://woocommerce.com/document/woopayments/fees-and-debits/fees/#united-states)をご覧ください。

サブスクリプション設定で[混合チェックアウト](https://woocommerce.com/document/subscriptions/store-manager-guide/#mixed-checkout)を有効にしている場合、特定の注文に対して予想よりも高い手数料が請求される可能性がありますのでご注意ください。例えば、顧客が安価なサブスクリプションと、はるかに高価な非サブスクリプション商品を同時に購入する場合、追加料金は安価なサブスクリプション商品だけでなく、注文金額全体に適用されます。

上記の条件を満たしている場合は、次のようにして Stripe Billing オプションを有効にできます。

1. サイトの管理者ダッシュボードに移動します。
2. **「支払い > 設定」** で WooPayments の設定を見つけます。
3. 一番下の *詳細設定* セクションまでスクロールします。
4. **「今後のサブスクリプションで Stripe 請求を有効にする」** の横にあるボックスにチェックを入れます。

1. ページの下部にある**変更を保存**をクリックします。

設定を有効にすると、WooPayments で支払われる新しいサブスクリプションはすべて、オフサイトの Stripe Billing エンジンによって実行されるようになります。

**注意:** この設定が「*今後の*サブスクリプションでStripe Billingを有効にする」という名前になっているのには理由があります。既存のサブスクリプションでオンサイトのサブスクリプション課金エンジンを使用している場合、それらをStripe Billingに移行することはできません。

Stripe Billing エンジンを使用しているサブスクリプションを見つけるには:

1. サイトのダッシュボードで**WooCommerce > サブスクリプション**に移動します。
2. *次回支払い*列の日付の後に疑問符アイコンが付いているサブスクリプションを探します。

1. 疑問符にマウスオーバーすると、「この日付はあくまでも推定値です。このサブスクリプションの支払いゲートウェイが支払い処理のタイミングを制御します。」というポップアップが表示されます（このメッセージはStripe Billingサブスクリプションでは通常表示されます）。
2. サブスクリプション番号をクリックして、サブスクリプションの詳細を開きます。
3. 詳細ボックスに「sub_」で始まるWooPaymentsサブスクリプションIDが表示されます。これは、表示しているサブスクリプションがオフサイトのStripe Billingエンジンによって実行されていることを示しています。

Stripe Billing が有効になっている場合、サブスクリプション拡張機能の設定は、**WooCommerce > 設定 > サブスクリプション** の通常の場所に残ります。

ただし、Stripe Billingエンジンを使用するサブスクリプションでは、一部の設定やその他のWooCommerce Subscriptions機能はご利用いただけません。具体的には以下のとおりです。

- [カスタマイズ可能な支払い再試行システム](https://woocommerce.com/document/subscriptions/develop/failed-payment-retry/)
- [早期更新](https://woocommerce.com/document/subscriptions/early-renewal/)
- [無料/無償サブスクリプション](https://woocommerce.com/document/subscriptions/store-manager-guide/#section-9)1
- [限定支払いクーポン](https://woocommerce.com/document/subscriptions/store-manager-guide/#section-12)
- [手動更新](https://woocommerce.com/document/subscriptions/renewal-process/#manual-recurring-payments)と[自動更新トグル](https://woocommerce.com/document/subscriptions/renewal-process/#auto-renew-toggle)
- [サブスクリプションを手動で作成](https://woocommerce.com/document/subscriptions/add-or-modify-a-subscription/)、カスタム[請求スケジュール](https://woocommerce.com/document/subscriptions/add-or-modify-a-subscription/#section-3)2
- [サブスクリプションを手動で編集](https://woocommerce.com/document/subscriptions/add-or-modify-a-subscription/#section-10)3
- [サブスクリプションの切り替え](https://woocommerce.com/document/subscriptions/switching-guide/)

1 無料サブスクリプションを購入できますが、常にオンサイト エンジンが使用されます。2 請求スケジュールは常に製品構成によって決まります。3 明細、金額、日付は変更できません。

また、サブスクリプションにStripe Billingをご利用いただくことは、[手動キャプチャ設定](https://woocommerce.com/document/woopayments/settings-guide/authorize-and-capture/)と互換性がありません。両方を同時にご利用いただくことはできません。

オフサイトの Stripe Billing エンジンはいつでも無効にすることができます。

無効化すると、Stripe Billingエンジンを使用している既存のサブスクリプションは、自動的にオンサイトのサブスクリプションエンジンに移行されます。これは、画面下部の「**変更を保存**」ボタンをクリックするとすぐに実行されます。

Stripe Billing で登録済みのサブスクリプション数によっては、移行に時間がかかる場合があります。このプロセスはバックグラウンドで実行されるため、お客様には動作の違いは感じられないはずです。必要に応じて、[移行ログ](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/#migration-logs)もご利用いただけます。

移行が完了すると、その旨をお知らせする通知が変更され、加入者はこれまでどおり自動的に更新され続けます。

**注意:** 設定を無効にしても移行通知が表示されず、設定ボックスが無効またはグレー表示になる場合は、Subscriptions拡張機能が完全にインストールされていないか、有効になっていない可能性があります。[こちらのセクション](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/#migrating-subscribers)をご覧ください。

サブスクリプション移行ログ ファイルを表示する必要がある場合 (たとえば、サポート スタッフから要求された場合)、次の手順に従って表示できます。

1. サイトの管理ダッシュボードで、**WooCommerce > ステータス > ログ** に移動します。
2. ドロップダウンを使用して、`woopayments-subscription-migration-` で始まり、`YYYY-MM-DD` 形式の日付が続くログファイルを探します。
3. ログを選択したら、**表示** ボタンをクリックして読み込みます。
4. ログの内容全体を選択し、クリップボードにコピーします。
5. コンピューターで新しいテキストファイルを開き、ログの内容を貼り付けます。
6. そのファイルをサポートスタッフへの返信メールに添付します。

バージョン10.2.0より前のWooPaymentsには、サブスクリプション拡張機能を必要としない統合型サブスクリプション機能が含まれていました。しかし、この機能の顧客向けおよび加盟店向けの機能はすべて、現在、すべてのユーザーに対して完全に削除されています。

**実際には**、この古い機能を使用している既存のサブスクリプションを停止することはありませんでした。つまり、サブスクリプション料金をお支払いいただいているサブスクライバーが引き続き存在し、更新注文も作成されている可能性がありますが、お客様も顧客もサブスクリプションを表示、管理、またはキャンセルすることはできません。10.2.0以降にアップデートした後にダッシュボードのサブスクリプションページが表示されなくなった場合は、ほぼ間違いなくこれが原因です。この状況を解決する方法については、以下をお読みください。

これらの古いサブスクリプションを管理するには、Subscriptionsプラグインをインストールする必要があります。お送りしたメールには、無料のコピーを入手する手順が記載されています。（メールが届いていない場合は、[サポートにお問い合わせください](https://woocommerce.com/my-account/contact-support/)。）

サブスクリプション拡張機能をインストールすると、サブスクリプションの表示、管理、作成の機能が復元されます。顧客も同様にこれらの機能を利用できるようになります。

その後は、オプションで [Stripe Billing を無効にする](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/#disabling) ことも、何もせずに使い続けることもできます。

[WooPaymentsゲートウェイの無効化](https://woocommerce.com/document/woopayments/settings-guide/#enable-woopayments)は、WooCommerceのチェックアウトフォームに表示される支払いオプションにのみ影響します。既存のサブスクリプションはチェックアウトフォームを経由せずに更新されるため、影響を受けず、引き続きWooPayments経由で自動更新されます。

ただし、ゲートウェイを無効化した場合、*新しい*Stripe Billingサブスクリプションは作成されません。これは、Stripe BillingサブスクリプションはWooPayments経由で支払いを行う必要があるものの、ゲートウェイが無効化されているため、その支払いが不可能になるためです。別のゲートウェイで行われたサブスクリプション購入は、WooCommerce Subscriptionsの課金エンジンによって処理されます。

サイトに Stripe Billing サブスクリプションがあるときに WooPayments プラグインを無効にしようとすると、ポップアップ警告が表示されます。

無効にすると、プラグインが無効になる前にキャンセルされなかった Stripe Billing サブスクリプションは引き続き顧客から支払いを収集します。これは、Stripe Billing が使用する [オフサイト課金エンジン](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/#billing-engines) によるものです。

さらに、WooPayments が無効化されているため、サイトは対応する WooCommerce 注文を生成したり、関連するメールを顧客に送信したりできなくなります。ご想像のとおり、**この状況はほとんど推奨されません**。

更新料金の請求が継続されないようにするには、WooPayments を非アクティブ化する前に、[すべての Stripe Billing サブスクリプションをキャンセル](https://woocommerce.com/document/subscriptions/store-manager-guide/#cancel-or-suspend-subscription)する必要があります。

サイトをオフラインにしてしまった場合、またはその他の理由で WooPayments プラグインを再アクティブ化して既存のサブスクリプションをキャンセルできない場合は、[お問い合わせ](https://woocommerce.com/my-account/contact-support/) からご連絡ください。

[オフサイト課金エンジン](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/#billing-engines)により、キャンセルされるまで更新が継続されます。これは、WooCommerce内で更新注文が引き続き作成されることを意味します。

もちろん、WooCommerce Subscriptions が無効になっている場合は、サブスクリプション製品が利用できなくなるため、新しいサブスクリプションを作成することはできません。

WooCommerce Subscriptions と連携する拡張機能のほとんどは、Stripe Billing サブスクリプションとも互換性があります。ただし、[互換性のない設定](https://woocommerce.com/document/woopayments/subscriptions/stripe-billing/#incompatible-settings)にご注意ください。

たとえば、AutomateWoo はほぼ互換性がありますが、Stripe Billing サブスクリプションの明細項目を編集するために使用しようとすると、機能しません。

はい、Stripe Billing を使用するサブスクリプションは、**WooCommerce > レポート > サブスクリプション** タブの通常のサブスクリプション レポートと互換性があります。

