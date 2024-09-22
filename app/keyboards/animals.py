from aiogram.utils.keyboard import InlineKeyboardBuilder


def aniamls_keyboard_builder(animals: list):
    builder = InlineKeyboardBuilder()

    for animal in animals:
        builder.button(text=animal, callback_data=f"animal_{animal}")

    builder.adjust(3)
    return builder.as_markup()

def animal_actions_keyboard(animal: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="Вилікувати тваринку", callback_data=f"animal_cured_{animal}")
    builder.button(text="Видалити тваринку", callback_data=f"animal_delete_{animal}")
    return builder.as_markup()