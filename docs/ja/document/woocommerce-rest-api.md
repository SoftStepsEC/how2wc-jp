---
title: WooCommerce REST API
url: https://woocommerce.com/document/woocommerce-rest-api/
---

WooCommerce REST APIは、WooCommerceショップを外部システムやリソースに接続するための強力なツールです。開発者でない限り、ほとんどの場合、連携機能を利用するにはAPIキーを生成し、それをシステムに入力するだけで外部サービスに接続できます。

このドキュメントでは、加盟店の視点からREST APIの基本について説明します。より高度なトピックについては、開発者向けドキュメントへのリンクも掲載しています。

**注記**：

REST API の [技術ドキュメント](https://woocommerce.github.io/woocommerce-rest-api-docs/) は GitHub で見つかります。

WordPress のパーマリンクは、**設定 > パーマリンク** で人間が簡単に読めるものに設定する必要があります。

**曜日と名前** はデフォルトで最適ですが、**プレーン** 以外であれば何でも機能します。

WooCommerce REST APIは、アクセス制御のためにキーシステムを採用しています。これらのキーは、サイト上のユーザーにリンクされています。

特定の WordPress ユーザーのキーを作成または管理するには:

1. **WooCommerce > 設定 > 詳細設定 > REST API** に移動します。
2. **API キーを作成** または **キーを追加** を選択します。**キーの詳細** 画面が表示されます。
3. **説明** を追加します。
4. ドロップダウンから、キーを生成する **ユーザー** を選択します。
5. この API キーのアクセスレベルを選択します。
- **読み取り** アクセス、
- **書き込み** アクセス、または；
- **読み取り/書き込み** アクセス。
  
6. **API キーを生成** を選択すると、WooCommerce がそのユーザーの API キーを作成します。
7. キーが生成されると、**コンシューマキー** と **コンシューマシークレット**、**QR コード**、そして赤い文字で「**キーを取り消す**」リンクが表示されます。
8. **コンシューマキー** と **コンシューマシークレット** は、WooCommerce REST API を使用して接続するアプリケーションに入力できます。アプリケーションがサイトの URL を要求する場合もあります。

レガシーREST APIは非推奨となり、WooCommerceから削除されました。WooCommerceはWordPress REST APIと直接連携できるようになりました。サイトに必要な連携のためにレガシーREST APIを引き続き使用する必要がある場合は、[WooCommerce Legacy REST API](https://developer.woocommerce.com/2024/01/17/the-woocommerce-legacy-rest-api-extension-is-now-available-in-wordpress-org/)プラグインをインストールしてください。

これは、専用の拡張機能がインストールされていない限り、レガシー REST API を使用するように構成された Webhook も機能しなくなることを意味します。

レガシー REST API プラグインをインストールしてアクティブ化すると、**WooCommerce > 設定 > 詳細** > **レガシー API** でレガシー REST API を有効にし、**レガシー REST API を有効にする** チェックボックスを選択できます。

ここからは、開発者向けドキュメントの手順に沿って、サイトでREST APIをテストし、動作を確認してください。[基本的なリクエストの作成](https://developer.woocommerce.com/docs/apis/rest-api/#make-a-basic-request)セクションでは、サイトから注文をリクエストする方法を概説しています。

完全な REST API ドキュメントは、[WooCommerce REST API ドキュメント](https://woocommerce.github.io/woocommerce-rest-api-docs/) で参照できます。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

