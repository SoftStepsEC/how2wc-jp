---
title: Etsyからの商品の輸入
url: https://woocommerce.com/document/importing-products-from-etsy/
---

Etsy から WooCommerce へストアを移行したい、あるいは Etsy 以外で個人ストアを立ち上げたいと考えている方は、以下の手順に従ってください。Etsy の商品リストを WooCommerce 対応ストアにすぐに取り込むことができます。

**注記：**

これは一度限りのインポートです。インポート後にEtsyショップで行った更新は、WooCommerceに自動的に同期されません。

そのためには、Etsy の商品リストデータを CSV ファイルで取得する必要があります。Etsy 自身が独自の手順を公開しており、下のボタンから手順に従うことができます。Etsy から商品リストデータを取得し、こちらの注意事項に従ったら、**ステップ 2** に進んでください。この手順では、CSV ファイルを WooCommerce にインポートし、WooCommerce が使用できる列にマッピングする方法についてのドキュメントが紹介されています。

留意すべき点がいくつかあります。

- **Etsy はバリエーションの価格や数量をエクスポートしません。** バリエーションがある場合、インポート後に価格は一致し、数量は 0 に設定されます。すべての商品をインポートしたら、[商品バリエーションの設定方法に関するこちらのガイド](https://woocommerce.com/document/variable-product/)に従ってください。
- **Etsy からインポートされたデジタル商品は、物理商品としてリストされます。** ただし、これは大きな問題ではありません。WooCommerce は、物理商品と同じくらい簡単にデジタル商品を扱うことができるように構築されています。これらの商品をデジタル商品としてリストするには、[こちらのガイド](https://woocommerce.com/document/managing-products/#section-6)にあるデジタル商品の設定方法と、こちらの[より詳細な説明](https://woocommerce.com/document/digital-downloadable-product-handling/)にあるデジタルファイルの取り扱い方法に従ってください。
- **手動で作成された .csv ファイルは正しくインポートされません。** Etsy から商品を正常にインポートするには、Etsy からエクスポートされた CSV ファイルを使用して以下の手順に従う必要があります。
- **Etsy 商品に複数の画像がある場合、どの画像もインポートされません。**Etsy 商品に複数の画像がある場合、これらの画像は CSV 内でそれぞれ個別の列ヘッダーを持ちます（例：IMAGE1、IMAGE2 など）。ただし、WooCommerce では、CSV に画像用の列が 1 つだけ必要です。複数の画像がある商品の場合、画像の URL をその 1 つの列に含めることができ、URL はカンマで区切られます。複数の商品画像の問題を解決するには、CSV を少し修正して、IMAGE1、IMAGE2、IMAGE3、IMAGE4 列のすべての画像が 1 つに結合されるようにします。

まだストアを作成していない場合は、[WooCommerce のインストール](https://woocommerce.com/document/installing-uninstalling-woocommerce/) に関するガイドをご覧ください。WooCommerce で動作するように調整された CSV ファイルが準備できたら、WooCommerce に組み込まれている商品 CSV インポーターの使い方に関するドキュメントを参照してください。

WooCommerce へのストア移行でサポートが必要ですか？WooExpert 代理店がお手伝いいたします。WooExpert は、高度にカスタマイズ可能で拡張性の高いオンラインストアの構築において実績のある信頼できる代理店です。[詳細はこちら](https://woocommerce.com/customizations/)

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

