# Board game "Battle for Rokugan"

### Инструкция по запуску (все файлы *.sh в директории "./scripts"):

---
- Необходимо установить Python библиотеки, а именно:
  - tkinter
  - pygame, pygame-menu
  - grpcio, grpcio-tools
  - psycopg2
- Для базы данных проверить наличие консольной утилиты psql, при необходимости установить
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
### Порядок хода игры:
- Все игроки подключаются
- Все прожимают ГОТОВО
- Все выбирают касты
- Игроки по очереди ставят жетоны контроля  

#### СТАРТ ИГРОВОГО ЦИКЛА
- Начало раунда. Игрокам выдается актив. Они выбирают использовать или не использовать карты
- Игроки по очереди ставят жетоны контроля из актива
- После того, как все игроки поставили все свои батл токены, они становятся видимыми
- Модель ждет пока игроки посмотрят на токены и ВСЕ прожмут ГОТОВО
- Далее происходит фаза исполнения. Ненужные токены сбрасываются, оставшиеся токены играют. При необходимости ставятся токены контроля. Сыгравшиеся токены битвы сбрасываются
- Переключаемся на следующий раунд. Идем в начало цикла, если сыграли меньше 5 раундов  

#### КОНЕЦ ИГРОВОГО ЦИКЛА
-После 5 раунда можно посмотреть количество набранных очков у каждого игрока, а также посмотреть, кто победитель
