from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from filters.is_admin import IsAdmin
from keyboards.main_keyboard import main_kb
from keyboards.base_keyboard import base_kb, buttons
from src.DecriptingASCII import get_descipted_binary_code, is_hex, is_bin


class Decription(StatesGroup):
    base = State()
    numState = State()

async def decryption(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Выберите в какой системе счисления находиться число:", reply_markup=base_kb)
    await Decription.base.set()

async def choose_base(message: types.Message, state: FSMContext):
    if(message.text not in buttons):
        await message.answer("Неверная СС! Выберите заново:", reply_markup=base_kb)
        return

    await state.update_data(base = int(message.text))
    await message.answer(f"Введите число в этой СС")
    await Decription.numState.set()

async def number(message: types.Message, state: FSMContext):
    data = await state.get_data()

    main_num = ''
    for letter in message.text: 
        if(letter != ' '):
            main_num+=letter

    if ((not main_num.isdigit() or not is_bin(main_num)) and data['base'] == 2): 
        await message.answer("Это не двоичное число! Введите снова!")
        return
    
    if(not is_hex(main_num) and data['base'] == 16):
        await message.answer("Это не шестнадцетеричное число! Введите снова!")
        return

    word = get_descipted_binary_code(main_num, data['base'])
    await message.answer(f"Слово:\n{word}", reply_markup=main_kb)
    await state.finish()

def register_handlers_decryption(dp:Dispatcher):
    dp.register_message_handler(decryption, Text(equals="расшифровка ASCII", ignore_case=True), state="*")
    dp.register_message_handler(number, state=Decription.numState)
    dp.register_message_handler(choose_base, state=Decription.base)