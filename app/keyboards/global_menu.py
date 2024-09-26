from aiogram.utils.keyboard import ReplyKeyboardBuilder


def global_menu_keyboard_builder():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Показати всіх тварин")
    builder.button(text="Показати всіх вилікуваних тварин")
    builder.button(text="Додати нову тварину")
    builder.button(text="Показати всі відгуки")
    builder.button(text="Додати новий відгук")
    builder.adjust(1)
    return builder.as_markup()