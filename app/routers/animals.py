from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from app.data import files_actions
from app.keyboards.animals import aniamls_keyboard_builder, animal_actions_keyboard


animals_router = Router()

@animals_router.message(F.text == "Показати всіх тварин")
async def show_animals(message: Message, state: FSMContext):
    animals = files_actions.open_file()
    keyboard = aniamls_keyboard_builder(animals)
    return message.answer(
        text = "Виберіть тваринку",
        reply_markup=keyboard
    )


@animals_router.callback_query(F.data.startswith("animal_"))
async def animal_action(callback: CallbackQuery, state: FSMContext):
    animal = callback.data.split("_")[-1]
    keyboard = animal_actions_keyboard(animal)
    return callback.message.answer(
        text=animal, 
        keyboard=keyboard
        )
