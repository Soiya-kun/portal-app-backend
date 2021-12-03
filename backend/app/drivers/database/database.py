from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import DATABASE_URL

# DBとの接続
echo: bool = False  # 実行されたSQLを表示する
ENGINE = create_engine(DATABASE_URL, encoding="utf-8", echo=echo)

# Sessionの作成 ORM実行時の設定：自動コミットするか、自動反映するか
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

# modelで使用する
Base = declarative_base()
