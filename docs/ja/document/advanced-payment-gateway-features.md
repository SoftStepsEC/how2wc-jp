---
title: Skyverge Extensions 高度な決済ゲートウェイ機能
url: https://woocommerce.com/document/advanced-payment-gateway-features/
---

```
Note: This documentation only covers payment gateway features for WooCommerce payment extensions developed by Skyverge. Features by other payment gateways such as WooPayments, Stripe, etc., aren't covered.
```

このドキュメントでは、WooCommerce 決済ゲートウェイ統合プラグイン（特に [SkyVerge](http://skyverge.com/) が開発したプラグイン）の高度な機能について説明します。以下のゲートウェイは、記載されている機能の 1 つ以上をサポートしています。

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [Cyber​​Source](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

各支払い方法は異なる機能をサポートしている可能性があるため、各セクションの支払いゲートウェイのリストを参照して、どのゲートウェイが機能をサポートしているかを確認してください。

**サポートされているゲートウェイ**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [Cyber​​Source](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

これらの決済ゲートウェイ拡張機能はそれぞれ、チェックアウト時に課金を承認し、後から手動でキャプチャすることを可能にします。これは、決済ゲートウェイのコントロールパネルまたは管理者から、またはWooCommerceの*注文編集*ページから簡単に行うことができます。

```
Not sure what this means? Check out this tutorial on Authorizing vs. Authorizing and Capturing.
```

注文の支払いが承認されると、注文ステータスは「保留中」に設定されます。注文を編集するには、**WooCommerce > 注文** に移動し、注文番号をクリックして、請求を確定する必要がある注文を編集してください。

決済ゲートウェイが PHP 5.3 を必要とする場合は、「Capture Charge」ボタンが表示されます。それ以外の場合は、**注文アクション** メニューの「Capture Charge」アクションを使用します。

「Capture Charge」を選択して注文を保存すると、支払いは支払いゲートウェイ経由でキャプチャされ、注文ステータスが「処理中」に更新され、注文メモもこれらの変更を反映して更新されます（ゲートウェイ名は注文メモによって異なります）。

一括で請求をキャプチャすることも可能です。「注文」ページで請求をキャプチャしたい注文を選択し、「請求をキャプチャ」アクションを使用して選択したすべての注文を一括で更新します。

**サポートされているゲートウェイ**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Cyber​​Source](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)

注文が支払済みステータス（通常は処理中または完了）に変更された際に、自動的にキャプチャーできるよう、一部のゲートウェイを改良中です。これにより、ステータスの変更時に自動的に取引のキャプチャーが試行されるため、「請求キャプチャ」アクションを使用する必要がなくなります。

自動キャプチャを処理するには、**この設定を有効にする必要があります**。

**サポートされているゲートウェイ**

- [Bambora](https://woocommerce.com/products/bambora/)
- [グローバルペイメントHPP](https://woocommerce.com/products/woocommerce-global-payments/)

これらの支払い方法では部分的なキャプチャが可能です。つまり、1つの注文に対して複数の支払いキャプチャを処理でき、キャプチャ金額は任意に選択できます。この機能はプラグイン設定で有効にする必要があります。

部分的なキャプチャを実行するには、注文を編集し、注文アクションの「料金のキャプチャ」をクリックします。

その後、キャプチャに必要な金額を入力し、キャプチャ処理を実行します。キャプチャ可能な合計金額が使用されるまで、この操作を繰り返すことができます。

**サポートされているゲートウェイ**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [Cyber​​Source](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

これらの決済ゲートウェイには**自動返金サポート**が追加されています。つまり、決済ゲートウェイのコントロールパネルや管理者にログインすることなく、WooCommerce内で直接返金処理を行うことができます。

自動返金を処理するには、返金の作成時に「クレジットカードによる返金」（または、支払い方法の名称を変更した場合は「{ゲートウェイ名}による返金」）オプションを選択してください。これにより、返金情報が決済ゲートウェイに送信され、返金処理が行われます。

```
If the transaction has been authorized but not yet been captured, or if the transaction has been captured but is not yet settled in the payment gateway, the order will be voided instead of refunded.
```

**一部払い戻し**の場合、「クレジットカードで払い戻し」を選択すると払い戻しが処理され、支払いゲートウェイ経由で払い戻された金額を指定する注文メモが作成されます。

**合計返金**の場合、返金額は注文メモに追加されますが、注文ステータスも更新されます。このゲートウェイ経由で合計金額が全額返金された場合、注文ステータスは「返金済み」に変更され、ステータス変更を記載した注文メモが追加されます。

これにより、販売者は返金取引を WooCommerce 内で完全に処理できるようになり、店舗管理にかかる時間を節約できます。

自動払い戻しを処理しようとすると、次のようなエラー メッセージが表示される場合があります。

```
Oops, you cannot partially void this order. Please use the full order amount.
```

これは、一部返金をしようとしているものの、請求額が未決済であることを意味します（通常、購入後1日以内に返金を試みた場合）。プラグインは、資金が未送金であるため、この注文を無効にしようとします（返金ではなく注文をキャンセルするため）。しかし、ほとんどの決済ゲートウェイでは一部返金は許可されていません。

この取引の払い戻しを行うには、請求が確定するまで（請求が行われてから約 1 日後）お待ちください。

**サポートされているゲートウェイ**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [Cyber​​Source](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

取引は、[払い戻し](https://woocommerce.com/document/advanced-payment-gateway-features/#refunds)と同じワークフローを使用して**無効化**できます。取引が*承認*されているものの*キャプチャ*されていない場合、無効化が発生します。ほとんどの決済ゲートウェイでは、承認済みかつキャプチャ済みの取引であっても、決済ゲートウェイアカウントでまだ決済が完了していない場合にも無効化が発生します。資金が送金されていないため、払い戻しは実際には処理されません。

代わりに、決済ゲートウェイで承認された請求が無効になり、注文書に請求が無効になったことが記録されます。**注意** WooCommerceでは、取引を無効にするためのテキストとして「クレジットカードによる返金」が引き続き表示されますが、これは正常な動作です。

注文が無効になると、注文ステータスは返金ではなく**キャンセル**に変更されます。

ほとんどの決済ゲートウェイでは部分的な無効化は**許可されていません**。そのため、注文全体を無効化する必要があります。注文の一部を無効化しようとすると、次のような通知が表示される可能性があります。

```
Oops, you cannot partially void this order. Please use the full order amount.
```

注文の一部のみを送金する必要がある場合は、請求をキャプチャする前に注文を編集するか、支払いをキャプチャしてからその一部を返金します。

**サポートされているゲートウェイ**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Cyber​​Source](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

強化されたチェックアウトフォームは、WooCommerceのデフォルトの支払いフォームよりも優れたチェックアウトエクスペリエンスを提供します。このフォームでは、**より大きな入力フィールド**、**カード番号の自動フォーマット**、**カードタイプアイコンの自動表示**、**有効期限の自動フォーマット**、**Retina対応カードアイコン**などの機能が追加されています。

これには**モバイルフレンドリーなフォームのサポート**も含まれており、クレジットカードとeCheckの両方の入力で`tel`タイプの入力が使用され、モバイルデバイスでは完全なキーボードではなく数字キーボードが表示されます。

**サポートされているゲートウェイ**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Cyber​​Source](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)

保存済み支払い方法をサポートする決済ゲートウェイであれば、アカウントからこれらの支払い方法を管理し、デフォルトの支払い方法の設定や削除が可能です。さらに、これらのゲートウェイは**拡張保存方法**をサポートしており、いくつかの追加機能を備えています。まず、商品に**ニックネーム**（「個人用」や「ビジネス用」など）を付けることができるため、お客様はチェックアウト時に商品を簡単に識別できます。ニックネームは、支払い方法の「編集」アクションをクリックすることで追加できます。

次に、これらの方法ではチェックアウト時にニックネームも使用されるため、顧客は保存したカードを簡単に識別できます。

**サポートされているゲートウェイ**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [Cyber​​Source](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

トークン化を許可する決済ゲートウェイを使用すると、ログインした顧客はチェックアウト プロセス中に支払い方法をデフォルトで保存し、将来のチェックアウト、サブスクリプション、または予約注文で使用できるようになります。

ただし、これらのゲートウェイでは、「マイアカウント」セクションから「支払い方法を追加」ワークフローを使用して保存済みの支払い方法を追加することもできます。保存済みの支払い方法を追加するには、「マイアカウント」ページにアクセスし、「支払い方法」セクションまでスクロールします。このセクションには、リンクされている支払い方法と支払い方法の種類が表示されます。

お客様は「新しいお支払い方法を追加」をクリックすることで、新しいお支払い方法を追加できます。これにより、チェックアウトを経ることなく、お支払い方法を安全​​に保存できるフォームが表示されます。

トークン化をサポートするメソッドのみがここにリストされます。

**サポートされているゲートウェイ**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [Cyber​​Source](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

これらの支払い方法はすべてWooCommerce Subscriptionsを完全にサポートしており、トークン化された支払い方法や保存済みの支払い方法をサブスクリプションに使用できます。そのため、顧客がこの保存済みの支払い方法を削除すると、次回の更新注文が失敗するため、問題が発生する可能性があります。顧客に新しい支払い方法を追加してもらい、サブスクリプションに紐付けられたトークンを手動で更新する必要があります。

これを回避するために、サブスクリプションがアクティブな場合、「私の支払い方法」テーブルはそれに適応し、サブスクリプションに関連付けられた方法の削除を無効にします。

1つの支払い方法が複数のサブスクリプションに紐付けられている場合、「サブスクリプション」列には各サブスクリプションがカンマ区切りで表示され、「サブスクリプションを表示」ボタンは表示されなくなります。サブスクリプションに紐付けられている支払い方法は、サブスクリプションを新しい支払い方法に切り替えるまで削除できません。

**サポートされているゲートウェイ**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [Cyber​​Source](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

これらの決済ゲートウェイは、利用可能な場合、チェックアウト画面で詳細な「支払い拒否」メッセージを表示できます。通常、ゲートウェイが取引を拒否した場合、WooCommerceは「支払い処理中にエラーが発生しました。別の方法をお試しください」といった一般的なメッセージを表示します。これは顧客にとってあまり役に立ちません。

ゲートウェイが、CVV の不一致や郵便番号の不一致などの役立つメッセージを表示できる応答コードを提供する場合、支払いゲートウェイは代わりに、チェックアウトを正常に完了できるように、よりインテリジェントなメッセージを顧客に表示します。

**サポートされているゲートウェイ**

- [Authorize.Net](https://woocommerce.com/products/authorize-net-cim/)
- [Bambora](https://woocommerce.com/products/bambora/)
- [Chase Paymentech](https://woocommerce.com/products/chase-paymentech/)
- [Cyber​​Source](https://woocommerce.com/products/cybersource-payment-gateway/)
- [Elavon Converge](https://woocommerce.com/products/elavon-vm-payment-gateway/)
- [Global Payments HPP](https://woocommerce.com/products/woocommerce-global-payments/)
- [Intuit Payments](https://woocommerce.com/products/intuit-qbms/)
- [Moneris](https://woocommerce.com/products/moneris-gateway/)

サイトに保存されている決済方法トークンが、決済ゲートウェイアカウントのトークンと同期しなくなる場合や、トークンを手動で追加しなければならない場合があります。顧客決済トークンエディターを使用すると、決済方法ごとにトークンを追加して、ライブトークンとサンドボックストークンの両方を保存できます。

顧客の請求詳細の直前の「ユーザーの編集」ページからトークン エディターにアクセスできます。

このエディタでは、トークンやその他のメソッド／トークン情報を変更したり、メソッドを削除したり、新しく保存したメソッドを顧客のデフォルトメソッドに設定したりできます。また、このページからトークンの詳細をコピーして新しいサブスクリプションに追加できるため、サブスクリプションを実行しているサイトにも便利です。

一部のゲートウェイでは、トークンの使用に必要な情報に応じて、追加情報が表示される場合があります。例えば、Authorize.Net CIMでは顧客ID（トークンの課金に必要な情報）が表示されます。また、ゲートウェイに保存されているその他の情報（AuthNet CIMの配送プロファイルIDなど）もトークンエディターに表示される場合があります。

ご購入前にご質問はございますか？[こちらの事前販売フォームにご記入ください。](http://skyverge.com/contact/?form_type=pre-sales)

すでに購入済みでサポートが必要ですか? ヘルプデスクから[サポートにお問い合わせください](https://woocommerce.com/my-account/create-a-ticket/)。

**サポート範囲:**

**サポートポリシー**に基づき、カスタマイズに関するサポートは提供できません。スニペットのカスタマイズや機能拡張が必要な​​場合は、[Woo エージェンシー パートナー](https://woocommerce.com/development-services/) または [Codeable](https://www.codeable.io/partners/woocommerce/?ref=qGefA6#tiers) の WooCommerce 開発者にご相談いただくことをお勧めします。

