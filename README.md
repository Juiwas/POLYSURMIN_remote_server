# POLYSURMIN_remote_server

Данный репозиторий содержит файлы для удаленного сервера.

Для работы необходимо создать виртуальное окружение и установить библиотеки, находящиеся в файле req.txt. 

После скачивания файлов, необходимо сделать миграцию. 


Все рабочие файлы находятся в папке remote_server, поэтому далее описывается только её содержание. 

```
│   manage.py  
│   req.txt  [файл с необходимыми библиотеками] 
├───TEST_SERVER
│   └───swan_server_test.py
├───static/admin [папка Django] 
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
│   ├───app  [файлы индустриального ПО] 
│   │   │   swan.exe 
│   │   │   swanrun
│   │   │   template.swn
│   │   └───bathymetry
│   │          └───port_not_bathy_25m_vobst_exp.bot
│   └───migrations [папка Django]  
└────swanweb
    │   __init__.py
    │   asgi.py
    │   settings.py
    │   urls.py
    └───views.py

```