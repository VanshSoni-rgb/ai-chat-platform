from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from app.data.database import Base

class ChatHistory(Base):
    """
    Sohbet geçmişi tablosu.
    Her satır bir kullanıcı-AI mesaj çiftini temsil eder.
    """
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    conversation_id = Column(String, index=True, nullable=False)
    user_id = Column(String, index=True)
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
