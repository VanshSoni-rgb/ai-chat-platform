from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config.settings import DATABASE_URL

# Veritabanı motoru
engine = create_engine(DATABASE_URL)

# Session fabrikası — her istek için yeni bir oturum üretir
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Tüm modellerin atası
Base = declarative_base()


def get_db():
    """
    Her API isteğinde yeni bir veritabanı oturumu açar,
    istek bitince otomatik kapatır. (Depends ile kullanılır)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
