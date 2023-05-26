from celery.result import AsyncResult
from flask import Blueprint, Flask
from flask import request
import os
from . import tasks

from werkzeug.utils import secure_filename


bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@bp.get("/result/<id>")
def result(id: str) -> dict[str, object]:
    result = AsyncResult(id)
    ready = result.ready()
    return {
        "ready": ready,
        "successful": result.successful() if ready else None,
        "value": result.get() if ready else result.result,
    }


@bp.post("/add")
def add() -> dict[str, object]:
    a = request.form.get("a", type=int)
    b = request.form.get("b", type=int)
    result = tasks.add.delay(a, b)
    return {"result_id": result.id}


@bp.post("/block")
def block() -> dict[str, object]:
    result = tasks.block.delay()
    return {"result_id": result.id}

@bp.post("/audio")
def audio() -> dict[str, object]:
    file = request.files['audio']
    filename = secure_filename(file.filename)
    file_path = os.path.join(os.getcwd(), filename)
    file.save(file_path)
    result = tasks.audio.delay(file_path)
    return {"result_id": result.id}


@bp.post("/process")
def process() -> dict[str, object]:
    result = tasks.process.delay(total=request.form.get("total", type=int))
    return {"result_id": result.id}
