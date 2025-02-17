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


# Решение задания №1


def user_max_message(messages): 
    id_user_message = []
    for one_message in messages:
        id_user = one_message['sent_by']
        id_user_message.append(id_user)

    numb_user_message = Counter(id_user_message)
    id_user_max_message = max(numb_user_message, key=numb_user_message.get)
    return id_user_max_message


# Решение задания №2


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


# Решение задания № 3


def get_id_with_max_unique_users(messages):
    id_users_with_unique_users = create_users_with_unique_users(messages)
    id_with_max_nubm_unique_users = max(id_users_with_unique_users, key=id_users_with_unique_users.get)
    max_nubm_unique_users = len(id_users_with_unique_users[id_with_max_nubm_unique_users])

    return [user for user in id_users_with_unique_users
                        if len(id_users_with_unique_users[user]) == max_nubm_unique_users]


def create_users_with_unique_users(messages):
    users_with_unique_users = {}
    for one_message in messages:
        id_user = one_message['sent_by']
        id_seen_by = one_message['seen_by']
        if id_user in users_with_unique_users:
            users_with_unique_users[id_user].update(id_seen_by)
        else:
            users_with_unique_users[id_user] = set(id_seen_by)

    return users_with_unique_users


# Решение задания №4


def what_time_with_max_message(messages):
    time_create_message = []
    for one_message in messages:
        hour_create_message = one_message['sent_at'].hour
        if hour_create_message < 12:
            time_create_message.append('утром')
        elif 12 <= hour_create_message >= 18:
            time_create_message.append('днём')
        else:
            time_create_message.append('вечером')

    numb_message_in_period_of_time = Counter(time_create_message)
    max_numb_message_in_period_of_time = max(numb_message_in_period_of_time, key=numb_message_in_period_of_time.get)
    return max_numb_message_in_period_of_time


# Решение задания №5


def create_id_with_reply_for(messages):
    id_with_reply_for = {}
    for one_message in messages:
        id_with_reply_for[one_message['id']] = one_message['reply_for']

    return id_with_reply_for

def get_id_last_messages_in_thread(id_with_reply_for):
    id_message_for_reply = [
        one_id for one_id in id_with_reply_for 
        if one_id in id_with_reply_for]

    while True:
        temp_list_id_message_for_reply = [
            one_id for one_id in id_with_reply_for 
            if id_with_reply_for.get(one_id) in id_message_for_reply]

        if len(temp_list_id_message_for_reply) == 0:
            break

        id_message_for_reply = temp_list_id_message_for_reply[:]

    return id_message_for_reply

def id_messages_with_most_long_replies(messages):
    id_with_reply_for = create_id_with_reply_for(messages)
    id_message_with_last_reply = get_id_last_messages_in_thread(id_with_reply_for)

    id_message_before_last_reply = [id_with_reply_for[id] for id in id_message_with_last_reply]
    finish_id_messages = []
    for id in id_message_before_last_reply:
        while True:
            if id_with_reply_for[id] is not None:
                id = id_with_reply_for[id]
            else:
                finish_id_messages.append(id)
                break
    
    return finish_id_messages


if __name__ == "__main__":
    messages = generate_chat_history()

    print(f'Больше всех сообщений написал пользователь с ID: {user_max_message(messages)}')
    print(f'Сообщение, на которое больше всего отвечали, принадлежит пользователю: {message_with_max_answer(messages)}')
    print(f'ID пользователей, сообщения, которых видело больше всего уникальных пользователей: {get_id_with_max_unique_users(messages)}')
    print(f'Больше всего сообщений в чате: {what_time_with_max_message(messages)}')
    print(f'Идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов) {id_messages_with_most_long_replies(messages)}')