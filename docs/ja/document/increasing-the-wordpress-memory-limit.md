---
title: WordPressのメモリ制限を増やす
url: https://woocommerce.com/document/increasing-the-wordpress-memory-limit/
---

WordPress のメモリ制限の問題に対処するには、次の 2 つの方法があります。

- メモリ制限を自分で調整してください。
- ホスティング会社にお問い合わせください。

以下に、WordPress のメモリ制限を自分で調整するいくつかの方法を示します。

**注:** このセクションでは高度な知識が必要です。

サイトの `wp-config.php` ファイルの先頭に次のコード スニペットを追加します。

```
define('WP_MEMORY_LIMIT', '256M');
```

このコード スニペットは、`/* 編集はこれで終わりです。公開を楽しんでください。*/` という行の **上** に追加する必要があります。

WordPressのメモリはサーバーのメモリと異なる場合があります。サーバーのメモリ設定に関係なく、WordPressのメモリを設定する必要があります。[wp-config.phpファイルの編集について詳しくは、こちらをご覧ください](https://developer.wordpress.org/advanced-administration/wordpress/wp-config/#Increasing_memory_allocated_to_PHP)。

サイトの `php.ini` ファイルにアクセスできる場合は、以下の行を調整します。

```
memory_limit = 256M ; Maximum amount of memory a script may consume (64M)
```

`php.ini` ファイルの行に 64M が指定されている場合は、代わりに 256M を試してください。

`PHP.ini` にアクセスできない場合は、次のスニペットを `.htaccess` ファイルに追加してみてください。

```
php_value memory_limit 256M
```

上記の方法を自分で試すことに不安がある場合 (または上記の方法が機能しなかった場合) は、ホスティング プロバイダーに連絡して、WordPress のメモリ制限を増やすように依頼してください。

