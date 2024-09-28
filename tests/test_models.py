from core.models import User, Portfolio

def test_user_model():
    user = User(username="testuser")
    assert user.username == "testuser"

def test_portfolio_model():
    portfolio = Portfolio(user_id=1, token="TOKEN", balance=100)
    assert portfolio.balance == 100
