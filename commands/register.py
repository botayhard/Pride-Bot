from commands.command import Command
from registration import Registration

class RegisterCommand(Command):
    def __init__(self):
        Command.__init__(self)
        self.registration = Registration()
        self.only_public_chats = True

    def run(self):
        user = self.last_update.message.from_user
        chat = self.last_update.message.chat
        name = self.get_display_name(user)

        if self.registration.is_user_registered(chat, user):
            self.reply_with_text(f"{name} уже зарегистрирован")
        else:
            self.registration.register(chat, user)
            self.reply_with_text(f'Теперь ты зарегистрирован в пидоре дня, {name}')
