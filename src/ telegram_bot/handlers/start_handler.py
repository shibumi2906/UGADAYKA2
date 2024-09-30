from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await state.clear()  # Очистка состояний, если они были
    await message.answer("Добро пожаловать! Введите /portfolio для проверки вашего портфеля.")
