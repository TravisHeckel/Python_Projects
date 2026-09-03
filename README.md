# Python Projects

A collection of my Python work from The Tech Academy — command-line exercises,
coding challenges, and several full Django web applications.

## Command-line & exercises

### [Nice or Mean Project](./Nice_or_Mean_Project)
A decision-making game. It asks for the user's name (handling the case where a
name was already entered and they chose to play again), then walks through
situational questions and responds with both a message and a sound based on each
choice.

### [Python Challenges](./Python%20Challenges)
Assorted exercises covering core Python: reading ranges of numbers, working with
date and time, accessing databases, generating a simple page, and loading one
script into another.

### [pyCharm Project](./Django_Projects/pyCharm%20Project)
My first project in PyCharm — building a basic `Car` object in the terminal and
changing its speed and capabilities.

## Django web applications

These are full Django projects. Each was built and tested with **Django 4.1 on
Python 3.11** and ships with a `requirements.txt`.

### [Checkbook Project](./Django_Projects/Django_Checkbook_Project)
A website that lets users record monetary transactions. It keeps a running record
and calculates the balance based on the entries.

### [Django University](./Django_Projects/djangoUniversity_Project)
Create different university buildings and add categories (courses) to each
building.

### [Tech Project](./Django_Projects/tech_project)
A full-fledged website for a hotel's room service. An admin can control which
menu items are offered and change prices, while users can add or remove items.

## Running a Django project

Each Django app is self-contained. From the folder that holds its `manage.py`:

```bash
# from the project folder (e.g. Django_Projects/tech_project/src/mainapp)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r ../../requirements.txt   # path to that project's requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser. A demo `db.sqlite3` is included
so the apps run with sample data out of the box. (The `SECRET_KEY` in settings is
Django's default insecure development key — fine for local demos, not production.)

## Author

**Travis Heckel** — [GitHub](https://github.com/TravisHeckel) ·
[LinkedIn](https://www.linkedin.com/in/travis-heckel-548010147/)
