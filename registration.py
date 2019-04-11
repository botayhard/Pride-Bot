from tinydb import TinyDB, Query
from time import time
import os

class Registration:

    def __init__(self):
        if not os.path.exists('data/'):
            os.makedirs('data')
        self.database = TinyDB('data/registrations.json')

    def register(self, chat, user):
        Chat = Query()
        if self.database.contains(Chat.id == chat.id):
            self.database.update(self.__register_in_chat(user.id), Chat.id == chat.id)
        else:
            chat_item = {
                'id': chat.id,
                'users': {}
            }

            self.__register_in_chat(user.id)(chat_item)
            self.database.insert(chat_item)
    
    def get_registered_users_for_chat(self, chat):
        Chat = Query()
        chat = self.database.get(Chat.id == chat.id)
        return chat['users'] if chat else None

    def is_user_registered(self, chat, user):
        Chat = Query()
        chat = self.database.get(Chat.id == chat.id)
        return chat != None and str(user.id) in chat['users']

    def reward_user(self, chat, user, name):
        Chat = Query()
        self.database.update(self.__reward(user, name), Chat.id == chat.id)

    def get_last_drawing_time(self, chat):
        Chat = Query()
        chat = self.database.get(Chat.id == chat.id)
        return chat['last_drawing_time'] if chat and 'last_drawing_time' in chat else 0

    def get_last_winner(self, chat):
        Chat = Query()
        chat = self.database.get(Chat.id == chat.id)
        return chat['last_winner'] if chat and 'last_winner' in chat else ''

    def __reward(self, user, name):
        def transform(element):
            element['last_drawing_time'] = time()
            element['last_winner'] = name
            element['users'][str(user.id)]['wins'] += 1
        return transform

    def __register_in_chat(self, user_id):
        def transform(element):
            element['users'][user_id] = {
                'wins': 0
            }

        return transform
