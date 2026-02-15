---
title: シミュレーターでWooCommerce Androidアプリをセットアップする
url: https://woocommerce.com/document/android/android-simulator/
---

WooCommerce Androidアプリのテストやトラブルシューティングを行う際に、Androidシミュレーターで確認すると便利な場合があります。このガイドでは、その設定方法を詳しく説明します。

**注:**このドキュメントは、高度なトラブルシューティングに役立つガイドとして提供されています。ただし、記載されている手順は[サポートポリシー](https://woocommerce.com/support-policy/)の対象外であり、実装に関する直接的なサポートは提供できません。資格のあるWordPress/WooCommerce開発者のサポートをご希望の場合は、[Codeable](https://codeable.io/?ref=z4Hnp)または[Woo Agency Partner](https://woocommerce.com/development-services/)を強くお勧めします。

1. [Android Studio](https://href.li/?https://developer.android.com/studio/)をダウンロードし、コンピューターにインストールします。

2. 完了したら、「既存の Android Studio プロジェクトを開く」を選択します。

3. [GitHub](https://href.li/?https://github.com/woocommerce/woocommerce-android/releases) に移動し、最新の Android リリース `.zip` ファイルをダウンロードします。

4. ファイルをコンピューター上で解凍します。

5. 「既存の Android Studio プロジェクトを開く」ように求められたら、解凍したフォルダを選択し、「OK」をクリックします。

6. Android Studioでプロジェクトのインストールが開始されますが、いわゆる「ビルド」が必要なため、完了できません。このプロセスを続行するためには「ビルド」は必要ありませんが、「ビルド設定ファイル gradle.properties が存在しません。READMEの指示に従ってください」というメッセージが表示されます。

7. シミュレーターで使用するデバイスを設定します。右上の電話アイコンをクリックして、AVD（Android Virtual Device）マネージャーを開きます。

8. AVD マネージャーで、「仮想デバイスの作成」ができる画面が開きます。

9. 「ハードウェアの選択」画面で、設定する仮想デバイスを選択します。

10. 「システムイメージ」を選択します。お好みのシステムイメージをダウンロードする必要があります。「次へ」をクリックしてからダウンロードとインストールには数分かかります。

次のステップは、WooCommerce Android アプリをシミュレータにインストールすることです。

1. 「再生」ボタンをクリックしてシミュレータを実行します。

2. シミュレーターにアプリをインストールするには、[GitHub](https://href.li/?https://github.com/woocommerce/woocommerce-android/releases) に移動し、最新リリースの `.apk` ファイルをダウンロードします。

3. `.apk` ファイルをコンピューターから実行中のシミュレーターにドラッグ アンド ドロップします。

4. APK のインストールが完了すると、シミュレーターに「WooCommerce」アイコンが表示されます。

5. `WooCommerce` アイコンをクリックして、シミュレーターでアプリを起動します。

**注:**このドキュメントは、高度なトラブルシューティングに役立つガイドとして提供されています。ただし、記載されている手順は[サポートポリシー](https://woocommerce.com/support-policy/)の対象外であり、実装に関する直接的なサポートは提供できません。資格のあるWordPress/WooCommerce開発者のサポートをご希望の場合は、[Codeable](https://codeable.io/?ref=z4Hnp)または[Woo Agency Partner](https://woocommerce.com/development-services/)を強くお勧めします。

