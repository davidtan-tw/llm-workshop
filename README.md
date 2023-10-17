# LLM Workshop

## Setup (for running notebook on AWS Studio Lab)

See workshop participants doc

## Setup (for running notebook locally)

```sh
# install poetry (Python dependency manager)
which poetry || pip install poetry

# configure poetry to use a local venv:

poetry config virtualenvs.in-project true

# install dependencies
poetry install

# start virtual environment
poetry shell

# start notebook locally
jupyter notebook
```