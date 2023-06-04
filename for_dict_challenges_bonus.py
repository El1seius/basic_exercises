"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def user_max_message(messages): 
    numb_user_message = {}
    for one_message in messages:
        id_user = one_message['sent_by']
        if id_user in numb_user_message:
            numb_user_message[id_user] +=1
        else:
            numb_user_message[id_user] =1

    id_user_max_message = max(numb_user_message, key=numb_user_message.get)
    return id_user_max_message
        

def message_with_max_answer(messages):
    numb_id_message = {}
    for one_message in messages:
        id_message = one_message['reply_for']
        if id_message != None:
            if id_message in numb_id_message:
                numb_id_message[id_message] += 1
            else:
                numb_id_message[id_message] = 1

    id_message_max = max(numb_id_message, key=numb_id_message.get)

    for one_message in messages:
        if id_message_max == one_message['id']:
            return one_message['sent_by']


def message_with_max_viewing(messages):
    numb_viewing = {}
    for one_message in messages:
        id_user = one_message['sent_by']
        numb_viewing[id_user] = len(one_message['seen_by'])
    max_viewing = max(numb_viewing, key=numb_viewing.get)
    
    id_users =[]
    for every_user in numb_viewing:
        if numb_viewing[max_viewing] == numb_viewing[every_user]:
            id_users.append(every_user)
    print(numb_viewing)
    return id_users


if __name__ == "__main__":
    messages = generate_chat_history()

    print(f'Больше всех сообщений написал пользователь с ID: {user_max_message(messages)}')
    print(f'Сообщение, на которое больше всего отвечали, принадлежит пользователю: {message_with_max_answer(messages)}')
    print(f'Cообщения, которые видело больше всего уникальных пользователей, принадлежит пользователям: {message_with_max_viewing(messages)}')