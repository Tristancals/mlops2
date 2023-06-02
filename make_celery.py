from task_app import create_app

print('make_celery.py - START')
flask_app = create_app()
celery_app = flask_app.extensions["celery"]
print('make_celery.py - END')
