from src.lib.sqlite_based_repository import SqliteBasedRepository

from src.domain.model.event import Event
import json


class EventsRepository(SqliteBasedRepository):

    def get_all_events(self, type):
        cursor = self._conn().cursor()
        cursor.execute("SELECT * FROM events WHERE type=?;", (type,))
        return [
            Event(user_id=record["user_id"], timestamp=record["timestamp"],
                  type=record["type"], data=json.loads(record["data"]))
            for record in cursor.fetchall()
        ]

    def get_events_by_user_id(self, user_id, type):
        cursor = self._conn().cursor()
        cursor.execute(
            "SELECT * FROM events WHERE type=? AND user_id=?;", (type, user_id))
        return [
            Event(user_id=record["user_id"], timestamp=record["timestamp"],
                  type=record["type"], data=json.loads(record["data"]))
            for record in cursor.fetchall()
        ]
