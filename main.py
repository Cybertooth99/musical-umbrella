from chatterbot import ChatBot

bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.db'
)

print('Type something to begin...')

while True:
    try:
        user_input = input()
        bot_response = bot.get_response(user_input)
        print(bot_response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break