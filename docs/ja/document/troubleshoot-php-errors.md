---
title: PHPエラーのトラブルシューティング
url: https://woocommerce.com/document/troubleshoot-php-errors/
---

PHPは、WordPressで作成されたウェブサイトを含む多くのウェブサイトで使用されている人気のスクリプト言語です。PHPはウェブホスティングサーバー上で実行され、フォーム送信の処理、ユーザーセッションの管理、データベースとのやり取りといった複雑な機能をウェブサイトで実行できるようにします。

**注:**このドキュメントは、高度なトラブルシューティングに役立つガイドとして提供されています。ただし、記載されている手順は[サポートポリシー](https://woocommerce.com/support-policy/)の対象外であり、実装に関する直接的なサポートは提供できません。資格のあるWordPress/WooCommerce開発者のサポートをご希望の場合は、[Codeable](https://codeable.io/?ref=z4Hnp)または[Woo Agency Partner](https://woocommerce.com/development-services/)を強くお勧めします。

WordPressサイトのPHPエラー（WooCommerceに影響するものも含む）を見つけるには、エラーログを確認するか、WordPressのデバッグを有効にするか、WooCommerceに組み込まれているステータスログを参照します。それぞれの方法にアクセスするには、以下の手順に従ってください。

- **エラーログを確認**: ウェブホスティングアカウントには通常、PHP に関する問題を記録したエラーログが含まれています。これらのログには、ホスティングコントロールパネルの「ログ」や「エラーログ」などのセクションからアクセスできます。
- **デバッグを有効にする**: [WordPress の組み込みデバッグ機能](https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/) を有効にすると、サイトにエラーが直接表示されます。これによりデバッグが有効になるだけでなく、サイトにもエラーが表示され、`/wp-content/` ディレクトリ内の `debug.log` ファイルに記録されます。機密情報を保護するために、**本番サイトではこの機能を無効にしてください**。
- **WooCommerce ステータスログ**: WooCommerce も独自のログを保持しており、オンラインストアの特定の問題のトラブルシューティングに非常に役立ちます。これらのログは、WordPress 管理ダッシュボードで *WooCommerce > ステータス > ログ* に移動して確認できます。

これらのツールを使用すると、PHP エラーを効果的に追跡して解決し、サイトとオンライン ストアが効率的に動作することを保証できます。

PHPには、いくつかの種類のエラータイプがあります。これらを理解することで、より効果的に問題をトラブルシューティングできるようになります。

発生する可能性のある主な PHP エラーの種類は次のとおりです。

- **パースエラー**: コードに構文エラーがある場合に発生します。このエラーが発生すると、スクリプトの実行が停止します。一般的な原因としては、セミコロン、中括弧、その他の構文ルールの欠落などが挙げられます。
- **致命的エラー**: これらのエラーは重大なもので、スクリプトの実行が停止します。PHP が要求内容を理解しても、タスクを実行できない場合（存在しない関数やクラスの呼び出しなど）に発生します。
- **警告エラー**: スクリプトの実行は停止しません。単に何か問題があることを警告するだけです。例としては、存在しないファイルをインクルードした場合などが挙げられます。警告が表示されても、PHP はスクリプトの実行を続行します。
- **通知エラー**: 通知は、コードの改善を示唆する軽微なエラーまたは警告であり、必ずしもスクリプトの実行に影響を与えるものではありません。例としては、未定義の変数や配列のインデックスへのアクセスなどが挙げられます。
- **非推奨エラー**: これらは、PHP コードが古く、将来の PHP バージョンではサポートされない可能性がある場合に発生します。コードを新しい標準に更新することをお勧めします。
- **回復可能なエラー**: これらは、キャッチ可能な例外によって致命的なエラーがキャッチされた場合に発生します。PHP では、カスタムエラーハンドラーを使用してスクリプトを続行することで、これらのエラーを適切に処理できます。

たとえば、WooCommerce ストアでテーマ ファイルまたはカスタム プラグインを編集しているときに、PHP の解析エラーが発生する可能性があります。

WooCommerceサイトで商品の価格を表示する方法を変更するカスタムPHPコードを追加したいとします。テーマの`functions.php`ファイルに次の関数を追加します。

```
function modify_product_price_display() {
    echo 'New price: ' . wc_get_price_to_display( $product;
}
```

上記のコード スニペットでは、関数 `wc_get_price_to_display` の末尾の閉じ括弧がありません。

正しいコードは次のようになります。

```
function modify_product_price_display() {
    echo 'New price: ' . wc_get_price_to_display( $product );
}
```

最初のスニペットに括弧がないと解析エラーが発生します。PHP では、スクリプトを実行する前に構文が正しいと想定されます。

このエラーは通常、スクリプトの実行を停止させ、サイトの読み込みを完全に停止させる可能性があります。`functions.php` ファイル内の問題のある行を示すエラーメッセージが表示される場合もあります。これにより、構文エラーを特定して修正することができます。

テーマ、プラグイン、拡張機能、サーバー構成など、さまざまな要因が致命的なエラーを引き起こす可能性があります。

例えば、WooCommerce のコンテキストでは、未定義の関数を使用しようとすると致命的なエラーが発生する可能性があります。テーマの `functions.php` ファイルに次のコードを追加して、特定の条件下で特別割引を適用する関数を追加しようとしていると想像してください。

```
function apply_special_discount() {
    if ( is_user_logged_in() ) {
        add_discount_to_cart(10); // Assume this is meant to add a 10% discount
    }
}
add_action('woocommerce_before_cart', 'apply_special_discount');
```

このコードでは、関数「add_discount_to_cart()」がテーマ、拡張機能、プラグイン、またはWooCommerceコアファイルのどこにも定義されていない場合、PHPは実行時に致命的なエラーをスローします。通常、このエラーメッセージは関数が未定義であることを示し、スクリプトの実行を停止させます。

このエラーにより、WooCommerce が依存する WordPress 実行の通常のライフサイクルが中断されるため、ページ全体の読み込みが妨げられます。

このシナリオで致命的なエラーが発生する可能性がある例を以下に示します。

```
Fatal error: Uncaught Error: Call to undefined function add_discount_to_cart() in /path/to/your/site/wp-content/themes/your-theme/functions.php:5
Stack trace:
#0 /path/to/your/site/wp-includes/class-wp-hook.php(307): apply_special_discount('')
#1 /path/to/your/site/wp-includes/class-wp-hook.php(331): WP_Hook->apply_filters(NULL, Array)
#2 /path/to/your/site/wp-includes/plugin.php(474): WP_Hook->do_action(Array)
#3 /path/to/your/site/wp-content/plugins/woocommerce/includes/class-wc-cart.php(138): do_action('woocommerce_bef...')
#4 /path/to/your/site/wp-content/plugins/woocommerce/includes/class-wc-cart.php(112): WC_Cart->calculate_totals()
#5 /path/to/your/site/wp-content/plugins/woocommerce/includes/class-wc-cart-session.php(53): WC_Cart->init()
#6 /path/to/your/site/wp-content/plugins/woocommerce/includes/class-woocommerce.php(597): WC_Cart_Session->get_cart_from_session()
#7 /path/to/your/site/wp-includes/class-wp-hook.php(307): WooCommerce->init('')
#8 {main} thrown in /path/to/your/site/wp-content/themes/your-theme/functions.php on line 5
```

このようなエラーを解決するには、コードで適切に定義された関数が使用されていることを確認する必要があります。

- [WooCommerce 関数](https://developer.woocommerce.com/docs/useful-core-functions/)
- [WordPress 関数](https://woocommerce.com/document/wordpress-functions/)

WooCommerce を使用する際に PHP で発生する警告エラーの例としては、ファイルのインクルードが挙げられます。PHP スクリプトを使って WooCommerce サイトをカスタマイズし、いくつかの機能を追加しようとしているとします。そこで、これらの機能に固有の様々な設定を含む設定ファイルをテーマの `functions.php` ファイルに含めることにしました。

```
include 'config/settings.php';
```

指定されたディレクトリにファイル `config/settings.php` が存在しない場合、またはパスが正しくない場合、PHP は警告エラーを生成します。このエラーはファイルが見つからなかったことを通知します。ただし、スクリプトは `functions.php` ファイル内の残りのコードの実行を続行します。

警告は次のようになります。

```
Warning: include(config/settings.php): failed to open stream: No such file or directory in /path/to/your/theme/functions.php on line 10

Warning: include(): Failed opening 'config/settings.php' for inclusion (include_path='.:/usr/lib/php:/usr/local/lib/php') in /path/to/your/theme/functions.php on line 10
```

このエラーはページの読み込みを完全に停止させるものではありませんが、設定ファイルが見つからないことで、その設定が他の機能にとって重要な場合、他の機能が意図したとおりに動作しない可能性があります。ファイルパスを修正するか、指定された場所にファイルが存在することを確認することで、この警告に対処できます。

WooCommerce を操作するときに PHP で通知エラーが発生する例として、未定義の変数を使用しようとしたときに発生することがあります。

WooCommerceで商品がセール中かどうかに応じて価格表示を調整する関数を作成するとします。テーマの`functions.php`ファイルに次のコードを追加します。

```
function show_discount_notice() {
    global $product;
    if ($product->is_on_sale()) {
        echo 'Sale Price: ' . $sale_price;
    }
}
add_action('woocommerce_after_shop_loop_item_title', 'show_discount_notice');
```

このスニペットでは、変数 `$sale_price` が echo される前に定義または初期化されていない場合、PHP は通知エラーをトリガーします。この通知は通常、次のような内容になります。

```
Notice: Undefined variable: sale_price in /path/to/your/theme/functions.php on line 4
```

この通知はスクリプトの実行を停止するものではありませんが、コードが未設定の変数を使用しようとしていることを示しています。これにより、ウェブサイトに誤った出力や予期しない出力が表示される可能性があります。この場合、`$sale_price` を初期化するか、商品データから正しく導出されていることを確認することで、問題は解決し、通知が表示されなくなります。

PHP の非推奨エラーは、サイトが古い関数や機能を使用している場合に発生します。

たとえば、テーマの `functions.php` ファイルで、新しい関数に置き換えられて廃止された古い WooCommerce フックまたはフィルター関数 (製品カテゴリを一覧表示する `woocommerce_get_product_terms` など) を使用すると、次のようになります。

```
function list_product_categories() {
    $terms = woocommerce_get_product_terms($product->id, 'product_cat');
    foreach ($terms as $term) {
        echo $term->name . ', ';
    }
}
add_action('woocommerce_after_shop_loop_item', 'list_product_categories');
```

この非推奨の関数を使用すると、PHPはスクリプトの実行を停止しません。代わりに、次のような非推奨の警告がログに記録されます。

```
Deprecated: woocommerce_get_product_terms is deprecated since version 3.0! Use wc_get_product_terms instead.
```

このエラーは、WooCommerce の最新のベストプラクティスまたは新しい関数に合わせてコードを更新するための警告です。代わりに推奨される `wc_get_product_terms` 関数を使用すると、この非推奨のエラーが解決され、WooCommerce および WordPress の将来のバージョンとの互換性が向上します。

回復可能なエラーは、カスタム エラー処理メカニズムによってエラーがキャッチされ、処理される可能性がある場合に発生します。

WooCommerce の決済処理関数をカスタマイズしているとします。決済処理関数で、誤ってパラメータの型ヒントを誤って入力してしまいました。

```
function process_payment(int $amount, array $order_details) {
    // Process payment logic here
    echo "Processing payment of $" . $amount . " for order #" . $order_details['order_id'];
}

try {
    // Simulating a call to process_payment with incorrect type for $order_details
    process_payment(100, "This should be an array");
} catch (TypeError $e) {
    echo "Error: " . $e->getMessage();
}
```

このコードスニペットでは、`process_payment` 関数は `$amount` に整数、`$order_details` に配列を期待しています。`$order_details` に配列ではなく文字列を渡すと、`TypeError` が発生します。このエラーは try ブロック内で発生しており、TypeError を処理する対応する catch ブロックによってキャッチされているため、回復可能なエラーとなります。

このエラー処理の出力は次のようになります。

```
Error: Argument 2 passed to process_payment() must be of the type array, string given
```

このタイプのエラーは、エラー発生後もスクリプトの実行が継続されるため、回復可能です。これにより、アプリケーション全体の機能を損なうことなく、エラーを適切に処理できます。

PHPには、プログラマーがコード内でどのような問題が発生したかを理解するのに役立つ、様々なレベルのエラーがあります。これらのエラーレベルを簡単に説明します。

- **致命的なエラー (E_ERROR)**: プログラムを直ちに停止させる重大な問題です。
- **警告 (E_WARNING)**: プログラムは停止しませんが、修正が必要な問題が発生したことを示します。
- **パースエラー (E_PARSE)**: コードの記述ミスにより、PHP がコードを全く理解できない場合に発生します。
- **通知 (E_NOTICE)**: コードが期待どおりに動作しない可能性を示唆する軽微な問題ですが、プログラムは実行可能です。
- **コアエラー (E_CORE_ERROR)**: 致命的なエラーに似ていますが、プログラムの実行中ではなく、PHP 自体の起動時に発生します。
- **コア警告 (E_CORE_WARNING)**: 警告と同様に、PHP の起動時に発生します。
- **コンパイルエラー (E_COMPILE_ERROR)**: PHP が実行前にコードを準備する際に発見された重大な問題です。
- **コンパイル警告 (E_COMPILE_WARNING)**: コード実行の準備中に検出された警告。
- **ユーザーエラー (E_USER_ERROR)**: 特殊なケースに対応するためにプログラマがコード内に意図的に追加したエラー。
- **ユーザー警告 (E_USER_WARNING)**: プログラマがコード内に意図的に追加した警告。
- **ユーザー通知 (E_USER_NOTICE)**: 深刻度の低い問題を特定するためにプログラマが追加した通知。
- **厳密な通知 (E_STRICT)**: コードを改善し、PHP の将来のバージョンとの互換性を高めるための提案。
- **回復可能なエラー (E_RECOVERABLE_ERROR)**: プログラム内で検出および対処できる深刻な問題。
- **非推奨警告 (E_DEPRECATED)**: 削除予定で今後使用すべきではない PHP の古い部分に関する警告。
- **ユーザーによる非推奨の警告 (E_USER_DEPRECATED)**: プログラマーがコードに追加した古い手法に関する警告。
- **すべてのエラー (E_ALL)**: すべての種類のエラーと警告を表します。

これらの各レベルは、開発者が対応方法（コードをすぐに修正する必要があるか、潜在的な問題がないか確認するか、新しいプログラミング手法を使用するために更新する必要があるか）を決定するのに役立ちます。

まだ質問があり、サポートが必要ですか?

- ヘルプデスクからハピネスエンジニアに[お問い合わせ](https://woocommerce.com/my-account/create-a-ticket/)ください。WooCommerce.comで開発または販売されている拡張機能、およびJetpack/WordPress.comをご利用のお客様には、サポートを提供しています。
- お客様でない場合は、[WooCommerceサポートフォーラム](https://wordpress.org/support/plugin/woocommerce/)でサポートを探すか、Wooエージェンシーパートナーにご依頼いただくことをお勧めします。これらのエージェンシーは、高度にカスタマイズされ、拡張性の高いオンラインストアの構築で実績のある信頼できるエージェンシーです。[Wooエージェンシーパートナーの詳細](https://woocommerce.com/development-services/)

