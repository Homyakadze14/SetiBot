from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from filters.is_admin import IsAdmin

from keyboards.main_keyboard import main_kb

async def start_command(message: types.Message):
    await message.answer("Привет, бот создан для упрощения решений задач по сетям!", reply_markup=main_kb)

async def cancel_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Отмена действия", reply_markup=main_kb)

async def admin_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Вы являетесь админом!")

def register_handlers_common(dp:Dispatcher):
    dp.register_message_handler(start_command, commands = ['start'], state="*")
    dp.register_message_handler(cancel_command, commands = ['cancel'], state="*")
    dp.register_message_handler(cancel_command, Text(equals="отмена", ignore_case=True), state="*")
    dp.register_message_handler(admin_command, IsAdmin(), commands = ['admin'], state="*")