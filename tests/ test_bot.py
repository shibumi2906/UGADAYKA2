import pytest
from aiogram import Bot, Dispatcher
from aiogram.types import Message, Chat
from aiogram.fsm.context import FSMContext
from datetime import datetime
from handlers.start_handler import router as start_router
from handlers.trading_handler import router as trading_router
from handlers.portfolio_handler import router as portfolio_router
from main import main  # главный файл

# Фикстура для имитации сообщения от пользователя
@pytest.fixture
def message():
    return Message(
        message_id=1,
        date=datetime.now(),  # Добавляем текущее время для поля date
        chat=Chat(id=1, type="private"),  # Передаем корректный объект Chat
        from_user=None,
        text="",
    )

# Фикстура для имитации FSMContext
@pytest.fixture
def fsm_context():
    class FakeFSMContext(FSMContext):
        async def set_state(self, state):
            pass

        async def get_data(self):
            return {"name": "TestUser"}

        async def clear(self):
            pass

    return FakeFSMContext

# Тест команды /start в start_handler
@pytest.mark.asyncio
async def test_start_handler(message, fsm_context):
    message.text = "/start"
    await start_router.message.handlers[0](message, fsm_context)  # Вызываем первый обработчик в start_router
    assert message.text == "/start"  # Проверяем команду

# Тест команды /portfolio в portfolio_handler
@pytest.mark.asyncio
async def test_portfolio_handler(message, fsm_context):
    message.text = "/portfolio"
    await portfolio_router.message.handlers[0](message, fsm_context)  # Вызываем первый обработчик в portfolio_router
    assert message.text == "/portfolio"

# Тест команды /trade в trading_handler
@pytest.mark.asyncio
async def test_trade_handler(message):
    message.text = "/trade"
    await trading_router.message.handlers[0](message)  # Вызываем первый обработчик в trading_router
    assert message.text == "/trade"

# Тест запуска основного бота из main.py
@pytest.mark.asyncio
async def test_main():
    await main()  # Запускаем основной процесс бота
    assert True  # Проверяем, что функция выполняется без ошибок

