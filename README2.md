# MLOPS flask redis et celery

## pyenv
[install pyenv](https://github.com/pyenv/pyenv)

```shell
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```


```shell
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
```
[dependencies pyenv](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
Ubuntu/Debian/Mint:
```shell
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
install python version: 
```shell
pyenv install <numero_version>
```
## POETRY
### Poetry install
[python-poetry](https://python-poetry.org/docs/)
```shell
curl -sSL https://install.python-poetry.org | python -
```
```shell
poetry --version
```
### Poetry setup
```shell
poetry init
poetry env use ~/.pyenv/shims/python
```

## Dependencies Project
```shell
poetry add celery
poetry add flask
poetry add openai-whisper
poetry add ffmpeg
poetry add setuptools-rust
poetry source add --priority=supplemental foo https://download.pytorch.org/whl/cpu
poetry add --source foo torch torchvision torchaudio
poetry add sympy
```
## test whisper
```shell
whisper test_audio.mp3 
```

## lancer Broker redis via docker
```shell
sudo docker run -d -p 6379:6379 redis
```

## Lancer Celery Worker
```shell
celery -A make_celery worker --loglevel INFO
```

## Lancer Flask Client
```shell
flask -A task_app run --debug
```



