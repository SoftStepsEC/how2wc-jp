---
title: WooCommerceストアオーナーのためのアクセシビリティのヒント
url: https://woocommerce.com/document/accessibility-tips-for-store-owners/
---

WooCommerce はアクセシビリティの基盤を提供していますが、ストアオーナーはインクルーシブなエクスペリエンスを実現する上で重要な役割を果たします。このページでは、ストアのコンテンツ、デザイン、カスタマイズのアクセシビリティを向上させるためのヒントとベストプラクティスをご紹介します。

世界の多くの地域では、eコマースストアはアクセシビリティ基準を満たすことが法的に義務付けられています。ストアをアクセシブルにすることは、顧客体験の向上につながるだけでなく、[アメリカ障害者法（ADA）](https://ada.gov/)や[欧州アクセシビリティ法（EAA）](https://employment-social-affairs.ec.europa.eu/policies-and-activities/social-protection-social-inclusion/persons-disabilities/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en)などの法律の遵守にも役立ちます。ほとんどの規制は、測定可能なアクセシビリティ要件を定義する[WCAG 2.2 レベルAA規格](https://www.w3.org/TR/WCAG22)を参照しています。

商品画像やその他の画像に説明的な代替テキストを追加します。これにより、スクリーンリーダーを使用するユーザーが画像の目的とコンテキストを理解しやすくなります。

画像が装飾的な場合を除き、代替テキストを空白のままにしないでください。画像が[装飾的](https://www.w3.org/WAI/tutorials/images/decorative/)である場合は、スクリーンリーダーが読み飛ばせるよう、代替テキストフィールドを空白にしてください。商品画像やリンクされた画像は装飾的ではありません。

カスタムフォームを追加する場合（拡張機能を使用するなど）、次の点を確認してください。

- 各フィールドには、目に見える形でプログラム的に表示されるラベルが含まれます。
- ユーザーが入力すると消えるプレースホルダーテキストだけに頼る必要はありません。

ラベルはフィールドの目的を明確に示し、関連する説明は入力フィールドの近くに配置する必要があります。エラーメッセージは、ARIA属性を使用して関連する入力にプログラム的にリンクされ、スクリーンリーダーによって読み上げられる必要があります。

テーマはアクセシビリティに大きな影響を与えます。WordPressリポジトリで[アクセシビリティ対応](https://wordpress.org/themes/tags/accessibility-ready/)とマークされているテーマを選択してください。これらのテーマは、確立されたアクセシビリティ基準を満たしています。

この指定を受けたテーマは、キーボードナビゲーション、色のコントラスト、その他の WCAG 基準をチェックする WordPress のアクセシビリティレビューに合格しています。

WordPress.org 以外のテーマを選択する場合は、選択する前に開発者にアクセシビリティ適合レポートまたはその他のアクセシビリティドキュメントを要求してください。

ユーザーが一時停止または無効化できる場合を除き、スライダー、動画、アニメーションの自動再生は避けてください。これらの効果は、前庭機能や認知機能に問題のあるユーザーにとって問題となる可能性があります。

アニメーションは、ユーザーのOSの「モーションを減らす」設定を尊重する必要があります。macOSまたはWindowsで「モーションを減らす」オプションを有効にし、サイトで不要なモーションが抑制されていることを確認することで、これをテストできます。テスト用にコンピューターでモーションを減らす機能を有効にする方法は次のとおりです。

- **Windows 11 の場合**: *設定 > アクセシビリティ > 視覚効果 > アニメーション効果* に移動します。
- **macOS の場合**: *システム環境設定 > アクセシビリティ > ディスプレイ > 動きを減らす* に移動します。

アクセシビリティ評価ツールを使用するか、手動テストを実行します。

- キーボードのみを使用してサイト内を移動します。すべてのボタン、リンク、フォームフィールドをTabキーで移動し、ボタンとリンクをReturnキーで操作します。マウスを使用せずに、商品の検索、カートへの商品の追加、チェックアウトの完了が可能であることを確認してください。
- スクリーンリーダーやブラウザ拡張機能（[WAVE](https://wave.webaim.org/)、[axe DevTools](https://chromewebstore.google.com/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd)、WordPressアクセシビリティプラグイン（[Equalize Digital Accessibility Checker](https://equalizedigital.com/accessibility-checker/?ref=woocommerce)）を使用して問題を特定します。
- 200%または400%に拡大して、すべてのコンテンツが読みやすく、要素が重なったり消えたりしていないことを確認してください。
- 視覚障害を持つユーザーがストアをどのように体験しているかをより深く理解するために、[NVDA](https://www.nvaccess.org/) (Windows) や [VoiceOver](https://support.apple.com/guide/voiceover/welcome/mac) (Mac) などの無料のスクリーン リーダーを使用してサイトをテストします。

次の一般的な制限とその軽減方法に注意してください。

- **サードパーティ製拡張機能**: すべての拡張機能が同じようにアクセシブルであるとは限りません。実装前にドキュメントを確認するか、テストを実施してください。
- **カスタムブロック**: カスタムブロックを使用または作成する場合は、セマンティックHTMLと[アクセシビリティのベストプラクティス](https://developer.woocommerce.com/docs/extensions/best-practices-extensions/accessibility/)に従ってください。
- **サイト固有のカスタマイズ**: カスタムコード (JS/CSS) は、意図せずアクセシビリティに影響を与える可能性があります。変更を加えた後は、必ず関連するフローを再テストしてください。
- カスタマイズに色のオプションが含まれている場合は、オンラインのコントラストチェッカーを使用してコントラストをテストしてください。例えば、ボタンのテキストが背景色に対して読みやすいことを確認してください。設定によってアクセシブルではない組み合わせが作成された場合は、管理UIからユーザーに警告することを検討してください。

店舗オーナー向けの役立つツールと参考資料:

- [WordPress アクセシビリティ ハンドブック](https://make.wordpress.org/accessibility/handbook/)
- [WAVE アクセシビリティ ツール](https://wave.webaim.org/)
- [axe DevTools 拡張機能](https://chromewebstore.google.com/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd)
- [NVDA スクリーン リーダー](https://www.nvaccess.org/)
- [VoiceOver (macOS/iOS)](https://support.apple.com/guide/voiceover/welcome/mac)
- [WordPress アクセシビリティ チェッカー プラグイン](https://wordpress.org/plugins/accessibility-checker/)

ストアオーナーの皆様からのご提案やフィードバックをお待ちしております。アクセシビリティに関する問題を発見された場合や、改善のためのアイデアをお持ちの場合は、[サポートにお問い合わせ](https://woocommerce.com/contact-us/)いただくか、[accessibility@woocommerce.com](mailto:accessibility@woocommerce.com)までメールでご連絡ください。皆様からのご意見は、よりインクルーシブなウェブ環境の構築に役立てさせていただきます。

