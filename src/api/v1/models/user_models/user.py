import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, String, Boolean, ForeignKey, Integer, text, JSON

from service_layer.database import Base
from sqlalchemy.orm import relationship

class Organisation(Base):
    __tablename__ = "organisations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    workflow = Column(JSON)
    questions = relationship("Question", back_populates="organisation")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    organisation_id = Column(Integer, ForeignKey("organisations.id"))
    question = Column(String)
    response_type = Column(String)
    question_type = Column(String)
    options = Column(JSON, nullable=True)
    organisation = relationship("Organisation", back_populates="questions")
