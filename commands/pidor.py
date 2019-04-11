from commands.command import Command
import random
from registration import Registration
from time import time
from telegram import TelegramError

class PidorCommand(Command):
    def __init__(self):
        super().__init__()
        self.only_public_chats = True
        self.registration = Registration()

    def run(self):
        chat = self.last_update.message.chat
        if self.need_to_choose(chat):
            self.choose_user(chat)
        else:
            self.show_last_winner(chat)

    def choose_user(self, chat):
        users = self.registration.get_registered_users_for_chat(chat)
        print(len(users))
        successful = False
        user_id = 0
        while not successful:
            index = random.randrange(0, len(users))
            user_id = list(users)[index]
            try:
                member = self.bot.getChatMember(chat.id, user_id)
                successful = True
            except TelegramError:
                continue
        name = self.get_display_name(member.user)
        self.registration.reward_user(chat, member.user, name)
        self.reply_with_text(f"Выбираю пидора дня...")
        self.reply_with_text(f"TODO: Сделать побольше сообщений")
        self.reply_with_text(f'Ты пидор дня, {name}, поздравляю!')

    def show_last_winner(self, chat):
        winner = self.registration.get_last_winner(chat)
        if len(winner) == 0:
            self.reply_with_text("О нет! Не могу получить победителя.")
        else:
            self.reply_with_text(f"Пидор дня – {winner}")

    def need_to_choose(self, chat):
        drawing_time = self.registration.get_last_drawing_time(chat)
        current_time = time()
        return current_time - drawing_time > 24 * 60 * 60
