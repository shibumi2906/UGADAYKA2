from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)

    # Связь с портфелем
    portfolios = relationship("Portfolio", back_populates="user")

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"


class Portfolio(Base):
    __tablename__ = 'portfolios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    token_id = Column(String, nullable=False)  # ID токена
    balance = Column(Float, nullable=False, default=0.0)

    # Связь с пользователем
    user = relationship("User", back_populates="portfolios")

    def __repr__(self):
        return f"<Portfolio(user_id={self.user_id}, token_id={self.token_id}, balance={self.balance})>"


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    token_id = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    to_address = Column(String, nullable=False)
    status = Column(String, nullable=False, default="pending")

    # Связь с пользователем
    user = relationship("User")

    def __repr__(self):
        return f"<Transaction(user_id={self.user_id}, token_id={self.token_id}, amount={self.amount}, status={self.status})>"
