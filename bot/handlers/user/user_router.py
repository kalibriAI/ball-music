from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.services.add import save_to_json

user_router = Router(name='user_router')


@user_router.message(Command('start'))
async def start_cmd(message: Message):
    await message.answer('🎶<b>Для того чтобы предложить песню просто отправьте боту название песни, и автора со следующей строки.</b>')


@user_router.message(Command('id'))
async def get_id_cmd(message: Message):
    await message.answer(f'ID: <code>{message.from_user.id}</code>')


@user_router.message()
async def song_handler(message: Message):
    if '\n' in message.text and len(message.text.split('\n')) == 2:
        name, author = message.text.split('\n')
        if len(name) <= 30 and len(author) <= 30:
            save_to_json({'name': name, 'author': author})
            await message.answer('<b>Песня успешно сохранена!</b>✅')
        else:
            await message.answer('Название песни или имя автора не может содержать более 30 символов.')
    else:
        await message.answer("Вводить нужно строго по правилам: в первой строке название песни, имя автора во второй")

