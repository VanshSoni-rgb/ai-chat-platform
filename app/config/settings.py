import os

# --- Uygulama Ayarları ---
# Tüm konfigürasyon değerleri tek bir yerde toplanır.

# PostgreSQL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:5353@localhost:5432/fastapi_chat"
)

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
AI_MODEL = "gpt-4o-mini"

# JWT
JWT_SECRET_KEY = "a-string-secret-at-least-256-bits-long"
JWT_ALGORITHM = "HS256"

# Rate Limiting
RATE_LIMIT_AUTH = 5       # Kimliği doğrulanmış kullanıcı: 5 istek/dk
RATE_LIMIT_ANON = 3       # Anonim kullanıcı: 3 istek/dk
RATE_LIMIT_WINDOW = 60    # Zaman penceresi (saniye)
