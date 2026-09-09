from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.models.schemas import (
    ChatHistoryItem, ConversationItem, DeleteResponse,
)
from app.auth.jwt_handler import get_user_identifier
from app.data.database import get_db
from app.data.dao import chat_dao

router = APIRouter()


@router.get("/conversations", response_model=List[ConversationItem])
async def list_conversations(
    user_id: str = Depends(get_user_identifier),
    db: Session = Depends(get_db),
):
    """Kullanıcının konuşma listesini getirir."""
    convs = chat_dao.get_conversations(db, user_id=user_id)
    return [
        ConversationItem(
            conversation_id=c.conversation_id,
            title=c.first_prompt[:50],
            message_count=c.message_count,
            last_active=c.last_active,
        )
        for c in convs
    ]


@router.get("/conversations/{conversation_id}", response_model=List[ChatHistoryItem])
async def get_conversation(
    conversation_id: str,
    user_id: str = Depends(get_user_identifier),
    db: Session = Depends(get_db),
):
    """Belirli bir konuşmanın tüm mesajlarını getirir."""
    return chat_dao.get_conversation_messages(
        db, conversation_id=conversation_id, user_id=user_id,
    )


@router.delete("/conversations/{conversation_id}", response_model=DeleteResponse)
async def delete_conversation(
    conversation_id: str,
    user_id: str = Depends(get_user_identifier),
    db: Session = Depends(get_db),
):
    """Belirli bir konuşmayı siler."""
    deleted = chat_dao.delete_conversation(
        db, conversation_id=conversation_id, user_id=user_id,
    )
    return DeleteResponse(message="Conversation deleted.", deleted_count=deleted)


@router.delete("/history", response_model=DeleteResponse)
async def delete_all(
    user_id: str = Depends(get_user_identifier),
    db: Session = Depends(get_db),
):
    """Tüm sohbet geçmişini siler."""
    deleted = chat_dao.delete_all_history(db, user_id=user_id)
    return DeleteResponse(message="All history deleted.", deleted_count=deleted)
