rem erase D:\Develop\python\dj_lavang\family\migrations\0001*.py
rem erase D:\Develop\python\dj_lavang\*sqlite3
python manage.py makemigrations
python manage.py migrate
rem python manage.py createsuperuser
python manage.py runserver