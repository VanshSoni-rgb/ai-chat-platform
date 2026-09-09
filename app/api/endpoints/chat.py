from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.models.schemas import ChatRequest, ChatResponse
from app.auth.jwt_handler import get_user_identifier
from app.auth.rate_limiter import apply_rate_limit
from app.data.database import get_db
from app.service import chat_service

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    user_id: str = Depends(get_user_identifier),
    db: Session = Depends(get_db),
):
    """AI ile sohbet et. Mesaj geçmişi otomatik olarak hatırlanır."""
    apply_rate_limit(user_id)
    result = chat_service.send_message(
        db, user_id=user_id,
        prompt=request.prompt,
        conversation_id=request.conversation_id,
    )
    return ChatResponse(**result)
