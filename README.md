# WooCommerce Documentation (Japanese Translation)

WooCommerceの公式ドキュメントを日本語に翻訳するプロジェクトです。

## 概要

このプロジェクトは、[WooCommerce公式ドキュメント](https://woocommerce.com/documentation/woocommerce/)を自動的にスクレイピングし、日本語に翻訳します。

## 機能

- **自動スクレイピング**: WooCommerce公式ドキュメントから階層構造を保持してコンテンツを取得
- **階層的保存**: ページの階層構造をディレクトリ構造として保存
- **自動翻訳**: Google Cloud Translation APIを使用して英語から日本語へ自動翻訳
- **週次更新**: GitHub Actionsで毎週自動的に更新をチェック
- **自動PR作成**: 更新があった場合、自動的にプルリクエストを作成

## ディレクトリ構造

```
how2wc-jp/
├── docs/
│   ├── en/          # 英語ドキュメント（オリジナル）
│   └── ja/          # 日本語ドキュメント（翻訳済み）
├── .github/
│   └── workflows/
│       └── update-docs.yml  # 自動更新ワークフロー
├── scraper.py       # ドキュメントスクレイパー
├── translator.py    # ドキュメント翻訳
├── update_checker.py # 更新チェッカー
├── main.py          # メインワークフロー
└── requirements.txt # Python依存関係
```

## セットアップ

### 必要要件

- Python 3.11以上
- pip

### インストール

```bash
# リポジトリをクローン
git clone https://github.com/SoftStepsEC/how2wc-jp.git
cd how2wc-jp

# 依存関係をインストール
pip install -r requirements.txt
```

### Google Cloud Translation API の設定

このプロジェクトは Cloud Translation API (v3) を使用します。サービスアカウント認証を前提としています。

1. Google Cloud プロジェクトを作成
2. Cloud Translation API を有効化
3. サービスアカウントを作成し、JSONキーをダウンロード
4. 環境変数を設定

```bash
# サービスアカウントキーのパス
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"

# Google Cloud プロジェクトID
export GOOGLE_CLOUD_PROJECT="your-gcp-project-id"

# 任意: 既定は global
export GOOGLE_CLOUD_LOCATION="global"
```

`.env` を使う場合は、同じ内容をプロジェクト直下の `.env` に記載できます。

`.env.example` を参考にして作成できます。

### GitHub Actions のシークレット設定

Actions で自動翻訳を実行する場合、以下のシークレットを設定してください。

- `GCP_SA_KEY`: サービスアカウントJSONの内容（そのまま貼り付け）
- `GOOGLE_CLOUD_PROJECT`: Google Cloud のプロジェクトID
- `GOOGLE_CLOUD_LOCATION`: 任意（未設定なら `global` を使用）

## 使用方法

### 手動実行

完全なワークフロー（スクレイピング + 翻訳）を実行:

```bash
python main.py
```

個別にスクリプトを実行:

```bash
# ドキュメントのスクレイピングのみ
python scraper.py

# 翻訳のみ
python translator.py

# 更新チェックのみ
python update_checker.py
```

### 自動更新

GitHub Actionsが毎週月曜日午前9時（UTC）に自動的に実行され、以下を行います：

1. WooCommerceドキュメントの更新をチェック
2. 新規・更新されたページをスクレイピング
3. 日本語に翻訳
4. 変更があればプルリクエストを作成

手動でワークフローをトリガーすることもできます：
- GitHubリポジトリの「Actions」タブ
- 「Update WooCommerce Documentation」ワークフローを選択
- 「Run workflow」をクリック

## スクリプトの説明

### scraper.py

WooCommerce公式ドキュメントをスクレイピングし、Markdown形式で保存します。

- 階層構造を保持
- ページタイトル、内容、URLを抽出
- メタデータをJSON形式で保存

### translator.py

英語のMarkdownファイルを日本語に翻訳します。

- Google Cloud Translation APIを使用
- Markdown構造を保持
- コードブロック、リンク、画像は翻訳せずに保持
- フロントマターのタイトルも翻訳

### update_checker.py

ドキュメントの更新をチェックします。

- 前回のメタデータと比較
- 新規、更新、削除されたページを検出
- ファイルハッシュで変更を検出

### main.py

完全なワークフローを実行するメインスクリプト。

## ライセンス

MIT License - 詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 貢献

プルリクエストや問題報告を歓迎します。

## 注意事項

- このプロジェクトは個人的な翻訳プロジェクトです
- 機械翻訳のため、翻訳の正確性は保証されません
- 公式の日本語ドキュメントは[WooCommerce公式サイト](https://woocommerce.com/)をご確認ください
