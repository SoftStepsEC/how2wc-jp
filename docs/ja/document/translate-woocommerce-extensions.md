---
title: WooCommerce拡張機能の翻訳
url: https://woocommerce.com/document/translate-woocommerce-extensions/
---

WooCommerce.com で販売されているプラ​​グインは翻訳に対応しており、あらゆる翻訳プラグインと併用できます。中には翻訳がバンドルされているプラ​​グインもあり、私たちは翻訳者と協力して翻訳範囲を拡大することに常に尽力しています。

WooCommerce または拡張機能の翻訳に興味がある場合は、[ローカリゼーションに関するこのドキュメント](https://woocommerce.com/document/woocommerce-localization/)を確認してから始めてください。

プラグインに翻訳がバンドルされている場合、サイトの言語が英語以外に切り替えられた際に自動的に読み込まれます。可能な限り完全な翻訳をバンドルするよう努めていますが、完全な翻訳が利用できない場合は部分的な翻訳をバンドルするため、一部の文字列が翻訳から欠落している可能性があります。

独自の翻訳を作成し、それをバンドル用に提出したい場合は、[ヘルプデスクに連絡](https://woocommerce.com/my-account/create-a-ticket/)して、翻訳をプラグイン開発者に渡してください。

**拡張機能を**手動で自分の言語に翻訳したい場合は、[PoEdit](https://poedit.net/)のようなgettextツールが役立ちます。.potファイルを適切に翻訳する方法を理解していることを確認してください。以下のチュートリアルが役立ちます。

- [WordPressプラグインを翻訳する](https://wplang.org/translate-theme-plugin/)
- [WordPressテーマまたはプラグインを翻訳する](https://nicola.blog/2015/09/02/translate-wordpress-theme-plugins-loco-translate/)

翻訳を始めるには、いくつか必要なものがあります。

- 使用するgettextツール（PoEdit（推奨）またはLocoTranslateなど）
- プラグインの**テキストドメイン**。どのテキストドメインを使用すればよいかわからない場合は、通常、メインプラグインファイルの先頭に記載されています。プラグインをダウンロードし、解凍してフォルダを開き、プラグインと同じ名前のファイル（サブフォルダではなく、常にメインフォルダ内にあります）を探してください。
- プラグインの**.potファイル** — これは通常、プラグイン内の`/languages/`ディレクトリまたは`/i18n/`ディレクトリにあります。

プラグインのテキストドメインと.potファイルを入手したら、翻訳を開始できます 🙂

完了したら、.potファイルと同じフォルダに翻訳ファイルを追加できます。名前が正しいことを確認してください。

たとえば、プラグインの .pot ファイルの名前が `woocommerce-plugin-textdomain.pot` の場合、翻訳ファイルの名前は `woocommerce-plugin-textdomain-aa_AA.po` と `woocommerce-plugin-textdomain-aa_AA.mo` になります。ここで、`aa_AA` は [言語のコード](https://wordpress.org/support/article/installing-wordpress-in-your-language/) (例: fr_FR) です。

```
text-domain
```

プラグインのアップグレード時に翻訳を保存したい場合は、WordPress コアディレクトリに移動することもできます。プラグインの翻訳は次の場所に保存できます。

```
wp-content/languages/plugins/woocommerce-plugin-textdomain-aa_AA.po
```

`wp-content/languages/plugins/` ディレクトリには、あらゆるプラグインの翻訳が保存されます。カスタム翻訳はここに安全に保存でき、プラグインのアップデートによって上書きされることはありません。

**注 #1:** Loco Translate では、翻訳の作成場所として 3 つの異なる場所を提供しています。独自の翻訳に最適なのは **Custom** です。これは、カスタム翻訳がアップデートによって元に戻ってしまうのを防ぐだけでなく、WooCommerce Subscriptions などの拡張機能内の文字列を正しく翻訳するためにも必要です。*Author* の場所はプラグイン内にあるため、拡張機能のアップデートによって上書きされてしまうため、また *System* の場所は *translate.wordpress.org* からの翻訳によって上書きされる可能性があるため、避けてください。**注 #2**: Loco Translate の使用中に技術的な問題が発生した場合は、[Loco Translate サポートチームにお問い合わせください](https://wordpress.org/support/plugin/loco-translate/)。

SkyVerge 拡張機能は開発に共通のスケルトンを使用しているため、プラグインにはテキストドメインと翻訳、そしてスケルトン用のテキストドメインと翻訳が含まれます。そのため、プラグイン内の文字列の一部はスケルトンの一部となる可能性があります。

プラグインと同じようにスケルトンを翻訳できますが、その翻訳は別の場所に保存する必要があります (一度翻訳すると、その文字列を使用するすべての SkyVerge 拡張機能に適用されるという利点があります)。

```
We recommend translating what you need to from the skeleton / framework by following the steps below, then moving onto the plugin's strings, following the steps in the section above.
```

SkyVerge プラグイン フレームワークを翻訳する手順は次のとおりです。以下の手順で、`nb_NO` を翻訳の適切なテキスト ドメインに置き換えてください。

フレームワークの .pot ファイルの翻訳をすでに開始している場合は、手順 1 ～ 5 をスキップして、`.po` ファイルと `.mo` ファイルの名前を `woocommerce-plugin-framework-nb_NO.po` と `woocommerce-plugin-framework-nb_NO.mo` に変更するだけです。

1. プラグイン内で、以下のいずれかの場所にある「woocommerce-plugin-framework.pot」ファイルを探します（プラグインにはどちらか一方のみ存在します）。 vendor/skyverge/wc-plugin-framework/woocommerce/i18n/languages/woocommerce-plugin-framework.pot lib/skyverge/woocommerce/i18n/languages/woocommerce-plugin-framework.pot
2. PoEditなどで「woocommerce-plugin-framework.pot」ファイルを開き、「Create New Translation」をクリックします。 [](https://woocommerce.com/wp-content/uploads/2015/10/poedit-new-translation.png)
3. 翻訳の言語を設定し、「OK」をクリックします [](https://woocommerce.com/wp-content/uploads/2015/10/poedit-save-translation.png)
4. **ファイル > 保存** を選択し、ファイルをコンピューターに保存します。ファイル名は「woocommerce-plugin-framework-nb_NO.po」にしてください（拡張子「.po」はアプリケーションによって自動的に追加されます）。
5. 文字列をいくつか翻訳し、**ファイル > MO にコンパイル…** をクリックして、ファイル名が `woocommerce-plugin-framework-nb_NO.mo` であることを確認してください。
6. テスト翻訳をいくつか行ったら、.po ファイルと .mo ファイルの両方を FTP 経由でサイトの `wp-content/languages/woocommerce-plugin-framework/` フォルダにアップロードしてください（このフォルダは作成する必要があります）。2 つのファイルのパスは以下のとおりです。wp-content/languages/woocommerce-plugin-framework/woocommerce-plugin-framework-nb_NO.mo wp-content/languages/woocommerce-plugin-framework/woocommerce-plugin-framework-nb_NO.po
7. サイトのフロントエンドまたは管理者にアクセスし、新しい翻訳が反映されているかどうかを確認してください。反映されていない場合は、管理者と FTP の認証情報をお送りください。喜んでトラブルシューティングさせていただきます。
8. 翻訳テストに合格した場合、ローカル コンピューターで翻訳を完了し、問題がなければ MO ファイルを再コンパイルし、2 つのファイルを `wp-content/languages/woocommerce-plugin-framework/` ディレクトリに再度アップロードします。

`woocommerce-plugin-framework` の翻訳を提出したい場合は、[GitHub で問題を開くか、リクエストをプルしてください](https://github.com/skyverge/wc-plugin-framework)。

複数の言語を使用したい場合や、サイトの言語とは異なる言語を表示したい場合は、WPMLのような多言語ツールが役立ちます。WPMLには、プラグインの翻訳に関する[ドキュメント](https://wpml.org/documentation/getting-started-guide/theme-localization/)が用意されています。

WPML を WooCommerce で使用するには、[WooCommerce Multilingual プラグイン](https://wordpress.org/plugins/woocommerce-multilingual/) をインストールする必要があります。セットアップと構成に関しては、WooCommerce チームがサポートします。

[Loco Translate は、WooCommerce で言語を管理するための確実なアプローチです](https://woocommerce.com/document/woocommerce-localization/#creating-custom-translations-with-Loco-Translate)。

- [PoEdit を入手](https://poedit.net/)
- [WPML ドキュメント](https://wpml.org/documentation/getting-started-guide/theme-localization/)

