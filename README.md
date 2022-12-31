# Places Remember

Веб-сервис, с помощью которого люди могут сохранить свои впечатления о посещённых местах. Сделан в качестве тестового задания на Django в 2022.
Посмотреть реализованную версию можно на https://am93.pythonanywhere.com/

## Возможности:
- Есть регистрация и логин как через ВК, так и с помощью e-mail.
- Каждый пользователь видит только свои записи
- Удобная панель администрирования, на русском (требует создание пользователя с правами администратора, средствами движка Django)
- Возможно наделение правами администрирования одного из пользователей (стандартными средствами админ.панели)
- Интегрирована панель для наладки Django  Debug  Tool (работает только при Debug=True)

## Описание работы.
Пользователь заходит на сайт, видит кнопки "Войти через VK" и "Войти по паролю". Через VK можно войти сразу, не проходя процедуру регистрации. Для входа по паролю можно зарегистрироваться (кнопка "Регистрация" в левом верхнем углу) или войти с существующим логином. После чего пользователя перебросит на главную страницу (index), где он увидит свои записи, если они есть. Кнопка "Новая запись" в верхней панели создаёт запись. Пользователя перебросит на страницу add_post, где ему нужно будет поставить точку на карте и написать сообщение. Оба элемента формы должны заполнены, иначе форма не отправится в БД. Элемент формы с карты реализован на компоненте Django Treasuremap с API Яндекс.Карт, для отображения требует подключения в шаблон jQuery. После сохранения формы добавляется запись в базу, пользователя перебрасывает на главную страницу, где он видит свой новый пост. Отображения поста реализуется на простом HTTP-запросе к Static API Яндекс.Карт (по прямой и явной ссылке прямо в шаблоне). Записи выглядят просто как "картинка + текст".
В панели администрирования, доступной по адресу /admin/, можно изменять и удалять различные параметры как самих постов, так и учетных записей пользователей. Эти функции реализованы стандартными средствами Django.

## Возможные проблемы:
- интерфейс не полностью соответствует описанному в ТЗ, функционал - соответствует
- не отображается фотография пользователя
- нет тестов
- нет авторизации через Google (с декабря недоступно API для РФ)
- не работает DjDT на PythonAnywhere
- Редактировать и удалять записи можно только в админ.панели
- Не работает кастомная страница 404 (специфика PythonAnywhere)

## Требования:
- Django
- django-treasuremap
- social-auth-app-django
- Django  Debug  Tool (для наладки, можно отключить)
- JQuery (подключено в шаблоне с CDN  jsdelivr, возможна статика)
- Bootstrap (подключено в шаблоне с CDN  jsdelivr, возможна статика)
- и их зависимости

## Установка на тестовом стенде:
- клонировать репозиторий на машину, с которой будет будет запускаться сервис (либо по SSH-ссылке, либо скопировать и распаковать zip-архив)
>  ```git clone https://github.com/andmerk93/homework_bot.git```


- На машине должен быть установлен Python актуальной версии (тестировалось на 3.8, 3.10)
- развернуть виртуальное окружение python в папке с проектом (remember_maps)
>```python3 -m venv venv```
- активировать виртуальное окружение
>```source ./venv/bin/activate ``` (для linux/unix)
```venv\Scripts\activate``` (для Windows, должно быть разрешено выполнение скриптов Powershell)

- с запущенным виртуальным окружением нужно выполнить установку требуемых компонентов
>```pip  install -r  requirements.txt```
- перейти в папку remember_maps/remember_maps  Дальнейшие команды будут выполняться отсюда
- создать необходимые таблицы в базе данных (нет необходимости делать makemigrations, описания миграций добавлены в репозиторий)
>```python  manage.py  migrate```


- собрать статические файлы для адекватной работы админской панели и Django Debug Tool
>```python  manage.py collectstatic```
- Для теста панели администратора нужно создать пользователя с правами администратора и следовать инструкциям в консоли.
>```python  manage.py  createsuperuser```
- По умолчанию, для тестового стенда включен режим отладки. Если его требуется выключить, то в файле ```remember_maps/remember_maps/remember_maps/settings.py``` нужно заменить 17-ю строку на ```DEBUG = False```. В этом случае, Django Debug Tool будет недоступен
- По умолчанию, требуемые компоненты Bootstrap и jQuery  подключаются с CDN  jsDelivr в шаблон base.html (в папке remember_maps/remember_maps/templates/). Можно сохранить их локально и подключить к проекту. Для этого нужно в base.html закомментировать 11 и 12 строки, раскомментировать 9 и 10. В папку remember_maps/static/ нужно скопировать jquery.min.js и bootstrap.min.css, взятые с официальных источников.
Например, на linux для этого можно выполнить команды из папки ```static```
>```wget https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css```
```wget https://cdn.jsdelivr.net/npm/jquery@3.6.3/dist/jquery.min.js```
- Для работы проекта потребуются ключи API. В папке remember_maps/remember_maps/remember_maps  нужно создать файл ```keys.py``` со следующим содержанием
>```SECRET_KEY = ''```
>```SOCIAL_AUTH_VK_OAUTH2_KEY = ''```
>```SOCIAL_AUTH_VK_OAUTH2_SECRET = ''```

 - Без этого файла проект не запустится и выдаст ошибку. Сами ключи при этом необязательно должны быть настоящими для тестового стенда, ошибок не должно быть. Первый ключ - это секретный ключ самого Джанго, второй и третий - параметры приложения VK, к которому привязывается авторизация. Если эти параметры не заполнить, то при нажатии кнопки "Войти через VK" браузер выдаст ошибку.
- После выполнения всех подготовительных работ из папки remember_maps/remember_maps выполнить
>```python  manage.py  runserver```

Тестовый сервер должен запуститься, и быть доступен по http://127.0.0.1:8000/
Панель администратора будет доступна по http://127.0.0.1:8000/admin/
