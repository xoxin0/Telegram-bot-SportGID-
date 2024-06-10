import telebot
from telebot import types

bot = telebot.TeleBot('7243172146:AAH35aQ68FhCBhS9KKLrsTehmC4Jfh6Pm84')

@bot.message_handler(commands=['start'])
def first_sms(message):
    first_choice = types.InlineKeyboardMarkup()
    first_choice.add(types.InlineKeyboardButton('Спортивные добавки', callback_data='sports supplements'))
    first_choice.add(types.InlineKeyboardButton('Программы тренировок', callback_data='training programs'))
    bot.send_message(message.chat.id, 'Привет! Здесь ты узнаешь о спортивном питании и тренировках в зале💪💊', reply_markup=first_choice)


@bot.callback_query_handler(func=lambda callback: True)
def callback_second_choice(callback):
    sports_supplements = types.InlineKeyboardMarkup()
    sports_supplements.add(types.InlineKeyboardButton('Креатин', callback_data='creatine'))
    sports_supplements.add(types.InlineKeyboardButton('Протеин', callback_data='protein'))
    sports_supplements.add(types.InlineKeyboardButton('BCAA', callback_data='bcaa'))
    sports_supplements.add(types.InlineKeyboardButton('Л-Карнитин', callback_data='l-carnitine'))
    sports_supplements.add(types.InlineKeyboardButton('Витамин-Д', callback_data='vitamine-d'))
    sports_supplements.add(types.InlineKeyboardButton('Предтрен', callback_data='pretrain'))

    training_programs = types.InlineKeyboardMarkup()
    training_programs.add(types.InlineKeyboardButton('1 раз в неделю', callback_data='once a week'))
    training_programs.add(types.InlineKeyboardButton('2 раза в неделю', callback_data='two times a week'))
    training_programs.add(types.InlineKeyboardButton('3 раза в неделю', callback_data='three times a week'))

    if callback.data == "sports supplements":
        bot.send_message(callback.message.chat.id, 'Существует большое множество разных добавок, как действенных, так и пустышек😢\nЯ могу вам рассказать о самых популярных и действенных добавках.\n \nЧто именно вас интересует?', reply_markup=sports_supplements)
    elif callback.data == "training programs":
        bot.send_message(callback.message.chat.id, 'Программ тренировок существует различное множество, а для профессиональных спортсменов подбирается индивидуально, но для начинающих есть простые программы😼\n \nВыберите кол-во занятий в неделю:', reply_markup=training_programs)
    if callback.data == "creatine":
        creatine_photo = open('photo/creatine.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, creatine_photo, caption='Креатин является важным элементом для организма, по своей сути это азотсодержащая карбоновая кислота. Прежде всего это источник энергии. Основным свойством вещества является насыщение клеток молекулами воды.\n\nПро какую еще добавку вы хотите узнать?', reply_markup=sports_supplements)
    elif callback.data == "protein":
        protein_photo = open('photo/protein.webp', 'rb')
        bot.send_photo(callback.message.chat.id, protein_photo, caption='Протеин - продукт с содержанием большого количества белка и содержащий в своем составе необходимое количество аминокислот, дополнительно обогащенный минералами и витаминами.\n\nПро какую еще добавку вы хотите узнать?', reply_markup=sports_supplements)
    elif callback.data == "bcaa":
        bcaa_photo = open('photo/bcaa.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, bcaa_photo, caption='Группа протеиногенных аминокислот, характеризующихся разветвлёнными строением алифатической боковой цепи. К таким аминокислотам относятся лейцин, изолейцин и валин.\n\nПро какую еще добавку вы хотите узнать?', reply_markup=sports_supplements)
    elif callback.data == "l-carnitine":
        l_carnitine = open('photo/L-carnitine.jpeg', 'rb')
        bot.send_photo(callback.message.chat.id, l_carnitine, caption='Аминокислота. Природное витаминоподобное вещество, которое по функциональности можно назвать родственным витаминам группы В (но витамином В оно не является).\n\nПро какую еще добавку вы хотите узнать?', reply_markup=sports_supplements)
    elif callback.data == "vitamine-d":
        vitamine_d = open('photo/vitamine-d.jpeg', 'rb')
        bot.send_photo(callback.message.chat.id, vitamine_d, caption='Cоединение, которое необходимо всем детям и взрослым. Он синтезируется в коже под действием солнечного света. Дефицит витамина д понижает уровень тестостерона (мужской половой гормон).\n\nПро какую еще добавку вы хотите узнать?', reply_markup=sports_supplements)
    elif callback.data == "pretrain":
        pretrain = open('photo/pretrain.png', 'rb')
        bot.send_photo(callback.message.chat.id, pretrain, caption='Это особый вид спортивного питания, который помогает организму дать заряд бодрости на тренировке, даже после тяжелого рабочего дня.\n\nПро какую еще добавку вы хотите узнать?', reply_markup=sports_supplements)

    if callback.data == "once a week":
        file_fullbody = open('training/fullbody.pdf', 'rb')
        bot.send_document(callback.message.chat.id, file_fullbody)
        bot.send_message(callback.message.chat.id, '🏋🏻Для покупки полного курса и ответам на ваши вопросы: @xonweb')
    elif callback.data == "two times a week":
        two_times_first_day = open('training/two_times_first_day.pdf', 'rb')
        two_times_second_day = open('training/two_times_second_day.pdf', 'rb')
        bot.send_document(callback.message.chat.id, two_times_first_day)
        bot.send_document(callback.message.chat.id, two_times_second_day)
        bot.send_message(callback.message.chat.id, '🏋🏻Для покупки полного курса и ответам на ваши вопросы: @xonweb')
    elif callback.data == "three times a week":
        file_three_times_1 = open('training/three_times_first_day.pdf', 'rb')
        file_three_times_2 = open('training/three_times_second_day.pdf', 'rb')
        file_three_times_3 = open('training/three_times_third_day.pdf', 'rb')
        bot.send_document(callback.message.chat.id, file_three_times_1)
        bot.send_document(callback.message.chat.id, file_three_times_2)
        bot.send_document(callback.message.chat.id, file_three_times_3)
        bot.send_message(callback.message.chat.id, '🏋🏻Для покупки полного курса и ответам на ваши вопросы: @xonweb')


bot.polling(none_stop=True)