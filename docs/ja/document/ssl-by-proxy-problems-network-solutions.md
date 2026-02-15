---
title: プロキシによる SSL の問題 (Network Solutions)
url: https://woocommerce.com/document/ssl-by-proxy-problems-network-solutions/
---

Network Solutionsなど、プロキシによるSSLを必須とするホストは、PHPとWordPressの[is_ssl()](http://codex.wordpress.org/Function_Reference/is_ssl)関数がページが**HTTPS**経由で配信されているかどうかを検出できないため、WordPressとWooCommerceで問題が発生します。これにより**リダイレクトループ**が発生します。

[Network Solutionsの言葉](http://www.networksolutions.com/support/ssl-redirects/)によれば、

> Network Solutions® はプロキシ SSL を使用しています。そのため、サーバー側の変数を使用して HTTPS（セキュア）を検出することはできません。サーバー側のコーディングはすべて HTTP（非セキュア）を検出します。非セキュア接続（http://）をセキュア接続（https://）にリダイレクトしようとするプログラムは、30 秒後に無限ループが発生し、サーバーエラーが発生します。

Network Solutions は 2007 年からこの制限を認識していたため、近いうちにポリシーが変更されることは期待できません。

PHP内では回避策はありません（http://stackoverflow.com/questions/4686668/https-redirect-for-network-solutions）。唯一の回避策は次のとおりです。

1. **WooCommerce 内の SSL 強制設定をオフにする**
2. **JavaScript を使用して SSL にリダイレクトする**

```
<script language="javascript">
if (document.location.protocol != "https:")
{
document.location.href = "https://subdomain.yourdomain.com" + document.location.pathname;
};
</script>
```

この非標準設定は公式にはサポートできないことにご注意ください。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

