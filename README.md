# portar\l-app-backend

## 開発環境構築

まずは`app/core/.env.example`の内容を参考に、環境変数を設定する。

```shell
# Docker Imageのビルド
make build
# コンテナ&サーバー起動
make dev
```

## DBのmigration

```shell
docker-compose -f docker-compose-dev.yml exec fastapi bash
# in /backend
# マイグレーションファイルの自動作成
alembic revision --autogenerate -m "migration comment"

# マイグレーションの実行。headで最新の状態まで移行。
alembic upgrade head
```

## 開発用の初期データの投入

```shell
docker-compose -f docker-compose-dev.yml exec fastapi bash
# in /backend
PYTHONPATH=/backend/ python app/load_data.py
```

## 文法チェックとテスト

```shell
# コンテナに入って
$ docker-compose -f docker-compose.yml exec fastapi bash
# コーディング規約のチェック
$ flake8 app
# 型チェック
$ mypy app
# コードフォーマットの修正
$ black app
# 全部チェック
$ black app && flake8 app && mypy app
# テスト実行
$ coverage run -m pytest -v -s app
```
