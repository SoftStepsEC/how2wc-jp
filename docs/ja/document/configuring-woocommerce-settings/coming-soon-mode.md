---
title: WooCommerce 近日公開モード
url: https://woocommerce.com/document/configuring-woocommerce-settings/coming-soon-mode/
---

**近日公開モード** を使用すると、サイト構築中の公開設定を管理できます。この機能は WooCommerce 設定の **サイトの公開設定** タブで管理でき、セットアップ段階でストアにアクセスできるユーザーを柔軟に制御できます。

[WooCommerce 9.1](https://developer.woocommerce.com/2024/07/11/woocommerce-9-1-coming-soon-product-lookup-optimizations-and-checkout-styling-galore/) 以降、すべてのストアで *近日公開* モードが**デフォルトで有効** になりました。さらに、[バージョン 9.4](https://developer.woocommerce.com/2024/11/11/woocommerce-9-4-supercharging-the-product-collection-block-more/) 以降では、**WooCommerce > 設定 > 詳細 > 機能** に**サイト表示バッジ** が追加されました。この機能により、ユーザーは管理画面でサイト表示バッジの表示/非表示を切り替えることができます。

*WooCommerce > 設定 > サイトの可視性* の下にある **サイトの可視性** 設定では、訪問者に対するサイトの表示方法を管理するための 2 つのオプションがあります。

*近日公開*モードが有効になっている場合、サイトは開発中となり、一般公開されません。サイトは*近日公開***ランディングページ**の背後に隠れ、訪問者からは見えなくなります。ストアを閲覧できるのは、承認されたユーザーまたはプライベートリンクを持つユーザーのみです。

次の追加設定が利用可能になります。

1. ストアページのみに適用：
- この設定は、**既存のサイト**にWooCommerceをインストールするマーチャントにとって最適です。このオプションを有効にすると、**ストア関連ページ**のみが*近日公開*モードで保護されます。
- 訪問者は許可なくストアページにアクセスできなくなりますが、サイトの他の部分には引き続きアクセスできます。
- このオプションを有効にすると、以下のWooCommerceストアページの代わりに、近日公開ランディングページが表示されます。
- カート（*WooCommerce > 設定 > 詳細設定*で設定）。
- チェックアウト（*WooCommerce > 設定 > 詳細設定*で設定）。
- 利用規約（*WooCommerce > 設定 > 詳細設定*で設定）。
- ショップ（*WooCommerce > 設定 > 商品 > 一般設定*で設定）。
- プライバシーポリシー（*設定 > アカウントとプライバシー*で設定）。
    
  
2. プライベートリンクでサイトを共有する：
- この機能を使用すると、構築中のサイトへのアクセスを友人、家族、同僚と共有できます。
- サイトへの選択的なアクセスを提供するためのプライベートリンクが生成され、セットアップフェーズでのフィードバックやコラボレーションが容易になります。
  

**ライブモード**を有効にすると、サイトはすべての訪問者に完全にアクセス可能になり、営業中であることが示されます。さあ、注文が殺到しそうです！

すでに公開されているストアは**デフォルトでライブ モードになります**。手動で変更しない限り、*近日公開*モードの影響を受けません。

WooCommerce をインストールし、オンボーディングプロセスを完了したストアは、**デフォルトで近日公開モード**になります。このモードの適用は、サイト全体に適用するか、ストアページのみに適用するかにかかわらず、特定のロジックに従います。

1. サイト全体に適用
- これは新規サイトのデフォルト設定で、WordPressの「fresh_site」フラグによって決定されます。WordPressの「fresh_site」フラグオプションは、「https://yoursitename.com/wp-admin/options.php」からアクセスできます。
- 最初の管理者ユーザー登録日から1か月以内の場合。
- 「**サイトを非公開リンクで共有**」オプションを使用して、サイトを非公開で共有できます。
  
2. ストアページのみに適用
- サイト全体の保護基準を満たさないサイトの場合、「**ストアページのみに適用**」トグルがデフォルトで有効になっています。
- これにより、ストアページのみが保護され、サイトの他の部分へのアクセスは維持されます。
  

*近日公開*ページテンプレートは[サイトエディタ](https://woocommerce.com/document/woocommerce-store-editing/the-editor/)で完全にカスタマイズ可能で、ブランドイメージに合わせて外観をカスタマイズできます。色、フォント、レイアウトを調整して、ストアのスタイルを反映した独自の近日公開ページを作成できます。詳しくは、[近日公開テンプレートのカスタマイズ](https://woocommerce.com/document/configuring-woocommerce-settings/coming-soon-mode/customising-coming-soon-template/)をご覧ください。

ストアを公開した後、サイトのフロントエンドにすぐにストアの情報が表示されない場合があります。これは**サーバーキャッシュ**が原因である可能性があります。**サーバーキャッシュ**とは、頻繁にアクセスされるデータを一時的に保存し、訪問者のサイト表示速度を向上させる機能です。新しく公開したストアは、サーバーのキャッシュが更新され次第、表示できるようになります。キャッシュが自動的に更新されるまで待つか、ウェブホストに連絡して手動で更新する方法をお問い合わせください。

サーバーキャッシュはページの読み込み速度を速め、ユーザーエクスペリエンスを向上させます。また、サーバー負荷を軽減し、ストアの効率性と信頼性を高めます。ただし、訪問者がストアの最新の更新情報を確認できるように、定期的にサーバーキャッシュをクリアする必要がある場合があります。

### サーバーのキャッシュをクリアする

以下に、一般的なホストをいくつかリストアップし、各プラットフォームのキャッシュ管理に関するサポート記事へのリンクを記載しました。ご利用のホストを以下から探し、ウェブサイトに記載されている手順に従ってサーバーキャッシュをクリアしてください。ご利用のホストがリストにない場合は、サポートチームにお問い合わせください。

- [Bluehost](https://www.bluehost.com/help/article/wordpress-how-to-use-our-page-caching-feature)
- [Nexcess](https://www.nexcess.net/help/how-to-use-the-nexcess-page-cache/)
- [Pressable](https://pressable.com/knowledgebase/edge-cache/#purging-flushing-edge-cache)
- [SiteGround](https://www.siteground.com/kb/clear-site-cache/)
- [WordPress.com](https://wordpress.com/support/clear-your-sites-cache/#clear-your-sites-cache)
- [Cloudflare](https://developers.cloudflare.com/cache/how-to/purge-cache/)
- [Hostinger](https://support.hostinger.com/en/articles/6215624-how-to-use-cache-manager)
- [Ionos](https://www.ionos.com/digitalguide/hosting/blogs/wordpress-cache-clear/)

### サードパーティの最適化ツール

サイト最適化のためにサードパーティ製ソフトウェア（コンテンツ配信ネットワーク（CDN）やWordPressプラグインなど）をご利用の場合は、それぞれのドキュメントをご参照ください。詳しくは、[WordPress.orgの開発者向けキャッシュドキュメント](https://developer.wordpress.org/advanced-administration/performance/cache/)をご覧ください。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

