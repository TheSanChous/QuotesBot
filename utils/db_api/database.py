import mysql.connector

from utils.db_api.models.user import User

from data import config
import logging


class DbContext:
    def __init__(self):
        logging.info("open connection...")
        self.connection = mysql.connector.connect(
            host=config.DB_SERVER,
            database=config.DB_DATABASE,
            user=config.DB_USER,
            password=config.PASSWORD)
        logging.info("database connected!")
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def get_user(self, user, chat=None):
        query = "SELECT * FROM users WHERE "

        if user is not None:
            query += f"user_id={user}"
        elif chat is not None:
            query += f"chat_id={chat}"
        else:
            raise Exception("")
        self.cursor.execute(query)
        row = self.cursor.fetchone()

        if row is None or row == ():
            self.create_user(user)
            return self.get_user(user)

        return User(row[0], row[1], row[2], row[3], row[4])

    def create_user(self, user):
        query = f"INSERT INTO users (user_id) VALUES ({user})"

        self.cursor.execute(query)
        self.connection.commit()
        pass

    def update_user(self, user: User):
        query = f"UPDATE users SET user_id=?, state=?, data=?, chat_id=? WHERE id={user.id}"

        self.cursor.execute(query, (user.user_id, user.state, user.data, user.chat_id))
        self.connection.commit()
