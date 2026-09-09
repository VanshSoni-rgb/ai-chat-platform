from sqlalchemy.orm import Session
from sqlalchemy import func
from app.domain.entities import ChatHistory


def save_chat(db: Session, conversation_id: str, user_id: str, prompt: str, response: str):
    """Yeni bir sohbet kaydını veritabanına kaydet."""
    chat = ChatHistory(
        conversation_id=conversation_id,
        user_id=user_id,
        prompt=prompt,
        response=response,
    )
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat


def get_conversations(db: Session, user_id: str, limit: int = 20):
    """Kullanıcının konuşma listesini getir."""
    return (
        db.query(
            ChatHistory.conversation_id,
            func.min(ChatHistory.prompt).label("first_prompt"),
            func.count(ChatHistory.id).label("message_count"),
            func.max(ChatHistory.created_at).label("last_active"),
        )
        .filter(ChatHistory.user_id == user_id)
        .group_by(ChatHistory.conversation_id)
        .order_by(func.max(ChatHistory.created_at).desc())
        .limit(limit)
        .all()
    )


def get_conversation_messages(db: Session, conversation_id: str, user_id: str):
    """Belirli bir konuşmanın tüm mesajlarını getir."""
    return (
        db.query(ChatHistory)
        .filter(
            ChatHistory.conversation_id == conversation_id,
            ChatHistory.user_id == user_id,
        )
        .order_by(ChatHistory.created_at.asc())
        .all()
    )


def get_recent_messages(db: Session, conversation_id: str, limit: int = 10):
    """Bir konuşmanın son N mesajını getir (AI hafızası için)."""
    messages = (
        db.query(ChatHistory)
        .filter(ChatHistory.conversation_id == conversation_id)
        .order_by(ChatHistory.created_at.desc())
        .limit(limit)
        .all()
    )
    return list(reversed(messages))


def delete_conversation(db: Session, conversation_id: str, user_id: str):
    """Belirli bir konuşmayı sil."""
    deleted = (
        db.query(ChatHistory)
        .filter(
            ChatHistory.conversation_id == conversation_id,
            ChatHistory.user_id == user_id,
        )
        .delete()
    )
    db.commit()
    return deleted


def delete_all_history(db: Session, user_id: str):
    """Tüm sohbet geçmişini sil."""
    deleted = (
        db.query(ChatHistory)
        .filter(ChatHistory.user_id == user_id)
        .delete()
    )
    db.commit()
    return deleted
