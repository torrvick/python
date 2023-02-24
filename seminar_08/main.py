import telebot
from telebot import types
import sql

edit_mode = False

def contact_find(data):
    record = sql.record_find(data)
    output = {}
    for rec in record:
        if rec[1] in output:
            output[rec[1]] += [rec[2],rec[3]]
        else:
            output[rec[1]]=[rec[0],rec[2],rec[3]]
    return output

API_TOKEN="PASTE_YOUR_TOKEN_HERE"
bot = telebot.TeleBot(API_TOKEN)

def get_name(message): 
    global name    
    name = message.text
    bot.send_message(message.from_user.id, "Введи номер телефона")
    bot.register_next_step_handler(message, get_phone)

def get_phone(message):
    global phone
    phone = message.text
    get_phone_type(message)

def get_phone_type(message):
    buttons = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Личный', callback_data='new_personal_phone')
    button2 = types.InlineKeyboardButton('Рабочий', callback_data='new_work_phone')
    buttons.add(button1, button2)
    bot.send_message(message.chat.id, "Выбери тип номера", reply_markup=buttons)

def get_contact_group(message):
    bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id,  reply_markup = '')
    buttons = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Семья', callback_data='group_family')
    button2 = types.InlineKeyboardButton('Друзья', callback_data='group_friends')
    button3 = types.InlineKeyboardButton('Работа', callback_data='group_work')
    buttons.add(button1, button2,button3)
    bot.send_message(message.chat.id,"Выбери группу контакта", reply_markup=buttons)

def write_new_contact(message):
    bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id,  reply_markup = '')
    try:
        sql.record_add(name, contact_group,phone,phone_type)
        bot.send_message(message.chat.id,f"Добавлен контакт *{name}* с номером *{phone}*",parse_mode="MarkdownV2")
    except:
        bot.send_message(message.chat.id,"Ошибка добавления")

def edit_select(message):
    if message.text == "Домой":
        start(message)
    else:
        if not edit_mode: return
        if edit_mode:
            global contacts
            contacts = contact_find(message.text)
            if len(contacts) == 0:
                bot.send_message(message.from_user.id, "Контакты не найдены")
                bot.register_next_step_handler(message,edit_select)
            else:

                reply_string = ""
                for key in contacts:
                    reply_string = f"*{key}*\n"
                    for i in range(1,len(contacts[key]),2):
                        reply_string += f"{contacts[key][i+1]}: {contacts[key][i]}\n"
                    buttons = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton('Редактировать', callback_data=f"e_c:{str(key)}")
                    buttons.add(button1)
                    bot.send_message(message.from_user.id, reply_string, parse_mode="MarkdownV2", reply_markup=buttons)
                bot.register_next_step_handler(message,edit_select)

def edit_contact(message, people_name):
    bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id,  reply_markup = '')
    editing_contact = contacts[people_name]
    reply_string = "Что сделать с контактом?"
    buttons = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton('Изменить имя', callback_data=f"change_name:{str(editing_contact[0])}")
    button2 = types.InlineKeyboardButton('Добавить телефон', callback_data=f"add_phone:{str(editing_contact[0])}")
    button3 = types.InlineKeyboardButton('Удалить телефон', callback_data=f"del_phone_sel:{str(editing_contact[0])}")
    button4 = types.InlineKeyboardButton('Удалить контакт', callback_data=f"del_contact:{str(editing_contact[0])}")
    buttons.add(button1,button2,button3,button4)
    bot.send_message(message.chat.id, reply_string, parse_mode="MarkdownV2", reply_markup=buttons)

def del_contact(message, id_people):
    try:
        bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id,  reply_markup = '')
        sql.record_del(id_people)
        bot.send_message(message.chat.id, "Контакт удален")
    except:
        bot.send_message(message.chat.id,f"Ошибка удаления контакта")
    start(message)

def change_name(message):
    global new_name
    new_name = message.text
    try:
        sql.change_name(new_name,changing_id)
        bot.send_message(message.chat.id,f"Контакт изменен")
    except:
        bot.send_message(message.chat.id,f"Ошибка изменения номера")
    start(message)

def add_phone_of_type(message):
    buttons = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Личный', callback_data='add_personal_phone')
    button2 = types.InlineKeyboardButton('Рабочий', callback_data='add_work_phone')
    buttons.add(button1, button2)
    global phone_adding
    phone_adding = message.text
    bot.send_message(message.chat.id, "Выбери тип номера", reply_markup=buttons)

def add_phone(message):
    try:
        bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id,  reply_markup = '')
        sql.add_phone(changing_id,phone_adding,phone_type)
        bot.send_message(message.chat.id,f"Номер добавлен")
    except:
        bot.send_message(message.chat.id,f"Ошибка добавления номера")
    start(message)

def del_phone(message, phone_del):
    try:
        bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id,  reply_markup = '')
        sql.del_phone(changing_id, phone_del)
        bot.send_message(message.chat.id,f"Номер удален")
    except:
        bot.send_message(message.chat.id,f"Ошибка удаления номера")
    start(message)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global phone_type
    global contact_group
    if call.data == 'new_personal_phone':
        phone_type = 1
        get_contact_group(call.message)
    elif call.data == 'new_work_phone':
        phone_type = 2
        get_contact_group(call.message)
    elif call.data == 'group_family':
        contact_group = 1
        write_new_contact(call.message)
    elif call.data == 'group_friends':
        contact_group = 2
        write_new_contact(call.message)
    elif call.data == 'group_work':
        contact_group = 3
        write_new_contact(call.message)
    elif call.data.startswith("e_c:"):
        global edit_mode
        edit_mode = False
        edit_contact(call.message, call.data.split(":")[1])
    elif call.data.startswith("del_contact:"):
        edit_mode = False
        del_contact(call.message, call.data.split(":")[1])
    elif call.data.startswith("change_name:"):
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,  reply_markup = '')
        bot.send_message(call.message.chat.id, "Введите новое имя контакта")
        edit_mode = False
        global changing_id
        changing_id = call.data.split(":")[1]
        bot.register_next_step_handler(call.message, change_name)
    elif call.data.startswith("add_phone:"):
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,  reply_markup = '')
        bot.send_message(call.message.chat.id, "Введите новый номер")
        edit_mode = False
        changing_id = call.data.split(":")[1]
        bot.register_next_step_handler(call.message, add_phone_of_type)
    elif call.data == 'add_personal_phone':
        phone_type = 1
        add_phone(call.message)
    elif call.data == 'add_work_phone':
        phone_type = 2
        add_phone(call.message)
    elif call.data.startswith("del_phone_sel:"):
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,  reply_markup = '')
        edit_mode = False
        changing_id = call.data.split(":")[1]
        buttons = types.InlineKeyboardMarkup()
        phone_dict = list(contacts.values())[0]
        for i in range(1,len(phone_dict),2):
            buttons.add(types.InlineKeyboardButton(f"{phone_dict[i+1]}: {phone_dict[i]}", callback_data=f"del_phone:{phone_dict[i]}"))
        bot.send_message(call.message.chat.id, "Какой номер удалить?", reply_markup=buttons)
    elif call.data.startswith("del_phone:"):
        edit_mode = False
        phone_del = call.data.split(":")[1]
        del_phone(call.message,phone_del)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    button1 = types.KeyboardButton("Добавить контакт")
    button2 = types.KeyboardButton("Редактировать контакт")
    markup.add(button1,button2)
    bot.send_message(message.chat.id, "Введи строку для поиска. Это может быть часть имени или часть телефонного номера", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def message_reply(message):
    if message.text == "Домой":
        start(message)

    elif message.text == "Добавить контакт":
        
        bot.send_message(message.from_user.id, "Введи имя")
        bot.register_next_step_handler(message, get_name)

    elif message.text == "Редактировать контакт":
        global edit_mode
        edit_mode = True
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
        button1 = types.KeyboardButton("Домой")
        markup.add(button1)
        bot.send_message(message.from_user.id, "Введи строку для поиска", reply_markup=markup)
        bot.register_next_step_handler(message,edit_select)

    else:
        contacts = contact_find(message.text)
        if len(contacts) == 0:
            bot.send_message(message.from_user.id, "Контакты не найдены")
        else:
            reply_string = ""
            for key in contacts:
                reply_string += f"*{key}*\n"
                for i in range(1,len(contacts[key]),2):
                    reply_string += f"{contacts[key][i+1]}: {contacts[key][i]}\n"
                reply_string += "\n"
            bot.send_message(message.from_user.id, reply_string, parse_mode="MarkdownV2")

bot.polling()