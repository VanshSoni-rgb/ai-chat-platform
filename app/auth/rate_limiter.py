import time
from fastapi import HTTPException, status
from app.config.settings import RATE_LIMIT_AUTH, RATE_LIMIT_ANON, RATE_LIMIT_WINDOW

# Bellekte istek kayıtları: { "user_id": [timestamp1, timestamp2, ...] }
request_log: dict[str, list[float]] = {}


def apply_rate_limit(user_id: str):
    """
    Kullanıcının istek limitini kontrol eder.
    Limit aşılırsa 429 Too Many Requests hatası fırlatır.
    """
    now = time.time()

    # Kullanıcının limitini belirle
    if user_id == "global_unauthenticated_user":
        max_requests = RATE_LIMIT_ANON
    else:
        max_requests = RATE_LIMIT_AUTH

    # Eski kayıtları temizle (zaman penceresi dışındakileri sil)
    if user_id not in request_log:
        request_log[user_id] = []

    request_log[user_id] = [
        t for t in request_log[user_id]
        if now - t < RATE_LIMIT_WINDOW
    ]

    # Limit kontrolü
    if len(request_log[user_id]) >= max_requests:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Max {max_requests} requests per minute.",
        )

    # İsteği kaydet
    request_log[user_id].append(now)
    print(f"User {user_id}: {len(request_log[user_id])}/{max_requests} requests used.")
