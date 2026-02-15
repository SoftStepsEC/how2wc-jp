---
title: WooCommerceのインストールとアンインストール
url: https://woocommerce.com/document/installing-uninstalling-woocommerce/
---

WooCommerce は他の WordPress プラグインと同様にインストールおよびアンインストールできます。セットアップウィザードには、WooCommerce をインストールして完全な設定を行うためのオプションの手順が用意されています。

インストール前に[サーバー要件](https://woocommerce.com/document/server-requirements/)をご確認ください。そうしないと、WooCommerceの使用時に問題が発生する可能性があります。新しいホスティングサービスが必要な場合、またはまだホスティングサービスをお持ちでない場合は、[推奨ホスティングサービス](https://woocommerce.com/hosting-solutions/)をご覧ください。WooCommerceをすぐにセットアップできます。

WooCommerce を有効にすると、サイトが適切に機能するためにいくつかの項目がサイトに追加されます。

- 注文、商品などのための新しいメニュー項目、[カスタム投稿タイプ、タクソノミー](https://woocommerce.com/document/installed-taxonomies-post-types/)。
- 新しい[WooCommerceページ](https://woocommerce.com/document/woocommerce-pages/)。
- 新しいウィジェットとショートコード。
- ショップマネージャーと顧客用のユーザーロール。

インストールしたプラグインを非アクティブ化して削除しても、サイト データベース内のデータは削除されないため、追加の破壊的な手順が必要になります。

既存のサイトがあり、WooCommerce をインストールする場合は、WordPress Admin を使用するとすべてが自動的に処理されるため、最も簡単なオプションです。

WooCommerce をインストールするには:

1. **プラグイン > 新規プラグインを追加** へ移動します。
2. 「WooCommerce」を検索します。
3. **今すぐインストール** を選択します。
4. **今すぐ有効化** を選択すると、WooCommerce ウィザードの準備が整います。

WooCommerce を初めて有効化する際、「有効化」をクリックした後、次の画面に [WooCommerce セットアップウィザード](https://woocommerce.com/document/woocommerce-setup-wizard/) が表示されます。このウィザードでは、WooCommerce 機能をサイトに設定および構成できます。

セットアップ ウィザード (オンボーディング ウィザードとも呼ばれます) の完全なチュートリアルについては、[WooCommerce セットアップ ウィザードのドキュメント](https://woocommerce.com/document/woocommerce-setup-wizard/) をお読みください。

[マルチサイトネットワークインストール](https://wordpress.org/support/article/create-a-network/)では、WooCommerce は他のほとんどのプラグインと同様に動作します。ネットワーク内の各サイトはデータベースを共有しますが、情報は別々のテーブルに保存されます。各ストアは独立したセットアップです。

WooCommerce とその拡張機能などのプラグインをネットワークで有効化することはできますが (*WordPress 管理 > マイサイト > ネットワーク管理 > プラグイン > 新規追加*)、ネットワーク内のサイト間で製品データベース、チェックアウト、ユーザー アカウントを共有することはできません。

サイトのネットワーク全体で共有されるのはテーマとプラグインのみです。

セキュリティ上の理由から、サイトで使用するすべてのプラグインと拡張機能は常に最新バージョンをご利用いただくことをお勧めいたします。また、最新バージョンのプラグインと拡張機能は、現在利用可能なすべての機能のメリットを常に享受できます。そのため、このセクションはあくまでもガイダンスとしてご提供しております。

WooCommerce の以前のバージョンを使用するには:

1. 現在のプラグインを無効化して削除します。
2. ストアのデータベースの以前のバックアップを復元します。
3. [詳細表示](https://wordpress.org/plugins/woocommerce/advanced/) から以前のバージョンの WooCommerce をダウンロードします。
4. **プラグイン > 新規追加** から以前のバージョンをアップロードします。
5. 以前のバージョンの WooCommerce を有効化します。

注意点が1つあります。手順2で述べたように、WooCommerceデータベースのバージョンが更新されているかどうかを確認する必要があります。多くの場合、WooCommerceのバージョンごとにデータベースも更新されるため、すべてが正常に動作することを確認するには、以前のバージョンのWooCommerceからデータベースを復元する必要があります。

そのため、WooCommerce のようなミッションクリティカルなソフトウェアの新リリースをテストするために、ステージング環境と並行してバックアップを用意することを強くお勧めします。詳しくは、[WooCommerce のアップデート](https://woocommerce.com/document/updating-woocommerce/) をご覧ください。

WooCommerce をアンインストールまたは削除する際に理解しておくべきことが 2 つあります。

- WordPressからプラグインを無効化して削除した場合、**プラグインとそのファイルのみが削除されます**。設定、注文、商品、ページなどはデータベースに残ります。
- 商品や注文データなど、**すべての** WooCommerceデータを削除する必要がある場合は、**プラグインを無効化して削除する前に**サイトの*wp-config.php*ファイルを変更できる必要があります。[WooCommerce開発者ドキュメント](https://developer.woocommerce.com/docs/code-snippets/uninstall_remove_all_woocommerce_data)で、その方法について詳しくお読みください。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

