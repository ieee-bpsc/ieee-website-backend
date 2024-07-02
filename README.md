# IEEE Website Backend

## Run the project

1. Clone the repository

2. Copy the `.env.example` file to `.env`.

```bash
cp .env.example .env
```

3. Create and activate a virtual environment

```bash
python -m venv env
./env/Scripts/activate.ps1 # Windows
source env/bin/activate # Linux
```

4. Install the dependencies

```bash
pip install -r requirements.txt
```

5. Make migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Run the server

```bash
python manage.py runserver
```

The server will be available at `http://localhost:8000`.
