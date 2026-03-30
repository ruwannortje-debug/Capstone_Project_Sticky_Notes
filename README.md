# Django Sticky Notes App

A Django-based Sticky Notes web application with Docker containerization and Sphinx-generated documentation, developed as a capstone project.

## Repository contents

- `sticky_notes_project/` - the Django project
- `capstone.txt` - public GitHub repository link
- `git_commands.txt` - Git command guide for creating the required history locally

## Local setup

1. Open a terminal in `sticky_notes_project`.
2. Create a virtual environment:
   - Windows: `python -m venv venv`
   - Linux/macOS: `python3 -m venv venv`
3. Activate it:
   - Windows: `venv\Scripts\activate`
   - Linux/macOS: `source venv/bin/activate`
4. Install dependencies:
   - `pip install -r requirements.txt`
5. Run migrations:
   - `python manage.py migrate`
6. Start the app:
   - `python manage.py runserver`

Open `http://127.0.0.1:8000/` in your browser.

## Docker setup

1. Open a terminal in `sticky_notes_project`.
2. Build the image:
   - `docker build -t sticky-notes-app .`
3. Run the container:
   - `docker run -p 8000:8000 sticky-notes-app`

## Documentation

To regenerate the Sphinx documentation, open a terminal in `sticky_notes_project/docs` and run:

- Linux/macOS: `make html`
- Windows: `make.bat html`

## Important notes

- Do not commit real secrets such as passwords or API keys.
- The generated SQLite database file is intentionally excluded. Recreate it with migrations.
- Upload the extracted files and folders to GitHub, not the ZIP file itself.
