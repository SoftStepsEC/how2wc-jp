---
title: 注文の支払い
url: https://woocommerce.com/document/managing-orders/paying-for-orders/
---

注文の支払いは重要なステップであり、多くの要素が組み合わさって、安全で顧客のプライバシーも保護されるスムーズで簡単な体験を買い物客に提供します。

WooCommerceでは、各注文に対して1つの支払い方法のみ受け付けられます。注文の支払い方法はいくつかあります。

- カートとチェックアウトのプロセスで注文作成時にお支払いいただけます。これは標準的なフローであり、ほとんどの注文で適用されます。
- 一部の決済ゲートウェイでは、対応カードリーダー、または[タップして支払う機能とWooモバイルアプリ](https://woocommerce.com/tap-to-pay/)を使用して[対面でお支払い](https://woocommerce.com/in-person-payments/)いただけます。
- 支払いステータスが「下書き」または「保留中」の注文は、以下の方法で入力できる他の注文決済フローでお支払いいただけます。
- 注文請求書メールに含まれる[この注文の支払いリンク](https://woocommerce.com/document/managing-orders/paying-for-orders/#pay-for-order-email-link)
- [支払いアクションボタン](https://woocommerce.com/document/managing-orders/paying-for-orders/#pay-button-my-account) は、顧客のアカウントエリアの「注文」タブにあります。
- [顧客の支払いページ → リンク](https://woocommerce.com/document/managing-orders/paying-for-orders/#customer-payment-page-link) は、管理画面の注文詳細ページにあります。このリンクを手動でコピーして顧客と共有できます。
  

以下では、**支払い保留中**および**下書き**ステータスの注文の支払い方法について詳しく説明します。また、顧客のプライバシー保護のために用意されている顧客確認方法についても説明します。

**注文の編集** 画面で、**注文アクション** > **注文の詳細を顧客に送信** を選択して、支払い手順とともに注文の詳細を顧客にメールで送信します。

お客様が受け取るメールには、請求書に添付されたリンクが記載されています。お客様はリンクをクリックして、注文の支払いフローに進むことができます。

顧客がサイトの登録ユーザーである場合、割り当てられた未払いの注文には、マイ アカウント領域の [**注文**] タブに [**支払い**] オプションが表示されます。

顧客の支払いフローをテストしていて、顧客として支払いたい場合は、[User Switching プラグイン](https://wordpress.org/plugins/user-switching/) (WooCommerce が作成または推奨しているものではありません) を使用して顧客のアカウントにログインし、顧客として支払いを完了することを検討してください。

管理画面の個々の注文ページには、「顧客の支払いページ →」というリンクが表示されます。このリンクを顧客と共有し、顧客が手順に従って支払いを完了できるようにすることができます。[顧客に注文メモ](https://woocommerce.com/document/managing-orders/view-edit-or-add-an-order/#order-notes)を送信すると、これらの支払いリンクを共有する際に、カスタムメッセージを添えて共有するのに最適です。

支払いリンクは顧客固有のものである場合があります。詳細は**顧客確認**をご覧ください。

WooCommerce には、お客様の注文のプライバシーを確​​保するための対策が講じられています。ただし、注文が**ゲスト**によるものか、サイトにアカウントを持つ顧客によるものかによって動作が異なります。仕組みは以下のとおりです。

- 注文が**登録済みの顧客に割り当てられ**、**ログアウトした状態で支払いリンクをクリックすると、顧客は支払いフォームに進むために自分のアカウントにログインするように求められます。

- 注文がゲスト顧客に割り当てられている場合、注文作成後 10 分以上経過してから支払いリンクをクリックしたユーザーは、支払いフォームに進むために注文に記載されているメールアドレスを確認するよう求められます。
- **ゲスト注文にメールアドレスが関連付けられていない場合**、支払いリンクを知っているユーザーなら誰でも注文の支払いを行うことができます。
  

**開発者の皆様へ:** 注文を認証なしでアクセスできる「猶予期間」の長さは、デフォルトで10分です。この時間は、[WooCommerceのコードベース](https://woocommerce.github.io/code-reference/files/woocommerce-includes-shortcodes-class-wc-shortcode-checkout.html#source-view.407)の`woocommerce_order_email_verification_grace_period`フィルターで変更できます。

注文用メールアドレスの確認は、悪意のある人物によるゲスト注文の注文詳細の閲覧を防ぐためのプライバシー機能として導入されています。ただし、この機能を有効にしない方が最適なカスタムユースケースが存在することを認識しています。ゲスト注文用メールアドレスの確認を無効にしたい場合は、以下のコードスニペットに示すように、`woocommerce_order_email_verification_required` フィルターを使用して無効にすることができます。

```
add_filter( 'woocommerce_order_email_verification_required', '__return_false' );
```

**注:**コードスニペットを使ってサイトを修正することに不安がある場合は、資格を持った開発者に依頼することをお勧めします。特におすすめなのは、[Codeable](https://codeable.io/?ref=z4Hnp) または [Certified WooExpert](https://woocommerce.com/experts/) です。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

