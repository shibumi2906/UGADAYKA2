import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.models import Base, User, Portfolio, Transaction

# Настройка тестовой базы данных SQLite в памяти
@pytest.fixture(scope='module')
def db_session():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_user_model(db_session):
    user = User(username="testuser", email="testuser@example.com", password_hash="hashed_password")
    db_session.add(user)
    db_session.commit()
    retrieved_user = db_session.query(User).filter_by(username="testuser").first()
    assert retrieved_user.username == "testuser"
    assert retrieved_user.email == "testuser@example.com"

def test_portfolio_model(db_session):
    user = User(username="portfolio_user", email="portfolio_user@example.com", password_hash="hashed_password")
    db_session.add(user)
    db_session.commit()

    portfolio = Portfolio(user_id=user.id, token_id="TOKEN", balance=100)
    db_session.add(portfolio)
    db_session.commit()

    retrieved_portfolio = db_session.query(Portfolio).filter_by(user_id=user.id).first()
    assert retrieved_portfolio.balance == 100
    assert retrieved_portfolio.token_id == "TOKEN"

def test_transaction_model(db_session):
    user = User(username="transaction_user", email="transaction_user@example.com", password_hash="hashed_password")
    db_session.add(user)
    db_session.commit()

    transaction = Transaction(user_id=user.id, token_id="TOKEN", amount=200, to_address="test_address", status="completed")
    db_session.add(transaction)
    db_session.commit()

    retrieved_transaction = db_session.query(Transaction).filter_by(user_id=user.id).first()
    assert retrieved_transaction.amount == 200
    assert retrieved_transaction.token_id == "TOKEN"
    assert retrieved_transaction.to_address == "test_address"
    assert retrieved_transaction.status == "completed"

