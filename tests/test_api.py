import pytest
from core.API.ton_api import TonAPI
from core.API.exchange_api import ExchangeAPI
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


# Тестируем функцию отправки транзакции в TON API
def test_send_transaction():
    ton_api = TonAPI("wallet_address", "private_key")
    result = ton_api.send_transaction("to_address", 100, "test message")
    assert result is not None  # Проверяем, что транзакция успешно отправлена

# Тестируем функцию получения цены токена в Exchange API
def test_get_token_price():
    rate = ExchangeAPI.get_token_price("bitcoin")
    assert rate > 0  # Проверяем, что цена больше 0

# Тестируем функцию получения рыночных трендов в Exchange API
def test_get_market_trends():
    trends = ExchangeAPI.get_market_trends()
    assert trends is not None  # Проверяем, что тренды возвращены
    assert len(trends) > 0  # Проверяем, что список трендов не пуст

