from aiogram.utils.keyboard import ReplyKeyboardBuilder


def global_menu_keyboard_builder():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Показати всіх тварин")
    builder.button(text="Додати нову тварину")
    builder.button(text="Вилікувати тваринку")
    builder.button(text="Видалити тваринку")
    builder.adjust(1)
    return builder.as_markup()