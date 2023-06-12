# Board game "Battle for Rokugan"

- Предварительно необходимо сгенерировать файлы для gRPC, для этого запустите скрипт "generate_proto.sh" из директории "proto"
- Для запуска клиента игры необходимо запустить файл "game_starter.py" из директории "client"  
- Для запуска сервера игры необходимо запустить файл "server_starter.py" из директории "server"  

По задумке авторов, постоянно должен работать сервер, расположенный на удаленном хосте, а также рядом с ним должна находиться база данных.  

Необходимо учесть, что для безопасности из файла "server/logic/generate_pwd.py" были удалены реализации функций де/шифрования пароля. А также оба файла-конфига ("server/logic/server_config.py" и "client/player_config.py") имеют заглушки вместо значений переменных.
