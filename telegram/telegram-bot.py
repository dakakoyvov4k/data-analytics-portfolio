import json
import telebot


with open(r'', encoding='utf-8') as config:
    config = json.load(config)


# =========================
# ТОКЕН БОТА И ID
# =========================
bot = telebot.TeleBot(config['*****'])
GroupID_ = config['*****']
ID_ = config['*****']


tasks = []

def show_menu() -> str:
    """Возвращает текст функционала TaskManager"""
    return f'Меню:\n/1. Показать задачи\n/2. Добавить задачу\n/3. Удалить задачу'

def show_tasks() -> str:
    """Возвращает строку со списком текущих задач"""
    if not tasks:
        return f'Список задач пуст'
    else:
        result = ''
        for i, task in enumerate(tasks, start=1):
            result += f'{i}. {task}\n'
        return result

def add_task(task_text: str) -> str:
    """Добавляет задачу в список и возвращает подтверждение"""
    tasks.append(task_text)
    return f'Задача добавлена'

def remove_task(number: int) -> str:
    """Удаляет задачу по номеру и возвращает изменённый список задач"""
    if len(tasks) == 0:
        return f'Список задач пуст'

    tasks_text = show_tasks()

    if 1 <= number <= len(tasks):
        tasks.pop(number - 1)
        return f'{tasks_text}\n\n Задача #{number} удалена'
    else:
        return f'{tasks_text}\n\n Неверный номер задачи: {number}'


@bot.message_handler(commands=['tasks'])
def start_handler(message):
    bot.send_message(message.chat.id, show_menu())


@bot.message_handler(func=lambda message: True)
def menu_handler(message):
    text = message.text

    if text == '/1':
        bot.send_message(message.chat.id, show_tasks())

    elif text == '/2':
        msg = bot.send_message(message.chat.id, 'Введите задачу:')
        bot.register_next_step_handler(msg, lambda m: bot.send_message(m.chat.id, add_task(m.text)))

    elif text == '/3':
        if len(tasks) == 0:
            bot.send_message(message.chat.id, 'Список задач пуст')
        else:
            msg = bot.send_message(message.chat.id, f'{show_tasks()}\nВведите номер задачи:')
            bot.register_next_step_handler(msg,
                                           lambda m: (
                                               bot.send_message(m.chat.id, remove_task(int(m.text)))
                                               if m.text.isdigit() else
                                               bot.send_message(m.chat.id, 'Ошибка! Нужно целое число')
                                           ))


# ========================
# СТАРТ БОТА
# ========================
if __name__ == '__main__':
    print('Бот функционирует...')
    bot.infinity_polling()
