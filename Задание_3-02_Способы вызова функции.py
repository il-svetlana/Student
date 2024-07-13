# Создайте функцию send_email, которая принимает
# 2 обычных аргумента: сообщение и получатель
# и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
# Внутри функции реализовать следующую логику:
# Проверка на корректность e-mail отправителя и получателя.
# Проверка на отправку самому себе.
# Проверка на отправителя по умолчанию.

def send_email(message, recipient, *, sender="university.help@gmail.com"):

    valid_domains = ['.com', '.ru', '.net']

    if ('@' not in recipient) or not recipient.endswith(tuple(valid_domains)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif ('@' not in sender) or not sender.endswith(tuple(valid_domains)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи',
           'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание',
           'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре',
           'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')
