from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

start_router = Router()

@start_router.message(CommandStart())
def start_heandler(message: Message, state: FSMContext):
    return message.answer(text=f"Вітаю у ветеринарній клініці '{message.from_user.full_name}'")