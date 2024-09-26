from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from app.data import files_actions, list_files
from app.keyboards.animals import aniamls_keyboard_builder, animal_actions_keyboard
from app.forms.animals import AnimalForm


animals_router = Router()

@animals_router.message(F.text == "Показати всіх тварин")
async def show_animals(message: Message, state: FSMContext):
    animals = files_actions.open_file()
    keyboard = aniamls_keyboard_builder(animals)
    await message.answer(
        text = "Виберіть тваринку",
        reply_markup=keyboard
    )


@animals_router.callback_query(F.data.startswith("animal_"))
async def animal_action(callback: CallbackQuery, state: FSMContext):
    animal = callback.data.split("_")[-1]
    keyboard = animal_actions_keyboard(animal)
    await callback.message.answer(
        text=animal, 
        reply_markup=keyboard
        )



@animals_router.callback_query(F.data.startswith("cured_animal_"))
async def animal_cured(callback: CallbackQuery, state: FSMContext):
    animal = callback.data.split("_")[-1]
    msg = files_actions.animal_cured(animal)
    await callback.message.answer(text=msg)


@animals_router.callback_query(F.data.startswith("delete_animal_"))
async def del_animal(callback: CallbackQuery, state: FSMContext):
    animal = callback.data.split("_")[-1]
    msg = files_actions.del_animal(animal)
    await callback.message.answer(text=msg)


@animals_router.message(F.text == "Додати нову тварину")
async def add_animal(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(AnimalForm.name)
    await message.answer(text="Введіть ім'я тваринки:")


@animals_router.message(AnimalForm.name)
async def save_new_animal(message: Message, state: FSMContext):
    data = await state.update_data(name=message.text)
    await state.clear()
    msg = files_actions.add_animal(data.get("name"))
    await message.answer(text=msg)


@animals_router.message(F.text == "Показати всіх вилікуваних тварин")
async def show_cured_animas(message: Message, state: FSMContext):
    animal_cured= files_actions.open_file(list_files.ANIMALS_CURED)

    msg = ""
    for i, animal in enumerate(animal_cured, start=1):
        msg += f"{i}. {animal}\n"

    await message.answer(text=msg)