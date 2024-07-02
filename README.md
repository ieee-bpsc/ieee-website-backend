# IEEE Website Backend

## Run the project

1. Clone the repository

2. Create and activate a virtual environment

```bash
python -m venv env
./env/Scripts/activate.ps1 # Windows
source env/bin/activate # Linux
```

3. Install the dependencies

```bash
pip install -r requirements.txt
```

4. Make migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the server

```bash
python manage.py runserver
```
