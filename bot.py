from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. Portuguese
import telebot


owm = OWM('f7d0dfd6f0b379a1d05dbbe858b4d13e', config_dict)
mgr = owm.weather_manager()
bot = telebot.TeleBot("1727235164:AAFz5vjDoVo6lYZhx0B0owxBT5zKBUCyFIc")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = mgr.weather_at_place('Россия,Уфа')
	w = observation.weather
	b = w.detailed_status 
	t = w.temperature('celsius')["temp"]

	answer = "В Уфе сейчас " + b + "\n"
	answer += "Температура " + str(t) + "\n\n"

	if t < 10:
		answer += "Эльвирочка, одевайся, пожалуйста теплее!" 
	elif t < 20:
		answer += "Эльвирочка, погода налаживается!"
	else:
		answer += "Эльвирочка, температура норм, одевай что угодно."

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True)