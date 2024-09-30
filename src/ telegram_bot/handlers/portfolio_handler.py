from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(Command("portfolio"))
async def portfolio_command(message: Message, state: FSMContext) -> None:
    user_data = await state.get_data()
    balance = get_user_balance()  # Функция для получения баланса пользователя
    await message.answer(f"Ваш баланс токенов: {balance}.")

# Пример функции для получения баланса пользователя (заглушка)
def get_user_balance():
    return 100  # Пример значения
