# LLM Workshop

## Setup for google colab

Open the main notebook [here](https://colab.research.google.com/github/mlops-and-crafts/llm-workshop/blob/main/llmops_and_crafts.ipynb).

Make sure you have a GPU runtime selected

![image](https://github.com/mlops-and-crafts/llm-workshop/assets/27999937/bb421a82-15c6-43eb-9783-8d62b56a54a7)

Run the cell in the notebook that install the CUDA compatible version of ctransformers:
```sh
!pip uninstall ctransformers -y
!CT_CUBLAS=1 pip install ctransformers --no-binary ctransformers
```

## Setup locally


```sh
# clone the repo
gh repo clone mlops-and-crafts/llm-workshop

# enter the llm-workshop folder
cd llm-workshop

# install poetry (Python dependency manager)
which poetry || pip install poetry

# configure poetry to use a local venv:
poetry config virtualenvs.in-project true

# install dependencies
poetry install
```

### Using jupyter notebook:

```
# start virtual environment
poetry shell

# start notebook from within the virtual environment
jupyter notebook
```

### Using vscode:

Open `llmops_and_crafts.ipynb` and select the kernel in `.venv`:

![image](https://github.com/mlops-and-crafts/llm-workshop/assets/27999937/8d46aed6-c168-4c0a-990f-e2c21cae021d)

### If you are on apple metal (M1, M2):

run the cell with

```
!pip uninstall ctransformers -y
!CT_METAL=1 pip install ctransformers --no-binary ctransformers
```

