---
title: 大量のデータが保存されない問題（変動、レートなど）
url: https://woocommerce.com/document/problems-with-large-amounts-of-data-not-saving-variations-rates-etc/
---

商品バリエーション、税率、その他の大規模なデータセットが保存されない場合、Suhosin（PHPのセキュリティモジュール）がPOSTデータの保存を妨げている可能性があります。この問題は、PHPバージョン**5.3.9以降、および**mod_security**を実行しているサーバーでも発生する可能性があります。

Suhosin が有効になっている場合、データ送信制限を増やすための設定が必要になる場合があります。Suhsoin の設定変更はホストによって異なるため、通常は自分で試すよりもプロバイダーに相談することをお勧めします。ただし、一部のホストでは、**php.ini、suhosin.ini、または .htaccess** を介して設定を変更できます。一般的に、以下の変数を変更する必要があります。

```
suhosin.post.max_array_index_length = 256
suhosin.post.max_totalname_length = 65535
suhosin.post.max_vars = 1024
suhosin.post.max_name_length = 256
suhosin.request.max_varname_length = 256
suhosin.request.max_array_index_length = 256
suhosin.request.max_totalname_length = 65535
suhosin.request.max_vars = 1024
```

保存後、変更を有効にするにはサーバーを再起動する必要があります。Suhosinの設定の詳細については、[http://www.hardened-php.net/suhosin/configuration.html](http://www.hardened-php.net/suhosin/configuration.html) をご覧ください。

**共有ホスティング環境**では、php.ini を編集できない場合があります。その場合は、.htaccess 経由で suhosin 設定を行うことができる場合があります。

```
php_value suhosin.max_array_index_length 256
php_value suhosin.post.max_array_index_length 256
php_value suhosin.post.max_totalname_length 65535
php_value suhosin.post.max_vars 1024
php_value suhosin.post.max_name_length 256
php_value suhosin.request.max_varname_length 256
php_value suhosin.request.max_array_index_length 256
php_value suhosin.request.max_totalname_length 65535
php_value suhosin.request.max_vars 1024
```

ただし、ホスティング プロバイダーのドキュメントを参照するか、ホスティング プロバイダーにチケットを発行してサポートを受けることをお勧めします。

**非ラテン文字を使用する場合**、次の値をデフォルトの 64 から増やすことをおすすめします。これにより、非ラテン文字に関する問題の解決に役立ちます。

```
suhosin.request.max_varname_length = 256
```

新しいバージョンの PHP では、通常 1000 に設定された max_input_vars という php.ini ディレクティブが実装されています。つまり、たとえば 1000 を超えるフォーム フィールドを送信すると切り捨てられ、データが保存されなくなります。

これはphp.iniで変更できます:

```
max_input_vars = 3000
```

これを htaccess 経由で実行する必要がある場合 (共有ホストなど)、次を使用できます。

```
php_value max_input_vars 3000
```

Mod_security もデータの保存を妨げる可能性があり、その場合は 503 エラーが発生する可能性があります。上記の問題と同様に、ホスティングサービスに問い合わせて解決することをお勧めします。回避策として以下が挙げられます。

- データの通過を許可するようにmod_securityを設定する（上級編）
- [IPアドレスによるmod_securityの無効化](http://www.askapache.com/htaccess/modsecurity-htaccess-tricks.html#Disabling_mod_security_conditionally_IP)
- (Dreamhostのみ) コントロールパネルで「追加のWebセキュリティ」設定をオフにする。

参考資料: [http://www.nivas.hr/blog/2012/04/04/beware-of-max_input_vars-php-ini-configuration-option/](http://www.nivas.hr/blog/2012/04/04/beware-of-max_input_vars-php-ini-configuration-option/) [https://shopplugin.net/kb/unable-to-save-products-with-large-amount-of-variations/](https://shopplugin.net/kb/unable-to-save-products-with-large-amount-of-variations/)

このドキュメントで説明されている問題が **本当に** 発生しているかどうかを確認するには、この無料プラグインを一時的にインストールして有効にすることができます: [WP Max Submit Protect](http://wordpress.org/plugins/wp-max-submit-protect/)。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

