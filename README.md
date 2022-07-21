# WebShop
### Планы: ###
```shell
Написать backend часть на django 
```
```shell
перенести функционал на DjangoRESTframework и написать frontend часть с помощью библиотеки React
```
### Функционал доступный на данный момент: ###
```shell
Написан models.AbstractBaseUser(client) и manager.CustomUserManager(client) для регистрации и авторизации через email
```
```shell
Написан models.Product(shop) для хранения свойств товара с привязкой к типу категории
```
```shell
Реализован models.Category(shop)
```
```shell
Реализована корзина, которая работает от сессии. В корзине можно изменять кол-во товара, удалять товар
```
```shell
Написана логика оформления товара models.Order(shop)
```


## Как запустить проект:

## Установка ##

### Клонировать репозиторий: ###
```shell
git clone https://github.com/batalova90/meeting_website/
```
### Установить виртуальное окружение: ###
```shell
python -m venv venv
```
### Включить виртуальное окружение: ###
```shell
source venv/bin/activate (macOS или Linux)
```
```shell
source venv/Scripts/activate (Windows)
```
### Установить зависимости из файла requirements.txt: ###
```shell
python -m pip install --upgrade pip
```
```shell
pip install -r requirements.txt
```

### Выполнить миграции: ###
```shell
python manage.py migrate
```
### Запустить проект: ###
```shell
python manage.py runserver
```
### Проверить, что все работает: ###
http://127.0.0.1/
