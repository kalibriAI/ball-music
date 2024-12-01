from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.add import save_to_json

user_router = Router(name='user_router')


@user_router.message(Command('start'))
async def start_cmd(message: Message):
    await message.answer('🎶<b>Для того чтобы предложить песню просто отправьте боту название песни и автора через тире.\n\nПример: I Need A Dollar - Aloe Blacc</b>')


@user_router.message(Command('id'))
async def get_id_cmd(message: Message):
    await message.answer(f'ID: <code>{message.from_user.id}</code>')


@user_router.message()
async def song_handler(message: Message):
    if '-' in message.text:
        if len(message.text.split('-')) == 2:
            name, author = message.text.split('-')
            name, author = name.strip(), author.strip()
            if 0 < len(name) <= 30 and 0 < len(author) <= 30:
                save_to_json({'user': message.from_user.first_name, 'name': name, 'author': author})
                await message.answer('<b>Спасибо за вашу активность.\nС уважением команда SLEO</b>')
            else:
                await message.answer('Название песни или имя автора не может быть пустым или содержать более 30 символов.')
        else:
            await message.answer("Вводить нужно строго по шаблону: <название песни> - <автор>", parse_mode=None)
    else:
        await message.answer("Вводить нужно строго по шаблону: <название песни> - <автор>", parse_mode=None)
