import sqlite3 as sl
import logging

logger = logging.getLogger(__name__)


class Database:
    def __init__(self, database_name: str):
        logger.info(f'connecting to DB {database_name}')
        self._con = sl.connect(f'{database_name}.db')

    def create_table(self, create_statement: str):
        try:
            with self._con:
                self._con.execute(create_statement)
            logger.info("Table successfully created")
        except sl.OperationalError as exc_info:
            logger.warning(str(exc_info))

    def insert_data(self, entry: dict, table_name: str):

        if isinstance(entry, dict):
            entry = [entry]

        for datapoint in entry:
            value_names = ""
            value_repl = ""
            data = []
            for key, value in datapoint.items():
                value_names += f'{key},'
                value_repl += '?,'
                data.append(value)

            value_names = f'({value_names})'.replace(",)", ")")
            value_repl = f'({value_repl})'.replace(",)", ")")
            data = [data]

            sql = f'INSERT INTO {table_name} {value_names} values{value_repl}'

            with self._con:
                logger.info(sql)
                self._con.executemany(sql, data)

    def query(self, sql):
        found_data = []
        with self._con:
            data = self._con.execute(sql)
            for row in data:
                found_data.append(row)
        return found_data

    def execute_command(self, sql):
        with self._con:
            data = self._con.execute(sql)
            for row in data:
                found_data.append(row)
        return found_data

    def update(self, sql, task):
        self._con.execute(sql, task)
        self._con.commit()


if __name__ == "__main__":
    db = Database(database_name='test')
    db.create_table("""
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
    """)
    entry = {'name': 'Alice', 'age': 21}
    db.insert_data(entry, table_name="USER")
    print(db.query("SELECT * FROM USER"))
