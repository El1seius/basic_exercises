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

from collections import Counter

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
    id_user_message = []
    for one_message in messages:
        id_user = one_message['sent_by']
        id_user_message.append(id_user)

    numb_user_message = Counter(id_user_message)
    id_user_max_message = max(numb_user_message, key=numb_user_message.get)
    return id_user_max_message
        

def message_with_max_answer(messages):
    list_with_id_message = []
    for one_message in messages:
        id_message = one_message['reply_for']
        if id_message is not None:
            list_with_id_message.append(id_message)

    numb_id_message = Counter(list_with_id_message)
    id_message_max = max(numb_id_message, key=numb_id_message.get)

    for one_message in messages:
        if id_message_max == one_message['id']:
            return one_message['sent_by']


def message_with_max_viewing(messages):
    users_with_unique_users = {}
    for one_message in messages:
        id_user = one_message['sent_by']
        id_seen_by = one_message['seen_by']
        if id_user in users_with_unique_users:
            for user_seen_by in id_seen_by:
                if user_seen_by not in users_with_unique_users[id_user]:
                    users_with_unique_users[id_user].append(user_seen_by)
        else:
            users_with_unique_users[id_user] = id_seen_by

        if id_user in users_with_unique_users[id_user]:
                users_with_unique_users[id_user].remove(id_user)

    id_with_max_nubm_unique_users = max(users_with_unique_users, key=users_with_unique_users.get)
    max_nubm_unique_users = len(users_with_unique_users[id_with_max_nubm_unique_users])
    users_with_max_unique_users = []
    for every_user in users_with_unique_users:
        nubm_unique_user = len(users_with_unique_users[every_user])
        if nubm_unique_user >=max_nubm_unique_users:
            users_with_max_unique_users.append(every_user)
    
    return users_with_max_unique_users


if __name__ == "__main__":
    messages = generate_chat_history()

    print(f'Больше всех сообщений написал пользователь с ID: {user_max_message(messages)}')
    print(f'Сообщение, на которое больше всего отвечали, принадлежит пользователю: {message_with_max_answer(messages)}')
    print(f'ID пользователей, сообщения, которых видело больше всего уникальных пользователей: {message_with_max_viewing(messages)}')