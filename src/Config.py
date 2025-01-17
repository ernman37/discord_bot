import discord
import yaml

from Client import Client

class Config():

    __ENV_FILE = '.env.yaml'
    __ENV_DISCORD_TOKEN_FIELD = 'discord_token'
    __ENV_OPENAI_TOKEN_FIELD = 'openai_token'
    __ENV_GUILD_ID_FIELD = 'guild_id'

    __CMD_PREFIX = '/'

    def __init__(self):
        self
        self.__intents = self.__get_intents()
        env = self.__get_env()
        self.__discord_token = env[Config.__ENV_DISCORD_TOKEN_FIELD]
        self.__openai_token = env[Config.__ENV_OPENAI_TOKEN_FIELD]
        guild_id = env[Config.__ENV_GUILD_ID_FIELD]
        self.__guild_id = discord.Object(id=guild_id)
        self.__bot = Client(intents=self.__intents, command_prefix=Config.__CMD_PREFIX, guild_id=self.__guild_id)


    def __get_intents(self) -> discord.Intents:
        intents = discord.Intents.default()
        intents.message_content = True
        return intents

    
    def __get_env(self) -> dict:
        raw_env = Config.read_file(Config.__ENV_FILE)
        env_yaml = yaml.safe_load(raw_env)
        return env_yaml

    
    def get_bot(self) -> Client:
        return self.__bot
    

    def get_discord_token(self) -> str:
        return self.__discord_token

    
    def get_openai_token(self) -> str:
        return self.__openai_token

    
    def get_guild_id(self) -> discord.Object:
        return self.__guild_id


    @staticmethod
    def read_file(file: str) -> str:
        try: 
            with open(file) as fin:
                return fin.read()
        except Exception as e:
            print(e)
            exit(1)
    