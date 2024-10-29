# Как скачать видео с Я.Диска
Документация: https://yandex.ru/dev/disk-api/doc/ru/concepts/quickstart

## 1. Получить ключ OAuth
Откройте страницу создания приложения (https://oauth.yandex.ru/client/new/)

![img_1.png](images/img_1.png)


Пропишите cloud_api:disk.read в названии доступа.

![img_2.png](images/img_2.png)

Нажмите создать приложение.

![img_3.png](images/img_3.png)

В новом окне найдите токен ClientID.

В браузере отправьте запрос на этот URL, <ClinetID> замените на ваш.

`https://oauth.yandex.ru/authorize?response_type=token&client_id=<ClientID>`

В открывшемся окне будет OAuth токен (Вставьте его вместо переменной `oauth_token` в jupyter notebook)

![img_4.png](images/img_4.png)

Откройте видео в своем я.диске. Скопируйте последнюю часть URL по примеру:

![img_5.png](images/img_5.png)

Копируйте начиная с `%2fФотокамера....`. (Вставьте его вместо переменной `file_path` в jupyter notebook)

Запустите `example.ipynb` с вашими OAuth токеном и путем до видео файла на диске.

Готово :)
