---
title: 配送方法API
url: https://woocommerce.com/document/shipping-method-api/
---

WooCommerceには**配送方法API**があり、プラグインはこれを使用して独自の配送料を追加できます。この記事では、新しい配送方法を作成し、APIを操作する手順を説明します。

配送方法 API の詳細については、[WooCommerce 開発者ドキュメント](https://developer.woocommerce.com/docs/shipping-method-api/) をご覧ください。

- [プラグインを作成する](https://developer.woocommerce.com/docs/shipping-method-api/#0-create-a-plugin)
- [クラスを格納する関数を作成する](https://developer.woocommerce.com/docs/shipping-method-api/#1-create-a-function-to-house-your-class)
- [クラスを作成する](https://developer.woocommerce.com/docs/shipping-method-api/#2-create-your-class)
- [設定/オプションを定義する](https://developer.woocommerce.com/docs/shipping-method-api/#3-defining-settings-options)
- [calculate_shipping() メソッド](https://developer.woocommerce.com/docs/shipping-method-api/#4-the-calculate-shipping-method)
- [すべてをまとめる]一緒に](https://developer.woocommerce.com/docs/shipping-method-api/#5-piecing-it-all-together)

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

