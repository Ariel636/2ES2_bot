import telebot
import time
import telegram
from telegram import ParseMode
bot = telebot.TeleBot('1787503746:AAGhA54zmaQYgcxhsdJNE_3Xul2r6LkSbg0')
owner=908927889
@bot.message_handler(content_types=["text"])
def fir(message):
    try:
        if message.text == '/go':
            bot.send_message(message.chat.id, text=(
            'Привет. я бот созыватель для 2тн2. Напиши имя конкретного человека, чтобы я его позвал.\n'
            '         Вы можете написать "Созвать всех", либо поименно по следующему списку:\n'
            '1)Аббос, либо Ариэль\n'
            '2)Зебо\n'
            '3)Шохрух, Шоха\n'
            '4)Азимжон\n'
            '5)Мухлиса\n'
            '6)Сарик, либо Сардор\n'
            '7)Чориев, Нечастивый, либо Бехзод\n'
            '8)Диора\n'
            '9)Али, либо Алижон\n'
            '10)Умид\n'
            '11)Омер\n'
            '12)Жамиля\n'
            '13)Руся, Рустам, либо Рухсора\n'
            '14)Амир, можно Амиракл\n'
            '15)Жас, либо Жасур\n'
            '16)Хасан\n'
            '17)Эльнора\n'
            '18)Аня\n'
            '19)Шохруз\n'
            '20)Дильшода\n'
            '21)Мадина\n'
            '22)Севара\n'
            '23)Камрон, либо Кама\n'
            '24)Шахризода, Шахри, либо Вождь\n'
            '25)Бехруз, либо Беха\n'
            '26)Элшод'))
        elif message.text.lower()=='сука' or message.text.lower()=='сучка':
            bot.restrict_chat_member(message.chat.id,
                                message.from_user.id,
                                can_send_messages=False,
                                until_date=int(time.time()) + 40)
            bot.send_message(908927889, f'ID: {message.from_user.id}\nUsername = @{message.from_user.username} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nTime = {time.localtime().tm_year}.{time.localtime().tm_mon}.{time.localtime().tm_mday}\nHour = {time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            bot.delete_message(message.chat.id, message.message_id)
        if 'пидр' in message.text.lower() or ' блять' in message.text.lower() or ' бля' in message.text.lower() or 'блять ' in message.text.lower()  or 'гомик' in message.text.lower() or 'котак' in message.text.lower() or 'жаляп' in message.text.lower() or 'obsos' in message.text.lower() or 'obbos' in message.text.lower() or 'obosanniy' in message.text.lower() or 'обосан' in message.text.lower() or 'оббос' in message.text.lower() or 'обосс' in message.text.lower() or ' хер' in message.text.lower():
            bot.restrict_chat_member(message.chat.id,
                                 message.from_user.id,
                                 can_send_messages=False,
                                 until_date=int(time.time()) + 40)
            bot.send_message(908927889, f'ID: {message.from_user.id}\nUsername = @{message.from_user.username} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nTime = {time.localtime().tm_year}.{time.localtime().tm_mon}.{time.localtime().tm_mday}\nHour = {time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            bot.delete_message(message.chat.id, message.message_id)
        elif "хрен" in message.text.lower():
            bot.restrict_chat_member(message.chat.id,
                                 message.from_user.id,
                                 can_send_messages=False,
                                 until_date=int(time.time()) + 40)
            bot.send_message(908927889, f'ID: {message.from_user.id}\nUsername = @{message.from_user.username} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nTime = {time.localtime().tm_year}.{time.localtime().tm_mon}.{time.localtime().tm_mday}\nHour = {time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            bot.delete_message(message.chat.id, message.message_id)
        elif "дибил" in message.text.lower() or 'дебил' in message.text.lower() or 'далба' in message.text.lower() or ' сука' in message.text.lower() or 'Сука' in message.text or ' сучка' in message.text.lower():
            bot.send_message(908927889, f'ID: {message.from_user.id}\nUsername = @{message.from_user.username} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nTime = {time.localtime().tm_year}.{time.localtime().tm_mon}.{time.localtime().tm_mday}\nHour = {time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            bot.delete_message(message.chat.id, message.message_id)
            bot.restrict_chat_member(message.chat.id,
                                 message.from_user.id,
                                 can_send_messages=False,
                                 until_date=int(time.time()) + 40)
        elif "ебат" in message.text.lower() or 'хуй' in message.text.lower() or 'хуя' in message.text.lower() or 'пизд' in message.text.lower() or 'вагин' in message.text.lower() or 'хуе' in message.text.lower():
            bot.restrict_chat_member(message.chat.id,
                                 message.from_user.id,
                                 can_send_messages=False,
                                 until_date=int(time.time()) + 40)
            bot.send_message(908927889, f'ID: {message.from_user.id}\nUsername = @{message.from_user.username} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nTime = {time.localtime().tm_year}.{time.localtime().tm_mon}.{time.localtime().tm_mday}\nHour = {time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            bot.delete_message(message.chat.id, message.message_id)
        elif message.text.lower() == 'шахризода' or message.text.lower() == 'вождь' or 'шахри' in message.text.lower():
            bot.reply_to(message, text="<a href='tg://user?id=150437928'>Дороогуу Вождюю</a>", parse_mode='html')
        elif  'абос' in message.text.lower() or 'ариэль' in message.text.lower() or 'аббос' in message.text.lower():
            bot.reply_to(message, text="<a href='tg://user?id=908927889'>Это сообщение</a>", parse_mode='html')
            bot.forward_message(1707358502, from_chat_id=message.chat.id, message_id=message.message_id)
        elif message.text.lower() == 'шохрух' or message.text.lower() == 'шоха':
            bot.reply_to(message, text="<a href='tg://user?id=994781283'>Шохрух</a>", parse_mode='html')
        elif message.text.lower() == 'азим' or message.text.lower() == 'азимжон':
            bot.reply_to(message, text="<a href='tg://user?id=320463139'>Азим</a>", parse_mode='html')
        elif message.text.lower() == 'мухлиса':
            bot.reply_to(message, text="<a href='tg://user?id=908434983'>Мухлиса</a>", parse_mode='html')
        elif message.text.lower() == 'сардор' or message.text.lower() == 'сарик':
            bot.reply_to(message, text="<a href='tg://user?id=328071900'>Сардор</a>", parse_mode='html')
        elif message.text.lower() == 'зулхумор' or message.text.lower() == 'хумора':
            bot.reply_to(message, text="<a href='tg://user?id=973677921'>Зулхумор</a>", parse_mode='html')
        elif message.text.lower() == 'бехзод' or message.text.lower() == 'чориев' or message.text.lower() == 'нечастивый':
            bot.reply_to(message, text="<a href='tg://user?id=1561442300'>Бехзод</a>", parse_mode='html')
        elif message.text.lower() == 'диера' or message.text.lower() == 'диора':
            bot.reply_to(message, text="<a href='tg://user?id=261168444'>Диора</a>", parse_mode='html')
        elif message.text.lower() == 'али' or message.text.lower() == 'алижон' or message.text.lower() == 'алиджон':
            bot.reply_to(message, text="<a href='tg://user?id=1195966769'>Алижон</a>", parse_mode='html')
        elif message.text.lower() == 'умид' or message.text.lower == 'умаров':
            bot.reply_to(message, text="<a href='tg://user?id=257388324'>Умид</a>", parse_mode='html')
        elif message.text.lower() == 'жамиля' or message.text.lower() == 'джамиля':
            bot.reply_to(message, text="<a href='tg://user?id=34843476'>Жамиля</a>", parse_mode='html')
        elif 'руся' in message.text.lower() or message.text.lower() == 'рустам' or 'рухсора' in message.text.lower() or'русе' in message.text.lower() or 'русю' in message.text.lower():
            bot.reply_to(message, text="<a href='tg://user?id=598408015'>Руся на связи</a>", parse_mode='html')
        elif message.text.lower() == 'амир' or message.text.lower() == 'амиракл':
            bot.reply_to(message, text="<a href='tg://user?id=3355451'>Амирхон</a>", parse_mode='html')
        elif message.text.lower() == 'жасур' or message.text.lower() == 'жас':
            bot.reply_to(message, text="<a href='tg://user?id=470617127'>Жасур</a>", parse_mode='html')
        elif message.text.lower() == 'хасан':
            bot.reply_to(message, text="<a href='tg://user?id=645143144'>Хасан</a>", parse_mode='html')
        elif message.text.lower() == 'эльнора' or message.text.lower() == 'эля':
            bot.reply_to(message, text="<a href='tg://user?id=971095948'>Эльнора</a>", parse_mode='html')
        elif message.text.lower() == 'аня' or message.text.lower() == 'анна':
            bot.reply_to(message, text="<a href='tg://user?id=1396286708'>Анна</a>", parse_mode='html')
        elif message.text.lower() == 'шохруз':
            bot.reply_to(message, text="<a href='tg://user?id=1458791988'>Шохруз</a>", parse_mode='html')
        elif message.text.lower() == 'дильшода' or message.text.lower() == 'дилшода':
            bot.reply_to(message, text="<a href='tg://user?id=1329175197'>Дильшода</a>", parse_mode='html')
        elif message.text.lower() == 'мадина':
            bot.reply_to(message, text="<a href='tg://user?id=568068622'>Мадина</a>", parse_mode='html')
        elif message.text.lower() == 'камрон' or message.text.lower() == 'кама' or message.text.lower() == 'импостер' or message.text.lower() == 'камри':
            bot.reply_to(message, text="<a href='tg://user?id=1076489613'>Камрон</a>", parse_mode='html')
        elif message.text.lower() == 'омер' or message.text.lower() == 'омэр':
            bot.reply_to(message, text="<a href='tg://user?id=245876076'>Омер</a>", parse_mode='html')
        elif message.text.lower() == 'эльшод' or message.text.lower() == 'элшод' or message.text.lower() == 'эльшот' or message.text.lower() == 'элшот':
            bot.reply_to(message, text="<a href='tg://user?id=893416762'>Элшод</a>", parse_mode='html')
        elif message.text.lower() == 'севара' or message.text.lower() == 'садыкова':
            bot.reply_to(message, text="<a href='tg://user?id=1029746208'>Севара</a>", parse_mode='html')
        elif message.text.lower() == 'зебо':
            bot.reply_to(message, text="<a href='tg://user?id=67444096'>Зебо</a>", parse_mode='html')
        elif message.text.lower() == 'беха' or message.text.lower() == 'бехруз':
            bot.reply_to(message, text="<a href='tg://user?id=616157584'>Бехруз</a>", parse_mode='html')
        elif message.text.lower() == 'эфе':
            bot.reply_to(message, text="<a href='tg://user?id=267690897'>Эфе</a>", parse_mode='html')
        elif message.text.lower() == 'акбар':
            bot.reply_to(message, text="<a href='tg://user?id=1145277075'>Акбар</a>", parse_mode='html')
        elif message.text.lower() == 'мехруза':
            bot.reply_to(message, text="<a href='tg://user?id=913435124'>Мехруза</a>", parse_mode='html')
        elif message.text.lower() == 'шахзода':
            bot.reply_to(message, text="<a href='tg://user?id=1280858486'>Шахзода</a>", parse_mode='html')
        elif message.text.lower() == 'ширин':
            bot.reply_to(message, text="<a href='tg://user?id=1822513216'>Ширин</a>", parse_mode='html')
        elif message.text.lower() == 'куратор' or message.text.lower()=='малика абдумаликовна':
            bot.reply_to(message, text="<a href='tg://user?id=233473811'>Малика Абдумаликовна</a>", parse_mode='html')
        elif message.text.lower() == 'созвать всех':
            if message.from_user.id == 908927889 or message.from_user.id== 233473811:
                bot.reply_to(message, text=('Щас позову'))
                time.sleep(1)
                bot.send_message(message.chat.id, text=('3'))
                time.sleep(2)
                bot.send_message(message.chat.id, text=('2'))
                time.sleep(2)
                bot.send_message(message.chat.id, text=('1'))
                time.sleep(2)
                bot.send_message(message.chat.id, text=('Пошло😋'))
                bot.send_message(message.chat.id, text=("<a href='tg://user?id=150437928'>Вождь</a> \n"
"<a href='tg://user?id=908927889'>Разработчик</a> \n"
"<a href='tg://user?id=67444096'>Зебо</a> \n"
        "<a href='tg://user?id=328071900'>Сардор</a> \n"
        "<a href='tg://user?id=1076489613'>Камрон</a> \n") , parse_mode='html')
                bot.send_message(message.chat.id, text=("<a href='tg://user?id=893416762'>Элшод</a> \n"
        "<a href='tg://user?id=320463139'>Азим</a> \n"
        "<a href='tg://user?id=994781283'>Шохрух</a> \n"
        "<a href='tg://user?id=1145277075'>Акбар</a> \n"
        "<a href='tg://user?id=1329175197'>Дильшода</a> \n"), parse_mode='html')
                bot.send_message(message.chat.id, text=("<a href='tg://user?id=971095948'>Эльнора</a> \n"
        "<a href='tg://user?id=1195966769'>Алижон</a> \n"
        "<a href='tg://user?id=267690897'>Эфе</a> \n"
        "<a href='tg://user?id=245876076'>Омер</a> \n"
        "<a href='tg://user?id=470617127'>Жасур</a> \n"), parse_mode='html')
                bot.send_message(message.chat.id, text=("<a href='tg://user?id=1458791988'>Шохруз</a> \n"
        "<a href='tg://user?id=1280858486'>Шахзода</a> \n"
        "<a href='tg://user?id=34843476'>Жамиля</a> \n"
        "<a href='tg://user?id=1396286708'>Анна</a> \n"
        "<a href='tg://user?id=1822513216'>Ширин</a> \n"), parse_mode='html')
                bot.send_message(message.chat.id, text=("<a href='tg://user?id=261168444'>Диора</a> \n"
        "<a href='tg://user?id=568068622'>Мадина</a> \n"
        "<a href='tg://user?id=3355451'>Амирхон</a> \n"
        "<a href='tg://user?id=908434983'>Мухлиса</a> \n"
        "<a href='tg://user?id=598408015'>Рухсора</a> \n"), parse_mode='html')
                bot.send_message(message.chat.id, text=("<a href='tg://user?id=645143144'>Хасан</a> \n"
        "<a href='tg://user?id=1029746208'>Севара</a> \n"
        "<a href='tg://user?id=257388324'>Умид</a> \n"
        "<a href='tg://user?id=1561442300'>Бехзод</a> \n"), parse_mode='html')
                bot.send_message(message.chat.id, text=("<a href='tg://user?id=973677921'>Зулхумор</a> \n"
        "<a href='tg://user?id=913435124'>Мехруза</a> \n"
        "<a href='tg://user?id=616157584'>Бехруз</a> \n"), parse_mode='html')
                bot.send_message(message.chat.id, text=('Я всех позвал 😉'))
            else:
                bot.reply_to(message, text=('Щас позову'))
                time.sleep(1)
                bot.send_message(message.chat.id, text=('3'))
                time.sleep(2)
                bot.send_message(message.chat.id, text=('2'))
                time.sleep(2)
                bot.send_message(message.chat.id, text=('1'))
                time.sleep(2)
                bot.send_message(message.chat.id, text=('Пошло😋'))
                bot.send_message(message.chat.id, text=("<a href='tg://user?id=150437928'>Вождь</a> \n"
"<a href='tg://user?id=908927889'>Разработчик</a> \n"
"<a href='tg://user?id=67444096'>Зебо</a> \n"
        "<a href='tg://user?id=328071900'>Сардор</a> \n"
        "<a href='tg://user?id=1076489613'>Камрон</a> \n") , parse_mode='html')
                bot.send_message(message.chat.id, text=("<a href='tg://user?id=893416762'>Элшод</a> \n"
        "<a href='tg://user?id=320463139'>Азим</a> \n"
        "<a href='tg://user?id=994781283'>Шохрух</a> \n"
        "<a href='tg://user?id=1145277075'>Акбар</a> \n"
        "<a href='tg://user?id=1329175197'>Дильшода</a> \n"), parse_mode='html')
                bot.send_message(message.chat.id, text=("<a href='tg://user?id=971095948'>Эльнора</a> \n"
        "<a href='tg://user?id=267690897'>Эфе</a> \n"
        "<a href='tg://user?id=245876076'>Омер</a> \n"
        "<a href='tg://user?id=470617127'>Жасур</a> \n"), parse_mode='html')
                bot.send_message(message.chat.id, text=("<a href='tg://user?id=1458791988'>Шохруз</a> \n"
        "<a href='tg://user?id=1280858486'>Шахзода</a> \n"
        "<a href='tg://user?id=34843476'>Жамиля</a> \n"
        "<a href='tg://user?id=1396286708'>Анна</a> \n"
        "<a href='tg://user?id=1822513216'>Ширин</a> \n"), parse_mode='html')
                bot.send_message(message.chat.id, text=("<a href='tg://user?id=261168444'>Диора</a> \n"
        "<a href='tg://user?id=568068622'>Мадина</a> \n"
        "<a href='tg://user?id=3355451'>Амирхон</a> \n"
        "<a href='tg://user?id=908434983'>Мухлиса</a> \n"
        "<a href='tg://user?id=598408015'>Рухсора</a> \n"), parse_mode='html')
                bot.send_message(message.chat.id, text=("<a href='tg://user?id=645143144'>Хасан</a> \n"
        "<a href='tg://user?id=1029746208'>Севара</a> \n"
        "<a href='tg://user?id=257388324'>Умид</a> \n"
        "<a href='tg://user?id=1561442300'>Бехзод</a> \n"), parse_mode='html')
                bot.send_message(message.chat.id, text=("<a href='tg://user?id=973677921'>Зулхумор</a> \n"
        "<a href='tg://user?id=913435124'>Мехруза</a> \n"
        "<a href='tg://user?id=616157584'>Бехруз</a> \n"), parse_mode='html')
                bot.send_message(message.chat.id, text=('Я всех позвал 😉'))
        elif message.from_user.id == 908927889:
            if message.text.lower() == 'минус':
                bot.delete_message(message.chat.id, message.message_id)
                bot.delete_message(message.chat.id, message.reply_to_message.message_id)
            elif message.text.lower() == 'замолкни':
                replied_user = message.reply_to_message.from_user.id
                bot.restrict_chat_member(message.chat.id,
                                        user_id=replied_user,
                                        can_send_messages=False,
                                        can_send_media_messages=False,
                                        can_send_other_messages=False,
                                        until_date=int(time.time()) + 600)
            else:
                return
    except:
        bot.send_message(owner, 'Че то пошло не так')
@bot.edited_message_handler(func=lambda message: True)
def edit_message(message):
    if message.text.lower()=="бля"  or message.text.lower()=='блять' or message.text.lower()=='бляя' or message.text.lower()=='бляяя' or message.text.lower()=='бляяяя':
        bot.restrict_chat_member(message.chat.id,
                                 message.from_user.id,
                                 can_send_messages=False,
                                 until_date=int(time.time()) + 45)
        bot.send_message(908927889, f'ID: {message.from_user.id}\nUsername = @{message.from_user.username} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nTime = {time.localtime().tm_year}.{time.localtime().tm_mon}.{time.localtime().tm_mday}\nHour = {time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)
    elif message.text.lower()=="сука" or message.text.lower()=="суки" or message.text.lower()=="сук" or message.text.lower()=="сучка":
        bot.restrict_chat_member(message.chat.id,
                                 message.from_user.id,
                                 can_send_messages=False,
                                 until_date=int(time.time()) + 40)
        bot.send_message(908927889, f'ID: {message.from_user.id}\nUsername = @{message.from_user.username} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nTime = {time.localtime().tm_year}.{time.localtime().tm_mon}.{time.localtime().tm_mday}\nHour = {time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)
    elif 'пидр' in message.text.lower() or ' блять' in message.text.lower() or ' бля' in message.text.lower() or 'блять ' in message.text.lower()  or 'гомик' in message.text.lower() or 'котак' in message.text.lower() or 'жаляп' in message.text.lower() or 'obsos' in message.text.lower() or 'obbos' in message.text.lower() or 'obosanniy' in message.text.lower() or 'обосан' in message.text.lower() or 'оббос' in message.text.lower() or 'обосс' in message.text.lower() or ' хер' in message.text.lower():
        bot.restrict_chat_member(message.chat.id,
                                 message.from_user.id,
                                 can_send_messages=False,
                                 until_date=int(time.time()) + 40)
        bot.send_message(908927889, f'ID: {message.from_user.id}\nUsername = @{message.from_user.username} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nTime = {time.localtime().tm_year}.{time.localtime().tm_mon}.{time.localtime().tm_mday}\nHour = {time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)
    elif "хрен" in message.text.lower():
        bot.restrict_chat_member(message.chat.id,
                                 message.from_user.id,
                                 can_send_messages=False,
                                 until_date=int(time.time()) + 45)
        bot.send_message(908927889, f'ID: {message.from_user.id}\nUsername = @{message.from_user.username} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nTime = {time.localtime().tm_year}.{time.localtime().tm_mon}.{time.localtime().tm_mday}\nHour = {time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)
    elif "дибил" in message.text.lower() or 'дебил' in message.text.lower() or 'далба' in message.text.lower() or ' сука' in message.text.lower() or 'Сука' in message.text or ' сучка' in message.text.lower():
        bot.send_message(908927889, f'ID: {message.from_user.id}\nUsername = @{message.from_user.username} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nTime = {time.localtime().tm_year}.{time.localtime().tm_mon}.{time.localtime().tm_mday}\nHour = {time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)
        bot.restrict_chat_member(message.chat.id,
                                 message.from_user.id,
                                 can_send_messages=False,
                                 until_date=int(time.time()) + 40)
    elif "ебат" in message.text.lower() or 'хуй' in message.text.lower() or 'хуя' in message.text.lower() or 'пизд' in message.text.lower() or 'вагин' in message.text.lower() or 'хуе' in message.text.lower():
        bot.restrict_chat_member(message.chat.id,
                                 message.from_user.id,
                                 can_send_messages=False,
                                 until_date=int(time.time()) + 40)
        bot.send_message(908927889, f'ID: {message.from_user.id}\nUsername = @{message.from_user.username} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nTime = {time.localtime().tm_year}.{time.localtime().tm_mon}.{time.localtime().tm_mday}\nHour = {time.localtime().tm_hour}.{time.localtime().tm_min}.{time.localtime().tm_sec} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)
    elif  'абос' in message.text.lower() or 'ариэль' in message.text.lower() or 'аббос' in message.text.lower():
        bot.reply_to(message, text="<a href='tg://user?id=908927889'>Это сообщение</a>", parse_mode='html')







bot.polling(none_stop=True, interval=0)