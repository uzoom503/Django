erase D:\Develop\python\dj_lavang\lavang\migrations\000?*.py
erase D:\Develop\python\dj_lavang\*sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver