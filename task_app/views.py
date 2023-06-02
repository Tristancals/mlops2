from celery.result import AsyncResult
from flask import Blueprint, Flask
from flask import request
import os
from . import tasks

from werkzeug.utils import secure_filename

bp = Blueprint("tasks", __name__, url_prefix="/tasks")

# Flask Client
# Partie API appeler par le frontend
# d'où partent les requêtes à redis à l'attention de
# Celery pour effectuer des opérations (calculs)
# Lorsqu'on effectue une requête "post" le Broker redis accuse reception
# en nous retournant un result (token) avec le status de la demande
# et une "id" et les datas issus de l'opération realise par Celery
# les datas sont attendus ("get") par la fonction result(id) qui relance
# ça demande jusqu'à obtenir le status "ready" (code javascript dans index.html)
#
@bp.get("/result/<id>")
def result(id: str) -> dict[str, object]:
    print("views.py - result(id: str)", id)
    result = AsyncResult(id)
    ready = result.ready()
    print("views.py - result(id: str) \n- result:\n", result)
    return {
        "ready": ready,
        "successful": result.successful() if ready else None,
        "value": result.get() if ready else result.result,
    }


@bp.post("/add")
def add() -> dict[str, object]:
    print("views.py - add()")
    a = request.form.get("a", type=int)
    b = request.form.get("b", type=int)
    result = tasks.add.delay(a, b)
    print("views.py - add() \n- result:\n", result)
    return {"result_id": result.id}


@bp.post("/block")
def block() -> dict[str, object]:
    print("views.py - block()")
    result = tasks.block.delay()
    print("views.py - block() \n- result:\n", result)
    return {"result_id": result.id}


@bp.post("/audio")
def audio() -> dict[str, object]:
    print("views.py - audio()")
    file = request.files['audio']
    filename = secure_filename(file.filename)
    file_path = os.path.join(os.getcwd(), filename)
    file.save(file_path)
    result = tasks.audio.delay(file_path)
    print("views.py - audio() \n- result:\n", result)
    return {"result_id": result.id}


@bp.post("/process")
def process() -> dict[str, object]:
    print("views.py - process()")
    result = tasks.process.delay(total=request.form.get("total", type=int))
    print("views.py - process() \n- result:\n", result)
    return {"result_id": result.id}
