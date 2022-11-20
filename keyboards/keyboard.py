from aiogram.types import ReplyKeyboardMarkup


class Keyboard():
    def __init__(self, buttons, resize_keyboard=True, row_width=2, one_time_keyboard=True):
        self.buttons = buttons
        self.resize_keyboard = resize_keyboard
        self.row_width = row_width
        self.one_time_keyboard = one_time_keyboard

    def get_keyboard(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=self.resize_keyboard, 
                                        row_width=self.row_width, 
                                        one_time_keyboard=self.one_time_keyboard)
        keyboard.add(*self.buttons)
        
        return keyboard