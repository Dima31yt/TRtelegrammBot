import telebot, json
from telebot import TeleBot
from telebot import types

token = "1771665425:AAFxHei3bsH3g4xabwnKkCaxISAgyk8g_GA"
bot = telebot.TeleBot(token)

exit_keyboard = telebot.types.ReplyKeyboardMarkup()  
exit_keyboard.add(telebot.types.KeyboardButton("Выход в главное меню"))

@bot.message_handler(commands=['start', 'help'])  
def help_command(message):
    try:
        with open('config.json', encoding='utf-8') as f:
            data = json.load(f)

        admins = data["admins"]
        if message.from_user.id in admins:
            admin_q_keyboard = telebot.types.InlineKeyboardMarkup()  
            admin_q_keyboard.add(telebot.types.InlineKeyboardButton("Главое меню", callback_data='main_area'))
            admin_q_keyboard.add(telebot.types.InlineKeyboardButton("Админ область", callback_data='admin_area'))

            user = message.from_user.first_name
            bot.send_message(  
                message.chat.id,  
                'Я бот. Приятно познакомиться, ' + user + '\nВы находитесь в главном меню.',
                reply_markup=admin_q_keyboard  
            )
        else:
            main_keyboard = telebot.types.ReplyKeyboardMarkup()  
            main_keyboard.add(telebot.types.KeyboardButton("Предметная область"))
            main_keyboard.add(telebot.types.KeyboardButton("Общая область"))
            main_keyboard.add(telebot.types.KeyboardButton("Обратная связь"))

            user = message.from_user.first_name
            bot.send_message(  
                message.chat.id,  
                'Я бот. Приятно познакомиться, ' + user + '\nВы находитесь в главном меню.',
                reply_markup=main_keyboard  
            )
            
    except Exception as e:
        print(e)
        bot.send_message(1356201546, e)
        bot.send_message(1024861899, e)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        with open('config.json', encoding='utf-8') as f:
            data = json.load(f)

        if message.text.lower() == 'предметная область':
            subject_keyboard = telebot.types.ReplyKeyboardMarkup()  
            subject_keyboard.add(telebot.types.KeyboardButton("Информатика"))
            subject_keyboard.add(telebot.types.KeyboardButton("Технология и ОБЖ"))
            subject_keyboard.add(telebot.types.KeyboardButton("Робототехника"))
            subject_keyboard.add(telebot.types.KeyboardButton("Выход в главное меню"))
            bot.send_message(  
                message.chat.id,  
                'Предметная область',
                reply_markup=subject_keyboard
            )
        if message.text.lower() == 'общая область':
            general_keyboard = telebot.types.ReplyKeyboardMarkup()  
            general_keyboard.add(telebot.types.KeyboardButton("Полезные ресурсы"))
            general_keyboard.add(telebot.types.KeyboardButton("Позиция 2"))
            general_keyboard.add(telebot.types.KeyboardButton("Выход в главное меню"))
            bot.send_message(  
                message.chat.id,  
                'Общая область',
                reply_markup=general_keyboard
            )
        if message.text.lower() == 'обратная связь':
            bot.send_message(message.chat.id, "Обратная связь\nФорма обратной связи\nФорма добавления новых ресурсов\nПотом что нибудь придумаем", reply_markup=exit_keyboard)

        if message.text.lower() == 'информатика':
            bot.send_message(  
                message.chat.id,  
                'Информатика\n' + data["informatics"]["sourse1"] + "\n" + data["informatics"]["sourse2"],
                reply_markup=exit_keyboard 
            )
        if message.text.lower() == 'технология и обж':
            bot.send_message(  
                message.chat.id,  
                'Технология и ОБЖ\n' + data["technology"]["sourse1"] + "\n" + data["technology"]["sourse2"],
                reply_markup=exit_keyboard 
            )
        if message.text.lower() == 'робототехника':
            bot.send_message(  
                message.chat.id,  
                'Робототехника\n' + data["robotics"]["sourse1"] + "\n" + data["robotics"]["sourse2"],
                reply_markup=exit_keyboard 
            )
        if message.text.lower() == 'полезные ресурсы':
            bot.send_message(  
                message.chat.id,  
                'Полезные ресурсы\n' + data["resources"]["sourse1"] + "\n" + data["resources"]["sourse2"],
                reply_markup=exit_keyboard 
            )
        if message.text.lower() == 'позиция 2':
            bot.send_message(  
                message.chat.id,  
                'Позиция 2\n' + data["position2"]["sourse1"] + "\n" + data["position2"]["sourse2"],
                reply_markup=exit_keyboard
            )

        if message.text.lower() == 'выход в главное меню':
            main_keyboard = telebot.types.ReplyKeyboardMarkup()  
            main_keyboard.add(telebot.types.KeyboardButton("Предметная область"))
            main_keyboard.add(telebot.types.KeyboardButton("Общая область"))
            main_keyboard.add(telebot.types.KeyboardButton("Обратная связь"))

            user = message.from_user.first_name
            bot.send_message(  
                message.chat.id,  
                'Я бот. Приятно познакомиться, ' + user + '\nВы находитесь в главном меню.',
                reply_markup=main_keyboard  
            )

        if message.text.lower() == 'айди':
            print(message)
        
        if "edit" in message.text.lower():
            text_s = message.text.split(" ", 3)
            if str(text_s[2]) == "1":
                if str(text_s[1]) == "inf":
                    with open('config.json', encoding='utf-8') as f:
                        data = json.load(f)

                    data["informatics"]["sourse1"] = text_s[3]

                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                    
                    bot.send_message(message.chat.id, 'Готово!')

                if str(text_s[1]) == "tech":
                    with open('config.json', encoding='utf-8') as f:
                        data = json.load(f)

                    data["technology"]["sourse1"] = text_s[3]

                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)

                    bot.send_message(message.chat.id, 'Готово!')

                if str(text_s[1]) == "rob":
                    with open('config.json', encoding='utf-8') as f:
                        data = json.load(f)

                    data["robotics"]["sourse1"] = text_s[3]

                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)

                    bot.send_message(message.chat.id, 'Готово!')

                if str(text_s[1]) == "res":
                    with open('config.json', encoding='utf-8') as f:
                        data = json.load(f)

                    data["resources"]["sourse1"] = text_s[3]

                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                        
                    bot.send_message(message.chat.id, 'Готово!')

                if str(text_s[1]) == "pos":
                    with open('config.json', encoding='utf-8') as f:
                        data = json.load(f)

                    data["position2"]["sourse1"] = text_s[3]

                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                        
                    bot.send_message(message.chat.id, 'Готово!')


            if str(text_s[2]) == "2":
                if str(text_s[1]) == "inf":
                    with open('config.json', encoding='utf-8') as f:
                        data = json.load(f)

                    data["informatics"]["sourse2"] = text_s[3]

                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                        
                    bot.send_message(message.chat.id, 'Готово!')

                if str(text_s[1]) == "tech":
                    with open('config.json', encoding='utf-8') as f:
                        data = json.load(f)

                    data["technology"]["sourse2"] = text_s[3]

                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                        
                    bot.send_message(message.chat.id, 'Готово!')

                if str(text_s[1]) == "rob":
                    with open('config.json', encoding='utf-8') as f:
                        data = json.load(f)

                    data["robotics"]["sourse2"] = text_s[3]

                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                        
                    bot.send_message(message.chat.id, 'Готово!')

                if str(text_s[1]) == "res":
                    with open('config.json', encoding='utf-8') as f:
                        data = json.load(f)

                    data["resources"]["sourse2"] = text_s[3]

                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)

                    bot.send_message(message.chat.id, 'Готово!')

                if str(text_s[1]) == "pos":
                    with open('config.json', encoding='utf-8') as f:
                        data = json.load(f)

                    data["position2"]["sourse2"] = text_s[3]

                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                        
                    bot.send_message(message.chat.id, 'Готово!')

    except Exception as e:
        print(e)
        bot.send_message(1356201546, e)
        bot.send_message(1024861899, e)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "main_area":
                main_keyboard = telebot.types.ReplyKeyboardMarkup()  
                main_keyboard.add(telebot.types.KeyboardButton("Предметная область"))
                main_keyboard.add(telebot.types.KeyboardButton("Общая область"))
                main_keyboard.add(telebot.types.KeyboardButton("Обратная связь"))

                user = call.message.from_user.first_name
                bot.send_message(  
                    call.message.chat.id,  
                    'Я бот. Приятно познакомиться, ' + user + '\nВы находитесь в главном меню.',
                    reply_markup=main_keyboard  
                )

            if call.data == "admin_area":
                edit_keyboard = telebot.types.InlineKeyboardMarkup()  
                edit_keyboard.add(telebot.types.InlineKeyboardButton("Информатика", callback_data='informatics'))
                edit_keyboard.add(telebot.types.InlineKeyboardButton("Технология и ОБЖ", callback_data='technology'))
                edit_keyboard.add(telebot.types.InlineKeyboardButton("Робототехника", callback_data='robotics'))
                edit_keyboard.add(telebot.types.InlineKeyboardButton("Полезные ресурсы", callback_data='resources'))
                edit_keyboard.add(telebot.types.InlineKeyboardButton("Позиция 2", callback_data='position2'))
                bot.send_message(  
                    call.message.chat.id,  
                    'Выберите предмет, текст которого нужно изменить',
                    reply_markup=edit_keyboard  
                )
                
            if call.data == "informatics":
                bot.send_message(call.message.chat.id, 'Напишите: edit inf 1/2 <текст>')
            if call.data == "technology":
                bot.send_message(call.message.chat.id, 'Напишите: edit tech 1/2 <текст>')
            if call.data == "robotics":
                bot.send_message(call.message.chat.id, 'Напишите: edit rob 1/2 <текст>')
            if call.data == "resources":
                bot.send_message(call.message.chat.id, 'Напишите: edit res 1/2 <текст>')
            if call.data == "position2":
                bot.send_message(call.message.chat.id, 'Напишите: edit pos 1/2 <текст>')

    except Exception as e:
        print(e)
        bot.send_message(1356201546, e)
        bot.send_message(1024861899, e)
        bot.send_message(1356201546, repr(e))
        bot.send_message(1024861899, repr(e))
        print(repr(e))

bot.polling(none_stop=True)