from aiogram import types
from keyboards.default.cats import cats_keyboard
from loader import dp



@dp.message_handler(text="🛍 Buyurtma berish")
async def bot_echo(message: types.Message):
    await message.answer("Nimadan boshlaymiz", reply_markup=cats_keyboard)
