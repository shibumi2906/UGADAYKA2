from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("trade"))
async def trade_command(message: Message):
    # Здесь реализуется логика обработки торговых ставок
    await message.answer("Торговля трендами в процессе. Выберите тренд.")
