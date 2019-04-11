import logging
from commands import StartCommand, RegisterCommand, PidorCommand, StatsCommand
from telegram.ext import Updater, CommandHandler
from config import load_configuration

class Bot:
    def run(self):
        """Start the bot"""
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO)

        config = load_configuration()
        print(config.token)
        updater = Updater(token=config.token)
        dispatcher = updater.dispatcher

        commands = {
            'start': StartCommand().execute,
            'register': RegisterCommand().execute,
            'pidor': PidorCommand().execute,
            'stats':  StatsCommand().execute,
        }

        for command, handler in commands.items():
            dispatcher.add_handler(CommandHandler(command, handler))
        dispatcher.add_error_handler(self.error_handler)

        updater.start_polling()

    def error_handler(self, bot, update, error):
        print(error)


if __name__ == '__main__':
    Bot().run()

