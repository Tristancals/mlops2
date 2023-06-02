import time

from celery import shared_task
from celery import Task

import whisper

# Celery Worker
# partis où l'ont définis les tâches à accomplir
# ignore_result=False est la pour preciser au Broker redis
# que la tâche(task) qu'il a demandé à Celery lui retournera
# des datas et qu'il doit garder en mémoire celle-ci pour
# faire renvoyer au front Flask les datas.

@shared_task(ignore_result=False)
def add(a: int, b: int) -> int:
    print("tasks.py - add(a: int, b: int)", a, b)
    return a + b


@shared_task()
def block() -> None:
    print('tasks.py - block()')
    time.sleep(5)


@shared_task(bind=True, ignore_result=False)
def process(self: Task, total: int) -> object:
    print('tasks.py - process(self: Task, total: int)', total)
    for i in range(total):
        self.update_state(state="PROGRESS", meta={"current": i + 1, "total": total})
        time.sleep(1)
    return {"current": total, "total": total}


@shared_task(ignore_result=False)
def audio(file_path: str) -> object:
    print('tasks.py - audio(file_path: str)', file_path)
    # charger le model de reconnaissance vocal de "base" pour
    # transcrire l'audio en data/text via whisper
    # https://github.com/openai/whisper
    model = whisper.load_model("base")
    data = model.transcribe(file_path)
    print('tasks.py - audio(file_path: str) \n- data :\n', data)
    return data
