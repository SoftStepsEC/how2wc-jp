---
title: キャッシュフォルダをCHMODする方法
url: https://woocommerce.com/document/how-to-chmod-the-cache-folder/
---

画像リサイズツールがリサイズされた画像を表示するには、リサイズされたファイルをキャッシュフォルダに保存する権限が必要です。このフォルダはテーマフォルダ内にあります（例：`wp-content/themes/freshnews/cache/`）。画像リサイズツールがこのフォルダに書き込みできるようにするには、キャッシュフォルダをCHMODで変更する必要があります。

CHMOD は、スクリプトがキャッシュフォルダに書き込みできるように **書き込み権限を設定する** ことを意味します。権限を 775 に設定する必要があります。

FTP経由で接続し、上記のテーマフォルダを見つけます。次に、FTPプログラムを使用して、キャッシュフォルダのパーミッションを775（または777、あるいは完全な書き込み権限）に設定します。

これに役立つチュートリアルをいくつか紹介します。

- [About.com: FTPからCHMODを実行する方法](http://php.about.com/od/phpbasics/ht/chmod.htm)
- [Siteground: FTPでCHMODを実行する方法](http://www.siteground.com/tutorials/ftp/ftp_chmod.htm)

すでに FTP プログラムがインストールされている場合は、ヘルプ ファイルを検索するか、Google で検索してください (例:「cuteftp how to chmod」)。

- [SmartFTP](http://www.smartftp.com/) は無料の FTP プログラムで、[CHMOD](http://www.smartftp.com/support/kb/how-to-chmod-file-folders-f13.html) も非常に簡単に行えます。
- [FireFTP](http://fireftp.mozdev.org/) は Firefox の無料アドオンです。

ホストに接続するために必要な接続詳細がない場合は、ホスティングプロバイダーにホスト名、ユーザー名、パスワードを問い合わせる必要があります。

まだ質問があり、サポートが必要ですか?

このドキュメントは、無料の[コア WooCommerce プラグイン](https://wordpress.org/plugins/woocommerce/)に関するものです。このプラグインのサポートは、[WordPress.org のコミュニティフォーラム](https://wordpress.org/support/plugin/woocommerce) で提供されています。このフォーラムを検索すると、同じ質問が過去に投稿され、回答されているケースがよくあります。フォーラムを利用するための WordPress.org アカウントをまだ作成していない場合は、[作成方法はこちら](https://make.wordpress.org/contribute/join/)をご覧ください。

- ここで紹介したコア機能を**拡張**したい場合は、[WooCommerce マーケットプレイス](https://woocommerce.com/products/)で利用可能な拡張機能をご確認ください。
- 継続的な高度なサポートや WooCommerce 向けの**カスタマイズ**が必要ですか？[Woo エージェンシー パートナー](https://woocommerce.com/customizations/)をご活用ください。
- 独自の WooCommerce 統合機能や拡張機能を開発している**開発者**ですか？[開発者向けリソース](https://developer.woocommerce.com/)をご確認ください。

必要な情報が見つからない場合は、下のフィードバック サムを使用してお知らせください。

