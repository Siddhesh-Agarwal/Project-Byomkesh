# Byomkesh

![Byomkesh](./static/Byomkesh.jpeg)

---

## Execution

1. create a virtual environment

    ```bash
    python3 -m venv venv
    ```

1. activate the virtual environment

    ```bash
    source venv/bin/activate
    ```

1. install the dependencies

    ```bash
    POETRY_VIRTUALENVS_CREATE=false
    poetry install
    ```

1. run the application

    ```bash
    streamlit run app.py
    ```