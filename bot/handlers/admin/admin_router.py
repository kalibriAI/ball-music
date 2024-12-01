from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, FSInputFile

from services.make_exel import make_excel

admin_router = Router(name='admin_router')
ADMIN_IDS = [1889892706, 7292402850]


@admin_router.message(Command('excel'))
async def get_songs(message: Message):
    if message.from_user.id in ADMIN_IDS:
        excel = FSInputFile("songs.xlsx", filename='musics.xlsx')
        make_excel(message.from_user.id)
        await message.answer_document(document=excel)
    else:
        await message.answer('Нет прав.')
