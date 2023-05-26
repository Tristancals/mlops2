import time

from celery import shared_task
from celery import Task

import whisper

@shared_task(ignore_result=False)
def add(a: int, b: int) -> int:
    return a + b


@shared_task()
def block() -> None:
    time.sleep(5)


@shared_task(bind=True, ignore_result=False)
def process(self: Task, total: int) -> object:
    for i in range(total):
        self.update_state(state="PROGRESS", meta={"current": i + 1, "total": total})
        time.sleep(1)

    return {"current": total, "total": total}


@shared_task()
def audio(file_path) -> str:

    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    print(result["text"])
    # print the recognized text
    return str(result["text"])

