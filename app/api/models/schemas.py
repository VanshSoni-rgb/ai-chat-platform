from typing import Optional
from datetime import datetime
from pydantic import BaseModel


# --- Request modelleri ---
class ChatRequest(BaseModel):
    prompt: str
    conversation_id: Optional[str] = None


# --- Response modelleri ---
class ChatResponse(BaseModel):
    response: str
    conversation_id: str


class ChatHistoryItem(BaseModel):
    id: int
    conversation_id: str
    user_id: str
    prompt: str
    response: str
    created_at: datetime

    class Config:
        from_attributes = True


class ConversationItem(BaseModel):
    conversation_id: str
    title: str
    message_count: int
    last_active: datetime


class DeleteResponse(BaseModel):
    message: str
    deleted_count: int
