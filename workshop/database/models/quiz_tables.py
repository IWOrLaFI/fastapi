from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)


from sqlalchemy.orm import relationship

from workshop.database.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(String)
    phone_number = Column(String, unique=True)
    username = Column(String, unique=True)  # email
    password_hash = Column(String)


class QuizResult(Base):
    __tablename__ = 'QuizResult'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    date = Column(String)
    result = Column(Integer)
    answer_list = Column(String)
    description = Column(String, nullable=True)


class Quiz(Base):
    __tablename__ = 'Quiz'

    id_question = Column(Integer, primary_key=True, unique=True)
    question = Column(String)
    answer = Column(String)
    info = relationship("QuizAnswer", back_populates="text")


class QuizAnswer(Base):
    __tablename__ = 'QuizAnswer'

    id_question = Column(Integer, ForeignKey('quiz.id'), index=True)
    answer_correct = Column(String)
    text = relationship("Quiz", back_populates="info")

