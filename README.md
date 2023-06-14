# Board game "Battle for Rokugan"

### Инструкция по запуску (все файлы *.sh в директории "./scripts"):

---
- Необходимо установить библиотеки, а именно:
  - tkinter
  - pygame, pygame-menu
  - grpcio, grpcio-tools
  - psycopg2
- Сгенерировать файлы для gRPC, для этого запустить скрипт "generate_proto.sh"
---
Перед первым запуском сервера необходимо создать базу данных (скрипт "create_bd.sh")  
Далее для запуска сервера игры необходимо запустить скрипт "server_starter.sh" (сервер слушает хост и порты из файла "server/server_config.py")

---
Для запуска клиента игры необходимо запустить скрипт "game_starter.sh" (клиент подключается к хосту и портам, указанным в файле "client/player_config.py")  
Существует два альтернативных интерфейса игры: графический и консольный:
  - Чтобы выбрать графический, необходимо в файле "client/player_config.py" поменять значение переменной RUNKEY на "VIEW"
  - Чтобы выбрать консольный, необходимо в файле "client/player_config.py" поменять значение переменной RUNKEY на "CONSOLE"  

Также можно отключить форму регистрации. Для этого в файле "client/player_config.py" необходимо поменять значение DISABLE_REGISTRATION на True.

---
