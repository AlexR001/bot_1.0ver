#Подключение библиотек
import telebot
from telebot import types
from config import token

# Инициализация бота с использованием его токена
bot = telebot.TeleBot(token)
#Обработка команды '/help'
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, f'''/start - Пишет привет и своё название,
/help - выводит все команды,
/hello - /start,
/graz - рассказывает про проблему мусора.''')




# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    with open(f'img/musor/ava_ver1.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f, caption='''
Привет! Я бот расскажу о проблеме загрязнения если стало интересно просто нажми.
/graz''', reply_markup=markup)

          

# Обработчик команды '/graz'
@bot.message_handler(commands=['graz'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/dengi")
    btn2 = types.KeyboardButton("/vreme")
    btn3 = types.KeyboardButton("/problema")
    markup.add(btn1, btn2, btn3)
    with open(f'img/musor/problema.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f, caption='''
Я могу рассказать сколько денег можно получить от сдачи мусора просто нажми.
/dengi
А ещё могу рассказать о времени разложении мусора просто нажми.
/vreme
А могу рассказать о самой проблеме если ты не знаешь просто нажми.
/problema      
''')

@bot.message_handler(commands=['problema'])
def send_welcome(message):
    with open(f'img/musor/musor.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f, caption=f'''
В чем заключается проблема загрязнения окружающей среды?
                       
Загрязнение окружающей среды, под которой понимаются также природная среда и биосфера
— это повышенное содержание в ней физических, химических или биологических реагентов,
                       
не характерных для данной среды, занесенных извне,
наличие которых приводит к негативным последствиям.
''')

# Обработчик команды '/dengi'
@bot.message_handler(commands=['dengi'])
def send_problem_dengi(message):
    with open(f'img/musor/dengi.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f, caption='''
За выброс этих веществ и материалов можно получить:
Медь до 820руб.
Латунь до 635руб.
Бронза до 600руб.
Алюминий от 148руб.
Картон – от 4 руб.
Бумага – от 11 руб.
Бутылки -  10 руб.
(за килограмм)
''')

    
# Обработчик команды '/vreme'
@bot.message_handler(commands=['vreme'])
def send_problem_vreme(message):
    with open(f'img/musor/vreme.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f, caption='''
Растворятся в природе будут:
Пластик - около 500 лет
Стекло - 1000 лет и более
Бумага - 2-5 месяцев
Алюминиевая банка — более 500 лет
''')
    
# Запуск бота
bot.polling()
