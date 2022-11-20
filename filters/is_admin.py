from aiogram.dispatcher.filters import Filter
from aiogram.types import Message

from config import admins

class IsAdmin(Filter): 
    key = "is_admin"

    async def check(self, message: Message):
        return message.from_user.id in admins