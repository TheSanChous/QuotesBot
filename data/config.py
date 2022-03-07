from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

DB_SERVER = env.str("DB_SERVER")
DB_USER = env.str("DB_USER")
PASSWORD = env.str("PASSWORD")
DB_DATABASE = env.str("DB_DATABASE")
DB = env.str("DB")

QUOTES_TOKEN = env.str("QUOTES_TOKEN")
