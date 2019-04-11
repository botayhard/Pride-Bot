"""Module for base command class"""
import telegram

class Command:
    """Base command class"""

    def __init__(self):
        self.bot = None
        self.last_update = None
        self.only_public_chats = False

    def execute(self, bot, update):
        """Execute the command"""
        chat = update.message.chat

        self.bot = bot
        self.last_update = update

        if self.only_public_chats and chat.type == chat.PRIVATE:
            self.reply_with_text("Chat is private")
        else:
            self.run()

    def run(self):
        pass

    def reply_with_text(self, text):
        """Reply to chat with text"""
        self.bot.send_message(chat_id=self.last_update.message.chat_id, text=text)

    def reply_with_markdown(self, text):
        """Reply to chat with markdown"""
        self.bot.send_message(
            chat_id=self.last_update.message.chat_id,
            text=text,
            parse_mode=telegram.ParseMode.MARKDOWN)

    def get_display_name(self, user):
        if len(user.username) > 0:
            return '@' + user.username
        else:
            return f'{user.first_name} {user.last_name}'
