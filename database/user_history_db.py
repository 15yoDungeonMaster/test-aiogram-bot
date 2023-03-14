import sqlite3
import json


class HistoryUserDb:
    """
    Пользовательский класс базу данных для работы с пользователем и его историей поиска
    """

    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.set_up_table()

    def set_up_table(self):
        """
        Устанавливает таблицу в БД если их нет
        :return:
        """

        with self.connection:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS UserHistory(
                userID INT,
                search_date datetime DEFAULT CURRENT_DATE,
                command TEXT,
                data json)
                ''')

    def set_data(self, user_id: int, command: str, data: dict) -> None:
        """
        Запись в БД пользователя, введенной команды и словаря отелей
        :param user_id: идентификатор пользователя
        :param command: команда поиска отелей
        :param data: Словарь отелей
        :return:
        """

        with self.connection:
            self.cursor.execute('''
                INSERT INTO UserHistory(`userID`,`command`,`data`)
                VALUES (?,?,?)''', (user_id, command, json.dumps(data)))

    def get_data(self, user_id: int, count: int):
        """
        Достать из БД историю
        :param user_id:Идентификатор пользователя
        :param count:Количество отелей
        :return:
        """

        with self.connection:
            self.cursor.execute('''
                SELECT `search_date`,`command`,`data` FROM UserHistory
                WHERE `userID` = ? LIMIT ?''', (user_id, count))
            data = self.cursor.fetchall()
            return data

    def del_data(self, user_id: int) -> None:
        """
        Стереть историю
        :param user_id: Идентификатор пользователя
        :return:
        """

        with self.connection:
            self.cursor.execute('''
                DELETE FROM UserHistory WHERE `userID` = ? ''', (user_id,))