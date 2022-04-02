# ninja-telegram-bot
Бот с элементами геймификации для бесед в телеграме.

# Возможности
* Бот распознаёт все голосовые сообщения и транслирует их в текст 
* Имеется расширенная система репутации. Каждый участник может повысить (`+реп`) или понизить (`-реп`) другому участнику беседы репутацию. Сила голоса зависит от количества влияния.
* * **Репутация** - это основной показатель рейтинга. Чем выше репутация, тем больше вклада вы внесли в общение в беседе.
* * **Влияние** - это показатель того, насколько ваш голос силен. Сила набирается вслед за репутацией, но не снижается вместе с ней.
* Все сообщения бота и команды пользователей удаляются в чате спустя 45 секунд для избежания спама.
* Имеется система просмотра своего рейтинга и рейтинга других участников.
* Каждый день формируется список тех людей, которые внесли наибольший вклад в общение сегодня. Лучшим флудильщикам выдаются дополнительные очки влияния.


# Конфигурация
Это приложение имеет несколько обязательных переменных среды для запуска (см. [bot/config.py](https://github.com/Ninja-Official/ninja-telegram-bot/blob/main/bot/config.py))

`TELEGRAM_TOKEN` - токен Телеграм бота от BotFather. [Документация для Телеграм ботов](https://core.telegram.org/bots)

`POSTGRES_URI` - ссылка для подключения к БД PostgreSQL

`MIREA_NINJA_GROUP_ID` - id беседы, в которой будет использоваться бот. Получить id можно с помощью бота @my_id_bot

`YANDEX_API_KEY` - API ключ сервисного аккаунта от Yandex Cloud с доступом к AI инстурментам (Spech Kit). Подробнее в [документации](https://cloud.yandex.ru/docs/speechkit/concepts/auth)

`YANDEX_FOLDER_ID` - идентификатор каталога в Yandex Cloud


# Запуск приложение

## Зависимости
* Docker
* PostgreSQL

## Запуск приложения локально


1. Установите все необходимые зависимости:

```bash
pip install -r requirements.txt
```
2. Измените конфигурацию в `bot/config.py`
3. Запустите приложение:
```bash
python -m bot
```

## Запуск с использованием Docker

Чтобы запустить это приложение с помощью docker, для начала вам необходимо собрать локальный образ контейнера:

```bash
docker build -t telegram_bot .
``` 

```bash
docker run -e TELEGRAM_TOKEN=<TELEGRAM_TOKEN> -e MIREA_NINJA_GROUP_ID=<MIREA_NINJA_GROUP_ID> -e YANDEX_API_KEY=<YANDEX_API_KEY> -e YANDEX_FOLDER_ID=<YANDEX_FOLDER_ID> -e POSTGRES_URI=<POSTGRES_URI> -v /etc/localtime:/etc/localtime:ro -t telegram_bot
```