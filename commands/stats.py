from commands.command import Command
from registration import Registration
from telegram import TelegramError

class StatsCommand(Command):

    first_places_formats = [
        "🌟 *{}* 🌟 –  мега-пидор, был пидором дня {} раз(а)",
        "⭐️ *{}* ⭐️ – почти всем пидорам пидор, был пидором дня {} раз(а)",
        "✨ *{}* ✨ – уважаемый в широких кругах пидор, был пидором дня {} раз(а)",
    ]

    def __init__(self):
        super().__init__()
        self.only_public_chats = True
        self.registration = Registration()
    
    def __get_format_string(self, place):
        if place < len(self.first_places_formats):
            return self.first_places_formats[place]
        else:
            return str(place + 1) + '. {} – {}'


    def run(self):
        chat = self.last_update.message.chat
        users = self.registration.get_registered_users_for_chat(chat)
        wins = sorted(users, key=lambda key: users[key]['wins'], reverse=True)[:10]
        usernames = {user: self.get_username(chat, user) for user in wins}
        lines = [
            self.__get_format_string(place).format(usernames[user], str(users[user]['wins']))
            for place, user in enumerate(wins)
            if users[user]['wins'] > 0
        ]

        text = "\n".join(lines)

        self.reply_with_markdown(text)

    def get_username(self, chat, user_id):
        try:
            user = self.bot.get_chat_member(chat.id, user_id).user
            return self.get_display_name(user)
        except TelegramError:
            return 'Ноунейм'
