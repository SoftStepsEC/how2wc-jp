---
title: フック、アクション、フィルター
url: https://woocommerce.com/document/actions-and-filters/
---

フック、アクション、フィルターは、コアコードを変更することなくWooCommerceサイトの機能を変更・拡張できる強力なツールです。このドキュメントでは、これらのツールの概要と、WooCommerceサイトへの適用例をご紹介します。

**注:**このドキュメントは、高度なトラブルシューティングに役立つガイドとして提供されています。ただし、記載されている手順は[サポートポリシー](https://woocommerce.com/support-policy/)の対象外であり、実装に関する直接的なサポートは提供できません。資格のあるWordPress/WooCommerce開発者のサポートをご希望の場合は、[Codeable](https://codeable.io/?ref=z4Hnp)または[Woo Agency Partner](https://woocommerce.com/development-services/)を強くお勧めします。

フックは、アクションとフィルターの両方を網羅する広範なカテゴリです。

フックは、プラットフォームの基盤となるプロセスに「フック」することで、コードがWordPressとやり取りできるようにする手段です。フックとは、カスタムコードをアタッチするポイントのことです。

WooCommerce で使用されるフックの例を次に示します。

- **フック: woocommerce_thankyou**
- **目的**: このアクションフックは、WooCommerce のチェックアウトページで注文が完了した後に実行されます。
- **使用例**: 顧客が購入を完了した直後に、カスタム注文確認メッセージを送信するなどのアクションを実行したい場合は、`woocommerce_thankyou` に関数をフックできます。

```
function custom_thankyou_action($order_id) {
    // Send a custom confirmation message or perform other actions
}

add_action('woocommerce_thankyou', 'custom_thankyou_action');
```

この例では、`custom_thankyou_action` は `woocommerce_thankyou` フックによってトリガーされ、WooCommerce によって提供された注文 ID を使用してカスタム コードを実行します。

アクションはフックの一種です。関数をアクションにフックすると、その関数はWordPress実行サイクルの特定の時点、または特定のイベントが発生したときに実行されます。

例えば、新規ユーザーがサイトに登録した際にウェルカムメールを送信するアクションなどです。アクションとは、アクションフックの実行時に、何か特別な処理や異なる処理を実行することです。

WooCommerce でアクションフックを使用するもう 1 つの簡単な例を次に示します。

- **フック: woocommerce_before_cart**
- **目的**: このアクションフックは、WooCommerce カートページにショッピングカートの内容が表示される直前に実行されます。
- **使用例**: カートページの上部にカスタムメッセージや通知を追加する場合は、このアクションフックを使用できます。

```
function display_custom_cart_message() {
    echo '<p>Don't forget to apply your discount code before checkout!</p>';
}

add_action('woocommerce_before_cart', 'display_custom_cart_message');
```

このスニペットは、カート ページの先頭でユーザーにカスタム メッセージを出力するための `display_custom_cart_message` 関数を `woocommerce_before_cart` フックに接続します。

フィルターは、データの変更に重点を置いた別の種類のフックです。データがフィルターを通過すると、フィルターフックに割り当てられたすべての関数が、データを返したり表示したりする前にデータを処理します。

これにより、製品価格の表示方法のカスタマイズ、タイトルの変更、ボタンのデフォルトテキストの変更など、出力や値を変更できます。フィルターは、追加のアクションをトリガーするのではなく、データを変更または調整します。

- **フィルター: woocommerce_sale_flash**
- **目的**: このフィルターを使用すると、セール中の商品に表示されるセールバッジのテキストをカスタマイズできます。
- **使用例**: 商品リストのセールバッジのテキストを「限定オファー」など、より具体的なものに変更したい場合、このフィルターを使用できます。

```
function customize_sale_flash() {
    return '<span class="onsale">Limited Offer</span>';
}

add_filter('woocommerce_sale_flash', 'customize_sale_flash');
```

この例では、`customize_sale_flash` 関数を `woocommerce_sale_flash` フィルターに接続し、セール中のすべての商品に表示されるデフォルトの「セール！」バッジを「限定オファー」に置き換えています。これにより、プロモーション期間中に顧客の注目を集めるためのシンプルなカスタマイズが可能になります。

WooCommerceサイトにカスタムアクションとフィルターを追加するには、WooCommerce、フック、PHPに関する高度な知識が必要です。このトピックに関する詳細は、[アクションとフィルターの追加に関する開発者向けドキュメント](https://developer.woocommerce.com/docs/extensions/core-concepts/adding-actions-and-filters/)をご覧ください。

サイトをさらにカスタマイズしたり、機能を拡張したりする必要がある場合は、[Codeable](https://codeable.io/?ref=z4Hnp) または [Certified WooExpert](https://woocommerce.com/experts/) を強くお勧めします。

まだ質問があり、サポートが必要ですか?

- ヘルプデスクからハピネスエンジニアに[お問い合わせ](https://woocommerce.com/my-account/create-a-ticket/)ください。WooCommerce.comで開発または販売されている拡張機能、およびJetpack/WordPress.comをご利用のお客様には、サポートを提供しています。
- お客様でない場合は、[WooCommerceサポートフォーラム](https://wordpress.org/support/plugin/woocommerce/)でサポートを探すか、Wooエージェンシーパートナーにご依頼いただくことをお勧めします。これらのエージェンシーは、高度にカスタマイズされ、拡張性の高いオンラインストアの構築で実績のある信頼できるエージェンシーです。[Wooエージェンシーパートナーの詳細](https://woocommerce.com/development-services/)

