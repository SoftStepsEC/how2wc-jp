---
title: PHPとWordPressを更新する
url: https://woocommerce.com/document/update-php-wordpress/
---

WooCommerceストアのパフォーマンスとセキュリティを最適化するには、サポートされている最低限のバージョンのPHPとWordPressを実行する必要があります。これにより、ビジネスをスムーズに運営し、顧客に最高のオンラインエクスペリエンスを提供できます。

PHPバージョン8.1未満およびMySQLバージョン5.6未満はアクティブなサポートが終了しており、多くのバージョンは*サポート終了*を迎えているため、メンテナンスも行われていません。そのため、古いバージョンのMySQLおよびPHPを使用すると、サイトがセキュリティ上の脆弱性にさらされる可能性があります。

**WooCommerce では PHP 8.3 以上を推奨します。** WooCommerce は PHP 7.4 以上で動作しますが、このバージョンは 2022 年 11 月に正式にサポート終了となり、サイトがセキュリティ上の脆弱性にさらされる可能性があります。

同様に、最適なパフォーマンスとセキュリティを得るには、MySQL 8.0 以上または MariaDB 10.6 以上をお勧めします。

セキュリティ上の理由だけでなく、利用可能なすべての機能を活用するためにも、Web サイトには [WooCommerce の最新リリース](https://wordpress.org/plugins/woocommerce/) と、必要な WordPress および PHP バージョンを使用する必要があります。

サイトで実行されている WooCommerce のバージョンを確認するには:

1. **WooCommerce > ステータス** に移動します。
2. **WordPress 環境** セクションを見つけます。
3. **WooCommerce バージョン:** の行を探します。

WooCommerce を最新バージョンにアップデートすることをお勧めします。詳しくは [WooCommerce のアップデート](https://woocommerce.com/document/how-to-update-woocommerce/) をご覧ください。

サイトで実行されている WordPress のバージョンを確認するには:

1. ダッシュボードで **WooCommerce > ステータス** に移動します。
2. **WordPress 環境** に移動します。
3. **WordPress バージョン** を確認します。

または、**[ツール] > [サイトヘルス] > [情報] > [WordPress]** に移動します。

サイトの WordPress バージョンが上記の表に記載されている最小要件を満たしていない場合は、「**WordPress を更新**」に進んでください。

サイトで実行されている PHP のバージョンを確認するには:

1. ダッシュボードで **WooCommerce > ステータス** に移動します。
2. **サーバー環境** までスクロールします。
3. **PHP バージョン** を見つけます。

サイトの PHP バージョンが上記の表に記載されている最小要件を満たしていない場合は、**PHP の更新** に進んでください。

WordPress は、ストアを運営し、最適な e コマース エクスペリエンスを構築するための基盤となるフレームワークを WooCommerce に提供するソフトウェアです。

＃＃＃＃ 安全

WordPressは世界で最も人気のあるコンテンツ管理システムであるため、ハッカーの標的となっています。WordPressチームは、セキュリティの修正、改善、強化に継続的に取り組んでいます。

#### 新機能

WordPressは、プラグインの開発基盤となる機能を追加しています。つまり、WooCommerceの新機能はWordPressの新しいバージョンに依存しており、利用するには両方のバージョンが必要になります。

WordPress では、リリース時に最新バージョンに更新することをお勧めします。

1. 予期せぬ事態に備えて、アップデートを実行する*前に***バックアップを作成してください。手順については、[バックアップ - 自動および手動](https://woocommerce.com/document/how-to-update-woocommerce/)をご覧ください。
2. WordPressを更新します。
- **ダッシュボード > 更新 > WordPressの更新** に移動します。または
- WordPressサポートチームが提供する[WordPressの更新](https://wordpress.org/support/article/updating-wordpress/)に記載されている手順に従ってください。
  

最新バージョンの PHP を実行することで、WooCommerce ストアはより高速かつ安全になります。

PHP は、WordPress と WooCommerce が実行されるコーディング言語であり、ホスティング会社によってサーバー レベルで設定され、通常はホスティング パネル内で制御できます。

＃＃＃＃ パフォーマンス

PHP の最新バージョンは、以前のバージョンの PHP よりもパフォーマンスと効率が向上するように開発されているため、更新すると WooCommerce ストアが最大 [3～4 倍高速](https://kinsta.com/blog/php-benchmarks/#wordpress-5-woocommerce-benchmarks) になります。

＃＃＃＃ 安全

PHPは世界で最も人気のあるウェブプログラミング言語であり、WordPressと同様にハッカーの標的となっています。PHPの最新バージョンを実行することで、開発チームが継続的に改善を行っているため、古いバージョンの脆弱性を悪用されることがなくなります。

1. 予期せぬ事態に備えて、アップデートを実行する*前に***バックアップを作成してください。手順については、[バックアップ - 自動および手動](https://woocommerce.com/document/how-to-update-woocommerce/)をご覧ください。
2. WordPress.orgのウェブサイトにある[PHPのアップデート](https://wordpress.org/support/update-php/)の**手順**に従ってください。このリンク先では、ホスティングプロバイダーにPHPのバージョンアップを依頼する際に、詳細情報とコピー＆ペーストできるテンプレートを提供しています。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

