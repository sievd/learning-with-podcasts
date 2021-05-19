from src.lib.sqlite_based_repository import SqliteBasedRepository

from src.domain.model.task import Task


class TaskRepository(SqliteBasedRepository):
    def get_all(self):
        cursor = self._conn().cursor()
        cursor.execute("SELECT * FROM tasks;")
        return [
            Task(id=record["id"], text=record["text"], pending=bool(record["pending"]))
            for record in cursor.fetchall()
        ]

    # def get_by_id(self, id):

    # def delete(self, entity):

    # def save(self, entity):
