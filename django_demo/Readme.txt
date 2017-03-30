pip install django

django-admin startproject Treasuregram
cd Treasuregram
python manage.py runserver
python manage.py startapp main_app



%% Create models.py
python manage.py makemigrations
        Migrations for 'main_app':
          main_app/migrations/0001_initial.py:
            - Create model Treasure
%%python manage.py sqlmigrate main_app 0001
python manage.py migrate

%% Add initial data
python manage.py shell
>>> from main_app.models import Treasure
>>> Treasure.objects.all()
>>> t = Treasure(name="Gold Nugget", value=500.00, material="gold", location="Curly's Creek, NM", img_url='http://courseware.codeschool.com/try_django/images/treasuregram-gold-nugget.png')
>>> t.save()
>>> t = Treasure(name="Fool's Glod", value=0, material="pyrite", location="Fool's Falls, CO", img_url='http://courseware.codeschool.com/try_django/images/treasuregram-fools-gold.png')
>>> t.save()
>>> t = Treasure(name="Coffee Can", value=2.00, material="tin", location="ACME, CA", img_url='http://courseware.codeschool.com/try_django/images/treasuregram-coffee-can.png')
>>> t.save()
>>> Treasure.objects.all()
>>> exit()




python manage.py createsuperuser
%% admin.site.register(Treasure) in admin.py

http://127.0.0.1:8000/admin
%% Manage Treasure objects
http://courseware.codeschool.com/try_django/images/treasuregram-arrowhead.png
http://courseware.codeschool.com/try_django/images/treasuregram-horseshoes.png


## ImageField
pip install pillow
python manage.py makemigrations
          main_app/migrations/0002_auto_20170330_0401.py:
            - Remove field img_url from treasure
            - Add field image to treasure
%%python manage.py sqlmigrate main_app 0002
python manage.py migrate

