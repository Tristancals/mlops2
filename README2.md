poetry add celery
poetry add flask
poetry add openai-whisper
poetry add ffmpeg
poetry add setuptools-rust
whisper anniv_8.mp3
poetry source add --priority=supplemental foo https://download.pytorch.org/whl/cpu
poetry add --source foo torch torchvision torchaudio
poetry add sympy

whisper anniv_8.mp3 



sudo docker run -d -p 6379:6379 redis


python3 -m venv .venv
. ./.venv/bin/activate
pip install -r requirements.txt && pip install -e .
celery -A make_celery worker --loglevel INFO




