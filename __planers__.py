import sqlite3
import __logging__ as log
logger=log.Logger()
class Planers:
    def __init__(self):
        # Подключаемся к SQLite базе данных
        self.sqliteConnection = sqlite3.connect('planers.db')
        self.cursor = self.sqliteConnection.cursor()
        self._create_table()

    def _create_table(self):
        # Создание таблицы для планеров, если её ещё нет
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS planers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            due_date TEXT
        );
        '''
        self.cursor.execute(create_table_query)
        self.sqliteConnection.commit()

    def add_planer(self, name, description, due_date):
        # Добавление нового планера
        insert_query = '''
        INSERT INTO planers (name, description, due_date)
        VALUES (?, ?, ?);
        '''
        self.cursor.execute(insert_query, (name, description, due_date))
        self.sqliteConnection.commit()
        logger.info(f'Планер "{name}" успешно добавлен.')

    def delete_planer(self, planer_id):
        # Удаление планера по ID
        delete_query = 'DELETE FROM planers WHERE id = ?;'
        self.cursor.execute(delete_query, (planer_id,))
        self.sqliteConnection.commit()
        logger.info(f'Планер с ID {planer_id} удалён.')

    def update_planer(self, planer_id, name=None, description=None, due_date=None):
        # Обновление данных планера
        update_query = 'UPDATE planers SET '
        updates = []
        params = []

        if name:
            updates.append('name = ?')
            params.append(name)
        if description:
            updates.append('description = ?')
            params.append(description)
        if due_date:
            updates.append('due_date = ?')
            params.append(due_date)

        update_query += ', '.join(updates) + ' WHERE id = ?;'
        params.append(planer_id)

        if updates:
            self.cursor.execute(update_query, tuple(params))
            self.sqliteConnection.commit()
            logger.info(f'Планер с ID {planer_id} обновлён.')
        else:
         logger.error('Нет данных для обновления.')

    def get_planers(self):
        # Получение списка всех планеров
        select_query = 'SELECT id, name, description, due_date FROM planers;'
        self.cursor.execute(select_query)
        planers = self.cursor.fetchall()
        return planers

    def close_connection(self):
        # Закрытие соединения с базой данных
        self.cursor.close()
        self.sqliteConnection.close()
        logger.info('Соединение с базой данных закрыто.')
