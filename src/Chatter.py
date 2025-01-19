from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt_tab')
    

class Chatter():
    
    __chatter = None


    def __init__(self, name: str = 'Chatter'): 
        if Chatter.__chatter is not None: 
            self = Chatter.__bot
            return
        self.__bot = ChatBot(name)
        self.__train()
        Chatter.__chatter = self

    def __train(self) -> None:
        trainer = ChatterBotCorpusTrainer(self.__bot)

        # Train the chatbot based on the english corpus
        trainer.train("chatterbot.corpus.english")

        # Train based on english greetings corpus
        trainer.train("chatterbot.corpus.english.greetings")
        trainer.train()

        trainer = ListTrainer(self.__bot)

    def ask(self, msg: str) -> str:
        return self.__bot.get_response(msg)
        
        
    
