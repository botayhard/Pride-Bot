from commands.command import Command

class StartCommand(Command):
    def run(self):
        self.reply_with_text("Для начала, добавь этого бота в чат.")
