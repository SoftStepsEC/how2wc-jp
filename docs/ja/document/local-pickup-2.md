---
title: 現地ピックアップ
url: https://docs.woocommerce.com/document/local-pickup/
---

**注記：**

このドキュメントは、従来のWooCommerceのローカルピックアップオプションについて言及しています。WooCommerce Blocksベースのチェックアウトをご利用の場合は、[ローカルピックアップブロックの設定手順はこちら](https://woocommerce.com/document/woocommerce-blocks-local-pickup/)をご覧ください。

ローカルピックアップは、顧客が注文品を自分で受け取ることができるWooCommerceのコア配送方法です。このページでは、以下の方法を学びます。

- 配送方法として「店舗受取」を追加します。
- 「店舗受取」を設定します。

店舗受取の設定は、まず配送ゾーンに[配送方法](https://woocommerce.com/document/setting-up-shipping-zones/#adding-shipping-methods-to-zones)として追加することから始まります。店舗受取オプションを追加するには、以下の手順に従ってください。

**注記：**

この配送方法は**配送ゾーン**に追加する必要があります。配送ゾーンをまだ設定していない場合は、続行する前に[配送ゾーンの設定ガイド](https://woocommerce.com/document/setting-up-shipping-zones/)をご確認ください。

1. **WooCommerce > 設定 > 配送 > 配送ゾーン** に移動します。

2. この配送方法を提供する配送ゾーンの**編集**リンクをクリックします。

3. 配送ゾーン内で、[**配送方法を追加**] ボタンをクリックします。

4. 「配送方法の作成」ポップアップが表示されたら、「ローカルピックアップ」配送方法を選択し、「**続行**」ボタンをクリックします。

5. カートページとチェックアウトページで顧客に表示される**名前**を入力します。

6. ローカルピックアップの**費用**に税金が適用されるかどうかを決定するには、**税金ステータス**を選択します。

- デフォルトでは、ローカルピックアップを選択した場合、顧客の住所に関係なく、店舗の住所を使用して税金が計算されます。

8. **（オプション）** このオプションの「価格」を入力します。これはカート全体に適用されます。

9. **作成** ボタンをクリックして終了します。

配送エリアに含まれる地域にお住まいの場合、お客様はカート/チェックアウト画面で「ローカルピックアップ」を選択できます。カートとチェックアウト画面に表示される内容は以下のとおりです。

**カートの表示**:

**チェックアウトビュー**

**注:** 顧客に店舗受取オプションが表示されず、店舗受取を含む配送ゾーンにお住まいの場合は、配送ゾーンの順序に問題がある可能性があります。[配送ゾーンの設定](https://woocommerce.com/document/setting-up-shipping-zones/)で説明されているように、ゾーンは最小の地理的エリアから最大の地理的エリアへと並べ替える必要があります。店舗受取を含む配送ゾーンが、重複する他の配送ゾーンよりも上位に表示されていることを確認してください（**例:** カリフォルニア州への配送を提供しながら、郵便番号90201のみで店舗受取を提供している場合、店舗受取の配送ゾーンはカリフォルニア州の配送ゾーンよりも上位にする必要があります）。

開発者は、[WooCommerce 開発者ドキュメント](https://developer.woocommerce.com/docs/legacy-local-pickup-advanced-settings-and-customization/) から以下を設定できます。

- [店舗受け取り時に地方税を無効にする](https://developer.woocommerce.com/docs/legacy-local-pickup-advanced-settings-and-customization/#0-disable-local-taxes-when-using-local-pickup)
- [地方税の所在地を変更する](https://developer.woocommerce.com/docs/legacy-local-pickup-advanced-settings-and-customization/#1-changing-the-location-for-local-taxes)
- [店舗受け取り用のカスタムメール](https://developer.woocommerce.com/docs/legacy-local-pickup-advanced-settings-and-customization/#2-custom-emails-for-local-pickup)
- [店舗受け取り用のカスタムメールを追加する](https://github.com/godaddy-wordpress/woocommerce-expedited-order-email) (サードパーティ製チュートリアル)

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

