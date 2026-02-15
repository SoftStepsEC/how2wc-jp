---
title: カートとチェックアウトページのカスタマイズ
url: https://woocommerce.com/document/cart-checkout-blocks-status/
---

カートページとチェックアウトページは、ショッピング体験において非常に重要な要素です。WooCommerceのカートブロックとチェックアウトブロックは、顧客がスムーズに購入内容を確認し、購入手続きを完了するためのシームレスなプロセスを提供し、コンバージョン率を最大化します。ここでは、これらのページに関連するテンプレートとブロックに加え、新しいエクスペリエンスへのアップグレード、カスタマイズ、そしてストアのデザインとニーズに合わせた外観と機能の設定方法について詳しく説明します。

- [テンプレート](https://woocommerce.com/document/cart-checkout-blocks-status/#templates)
- [カートブロック](https://woocommerce.com/document/cart-checkout-blocks-status/#cart-block)
- [チェックアウトブロック](https://woocommerce.com/document/cart-checkout-blocks-status/#checkout-block)
- [ミニカートブロック](https://woocommerce.com/document/cart-checkout-blocks-status/#mini-cart-block)

2023年11月のバージョン8.3リリース以降に開始されたWooCommerceストアでは、カートブロックとチェックアウトブロックがデフォルトで表示されます。カートブロックとチェックアウトブロックを配置するための設定は不要です。サイトでブロックテーマを使用している場合は、ニーズに合わせてテンプレートをすぐにカスタマイズできます。ブロックカートとチェックアウトは、カスタマイズなしでも機能します。

既存のストアをアップグレードしてブロック エクスペリエンスを使用する場合、またはブロックを削除して元に戻したい場合は、以下のセクションを展開して、ブロック カートとチェックアウトにアップグレードする手順を確認してください。

カート ブロックとチェックアウト ブロックはどちらも、[ブロック ツールバー](https://woocommerce.com/document/woocommerce-store-editing/blocks/#block-toolbar) の変換ボタンを使用してクラシック バージョンに戻すことができます。

カート ページとチェックアウト ページの表示を制御する 2 つの [テンプレート](https://woocommerce.com/document/woocommerce-store-editing/templates/) があります。

- カートページは「ページ：カート」テンプレートによって制御されます。
- カートテンプレートには、ユーザーが購入対象として選択した商品（数量、価格、割引など）が表示されます。ユーザーはチェックアウトに進む前に、選択した商品を確認できます。
  
- チェックアウトページは、「ページ：チェックアウト」テンプレートによって制御されます。
- チェックアウトテンプレートは、ユーザーを購入プロセスの最終ステップへと導きます。ユーザーは、配送先情報と請求先情報を入力し、支払い方法を選択し、注文内容を確認することができます。
  

次のいずれかの方法でアクセスします。

1. サイトの管理画面から**「外観」>「エディター」**に移動します。
2. **「テンプレート」**をクリックします。
3. 編集したいテンプレートを選択します。
4. 鉛筆アイコンをクリックしてテンプレートを編集します。

カートページとチェックアウトページの両方のテンプレートで、ストア通知ブロックを使用しています。ストア通知ブロックは、WooCommerceまたは拡張機能によって生成された、買い物客向けの通知を表示する場所です。例えば、商品がカートに正常に追加された場合、ここに通知が表示されます。ストア通知ブロックは、サイトの任意のページまたはテンプレートに追加できます。

異なるタイプの通知はそれぞれ独自のスタイルを持っているため、このブロックにはスタイル設定はありません。

カートページにはカートブロックが表示されます。カートブロックでは、購入予定の商品を確認・管理でき、数量の更新や商品の削除などのオプションも利用できます。リンク先のガイドでは、カートブロックの構成要素の詳細と、ユーザーエクスペリエンスを向上させるためのレイアウトと設定のカスタマイズ手順を説明しています。

[カート ブロックをカスタマイズ](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/cart-block/)の設定とオプションを確認します。

## チェックアウトブロック

チェックアウトページテンプレートにはチェックアウトブロックがあります。これは、顧客が配送先と支払い情報を入力して購入を完了する場所です。以下のドキュメントでは、チェックアウトブロックの要素の概要と、チェックアウトプロセスを効率化し、特定のニーズを満たすための設定のカスタマイズ方法について説明しています。

[チェックアウト ブロックのカスタマイズ](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/)の設定とオプションを確認してください。

ミニカートブロックを使えば、ストア内のどのページからでもカートの中身を一目で確認できます。以下のガイドでは、ミニカートブロックの機能と、スムーズで便利なショッピング体験を実現するための外観と動作のカスタマイズ方法について解説しています。

[ミニカート ブロックをカスタマイズ](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/mini-cart/)の設定とオプションを確認してください。

カートとチェックアウトのフローでは、WooCommerce に付属するいくつかのテンプレートパーツを使用しています。[テンプレートパーツ](https://woocommerce.com/document/woocommerce-store-editing/patterns-template-parts/#template-parts) について詳しくはこちらをご覧ください。

チェックアウトページのテンプレートでは、サイトの他の部分と同じヘッダーではなく、サイトのタイトルのみを表示するシンプルなヘッダーがデフォルトで表示されていることにお気づきでしょう。これは、チェックアウトページと決済フローへの集中度を低下させるために意図的に行われており、カートのコンバージョン率を向上させ、カート放棄率を削減する最適化となっています。

もちろん、このヘッダーをお好みに合わせてカスタマイズしたり、サイトの他の部分で使用しているヘッダーに置き換えたりすることも可能です。ただし、チェックアウトプロセスから外れたリンクを含まないシンプルなヘッダーを使用することをお勧めします。

ミニカートブロックは、テンプレートパーツを使用してミニカートのコンテンツを表示します。テンプレートパーツへのアクセスと編集方法の詳細については、[ミニカートページ](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/mini-cart/#editing-the-mini-cart-template-part)をご覧ください。

WooCommerce.com の拡張機能のカートブロックとチェックアウトブロックとの互換性は、製品ページに記載されています。製品の**互換性**セクションを確認し、カートブロックとチェックアウトブロックとの互換性があるかどうかを確認してください。

[互換性がないことが宣言されている](https://developer.woocommerce.com/2023/11/06/faq-extending-cart-and-checkout-blocks/)互換性のない拡張機能を使用している場合は、チェックアウト ブロックまたはその内部ブロックのいずれかを選択すると、設定サイドバーに警告と、ワンクリックでクラシック チェックアウトに切り替えるボタンが表示されます。

互換性のない拡張機能を使用すると、チェックアウトの要素が期待どおりに利用できない場合があります。例えば、決済ゲートウェイがブロック版チェックアウトと互換性がない場合、チェックアウトページに[支払いオプションとして表示されない](https://woocommerce.com/document/cart-checkout-blocks-status/#seeing-there-are-no-payment-methods-available-at-checkout)可能性があります。

カートブロックとチェックアウトブロックで期待通りに動作しないプラグインをご利用の場合は、開発者にご連絡の上、新しいブロックベースのチェックアウトをご利用になりたい旨をお伝えください。開発者の皆様の取り組みを支援するため、既存のプラグインをカート/チェックアウトブロックおよびストアAPIと統合するための[ドキュメント](https://github.com/woocommerce/woocommerce-blocks/tree/trunk/docs#third-party-developers)と[リソース](https://github.com/woocommerce/woocommerce-blocks/tree/trunk/docs#developer-resources)を公開しました。

互換性がないと思われるサードパーティ製プラグインをご利用の場合は、プラグイン開発者に連絡し、[この新しいデフォルトとの互換性を宣言する](https://developer.woocommerce.com/2023/11/06/faq-extending-cart-and-checkout-blocks/)に関するガイダンスを参照するようお伝えください。プラグイン開発者は、ユーザーがトラブルシューティングや解決に追われることのないよう、プラグインに互換性（非互換性）を明記してください。

互換性の問題が発生した場合にクラシック テンプレートに戻す方法の詳細については、[ブロックの使用に関する入門書](https://woocommerce.com/document/woocommerce-store-editing/blocks/#using-classic-templates-placeholder-blocks-and-shortcodes)を参照してください。

チェックアウト ブロックを使用しており、互換性のない **支払いゲートウェイ** のみがインストールされアクティブになっている場合、チェックアウト時に利用できる支払い方法がないため、チェックアウト ページに警告が表示されます。

チェックアウト ブロックの **支払いオプション** 内部ブロックの [ブロック設定サイドバー](https://woocommerce.com/document/woocommerce-store-editing/blocks/#block-settings) に、ワンクリックで従来のチェックアウトに戻すオプションが表示されます。

カートブロックとチェックアウトブロックの拡張インターフェースは現在も開発中です。WooCommerce のカートとチェックアウトを統合する拡張機能やカスタマイズを開発中の方は、[開発の進捗状況を確認](https://developer.woocommerce.com/category/roadmap-insights/)し、[GitHub](https://github.com/woocommerce/woocommerce/discussions)でフィードバックをお寄せいただくことを強くお勧めします。

フックを使用してカート ページまたはチェックアウト ページで追加のマークアップ (カスタム チェックアウト フィールドなど) をレンダリングする拡張機能では、通常、カート ブロックとチェックアウト ブロックをサポートするための統合作業が必要になります。

WooCommerce.com で互換性がないと思われるプラグインを見つけましたか？需要を測定し、当社側での拡張作業の優先順位付けにご協力いただけるよう、[問題を報告](https://github.com/woocommerce/woocommerce/issues/new/choose)ください。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

