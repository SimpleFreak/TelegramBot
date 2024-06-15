from serialization.serialization_images import get_user_data

from aiogram.types import InputFile, MediaGroup, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from image_processing.processing import Processing

import os

from handlers import dispatcher


@dispatcher.callback_query_handler(lambda query: query.data == "phrases_and_memes")
async def sending_photos_phrases_and_memes(query: CallbackQuery):
    photo_1 = InputFile(
        path_or_bytesio="./media/themes/phrases_and_memes/image_1.png")
    photo_2 = InputFile(
        path_or_bytesio="./media/themes/phrases_and_memes/image_2.png")
    photo_3 = InputFile(
        path_or_bytesio="./media/themes/phrases_and_memes/image_3.png")

    album = MediaGroup()

    album.attach_photo(photo=photo_1)
    album.attach_photo(photo=photo_2)
    album.attach_photo(photo=photo_3)

    await query.message.answer_media_group(media=album)

    # Сериализация данных пользователя
    get_user_data(fullname=f"{query.from_user.full_name}_1",
                  theme=query.data, photo="./media/themes/phrases_and_memes/image_1.png")

    get_user_data(fullname=f"{query.from_user.full_name}_2",
                  theme=query.data, photo="./media/themes/phrases_and_memes/image_2.png")

    get_user_data(fullname=f"{query.from_user.full_name}_3",
                  theme=query.data, photo="./media/themes/phrases_and_memes/image_3.png")

    keyboard = InlineKeyboardMarkup(row_width=3)

    button_view_stickers = InlineKeyboardButton(text="Посмотреть стикеры",
                                                callback_data="phrases_and_memes_view_stickers")
    button_emotions_and_expressions = InlineKeyboardButton(text="Эмоции и выражения",
                                                           callback_data="emotions_and_expressions")
    button_phrases_and_memes = InlineKeyboardButton(text="Фразы и мемы",
                                                    callback_data="phrases_and_memes")

    keyboard.add(button_view_stickers)
    keyboard.add(button_emotions_and_expressions)
    keyboard.add(button_phrases_and_memes)

    await query.message.answer("Выберите тему для стикерпака", reply_markup=keyboard)


@dispatcher.callback_query_handler(lambda query: query.data == "phrases_and_memes_view_stickers")
async def view_stickers(query: CallbackQuery):
    username = query.from_user.full_name
    directory = f"./media/users_photo_id/{username}"

    file_list = os.listdir(directory)
    for file in file_list:
        photo = file

    # Создание стикерпака
    processing = Processing()
    processing.save_swap_faces(f"{directory}/{photo}",
                               "./media/themes/phrases_and_memes/image_1.png",
                               "phrases_and_memes", "image_1.png")
    processing.save_swap_faces(f"{directory}/{photo}",
                               "./media/themes/phrases_and_memes/image_2.png",
                               "phrases_and_memes", "image_2.png")
    processing.save_swap_faces(f"{directory}/{photo}",
                               "./media/themes/phrases_and_memes/image_3.png",
                               "phrases_and_memes", "image_3.png")

    # Сериализация данных пользователя
    get_user_data(fullname=f"{query.from_user.full_name}_1",
                  theme=query.data,
                  photo=f".\\media\\save_users_stickers\\phrases_and_memes\\image_1.png")

    get_user_data(fullname=f"{query.from_user.full_name}_2",
                  theme=query.data,
                  photo=f".\\media\\save_users_stickers\\phrases_and_memes\\image_2.png")

    get_user_data(fullname=f"{query.from_user.full_name}_3",
                  theme=query.data,
                  photo=f".\\media\\save_users_stickers\\phrases_and_memes\\image_3.png")

    await query.message.answer("Ваш стикерпак:")

    sticker_1 = InputFile(
        path_or_bytesio="./media/save_users_stickers/phrases_and_memes/image_1.png")
    sticker_2 = InputFile(
        path_or_bytesio="./media/save_users_stickers/phrases_and_memes/image_2.png")
    sticker_3 = InputFile(
        path_or_bytesio="./media/save_users_stickers/phrases_and_memes/image_3.png")

    sticker_album = MediaGroup()
    sticker_album.attach_photo(photo=sticker_1)
    sticker_album.attach_photo(photo=sticker_2)
    sticker_album.attach_photo(photo=sticker_3)

    await query.message.answer_media_group(media=sticker_album)

    keyboard = InlineKeyboardMarkup(row_width=2)

    button_emotions_and_expressions = InlineKeyboardButton(text="Эмоции и выражения",
                                                           callback_data="emotions_and_expressions")
    button_phrases_and_memes = InlineKeyboardButton(text="Фразы и мемы",
                                                    callback_data="phrases_and_memes")

    keyboard.add(button_emotions_and_expressions)
    keyboard.add(button_phrases_and_memes)

    await query.message.answer("Выберите тему для стикерпака", reply_markup=keyboard)
