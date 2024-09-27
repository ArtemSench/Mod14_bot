from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_buy = InlineKeyboardMarkup(resize_keyboard=True)
prod1_ib = InlineKeyboardButton('Банка', callback_data='product_buying')
prod2_ib = InlineKeyboardButton('Бутылка', callback_data='product_buying')
prod3_ib = InlineKeyboardButton('Зупырёк', callback_data='product_buying')
prod4_ib = InlineKeyboardButton('"Колёса"', callback_data='product_buying')
back_ib = InlineKeyboardButton('ничЁ не нравится, хочу назад', callback_data='back')
ikb_buy.row(prod1_ib, prod2_ib, prod3_ib, prod4_ib)
ikb_buy.add(back_ib)

ikb = InlineKeyboardMarkup(resize_keyboard=True)
calc_ib = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
formula_ib = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')

ikb.row(calc_ib, formula_ib)


kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_button = KeyboardButton(text="Информация")
calc_button = KeyboardButton(text='Рассчитать')
buy_button = KeyboardButton(text='Купить')

kb.row(start_button, calc_button)
kb.add(buy_button)