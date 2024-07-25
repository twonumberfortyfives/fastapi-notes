from sqlalchemy import Integer, Column, String, Boolean

from database import Base


class Note(Base):
    __tablename__ = "note"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(255), nullable=False, unique=True)
    completed = Column(Boolean, nullable=False, default=False)
