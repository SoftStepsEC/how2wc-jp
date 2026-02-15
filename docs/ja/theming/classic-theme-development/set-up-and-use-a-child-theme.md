---
title: 子テーマの設定と使用方法
url: https://woocommerce.com/document/set-up-and-use-a-child-theme/
---

<ul class="documentation_categories">
<li class="documentation_category">テーマ設定</li>
<li class="documentation_category">クラシックテーマの開発</li>
</ul>
**注:** このドキュメントは、クラシック子テーマの作成と使用を目的としています。子ブロックテーマの作成方法や、クラシックテーマとブロックテーマの違いについて詳しくは、[WooCommerce ブロックテーマの開発](https://woocommerce.com/docs/theming/block-theme-development/theming-woo-blocks/)および[WordPress ブロック子テーマの開発](https://learn.wordpress.org/lesson-plan/create-a-basic-child-theme-for-block-themes/)をご覧ください。

場合によっては、オプションで可能な範囲を超えてテーマやWooCommerceをカスタマイズする必要があるかもしれません。このガイドラインでは、子テーマを使用してサイトをカスタマイズする基本的な方法を説明します。

## 子テーマとは何ですか?

始める前に、子テーマとは何かを理解しておくことが重要です。簡単に言うと、子テーマとは親テーマの上に重ねて、新しいテーマを一から開発することなく変更を加えることができるレイヤーのことです。子テーマを使用する主な理由は2つあります。

- テーマ開発者は、子テーマを使用してテーマのバリエーションを提供できます。これは、[Storefront 子テーマ](https://woocommerce.com/products/storefront/) で行っていることと同様です。
- 子テーマはプラグインや親テーマよりも優先されるため、開発者は子テーマを使用して、親テーマやサイト上のプラグインのカスタマイズをホストできます。

[WordPress Codex のこのガイド](https://developer.wordpress.org/themes/advanced-topics/child-themes/)をお読みください。

## バックアップを作成する​

ウェブサイトをカスタマイズする前に、万が一のトラブルに備えて、必ずサイトのバックアップを作成してください。詳しくは、[WordPressコンテンツのバックアップ](https://woocommerce.com/document/backup-wordpress-content/)をご覧ください。

## はじめに

まず、子テーマを準備する必要があります。

### 子テーマの作成​

まず、子テーマ用の新しいスタイルシートを作成する必要があります。「style.css」という新しいファイルを作成し、そこに以下のコードを追加します。

```
/*Theme Name: Child ThemeVersion: 1.0Description: Child theme for Woo.Author: WooAuthor URI: https://woocommerce.comTemplate: themedir*/
```

次に、**Template** フィールドをインストール済みの WooTheme を指すように変更する必要があります。この例では、`wp-content/themes/storefront/` にインストールされている Storefront テーマを使用します。結果は次のようになります。

```
/*Theme Name: Storefront ChildVersion: 1.0Description: Child theme for Storefront.Author: WooAuthor URI: https://woocommerce.comTemplate: storefront*//* --------------- Theme customization starts here ----------------- */
```

**注:** Storefront では、メインの親 Storefront テーマによって自動的に実行されるため、テーマの `functions.php` ファイルから PHP を使用して親テーマのスタイル ファイルをキューに追加したり、子テーマの `style.css` ファイルに `@import` したりする必要はありません。

Storefront では、子テーマを起動して実行するために必要なのは、空の `functions.php` ファイルと `style.css` ファイルだけです。

## アップロードとアクティベート

子テーマは、FTP クライアント経由、または WordPress の「新しいテーマの追加」オプションを使用してアップロードできます。

- **FTP経由。** FTPを使用する場合、ウェブサイトのフォルダに直接アクセスすることになります。つまり、新しい子テーマをアップロードするには、ホストへの**FTPアクセス**が必要です。アクセスできない場合は、ホストに問い合わせてFTPログイン情報を入手し、FTPプログラムをダウンロードしてファイルをアップロードしてください。
- **WPダッシュボード経由。** 子テーマフォルダの.zipファイルを作成すれば、**WordPress > 外観 > テーマ > 新規追加** セクションからサイトにアップロードできます。

完了すると、子テーマが `wp-content/themes/` 内の新しいフォルダ（例：`wp-content/themes/storefront-child/`）にアップロードされます。アップロードが完了したら、**WP ダッシュボード > 外観 > テーマ** に移動して子テーマを有効化できます。

## デザインと機能のカスタマイズ​

子テーマの変更準備が整いました。現時点ではカスタマイズ項目がまだありませんので、親テーマを変更せずに子テーマをカスタマイズする方法をいくつか見ていきましょう。

### デザインのカスタマイズ​

サイトのタイトルの色を変更する例を一緒に見てみましょう。`/storefront-child/style.css` に次のコードを追加してください。

```
.site-branding h1 a {    color: red;}
```

ファイルを保存してブラウザを更新すると、サイトタイトルの色が変更されていることがわかります。

### テンプレートの変更​

**注:** これはStorefrontの子テーマには適用されません。Storefrontの子テーマのファイルへのカスタマイズは、アップデート時に失われます。Storefrontの子テーマのファイルを直接カスタマイズするのではなく、カスタマイズプラグインにコードスニペットを追加することをお勧めします。そのためのプラグインを作成しました。[Theme Customizations](https://github.com/woocommerce/theme-customisations)を無料でダウンロードしてください。

でも、待ってください！テーマフォルダ内のテンプレートファイル（`*.php`）でも同じことができます。例えば、ヘッダーのコードを変更したい場合は、親テーマフォルダ（`wp-content/themes/storefront/header.php`）から子テーマフォルダ（`wp-content/themes/storefront-child/header.php`）にheader.phpをコピーする必要があります。子テーマにコピーしたら、`header.php`を編集して必要なコードをカスタマイズします。子テーマの`header.php`は、親テーマの`header.php`の代わりに使用されます。

WooCommerceテンプレートも同様です。子テーマに「WooCommerce」という新しいフォルダを作成すれば、WooCommerceテンプレートをウェブサイト全体のデザインに合わせて変更することができます。WooCommerceのテンプレート構造の詳細については、[こちら](https://woocommerce.com/document/template-structure/)をご覧ください。

### 機能の変更​

**注意**: 子テーマの functions.php は **空** で、親テーマの functions.php の内容は何も含めないでください。

子テーマの `functions.php` は、親テーマの `functions.php` より **先に** 読み込まれます。親テーマの関数が **プラガブル** な場合、親テーマの関数を子テーマの `functions.php` にコピーし、親テーマの関数を置き換えることができます。唯一の要件は、親テーマの関数が **プラガブル** であることです。つまり、条件文で囲まれているということです。例:

```
if ( ! function_exists( "parent_function_name" ) ) {    parent_function_name() {        ...    }}
```

親テーマの関数が **プラグ可能** な場合は、それを子テーマの `functions.php` にコピーし、関数を好みに合わせて変更できます。

## テンプレートディレクトリとスタイルシートディレクトリ​

WordPressは子テーマでは処理が異なる点がいくつかあります。子テーマにテンプレートファイルがある場合は、WordPressがファイルを読み込む方法を変更する必要があります。`get_template_directory()`は親テーマを参照します。子テーマのファイルを使用するには、`get_stylesheet_directory();` を変更する必要があります。

[More info on this from the WP Codex](https://developer.wordpress.org/themes/advanced-topics/child-themes/#referencing-or-including-other-files)

## 子テーマのサポート​

子テーマに関する基本的なサポートは提供しており、簡単に回答できますが、テーマのカスタマイズに含まれます。サポート内容については、[サポートポリシー](https://woocommerce.com/support-policy/)をご参照ください。子テーマについてご不明な点がございましたら、[WordPressフォーラム](https://wordpress.org/support/forums/)をご利用ください。

## サンプル子テーマ​

まずはこの記事の冒頭にあるサンプルの子テーマをダウンロードしてください。子テーマは親テーマと一緒に **wp-content/themes/** フォルダに配置してください。

