# Django Tutorial

https://docs.djangoproject.com/en/3.1/intro/tutorial01/

## Setup

1. Install `poetry`: https://python-poetry.org/docs/1.5/
2. Install dependencies (I think a virtual environment would be automatically create)
    ```bash
    poetry install
    ```
    * additional info: https://python-poetry.org/docs/1.5/basic-usage/#installing-dependencies

## Run

1. Activate the virtual environment:
    ```bash
    source $(poetry env info --path)/bin/activate
    ```
    * additional info: https://python-poetry.org/docs/1.5/basic-usage/#activating-the-virtual-environment
    * to verify:
        ```bash
        which python
        which pip
        ```
2. Start the server:
    ```bash
    python manage.py runserver 
    ```