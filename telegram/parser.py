import json
from bs4 import BeautifulSoup
import os
import re


export = r''
output = r'.json'


def sort_key(s: str) -> list[int | str]:
    """Естественная сортировка"""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]


def parsing():
    messages = {}

    files = [f for f in os.listdir(export)
             if f.startswith('messages') and f.endswith('.html')]
    files.sort(key=sort_key)

    for filename in files:
        filepath = os.path.join(export, filename)
        print(f'Обработка файла: {filename}')

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                file = BeautifulSoup(f.read(), 'html.parser')

                for message in file.find_all(class_='message'):
                    user_elem = message.find(class_='from_name')
                    username = user_elem.get_text(strip=True) if user_elem else 'Системное сообщение'

                    text_elem = message.find(class_='text')
                    if not text_elem:
                        continue

                    message_text = text_elem.get_text(' ', strip=True)

                    if username == '*****':
                        messages[len(messages) + 1] = {
                            'user': '*****',
                            'message': message_text
                        }
                    #elif username == '*****':
                    #    messages[len(messages) + 1] = {
                    #        'user': '*****',
                    #        'text': message_text
                    #    }
                    else:
                        messages[len(messages) + 1] = {
                            'user': username,
                            'message': message_text
                        }

        except Exception as e:
            print(f'Ошибка при обработке {filename}: {str(e)}')
            continue


    with open(output, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

    print(f'Сохранено {len(messages)} сообщений в {output}')


if __name__ == '__main__':
    parsing()
