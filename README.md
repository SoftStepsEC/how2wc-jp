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

# pip が使えなかった場合はpip環境を作成し試験環境に移行(.venv)
source .venv/bin/activate

# 依存関係をインストール
pip install -r requirements.txt
```

### Google Cloud Translation API の設定

このプロジェクトは Cloud Translation API (v3) を使用します。サービスアカウント認証を前提としています。
また、用語集（Glossary）機能を使用するため、Google Cloud Storage のバケットも必要になる場合があります（用語集自動作成時）。

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

# 用語集CSV保存用バケット (初回作成時のみ必要)
export GOOGLE_CLOUD_GLOSSARY_BUCKET="your-glossary-bucket-name"
```

`.env` を使う場合は、同じ内容をプロジェクト直下の `.env` に記載できます。

`.env.example` を参考にして作成できます。

### 用語集 (Glossary) について

`glossary.csv` ファイルをプロジェクトルートに配置することで、特定の技術用語やWooCommerce固有の用語の翻訳を統一しています。
初回実行時にこのCSVファイルが自動的にGoogle Cloud上にアップロードされ、用語集リソースが作成されます。

### GitHub Actions のシークレット設定

Actions で自動翻訳を実行する場合、以下のシークレットを設定してください。

- `GCP_SA_KEY`: サービスアカウントJSONの内容（そのまま貼り付け）
- `GOOGLE_CLOUD_PROJECT`: Google Cloud のプロジェクトID
- `GOOGLE_CLOUD_LOCATION`: 任意（未設定なら `global` を使用）
- `GOOGLE_CLOUD_GLOSSARY_BUCKET`: 用語集用バケット名

## 使用方法

### 手動実行

完全なワークフロー（スクレイピング + 翻訳）を実行:

```bash
python main.py
```

### 翻訳ツールの詳細オプション

`translator.py` は個別のファイルやディレクトリ単位での実行、およびコスト見積もりが可能です。

#### 全体を翻訳
```bash
python translator.py
```

#### 特定のファイルのみ翻訳
```bash
python translator.py --file docs/en/getting-started.md
```

#### 特定のディレクトリ以下を翻訳
```bash
python translator.py --dir docs/en/products
```

#### 翻訳コストの見積もり (Dry Run)
実際にAPIを呼び出さず、翻訳対象の文字数と推定コストを表示します。

```bash
# 全体の見積もり
python translator.py --estimate-cost

# 特定ディレクトリの見積もり
python translator.py --dir docs/en/products --estimate-cost
```

スクリプトを個別に実行:

```bash
# ドキュメントのスクレイピングのみ

python scraper.py

# 翻訳のみ
python translator.py

# 更新チェックのみ
python update_checker.py
```

### テスト用スクレイピング

特定のページのみをスクレイピングしてテストする:

```bash
# 特定のページを1ページのみスクレイピング
python scraper.py --url "https://woocommerce.com/documentation/woocommerce/getting-started/" --max-pages 1

# 特定のカテゴリから最大10ページをスクレイピング
python scraper.py --url "https://woocommerce.com/documentation/woocommerce/products/" --max-pages 10

# 全ページをスクレイピング（デフォルト）
python scraper.py
```

**オプション:**
- `--url`: スクレイピング開始URL（省略時は全ドキュメント）
- `--max-pages`: スクレイピングするページ数の上限（テスト用）

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
