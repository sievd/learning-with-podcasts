class TaskInteractor:
    def __init__(self, config, task_repository):
        self.config = config
        self.task_repository = task_repository

    def get_all_tasks(self):
        return self.task_repository.get_all()
