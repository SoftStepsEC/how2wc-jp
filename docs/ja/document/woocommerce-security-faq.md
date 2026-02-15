---
title: WooCommerce サイトとデータセキュリティに関する FAQ
url: https://woocommerce.com/document/woocommerce-security-faq/
---

- 顧客が注文した商品と注文日時
- 顧客が提供した氏名、メールアドレス、電話番号
- 顧客が入力した請求先住所（およびオプションで配送先住所）
- 顧客が使用した支払い方法に関するメモ

- [BACS](https://woocommerce.com/document/bacs/) などの手動決済ゲートウェイは、顧客情報を収集し、お客様に詳細情報を提供して支払いを送金できるようにします。
- 自動決済ゲートウェイは、顧客から情報を安全に要求し、それをサードパーティの決済処理サービス（クレジットカード決済代行会社や PayPal など）に中継するアプリケーションです。

- 顧客の請求情報を確認する
- 資金が利用可能かどうかを確認する
- 顧客から資金を送金する
- 支払い確認をWooCommerceサイトに送信する

- 不正と思われる取引はすべて返金してください。
- [WooCommerce Anti-Fraud](https://href.li/?https://woocommerce.com/products/woocommerce-anti-fraud/?aff=10486&cid=1131038) などの不正防止ソフトウェアをサイトに追加することを検討してください。
- チェックアウトに reCaptcha ソフトウェアを追加することを検討してください。[reCaptcha for WooCommerce](https://href.li/?https://woocommerce.com/products/recaptcha-for-woocommerce/?aff=10486&cid=1131038)
- こうしたテストの影響を受けやすい特定の商品（例えば、「寄付」や「価格指定」商品など）があるかどうかを判断します。
- サイト上での[ゲストチェックアウト](https://woocommerce.com/document/configuring-woocommerce-settings/accounts-and-privacy/#guest-checkout-and-accounts)の防止を検討します。
- 決済プロバイダと連携し、アカウントのセキュリティを強化します。例えば、導入されている不正防止対策を更新または見直します。

