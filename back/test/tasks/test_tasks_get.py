import pytest  # type: ignore

from src.domain.repository.task_repository import TaskRepository
from src.domain.interactor.task_interactor import TaskInteractor

import sqlite3


@pytest.fixture
def database():
    conn = sqlite3.connect(":memory:")
    conn.executescript(
        """
        DROP TABLE IF EXISTS tasks;
        CREATE TABLE tasks (
            id varchar primary key,
            text varchar,
            pending boolean
        );
        """
    )
    return conn


def test_should_get_empty_array_if_no_data(database):
    task_repository = TaskRepository(None, database)

    interactor = TaskInteractor(None, task_repository)

    all_tasks = interactor.get_all_tasks()

    assert all_tasks == []


def test_should_get_array_if_data(database):

    database.executescript(
        """
        INSERT INTO tasks (id, text, pending) values
            ("task-1", "Pensar primero con la cabeza", 0),
            ("task-2", "Aprender algo de javascript", 1),
            ("task-3", "Hacer una aplicaci\u00f3n superchula", 1);
        """
    )
    task_repository = TaskRepository(None, database)

    interactor = TaskInteractor(None, task_repository)

    all_tasks = interactor.get_all_tasks()

    assert all_tasks[0].id == "task-1"
    assert all_tasks[0].text == "Pensar primero con la cabeza"
    assert all_tasks[0].pending is False

    assert [i.id for i in all_tasks] == [
        "task-1",
        "task-2",
        "task-3",
    ]
