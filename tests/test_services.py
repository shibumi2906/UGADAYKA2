import pytest
from core.services.portfolio_service import PortfolioService
from core.services.trading_service import TradingService
from core.services.transaction_service import TransactionService
from core.API.exchange_api import ExchangeAPI
from core.API.ton_api import TonAPI

# Моки для API
class MockExchangeAPI:
    def get_token_price(self, token_id):
        return 100  # Возвращаем фиксированную цену для тестов

class MockTonAPI:
    def send_transaction(self, to_address, amount):
        return {"id": "tx123", "status": "pending"}  # Возвращаем фиктивную транзакцию

    def get_transaction_status(self, transaction_id):
        return "completed"  # Возвращаем фиктивный статус транзакции


@pytest.fixture
def portfolio_service():
    return PortfolioService()

@pytest.fixture
def trading_service(portfolio_service):
    exchange_api = MockExchangeAPI()
    return TradingService(exchange_api, portfolio_service)

@pytest.fixture
def transaction_service():
    ton_api = MockTonAPI()
    return TransactionService(ton_api)

def test_portfolio_service(portfolio_service):
    # Тест получения и обновления баланса
    user_id = 1
    token_id = "TOKEN"
    portfolio_service.update_balance(user_id, token_id, 100)
    assert portfolio_service.get_balance(user_id, token_id) == 100

    portfolio_service.update_balance(user_id, token_id, -50)
    assert portfolio_service.get_balance(user_id, token_id) == 50

def test_trading_service(trading_service, portfolio_service):
    # Тест размещения ставки
    user_id = 1
    token_id = "TOKEN"
    portfolio_service.update_balance(user_id, token_id, 200)

    bet = trading_service.place_bet(user_id, token_id, 100, "up")
    assert bet["amount"] == 100
    assert bet["trend"] == "up"
    assert bet["initial_price"] == 100

    # Тест расчета прибыли
    profit = trading_service.calculate_profit(user_id, bet)
    assert profit == 0  # В этом тесте текущая цена равна начальной

def test_transaction_service(transaction_service):
    # Тест создания транзакции
    user_id = 1
    token_id = "TOKEN"
    transaction = transaction_service.create_transaction(user_id, "recipient_address", token_id, 100)
    assert transaction["status"] == "pending"
    assert transaction["transaction_id"] == "tx123"

    # Тест проверки статуса транзакции
    status = transaction_service.check_transaction_status("tx123")
    assert status == "completed"

