# POLYSURMIN_remote_server

Данный репозиторий содержит файлы для удаленного сервера.

Для работы необходимо создать виртуальное окружение и установить библиотеки, находящиеся в файле req.txt. 

После скачивания айлов, необходимо сделать миграцию. 


Все рабочие файлы аходятся в папке remote_server, поэтому далее описывается только её содержание. 

```
│   manage.py  
│   req.txt 
├───TEST_SERVER
│   └───swan_server_test.py
├───static/admin
│   │   css
│   │   img
│   └───js
├───swanapp
│   │   __init__.py
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   swan.py
│   │   swanstarter.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   ├───app
│   │   │   swan.exe 
│   │   │   swanrun
│   │   │   template.swn
│   │   └───bathymetry
│   │          └───port_not_bathy_25m_vobst_exp.bot
│   └───migrations
└────swanweb
    │   __init__.py
    │   asgi.py
    │   settings.py
    │   urls.py
    └───views.py

```