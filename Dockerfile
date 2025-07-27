FROM python:3.12-slim-bullseye


# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instala dependências do sistema
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    gcc \
 && rm -rf /var/lib/apt/lists/*

# Instala Poetry versão 1.7.1
RUN curl -sSL https://install.python-poetry.org | python3 - --version $POETRY_VERSION

# Define diretório de trabalho para instalar dependências Python
WORKDIR $PYSETUP_PATH

# Copia arquivos de dependências para cache
COPY poetry.lock pyproject.toml ./

# Instala dependências (sem dev)
RUN poetry install 

# Também pode rodar só `poetry install`, mas com --no-dev é melhor para produção


# Copia todo código da aplicação
WORKDIR /app
COPY . /app/

EXPOSE 8000

# Corrige o comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
