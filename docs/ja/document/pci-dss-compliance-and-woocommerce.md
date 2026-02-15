---
title: PCI-DSSコンプライアンスとWooCommerce
url: https://woocommerce.com/document/pci-dss-compliance-and-woocommerce/
---

ペイメントカード業界データセキュリティ基準（PCI-DSS）は、[ペイメントカード業界セキュリティ基準協議会](https://www.pcisecuritystandards.org/) (PCI SSC) によって策定された、実用的な一連のルールです。その主な目的は、一貫性のあるグローバルなデータセキュリティ慣行を促進し、クレジットカード詐欺を削減することです。

これらの規則は、カード会員データを保存、処理、または送信するすべての人に適用されます。PCI-DSSの詳細については、[クイックリファレンスガイド](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Supporting%20Document/PCI_DSS-QRG-v4_0.pdf)をご覧ください。

[PCI SSC 用語集](https://www.pcisecuritystandards.org/pci_security/glossary) の定義に従ってカード所有者データを保存、処理、または送信する場合は、**PCI-DSS が適用されます**。

オフサイトまたはホストされたフィールドを介して支払いを処理する決済ゲートウェイ（Stripe、PayPal、WooPaymentsなど）を使用している場合、サイトはカード会員の生データを直接処理していません。ただし、サイトはチェックアウトページを提供しているため、**PCI-DSSは引き続き適用されます**。ただし、コンプライアンスの範囲は大幅に縮小される可能性があります。

[WooPayments](https://woocommerce.com/products/woocommerce-payments/)は、対象地域の販売者が自社サイトでPCI準拠の決済を受け入れるための最適な選択肢です。[WooPaymentsのPCI準拠の詳細については、こちらをご覧ください](https://woocommerce.com/document/woopayments/our-policies/pci-compliance/)。

12 のコア PCI-DSS 要件は次のとおりです。

**最終更新**: 2025年6月6日。この概要は、**PCI DSS v4.0.1**で定義されている12の中核要件を反映しています。詳細と最新のドキュメントについては、[PCI SSCウェブサイト](https://www.pcisecuritystandards.org/document_library)をご覧ください。

PCI コンプライアンスは多くの場合、決済処理業者によって強制されており、自己評価アンケート (SAQ) を完了するように求められたり、[承認されたスキャン ベンダー](https://listings.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors) (ASV) によるスキャンを受けるように求められたりすることがあります。

PCI DSS コンプライアンスは、最終的にはストアオーナーの責任となります。WooCommerce プラグインのコア部分は、カード会員データを処理したり、決済処理を直接行わないため、PCI 認定を受けていません。ただし、サイトでカード決済を受け付けるようになれば、たとえ WooPayments のような安全なホスト型ゲートウェイを介してであっても、PCI DSS の適用範囲となります。安全なホスティング環境を使用し、セキュリティのベストプラクティスに従い、PCI 準拠の決済ゲートウェイを統合することで、サイトはコンプライアンス要件を満たすことができます。

多くの PCI 要件は、ホスティング プロバイダー、使用するプラグイン、ユーザー アクセス、更新、セキュリティ スキャンに関するポリシーなど、より広範な環境に適用されます。

以下にいくつかの考慮事項を示します。

1. ホストまたはネットワーク管理者と協力して、ファイアウォールを適切に設定してください。
2. 強力なパスワードを使用し、ホスティング環境のセキュリティを確保してください。
3. **WooCommerce はカード情報を保存することはありません**。[公式 WooCommerce 決済ゲートウェイ](https://woocommerce.com/learn-more-about-official-partner-badging/) は、決済トークン（例：下4桁）を使用する際に、一部のデータのみを保持します。
4. チェックアウトページで SSL を使用し、ホストが SSL に対応していることを確認してください。
5. ホストにマルウェア対策と安全なシステムメンテナンスについて問い合わせてください。
6. 管理者ユーザーを管理する際は、WordPress のロール機能を使用し、[セキュリティのベストプラクティス](https://woocommerce.com/posts/woocommerce-security/) に従ってください。
7. 可能な場合は、管理者レベルのアクティビティを記録・確認し、機密性の高い領域へのアクセスを制限してください。
8. ホストまたは開発者と連携して、データアクセスとストレージのセキュリティを確保してください。
9. 決済処理業者から要求された場合は、[ASV](https://listings.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors) を使用してください。
10. PCI-DSS に関するポリシーを策定・維持し、定期的にリスク評価を実施してください。

PCIコンプライアンスを目指す場合は、まず次のことを行います。

- [安全でPCI準拠のホスティングプロバイダー](https://woocommerce.com/hosting-solutions/)を選択する。
- 強力なパスワードを使用し、管理環境へのアクセスを最小限に抑える。
- サーバーやサイトにクレジットカード情報を保存しない。
- チェックアウトページとアカウントページのトラフィックをSSLで暗号化する。
- プラグイン、テーマ、WordPress、WooCommerceを最新の状態に保つ。
- [ASV](https://listings.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors)を使用して、定期的にサイトをスキャンする。

まだ質問があり、サポートが必要ですか?

- ヘルプデスクからハピネスエンジニアに[お問い合わせ](https://woocommerce.com/my-account/create-a-ticket/)ください。WooCommerce.comで開発または販売されている拡張機能、およびJetpack/WordPress.comをご利用のお客様には、サポートを提供しています。
- お客様でない場合は、[WooCommerceサポートフォーラム](https://wordpress.org/support/plugin/woocommerce/)でサポートを探すか、Wooエージェンシーパートナーにご依頼いただくことをお勧めします。これらのエージェンシーは、高度にカスタマイズされ、拡張性の高いオンラインストアの構築で実績のある信頼できるエージェンシーです。[Wooエージェンシーパートナーの詳細](https://woocommerce.com/development-services/)

