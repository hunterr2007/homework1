import logging, ephem
 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date
 
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)
 
 
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}
 
 
def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)
 
def get_constel(bot, update):
    # planets = {"Mercury": ephem.Mercury("2019/09/12"), 
    # "Venus": ephem.Venus("2019/09/12"), 
    # "Mars" : ephem.Mars("2019/09/12"), 
    # "Jupiter": ephem.Jupiter("2019/09/12"), 
    # "Saturn": ephem.Saturn("2019/09/12"), 
    # "Uranus": ephem.Uranus("2019/09/12"), 
    # "Neptune": ephem.Neptune("2019/09/12")}
 
    planet_input = str(update.message.text.split()[1]).lower().capitalize()  
 
    # if planet_input in planets:
    #     print(ephem.constellation(planets[planet_input]))
 
    day = date.today().split("-")
    print(day)
 
    # today = f"{day[0]}/{day[1]}/{day[2]}"
    # print("Today's date:", today)
    print(planet_input)
    # update.message.reply_text("Today's date:", today)
    update.message.reply_text(planet_input)
 
def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 
API_KEY = "1470382150:AAGPizAlIEPu0etPm1-VJ7xSNlUaTpTaAKE"
#with open("token.txt") as f:
    #API_KEY = f.read().strip()
 
def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constel))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       
 
if __name__ == "__main__":
    main()