from core.services.trading_service import distribute_income
from core.services.transaction_service import create_transaction

def test_distribute_income():
    result = distribute_income("trend", 1000)
    assert result == "Income distributed"

def test_create_transaction():
    transaction = create_transaction("user_id", "TOKEN", 50)
    assert transaction.status == "Created"
