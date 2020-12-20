# Promo-System-
promo system in which users are assigned various promos and can use the promo points in a specific task of their choosing

# How To Run 
1. install pipenv package manager 
```
sudo pip3 install pipenv
```
2. clone project from github
```
git clone https://github.com/BakrFrag/Promo-System-
```
3. cd into project folder
```
cd Promo-System-
``` 
4. active virtualenv
```
pipenv shell 
```

5. install requested libraries
```
pipenv install -r requirements.txt
```
. if some thing go wrong run 
```
pipenv install django djangorestframework django-cors-header djangorestframework-simplejwt
```
6.
``` 
cd promoProject
```
7. applay migrations in database 
```
python manage.py makemigrations
```
```
python manage.py migrate
```
8. run development server
```
python manage.py runserver
```
9. if you mant to check tests
```
python manage.py test
```

10. vist local host in your browser 
and play with urls 

# Python Libraries

1. [Django Framework](https://www.djangoproject.com/)
2. [Django Rest Framework](https://www.django-rest-framework.org/)
3. [Simple JWT ](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
4. [Django Cors Headers](https://pypi.org/project/django-cors-headers/)


# Important Notes

> Comments Tell You More Please Read It 

> This Project Developed On Ubuntu 20.04 Please If You use Different OS Some Issues May Happen

> This Project Developed In DEVELOPMENT MODE and settings of it not Suitable For Production Enviroment


