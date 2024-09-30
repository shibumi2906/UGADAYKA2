import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import TELEGRAM_API_TOKEN
from handlers import start_handler, trading_handler, portfolio_handler

async def main():
    # Инициализация бота и диспетчера с использованием памяти для хранения состояний
    bot = Bot(token=TELEGRAM_API_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Подключаем обработчики команд
    dp.include_router(start_handler.router)
    dp.include_router(trading_handler.router)
    dp.include_router(portfolio_handler.router)

    # Запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
