import sys
import sqlite3
from pathlib import Path
import json

sys.path.append(".")
from config import config
from src.domain.model.user import hash_password


class Hasher:
    def __getitem__(self, key):
        return hash_password(key)

class DictFormater:
    def __getitem__(self, value):
        return json.dumps({"episode_id": value})

def executescript(filenames):
    conn = sqlite3.connect(config["database"])

    for filename in filenames:
        sql = Path(filename).read_text().format(hash_password=Hasher(), episode_id=DictFormater())
        conn.executescript(sql)


if __name__ == "__main__":
    executescript(sys.argv[1:])

